import random
import requests

import rest_framework.request
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from account.models import UserSerializer, User, Buyer
from .serializers import BuyerSerializer


# Create your views here.

class UserView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request: rest_framework.request.Request):
        if request.user.status:
            return Response(UserSerializer(request.user, many=False).data, status=status.HTTP_200_OK)
        return Response("Not user", status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def put(request: rest_framework.request.Request):
        if str(request.data['code']) == request.user.code:
            request.user.status = True
            request.user.save()
            return Response("Success full!", status=status.HTTP_200_OK)
        return Response('Not edit!', status=status.HTTP_400_BAD_REQUEST)


class UserCreateView(APIView):
    permission_classes = ()

    @staticmethod
    def post(request: rest_framework.request.Request):
        data = request.data
        data['code'] = str(random.randint(100, 999)) + str(random.randint(100, 999))
        user = UserSerializer(data=data)
        if user.is_valid():
            user.save()
            TOKEN = "5179562412:AAGGQcgs2kD1rJpDZCTnzrjSiQm5zk9n0IA"
            chat_id = "5012085359"
            message = user.data['full_name'] + '\nPhone number: ' + user.data['phone_number'] + '\nCode: ' + user.data[
                'code']
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
            requests.get(url).json()
            token = Token.objects.create(user=User.objects.get())
            return Response(token.key, status=status.HTTP_201_CREATED)
        print(user.errors)
        return Response("Not create!", status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = ()

    @staticmethod
    def post(request: rest_framework.request.Request):
        user = User.objects.filter(phone_number=request.data['phone_number'], password=request.data['password'])
        if user and user[0].status:
            token = Token.objects.get(user_id=user[0].id)
            return Response(token.key, status=status.HTTP_200_OK)
        return Response("Not user!", status=status.HTTP_404_NOT_FOUND)


class BuyerView(APIView):
    @staticmethod
    def post(request: rest_framework.request.Request):
        buyer = BuyerSerializer(data=request.data)
        if buyer.is_valid():
            buyer.save()
            return Response(buyer.data, status=status.HTTP_201_CREATED)
        return Response('Not created!', status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request: rest_framework.request.Request, id: int):
        buyer = Buyer.objects.filter(id=id)
        if buyer:
            return Response(BuyerSerializer(buyer[0]).data)
        return Response('Not buyer!', status=status.HTTP_404_NOT_FOUND)
