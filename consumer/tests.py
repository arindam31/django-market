from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


class ProductTest(TestCase):

    def test_all_products(self):
        response = self.client.get(reverse('allProducts'))  # No need to create self.client. Its omni present.
        self.assertEqual(response.status_code, 200)


class HomePageTest(SimpleTestCase):

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
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('registration/register.html')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)