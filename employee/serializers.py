from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from company.serializers import CompanySerializer

EmployeeModel = get_user_model()

class EmployeeSerializer(ModelSerializer):
    company = CompanySerializer(many=True, required=False)
    class Meta:
        model = EmployeeModel
        fields = ['id','email',  'password', 'name', 'surname', 'age', 'profession', 'company']
        extra_kwargs ={
            'password': {'write_only': True}
        }

    def create(self, validated_data):

        employee = EmployeeModel.objects.create_employee(**validated_data)
        return employee
