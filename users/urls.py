from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('profile/', views.UploadImageView.as_view(), name='profile'),
    path('profile/', views.ShowPortfolioImagesList.as_view(), name='profile'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]