from django.test import TestCase
from .models import User


class UserTests(TestCase):
    def test_is_not_none(self):
        user = User.objects.create("test@test.com", "123")

        self.assertIs(user is not None, True)

        return user

    def test_is_not_admin(self):
        user = self.test_is_not_none()

        self.assertIs(user.admin, False)
