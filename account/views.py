import random
import requests

import rest_framework.request
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from account.models import UserSerializer, User, Buyer, SiteAbout, Location
from employee.models import Employee
from new.models import NewModel
from product.models import Product
from .serializers import BuyerSerializer, AboutSerializer, LocationSerializer


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
            token = Token.objects.create(user=User.objects.get(id=user.data['id']))
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
        print(user)
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


class SiteAboutView(APIView):
    serializer_class = AboutSerializer
    model = SiteAbout.objects.all()
    permission_classes = (IsAuthenticated,)

    def get(self, request: rest_framework.request.Request):
        if not self.model:
            serializer = self.serializer_class(data={'products': 0, 'employee': 0, 'news': 0})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(self.serializer_class(self.model[0], many=False).data)

    def put(self, request):
        news = NewModel.objects.all()
        products = Product.objects.all()
        employee = Employee.objects.all()
        self.model = self.model[0]
        self.model.news = len(news)
        self.model.products = len(products)
        self.model.employee = len(employee)
        self.model.save()
        return Response(self.serializer_class(self.model, many=False).data)


class LocationView(APIView):
    serializer_class = LocationSerializer
    permission_classes = ()

    def post(self, request: rest_framework.request.Request):
        model = Location.objects.all()
        if not model:
            print(request.data)
            serializer = self.serializer_class(data=request.data, many=False)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        model[0].longitude = request.data['longitude']
        model[0].latitude = request.data['latitude']
        model[0].save()
        return Response(self.serializer_class(model[0], many=False).data, status=status.HTTP_201_CREATED)

    def get(self, request: rest_framework.request.Request):
        model = Location.objects.all()
        if model:
            return Response(self.serializer_class(model[0], many=False).data)
        return Response(status=status.HTTP_404_NOT_FOUND)