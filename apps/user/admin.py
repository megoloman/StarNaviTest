from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from apps.user.models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    list_display = ('email', 'github_name', 'github_id', 'created_at', 'updated_at')
