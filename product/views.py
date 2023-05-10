import rest_framework.request
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status

from .pagination import StandardResultsSetPagination
from product.models import Product, Video
from product.serializers import ProductSerializer, VideoSerializer


# Create your views here.

class ProductView(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer

    def post(self, request: rest_framework.request.Request):
        post = self.serializer_class(data=request.data)
        if post.is_valid():
            post.save()
            return Response(post.data, status=status.HTTP_201_CREATED)
        print(post.errors)
        print(request.data)
        return Response("Not create!", status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        product = Product.objects.filter(id=id)
        if product:
            return Response(self.serializer_class(product[0], many=False).data)
        return Response("Not product", status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def delete(request: rest_framework.request.Request, id: int):
        Product.objects.filter(id=id).delete()
        return Response("Deleted!")

    def put(self, request: rest_framework.request.Request, id: int):
        post = Product.objects.filter(id=id)
        if post:
            post = post[0]
            post.name = request.data['name']
            post.description = request.data['description']
            if type(request.data['image']) != str:
                post.image = request.data['image']
            if type(request.data['pdf']) != str:
                post.pdf = request.data['pdf']
            post.price = request.data['price']
            post.save()
            return Response(self.serializer_class(post, many=False).data, status=status.HTTP_201_CREATED)
        return Response("Not product!", status=status.HTTP_404_NOT_FOUND)


class ProductListView(ListAPIView, APIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    queryset = []
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination

    def post(self, request: rest_framework.request.Request, *args, **kwargs):
        self.queryset = Product.objects.filter(name__contains=request.data['name'])
        return self.list(request, *args, **kwargs)


class VideoView(APIView):
    serializer_class = VideoSerializer
    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self, request: rest_framework.request.Request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: rest_framework.request.Request):
        return Response(self.serializer_class(Video.objects.all(), many=True).data)

    def delete(self, request: rest_framework.request.Request, id: int):
        model = Video.objects.filter(id=id)
        if model:
            model.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
