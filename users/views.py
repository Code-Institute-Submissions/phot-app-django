from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from users.forms import CustomUserCreationForm, UploadImageForm
from users.models import CustomUser, Pictures
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
 
    
class UploadImageView(generic.CreateView):
    form_class = UploadImageForm
    success_url = reverse_lazy('profile')
    template_name = 'users/profile.html'
    
    def get_queryset(self):
        return Pictures.objects.filter(user=self.request.user)


class ShowPortfolioImagesList(ListView):
    template_name = 'users/portfolio.html'
    context_object_name = 'pictures_list'
    ordering = ['-date']
    
    def get_queryset(self):
        return Pictures.objects.filter(user=self.request.user)