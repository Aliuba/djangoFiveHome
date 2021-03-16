from django.contrib.auth.base_user import BaseUserManager

class CustomEmployeeManager(BaseUserManager):
    def create_employee(self, email, password, **extra_kwargs):
        if not email:
            raise ValueError('The email must be set')
        email = self.normalize_email(email)
        employee = self.model(email= email, **extra_kwargs)
        employee.set_password(password)
        employee.save()
        return employee

