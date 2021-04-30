from django.test import TestCase
from django.http import HttpRequest
from django.urls import resolve
from PresList.views import homepage
from django.template.loader import render_to_string
class HomePageTest(TestCase):
	def test_root_url_resolves_to_home_page_views(self):
		found = resolve('/')
		self.assertEqual(found.func, homepage)
	def test_home_page_return_correct_html(self):
		request = HttpRequest()
		response = homepage(request)
		expected_html = render_to_string('homepage.html')
	def test_save_POST_request(self):
		response = self.client.post('/', data={'permit': 'permit'})
		self.assertIn('permit', response.content.decode())
		#self.assertTemplateUsed(response,'homepage.html')
		#self.assertTrue(response.content.startswith(b'<html>'))
		#self.assertIn(b'<title>Rawr</title>',response.c