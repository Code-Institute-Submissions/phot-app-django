from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('profile/', views.uploadImage, name='profile'),
    path('profile/<int:pk>', views.delete_picture, name='delete_picture'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]