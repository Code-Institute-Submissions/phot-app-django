from django.shortcuts import render, get_object_or_404
from users.models import Pictures, CustomUser
from django.shortcuts import render

def get_all_images(request):
    images = Pictures.objects.all().order_by('-date')
    return render(request, 'home/home.html', {'images': images})