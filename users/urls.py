from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('profile/', views.uploadImage, name='profile'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]