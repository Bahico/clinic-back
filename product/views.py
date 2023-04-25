import rest_framework.request
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .pagination import StandardResultsSetPagination
from product.models import Product
from product.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class ProductView(APIView):
    permission_classes = ()

    @staticmethod
    def post(request: rest_framework.request.Request):
        post = ProductSerializer(data=request.data)
        if post.is_valid():
            post.save()
            return Response(post.data, status=status.HTTP_201_CREATED)
        print(post.errors)
        print(request.data)
        return Response("Not create!", status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request, id):
        product = Product.objects.filter(id=id)
        if product:
            return Response(ProductSerializer(product[0], many=False).data)
        return Response("Not product", status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def delete(request: rest_framework.request.Request, id: int):
        Product.objects.filter(id=id).delete()
        return Response("Deleted!")

    @staticmethod
    def put(request: rest_framework.request.Request, id: int):
        post = Product.objects.filter(id=id)
        if post:
            serializer = ProductSerializer(post[0], data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("Not product!", status=status.HTTP_400_BAD_REQUEST)


class ProductListView(ListAPIView, APIView):
    permission_classes = ()
    queryset = []
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination

    def post(self, request: rest_framework.request.Request, *args, **kwargs):
        self.queryset = Product.objects.filter(name__contains=request.data['name'])
        return self.list(request, *args, **kwargs)
