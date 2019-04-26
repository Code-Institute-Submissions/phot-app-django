from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Pictures
from django.contrib.auth.models import User

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
        model = Pictures
        fields = ['picture', 'category']

class DeleteForm(forms.ModelForm):
    class Meta:
        model = Pictures
        fields = []
       
        
class EditProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('full_name', 'first_name', 'last_name', 'email', 'password')
        