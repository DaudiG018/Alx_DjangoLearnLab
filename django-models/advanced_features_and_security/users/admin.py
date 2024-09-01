from django.contrib import admin

# Register your models here.
 
 # admin.py

from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm  # type: ignore # You will need to create this form
    form = CustomUserChangeForm  # type: ignore # You will need to create this form
    list_display = ('email', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)

# management/commands/setup_permissions.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from myapp.models import Article

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Create Groups
        editors, created = Group.objects.get_or_create(name='Editors')
        viewers, created = Group.objects.get_or_create(name='Viewers')
        admins, created = Group.objects.get_or_create(name='Admins')

        # Define Permissions
        can_view = Permission.objects.get(codename='can_view', content_type__app_label='myapp')
        can_create = Permission.objects.get(codename='can_create', content_type__app_label='myapp')
        can_edit = Permission.objects.get(codename='can_edit', content_type__app_label='myapp')
        can_delete = Permission.objects.get(codename='can_delete', content_type__app_label='myapp')

        # Assign Permissions to Groups
        editors.permissions.add(can_edit, can_create)
        viewers.permissions.add(can_view)
        admins.permissions.add(can_view, can_create, can_edit, can_delete)
