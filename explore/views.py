from django.shortcuts import render
from users.models import Pictures
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def get_category_nature(request):
    
    nature_list = Pictures.objects.filter(category__exact="nature").order_by('-date')
    page = request.GET.get('page', 1)
    paginator = Paginator(nature_list, 15)
    try:
        nature = paginator.page(page)
    except PageNotAnInteger:
        nature = paginator.page(1)
    except EmptyPage: 
        nature = paginator.page(paginator.num_pages)
    return render(request, 'explore/nature.html', {'nature': nature})



def get_category_animals(request):
    
    animals_list = Pictures.objects.filter(category__exact="animals").order_by('-date')
    page = request.GET.get('page', 1)
    paginator = Paginator(animals_list, 15)
    try:
        animals = paginator.page(page)
    except PageNotAnInteger:
        animals = paginator.page(1)
    except EmptyPage: 
        animals = paginator.page(paginator.num_pages)
        
    return render(request, 'explore/animals.html', {'animals': animals})


   
def get_category_cars(request):
    
    cars_list = Pictures.objects.filter(category__exact="cars").order_by('-date')
    page = request.GET.get('page', 1)
    paginator = Paginator(cars_list, 15)
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage: 
        cars = paginator.page(paginator.num_pages)
        
    return render(request, 'explore/cars.html', {'cars': cars})
 
 
    
def get_category_cities(request):
    
    cities_list = Pictures.objects.filter(category__exact="cities").order_by('-date')
    page = request.GET.get('page', 1)
    paginator = Paginator(cities_list, 15)
    try:
        cities = paginator.page(page)
    except PageNotAnInteger:
        cities = paginator.page(1)
    except EmptyPage: 
        cities = paginator.page(paginator.num_pages)
    return render(request, 'explore/cities.html', {'cities': cities})



def get_category_fitness(request):
    
    fitness_list = Pictures.objects.filter(category__exact="fitness").order_by('-date')
    page = request.GET.get('page', 1)
    paginator = Paginator(fitness_list, 15)
    try:
        fitness = paginator.page(page)
    except PageNotAnInteger:
        fitness = paginator.page(1)
    except EmptyPage: 
        fitness = paginator.page(paginator.num_pages)
    return render(request, 'explore/fitness.html', {'fitness': fitness})



def get_category_motorcycles(request):
    
    motorcycles_list = Pictures.objects.filter(category__exact="motorcycle").order_by('-date')
    page = request.GET.get('page', 1)
    paginator = Paginator(motorcycles_list, 15)
    try:
        motorcycles = paginator.page(page)
    except PageNotAnInteger:
        motorcycles = paginator.page(1)
    except EmptyPage: 
        motorcycles = paginator.page(paginator.num_pages)
    return render(request, 'explore/motorcycles.html', {'motorcycles': motorcycles})



def get_category_people(request):
    
    people_list = Pictures.objects.filter(category__exact="people").order_by('-date')
    page = request.GET.get('page', 1)
    paginator = Paginator(people_list, 15)
    try:
        people = paginator.page(page)
    except PageNotAnInteger:
        people = paginator.page(1)
    except EmptyPage: 
        people = paginator.page(paginator.num_pages)
    return render(request, 'explore/people.html', {'people': people})



def get_category_space(request):
    
    space_list = Pictures.objects.filter(category__exact="space").order_by('-date')
    page = request.GET.get('page', 1)
    paginator = Paginator(space_list, 15)
    try:
        space = paginator.page(page)
    except PageNotAnInteger:
        space = paginator.page(1)
    except EmptyPage: 
        space = paginator.page(paginator.num_pages)
    return render(request, 'explore/space.html', {'space': space})
 
 
    
def get_category_technology(request):
    
    technology_list = Pictures.objects.filter(category__exact="technology").order_by('-date')
    page = request.GET.get('page', 1)
    paginator = Paginator(technology_list, 15)
    try:
        technology = paginator.page(page)
    except PageNotAnInteger:
        technology = paginator.page(1)
    except EmptyPage: 
        technology = paginator.page(paginator.num_pages)
    return render(request, 'explore/technology.html', {'technology': technology})
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    