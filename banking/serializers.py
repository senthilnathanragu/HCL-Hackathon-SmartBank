from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Account
import random

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    # Write-only password for security
    password = serializers.CharField(write_only=True, required=True, min_length=6)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "role")

    def create(self, validated_data):
        # Hash password and set default role
        user = User(
            username=validated_data["username"],
            email=validated_data["email"],
            role=validated_data.get("role", "customer"),
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["account_type", "initial_deposit"]

    def generate_unique_account_number(self):
        # Ensure account number is unique
        while True:
            account_number = str(random.randint(100000000000, 999999999999))
            if not Account.objects.filter(account_number=account_number).exists():
                return account_number

    def create(self, validated_data):
        validated_data["account_number"] = self.generate_unique_account_number()
        return super().create(validated_data)