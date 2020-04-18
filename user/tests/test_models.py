from django.test import TestCase
from django.contrib.auth import get_user_model


class UserModelTests(TestCase):

    def test_create_user_valid(self):
        user = get_user_model().objects.create_user(email='test@test.com', password='testpass')
        self.assertEqual(user.email, 'test@test.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user_invalid(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email='', password='testpass')

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(email='test@test.com', password='testpass')
        self.assertEqual(user.email, 'test@test.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_create_super_user_invalid(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_superuser(email='', password='testpass')
        
        




    


