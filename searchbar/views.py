from django.shortcuts import render
from users.models import Pictures
from django.db.models import Q

def search(request):
    images = Pictures.objects.filter(Q(picture__icontains=request.GET['q']) | Q(category__icontains=request.GET['q']))
    return render(request, 'home/home.html', {'images': images})