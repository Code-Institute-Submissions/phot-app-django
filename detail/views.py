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
 

"""
Match the comment with the picture you're commenting on 
"""
def comments_detail_page(request):
    
    if request.method == 'POST':
        comment = CommentForm(request.POST, request.FILES)
        if comment.is_valid():
            comment.save()
            return redirect(all_comments_page)
    
    else: 
        comment = CommentForm()
        
    return render(request, 'detail/comment.html', {'comment': comment})
    
    
def all_comments_page(request):
    
    comments = Comment.objects.all().order_by('-date')
    return render(request, 'detail/comments.html', {'comments': comments})