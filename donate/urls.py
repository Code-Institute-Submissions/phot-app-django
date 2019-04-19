from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
        path('plans/', views.DonatePageView.as_view(), name='donate'),
        path('charge_five/', views.charge_five, name='charge_five'),
        path('charge_ten/', views.charge_ten, name='charge_ten'),
        path('charge_fifteen/', views.charge_fifteen, name='charge_fifteen'),
    ]