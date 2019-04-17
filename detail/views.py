from django.shortcuts import render, get_object_or_404, redirect, reverse
from users.models import Pictures, CustomUser
from home.views import get_all_images

def detail_image(request, pk):
    image = get_object_or_404(Pictures, pk=pk)
    image.views +=1
    image.save()
    
    if request.method == 'POST':
        image.likes +=1
        image.save()
        return redirect(get_all_images)
        
    return render(request, 'detail/detail.html', {'image': image})