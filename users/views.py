from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from users.forms import CustomUserCreationForm, UploadImageForm, DeleteForm
from users.models import CustomUser, Pictures
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from home.views import get_all_images

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def uploadImage(request):
    user=request.user
    portfolio_posts = Pictures.objects.filter(user=user).order_by('-date')
    
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    else : 
        form = UploadImageForm()
        
    return render(request, 'users/profile.html', {'form': form, 'portfolio_posts': portfolio_posts})


def delete_picture(request, pk):
    if request.method == 'POST':
        picture = Pictures.objects.get(pk=pk)
        picture.delete()
    return redirect(uploadImage)
        
        
        
        
        
        