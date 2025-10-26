from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Account

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'email', 'role', 'is_active', 'is_staff', 'is_superuser')
    list_display_links = ('username', 'email')  # Make username/email clickable
    search_fields = ('username', 'email')
    list_filter = ('role', 'is_active', 'is_staff', 'is_superuser')

    # Optional: customize forms
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role'),
        }),
    )

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'account_number', 'user', 'account_type', 'balance', 'created_at')
    search_fields = ('account_number', 'user__username')
    list_filter = ('account_type',)
