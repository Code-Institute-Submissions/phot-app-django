from django.test import TestCase
from django.shortcuts import reverse
from users.models import Pictures


class PicturesListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_pictures = 15

        for pictures_id in range(number_of_pictures):
            Pictures.objects.create(
                picture='test {}'.format(pictures_id), 
                
            )
    """
    every view in explore has been tested, 
    it would have made not much sense to rewrite 
    this code over and over again nine times, this 
    code has been used as boiler plate to test all nine views.
    """
    
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/explore/technology/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('technology'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('technology'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'explore/technology.html')

    def test_pagination_is_fifteen(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['images_list']) == 15)