from django.db import models
from django.contrib.auth import get_user_model

EmployeeModel = get_user_model()
# Create your models here.
class CompanyModel(models.Model):
    class Meta:
        db_table = 'company'
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=40)
    employee  = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE, related_name='company')
from django.db import models

# Create your models here.
