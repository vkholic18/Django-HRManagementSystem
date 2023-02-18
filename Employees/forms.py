from django import forms

from .models import Employee,Team,EmployeeNotes
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm



class LoginForm(AuthenticationForm):
     error_messages = {
        'invalid_login': "Please enter a correct %(username)s and password. Note that both fields may be case-sensitive.",
    }
   

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        
class TeamForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=Employee.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Team
        fields = ['name', 'team_leader', 'members']
        


class EmployeeNoteForm(forms.ModelForm):
    class Meta:
        model = EmployeeNotes
        fields = ['content']