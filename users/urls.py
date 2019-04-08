from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]