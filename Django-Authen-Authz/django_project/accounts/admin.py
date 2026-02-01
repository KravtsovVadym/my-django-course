from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from accounts.models import User
from accounts.forms import CreateUserForm, ChangeUserForm


@admin.register(User)
class UserAdmin(BaseAdmin):
    form = ChangeUserForm
    add_form = CreateUserForm

    list_display = [
        'email',
        'first_name',
        'last_name',
        'created_at',
        'is_superuser'
    ]
    list_filter = ['is_superuser']
    fieldsets = [
        (
            None,
            {
                'fields': [
                    'email',
                    'first_name',
                    'last_name',
                    'is_superuser'
                ]
            }
        ),
    ]
    add_fieldsets = [
        (
            None,
            {
                'fields': [
                    'email',
                    'first_name',
                    'last_name',
                    'password1',
                    'password2',
                    'is_superuser'
                ]
            }
        ),
    ]
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()

admin.site.unregister(Group)