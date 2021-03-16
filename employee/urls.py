from django.urls import path
from .views import EmployeeListCreateView, CompanyCreate

urlpatterns = [
    path('', EmployeeListCreateView.as_view(), name='employee_list_create'),
    path('/<int:pk>/company', CompanyCreate.as_view(), name='employee_company_create' )
]
