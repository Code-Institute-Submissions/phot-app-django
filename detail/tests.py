from django.test import TestCase
from django.shortcuts import reverse
from users.models import Pictures


class PicturesListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Pictures.objects.create(picture="test")
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/details/image/<int:pj>')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('detail_image'))
        self.assertEqual(response.status_code, 200)
       
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('detail_image'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail/detail.html')