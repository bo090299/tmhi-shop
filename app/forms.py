from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Appointment

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['customer_name', 'phone_number', 'appointment_date']