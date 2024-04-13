from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from .managers import MyUserManager


class User(AbstractBaseUser):
    username = models.CharField(
        max_length=123,
        unique=True
    )
    email = models.EmailField(
        unique=True,
        blank=True,
        null=True
    )
    phone_number = models.CharField(
        max_length=13,
        unique=True
    )
    status = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Обычный пользователь'),
            (2, 'Суперпользователь')
        ),
        default=1
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )

    is_admin = models.BooleanField(
        default=False
    )

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin

