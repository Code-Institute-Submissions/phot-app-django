from django.shortcuts import render
from django.urls import reverse_lazy
from users.forms import CustomUserCreationForm, UploadImageForm
from users.models import CustomUser, Pictures
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#use it to redirect a user to the login page before accessing a certain page
#  login_url = '/'

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'
    
class UploadImageView(generic.CreateView):
    form_class = UploadImageForm
    success_url = reverse_lazy('profile')
    template_name = 'users/profile_list.html'
    
class ShowPortfolioImagesList(ListView):
    template_name = 'users/profile_list.html'
    queryset = Pictures.objects.all()
    context_object_name = 'pictures'
    ordering = ['-views']
    paginate_by = 10
    

    
    

