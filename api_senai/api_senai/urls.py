"""api_senai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path, re_path
from rest_framework import routers
from django.urls import re_path as url
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_api.views import LogoutView, UserView, MonitoringView, DashboardView

router = routers.DefaultRouter()

schema_view = get_swagger_view(title='SENAI API')

urlpatterns = [
    url('^$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^api/autentication/login/', TokenObtainPairView.as_view()),
    url(r'^api/autentication/renovate/', TokenRefreshView.as_view()),
    url(r'^api/autentication/logout/', LogoutView.as_view()),
    url(r'^api/user/', UserView.as_view()),
    url(r'^api/monitoring/', MonitoringView.as_view()),
    url(r'^api/dashboard/', DashboardView.as_view()),
]
