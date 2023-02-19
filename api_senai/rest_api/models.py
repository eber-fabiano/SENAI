from django.db import models
from rest_framework import serializers
from django_base64field.fields import Base64Field

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=10)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        db_table = 'auth_user'
        app_label = ''

    def __str__(self):
        return self

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'email')

class Monitoring(models.Model):
    id = models.AutoField(primary_key=True)
    mac_address = models.CharField(max_length=50)
    date = models.DateTimeField()
    classe = models.CharField(max_length=100)
    evidence = Base64Field(max_length=900000)

    class Meta:
        db_table = 'monitoring'
        app_label = ''

    def __str__(self):
        return self

class MonitoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitoring
        fields = ('mac_address',
                  'date',
                  'classe',
                  'evidence')






