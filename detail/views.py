import csv
from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from users.models import Pictures, CustomUser
from home.views import get_all_images
from django.contrib.auth.models import User
from users.models import CustomUser

def detail_image(request, pk):
    image = get_object_or_404(Pictures, pk=pk)
    image.views +=1
    image.save()
    
    if request.method == 'POST':
        image.likes +=1
        image.save()

    return render(request, 'detail/detail.html', {'image': image})
