from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from users.models import CustomUser, Pictures
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.views import generic
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from home.views import get_all_images
from users.forms import ( 
        CustomUserCreationForm, 
        UploadImageForm,
        DeleteForm, 
        EditProfileForm 
        )
from django.views.generic import (
        CreateView, 
        UpdateView, 
        DeleteView,
        ListView, 
        DetailView 
        )
from django.http import (
        HttpResponseForbidden, 
        HttpResponse, 
        HttpResponseRedirect
        )



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
    
        
def edit_profile(request):
    
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(uploadImage)
        
    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'edit_profile/edit_profile.html', {'form': form})
        
       
        
def change_password(request):
    
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(uploadImage)
        else:
            return redirect(change_password)
        
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'edit_profile/edit_password.html', {'form': form})
    
    
    
    
    
        