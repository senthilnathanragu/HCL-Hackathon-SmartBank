from django.contrib.auth.models import AbstractUser
from django.db import models


# Custom User model
class User(AbstractUser):
    ROLE_CHOICES = (
        ("customer", "Customer"),
        ("admin", "Admin"),
        ("auditor", "Auditor"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="customer")

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = "admin"
        super().save(*args, **kwargs)


# Bank Account model
class Account(models.Model):
    ACCOUNT_TYPES = (
        ("savings", "Savings"),
        ("current", "Current"),
        ("fd", "Fixed Deposit"),
    )

    account_number = models.CharField(max_length=12, unique=True)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account_number} - {self.user.username}"
