from django.shortcuts import render, get_object_or_404
from users.models import Pictures


def profile_page(request, pk):
    image = get_object_or_404(Pictures, pk=pk)
    return render(request, 'profile_page/profile_page.html', {'image': image})
