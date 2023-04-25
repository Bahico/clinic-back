import rest_framework.request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Employee
from .serializers import EmployeeSerializer
from product.pagination import StandardResultsSetPagination


# Create your views here.

class EmployeeView(ListAPIView, APIView):
    permission_classes = ()
    queryset = []
    serializer_class = EmployeeSerializer
    pagination_class = StandardResultsSetPagination

    @staticmethod
    def post(request: rest_framework.request.Request):
        employee = EmployeeSerializer(data=request.data)
        if employee.is_valid():
            employee.save()
            return Response(employee.data, status=status.HTTP_201_CREATED)
        print(employee.errors)
        print(request.data)
        return Response("Not create!", status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: rest_framework.request.Request, id: int = None, *args, **kwargs):
        if id:
            employee = Employee.objects.filter(id=id)
            if employee:
                return Response(EmployeeSerializer(employee[0], many=False).data)
        else:
            self.queryset = Employee.objects.all()
            return self.list(request, *args, **kwargs)
        return Response("Not employee!")

    @staticmethod
    def delete(request: rest_framework.request.Request, id: int):
        Employee.objects.filter(id=id).delete()
        return Response("Deleted!")

    @staticmethod
    def put(request: rest_framework.request.Request, id: int):
        employee = Employee.objects.filter(id=id)
        print(True)
        if employee:
            serializer = EmployeeSerializer(employee[0], data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            print(serializer.errors)
        return Response("Not employee!", status=status.HTTP_400_BAD_REQUEST)


class EmployeeHomeView(ListAPIView, APIView):
    permission_classes = ()
    queryset = []
    serializer_class = EmployeeSerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        self.queryset = Employee.objects.all()[:3]
        return self.list(request, *args, **kwargs)
