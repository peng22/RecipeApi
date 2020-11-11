from django.test import TestCase
from django.contrib.auth import get_user_model


class modelTests(TestCase):
    def test_create_user_with_email_successful(self):
        '''
        test creating new user and email is successful
        '''
        email="peng@peng.peng"
        password="Test1234@"
        user=get_user_model().objects.create_user(
         email=email,
         password=password
         )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalised(self):
        "check that case is not sensitive"
        email="peng@PENG.PENG"
        user=get_user_model().objects.create_user(email=email)
        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None)

    def test_create_super_user(self):
        email="peng@peng.com"
        user=get_user_model().objects.create_super_user(email=email)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
