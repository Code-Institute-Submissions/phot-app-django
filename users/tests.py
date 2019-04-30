from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from users.models import Pictures, CustomUser
from users.forms import UploadImageForm, EditProfileForm

#models

class PictureTest(TestCase):

    def create_picture(self, picture="only a test"):
        return Pictures.objects.create(picture=picture)

    def test_picture_creation(self):
        w = self.create_picture()
        self.assertTrue(isinstance(w, Pictures))
        self.assertEqual(w.__unicode__(), w.picture)
        
        
        

class CustomUserTest(TestCase):

    def create_email(self, email="only a test"):
        return CustomUser.objects.create(email=email)

    def test_email_creation(self):
        w = self.create_email()
        self.assertTrue(isinstance(w, CustomUser))
        self.assertEqual(w.__unicode__(), w.email)