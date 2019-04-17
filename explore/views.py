from django.shortcuts import render
from users.models import Pictures
from django.shortcuts import render, get_object_or_404, redirect, reverse

def get_category_nature(request):
    nature = Pictures.objects.filter(category__exact="nature").order_by('-date')
    return render(request, 'explore/nature.html', {'nature': nature})

def get_category_animals(request):
    animals = Pictures.objects.filter(category__exact="animals").order_by('-date')
    return render(request, 'explore/animals.html', {'animals': animals})
    
def get_category_cars(request):
    cars = Pictures.objects.filter(category__exact="cars").order_by('-date')
    return render(request, 'explore/cars.html', {'cars': cars})
    
def get_category_cities(request):
    cities = Pictures.objects.filter(category__exact="citites").order_by('-date')
    return render(request, 'explore/cities.html', {'cities': cities})

def get_category_fitness(request):
    fitness = Pictures.objects.filter(category__exact="fitness").order_by('-date')
    return render(request, 'explore/fitness.html', {'fitness': fitness})

def get_category_motorcycles(request):
    motorcycles = Pictures.objects.filter(category__exact="motorcycles").order_by('-date')
    return render(request, 'explore/motorcycles.html', {'motorcycles': motorcycles})

def get_category_people(request):
    people = Pictures.objects.filter(category__exact="people").order_by('-date')
    return render(request, 'explore/people.html', {'people': people})

def get_category_space(request):
    space = Pictures.objects.filter(category__exact="space").order_by('-date')
    return render(request, 'explore/space.html', {'space': space})
    
def get_category_technology(request):
    technology = Pictures.objects.filter(category__exact="technology").order_by('-date')
    return render(request, 'explore/technology.html', {'technology': technology})
    