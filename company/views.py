from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import  CompanyModel
from .serializers import CompanySerializer

class CompanyListView(ListAPIView):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer
