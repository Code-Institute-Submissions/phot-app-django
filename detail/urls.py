from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
        path('image/<int:pk>', views.detail_image, name="detail_image"),
    ]