from django.shortcuts import render, get_object_or_404, redirect, reverse
from users.models import Pictures, CustomUser
from detail.models import Comment
from django.shortcuts import render
from detail.forms import CommentForm

def detail_image(request, pk):
    image = get_object_or_404(Pictures, pk=pk)
    image.views +=1
    image.save()
    return render(request, 'detail/detail.html', {'image': image})
 
    
def comments_detail_page(request):
    
    if request.method == 'POST':
        comment = CommentForm(request.POST, request.FILES)
        if comment.is_valid():
            comment.save()
            return redirect(detail_image)
    
    else: 
        comment = CommentForm()
        
    return render(request, 'detail/comment.html', {'comment': comment})
    
    
def get_comments_on_detail_page(request):
    comments = get_object_or_404(Comment)
    return render(request, 'detail/detail.html', {'comments': comments})