import rest_framework.views
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny


from partner.models import PartnerModel
from partner.serializers import PartnerSerializer


# Create your views here.


class PartnerView(APIView):
    serializer_class = PartnerSerializer
    model = PartnerModel.objects.all()
    authentication_classes = ()
    permission_classes = (AllowAny,)

    def get(self, request: rest_framework.views.Request, id: int | None = None):
        if not id:
            return Response(self.serializer_class(PartnerModel.objects.all(), many=True).data)
        model = self.model.filter(id=id)
        if model:
            return Response(self.serializer_class(model[0], many=False).data)

    def delete(self, request: rest_framework.views.Request, id: int):
        model = self.model.filter(id=id)
        if model:
            model.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class PartnerCreateView(APIView):
    serializer_class = PartnerSerializer
    model = PartnerModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request: rest_framework.views.Request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: rest_framework.views.Request, id: int):
        model = self.model.filter(id=id)
        if model:
            serializer = self.serializer_class(model,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
