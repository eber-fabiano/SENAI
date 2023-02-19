from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, UserSerializer, Monitoring, MonitoringSerializer
from datetime import datetime
from django.contrib.auth.hashers import make_password
from django.http.response import JsonResponse

class LogoutView(APIView):

    def post(self, request):
        try:
            refresh = request.data.get('refresh')
            token = RefreshToken(token=refresh)
            token.blacklist()
        finally:
            return Response({"msg_logout_sucess": "Logout efetuado com sucesso."})

class UserView(APIView):

    def post(self, request):
        try:
            User.objects.create(
                username=request.data.get('username'),
                email=request.data.get('email'),
                password=make_password(request.data.get('password')),
                is_superuser=False,
                first_name='',
                last_name='',
                is_staff=True,
                is_active=True,
                date_joined=datetime.now()
            )
            return Response({"msg_sucess": "Usuário cadastrado com sucesso."})
        except Exception as e:
            return Response({"msg_error": e.__str__()})

    def get(self, request):
        try:
            id = request.GET.get('id')
            if id is not None:
                user = User.objects.get(id=id)
                return JsonResponse(UserSerializer(user).data, safe=False)

            users = User.objects.order_by('id')
            return JsonResponse(UserSerializer(users, many=True).data, safe=False)
        except Exception as e:
            return Response({"msg_error": e.__str__()})

    def put(self, request):
        try:
            user = User.objects.get(id=request.data.get('id'))
            user.username=request.data.get('username')
            user.email=request.data.get('email')
            user.password=make_password(request.data.get('password'))
            user.save()
            return Response({"msg_sucess": "Usuário atualizado com sucesso."})
        except Exception as e:
            return Response({"msg_error": e.__str__()})

    def delete(self, request):
        try:
            user = User.objects.get(id=request.data.get('id'))
            user.delete()
            return Response({"msg_sucess": "Usuário excluído com sucesso."})
        except Exception as e:
            return Response({"msg_error": e.__str__()})

class MonitoringView(APIView):

    def post(self, request):
        try:
            Monitoring.objects.create(
                mac_address=request.data.get('mac_address'),
                date=request.data.get('date'),
                classe=request.data.get('classe'),
                evidence=request.data.get('evidence')
            )
            return Response({"msg_sucess": "Objeto de interesse cadastrado com sucesso."})
        except Exception as e:
            return Response({"msg_error": e.__str__()})

class DashboardView(APIView):

    def get(self, request):
        try:
            dia = request.GET.get('dia')
            mes = request.GET.get('mes')
            ano = request.GET.get('ano')

            if dia is not None and mes is not None and ano is not None:
                monitorings = Monitoring.objects.filter(date__day=dia, date__month=mes, date__year=ano)
                return JsonResponse(MonitoringSerializer(monitorings, many=True).data, safe=False)
            elif mes is not None and ano is not None:
                monitorings = Monitoring.objects.filter(date__month=mes, date__year=ano)
                return JsonResponse(MonitoringSerializer(monitorings, many=True).data, safe=False)
            elif ano is not None:
                monitorings = Monitoring.objects.filter(date__year=ano)
                return JsonResponse(MonitoringSerializer(monitorings, many=True).data, safe=False)
            else:
                return Response({"msg_error": "Os parâmetros de dia, mês e ano não foram informados."})
        except Exception as e:
            return Response({"msg_error": e.__str__()})
