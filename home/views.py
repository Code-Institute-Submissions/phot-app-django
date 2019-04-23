from django.shortcuts import render, get_object_or_404
from users.models import Pictures, CustomUser
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_all_images(request):
    images_list = Pictures.objects.all().order_by('-date')
    page = request.GET.get('page', 1)
    paginator = Paginator(images_list, 5)
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage: 
        images = paginator.page(paginator.num_pages)
    
    return render(request, 'home/home.html', {'images': images})
    
def explore(request):
    return render(request, 'explore/explore.html')