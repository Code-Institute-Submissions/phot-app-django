from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Pictures

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'full_name', 'email','introduction', 'profile_picture')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'full_name','introduction' ,'email', 'profile_picture')
        

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['portfolio']
        