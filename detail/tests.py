from django.test import TestCase
from . import views 
from detail import views 
from django.urls import reverse
from home.views import get_all_images
from users.models import Pictures