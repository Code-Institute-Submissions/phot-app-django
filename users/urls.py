from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('profile/', views.uploadImage, name='profile'),
    path('profile/<int:pk>', views.delete_picture, name='delete_picture'),
    path('profile/edit', views.edit_profile, name="edit_profile"),
    path('change-password', views.change_password, name="change_password"),
    path('signup/', views.SignUp.as_view(), name='signup'),
]