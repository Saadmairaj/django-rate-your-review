from django import forms
from .models import Review
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'text',)
