from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    account = models.OneToOneField(
        "bank_app.Customer", on_delete=models.CASCADE, null=True, blank=True
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["password"]
    # Add any additional fields you need for registration like address, date of birth, etc.

    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"

    def __str__(self):
        return self.username


class Meta:
    verbose_name = "Custom User"
    verbose_name_plural = "Custom Users"


# Add related_name for groups and user_permissions
CustomUser._meta.get_field("groups").remote_field.related_name = "customuser_groups"
CustomUser._meta.get_field("user_permissions").remote_field.related_name = (
    "customuser_user_permissions"
)
