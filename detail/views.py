from django.shortcuts import render, get_object_or_404, redirect, reverse
from users.models import Pictures, CustomUser
from django.shortcuts import render

def detail_image(request, pk):
    image = get_object_or_404(Pictures, pk=pk)
    image.views +=1
    image.save()
    return render(request, 'detail/detail.html', {'image': image})