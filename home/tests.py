from django.test import TestCase
from django.shortcuts import reverse
from home.views import get_all_images
from users.models import Pictures


class Test_Home_view(TestCase):
    
    def create_picture(self, picture="only a test"):
        return Pictures.objects.create(picture=picture)