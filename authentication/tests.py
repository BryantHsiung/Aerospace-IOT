from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.
class ViewsTestCase(TestCase):

    # Create a fake user for testing purpose
    def setUp(self):
        self.username = "testuser"
        self.password = "testpassword"
        self.user = get_user_model().objects.create_user(username = self.username, password = self.password)

    def test_login_view(self):
        # Test login with valid credentials
        response = self.client.post(reverse('login'), {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 302)  # Should redirect to 'home'

        # Test login with invalid credentials
        response = self.client.post(reverse('login'), {'username': 'invaliduser', 'password': 'invalidpassword'})
        self.assertEqual(response.status_code, 200)  # Should stay on the login page
        self.assertContains(response, "Invalid username or password")  # Check for error message in response content

    def test_logout_view(self):
        # Log in the user first
        self.client.login(username=self.username, password=self.password)
        
        # Test logout view
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Should redirect to 'login'

    def test_register_view(self):
        # Test register view with valid form data
        response = self.client.post(reverse('register'), {'username': 'newuser', 'password1': 'newpassword', 'password2': 'newpassword'})
        self.assertEqual(response.status_code, 200)  # Should redirect to 'home'


        # Test register view with invalid form data
        response = self.client.post(reverse('register'), {'username': 'newuser', 'password1': 'password', 'password2': 'password'})
        self.assertEqual(response.status_code, 200)  # Should stay on the registration page
        self.assertContains(response, "error")  # Check for error message in response content


    def test_home_view(self):
        # Test home view when the user is not logged in
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)  # Should return a success response
        self.assertContains(response, "Welcome to Our Website!")  # Check for a specific content in response

        