from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Add your custom fields to fieldsets
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

    # Add fields to display when creating a new user via admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

    # Show in admin list view
    list_display = ['username', 'email', 'first_name', 'last_name', 'date_of_birth', 'is_staff']
    search_fields = ['username', 'email']

admin.site.register(CustomUser, CustomUserAdmin)
