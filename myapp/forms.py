from django.forms import ModelForm
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class StudentForm(ModelForm):

    class Meta:
        model = Student
        fields = [
            'name',
            'age',
            'email'
        ]

class RegisterForm(UserCreationForm):

    class Meta:

        model = User

        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]