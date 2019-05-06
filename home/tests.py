from django.test import TestCase
from django.shortcuts import reverse
"""
from users.models import Pictures


class PicturesListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_pictures = 15

        for pictures_id in range(number_of_pictures):
            Pictures.objects.create(
                picture='test {}'.format(pictures_id), 
                
            )
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html')
    

    def test_pagination_is_fifteen(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['images_list']) == 15)
"""