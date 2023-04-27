import rest_framework.request
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from product.pagination import StandardResultsSetPagination
from rest_framework.permissions import IsAuthenticated


from .serializers import NewSerializer
from .models import NewModel


# Create your views here.


class NewCreateView(APIView):
    serializer_class = NewSerializer
    model = NewModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request: rest_framework.request.Request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: rest_framework.request.Request, id: int):
        model = self.model.filter(id=id)
        if model:
            model = model[0]
            model.title = request.data['title']
            model.description = request.data['description']
            if model.image and type(request.data['image']) != str:
                model.image = request.data['image']
            if model.video and type(request.data['video']) != str:
                model.video = request.data['video']
            if type(request.data['pdf']) != str:
                model.pdf = request.data['pdf']
            model.save()
            return Response(self.serializer_class(model, many=False).data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request: rest_framework.request.Request, id: int):
        model = self.model.filter(id=id)
        if model:
            model[0].delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class NewView(ListAPIView, APIView):
    model = NewModel.objects.all()
    serializer_class = NewSerializer
    permission_classes = ()
    queryset = []
    pagination_class = StandardResultsSetPagination

    def get(self, request: rest_framework.request.Request, id: int | None = None, *args, **kwargs):
        if not id:
            self.queryset = self.model
            return self.list(request, *args, **kwargs)
        model = self.model.filter(id=id)
        if model:
            return Response(self.serializer_class(model[0], many=False).data)
