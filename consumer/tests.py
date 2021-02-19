"""Test for Consumer app"""

import json

from django.contrib.auth import get_user_model
# 3rd party imports
from django.test import TestCase
from django.urls import reverse
from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase

# App imports
from consumer.models import CustomUser, ProductCategory


class ProductTest(TestCase):

    def setUp(self):
        self.product_category = mommy.make(ProductCategory)

    def test_products_by_category_link(self):
        response = self.client.get(reverse('consumer:product_by_category', kwargs={'product_category_id': 1}))
        self.assertEqual(response.status_code, 200)


class HomePageTest(TestCase):

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('home.html')


class SignUpPageTests(TestCase):

    username = 'testuser'
    email = 'testuser@example.com'

    def test_signup(self):
        response = self.client.get('/consumer/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('consumer:register'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('consumer:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('registration/register.html')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)


class TestApiConsumer(APITestCase):

    def setUp(self) -> None:
        self.user = CustomUser.objects.create_user('SomeOne', 'mymail@ex.com', age=10)
        self.user.save()

    def test_users_api(self):
        response = self.client.get('/api/v1/consumer/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(response.content)), 1)

    def test_user_details(self):
        response = self.client.get('/api/v1/consumer/users/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['username'], self.user.username)
