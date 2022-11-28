from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from uuid import uuid4


class Users(AbstractUser):
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    email = models.EmailField(
        _("email address"),
        max_length=255,
        unique=True,
        help_text="Email is unique with 255 char length, and used for user authentication",
    )
    phone = models.CharField(
        _("phone number"),
        max_length=25,
        unique=True,
        help_text="Phone is unique with 25 char length, and used for user authentication",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name", "phone"]

    def __str__(self) -> str:
        return self.username

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
