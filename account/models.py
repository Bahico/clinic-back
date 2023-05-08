from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import serializers


# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, full_name, phone_number, password=None):
        if not full_name:
            raise ValueError('Users must have an username')
        user = self.model(
            full_name=full_name,
        )
        user.set_password(password)
        user.phone_number = phone_number
        user.save()
        user_serializer = UserSerializer(data={'user': user.id})
        if user_serializer.is_valid():
            user_serializer.save()
        print(user_serializer.errors)
        return user

    def create_staffuser(self, full_name, phone_number, password):
        if not password:
            raise ValueError('staff/admins must have a password.')
        user = self.create_user(full_name, phone_number, password=password)
        user.is_staff = True
        user.save()
        return user

    def create_superuser(self, full_name, phone_number, password=None):
        if not password:
            raise ValueError('superusers must have a password.')
        user = self.create_user(full_name, phone_number, password=password)
        user.full_name = full_name
        user.email = phone_number
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractUser):
    username = models.CharField(unique=True, blank=True, null=True, max_length=10)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=19, unique=True)
    password = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    code = models.CharField(max_length=6)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def __str__(self):
        return self.full_name


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class Buyer(models.Model):
    phone_number = models.CharField(max_length=19)
    full_name = models.CharField(max_length=50)


class SiteAbout(models.Model):
    products = models.IntegerField(default=0)
    employee = models.IntegerField(default=0)
    news = models.IntegerField(default=0)


class Location(models.Model):
    longitude = models.CharField(max_length=30)
    latitude = models.CharField(max_length=30)
