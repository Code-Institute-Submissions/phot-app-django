from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
        path('nature/', views.get_category_nature, name='nature'),
        path('animals/', views.get_category_animals, name='animals'),
        path('cars/', views.get_category_cars, name='cars'),
        path('cities/', views.get_category_cities, name='cities'),
        path('fitness/', views.get_category_fitness, name='fitness'),
        path('motorcycles/', views.get_category_motorcycles, name='motorcycles'),
        path('people/', views.get_category_people, name='people'),
        path('space/', views.get_category_space, name='space'),
        path('technology/', views.get_category_technology, name='technology'),
    ]