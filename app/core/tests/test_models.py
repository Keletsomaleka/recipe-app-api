"""Tests for models"""

from django.test import TestCase
# base test class
from django.contrib.auth import get_user_model
# helper function


class ModelTests(TestCase):

    """Test models"""

    def test_create_user_with_email_successful(self):

        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))