from rest_framework.serializers import  ModelSerializer
from .models import CompanyModel

class CompanySerializer(ModelSerializer):
    class Meta:
        model = CompanyModel
        exclude = ['employee']
