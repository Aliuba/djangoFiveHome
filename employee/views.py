
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from django.contrib.auth import get_user_model

from employee.serializers import EmployeeSerializer
from company.serializers import CompanySerializer

EmployeeModel = get_user_model()
# Create your views here.


class EmployeeListCreateView(ListCreateAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer


class CompanyCreate(CreateAPIView):
    serializer_class = CompanySerializer

    def perform_create(self, serializer):
        employee_id = self.kwargs.get('pk')
        print(employee_id)
        employee = get_object_or_404(EmployeeModel, pk=employee_id)
        serializer.save(employee=employee)
