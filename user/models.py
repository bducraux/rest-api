from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create(self, email, password, is_admin=False, is_staff=False):
        if not email:
            raise ValueError("User must have an email.")

        if not password:
            raise ValueError("User must have a password.")

        user = self.model(email=self.normalize_email(email))

        user.admin = is_admin
        user.staff = is_staff
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create(email, password, is_admin=True, is_staff=True)

        return user


class User(AbstractBaseUser):
    email = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=100)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    USERNAME_FIELD = 'email'
