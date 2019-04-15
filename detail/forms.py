from django import forms 
from detail.models import Comment

class CommentForm(forms.ModelForm):
    class Meta: 
        model= Comment
        fields = ["name", "comment"]