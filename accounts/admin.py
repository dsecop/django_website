from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.forms import UserRegistrationForm, UserChangeForm
from accounts.models import User


class UserAdmin(UserAdmin):
    add_form = UserRegistrationForm
    form = UserChangeForm
    model = User
    list_display = (
        'email',
        'first_name',
        'last_name',
        'username',
        'is_staff',
        'is_active',
    )

    # Change user
    fieldsets = (
        ('Dane osobowe', {'fields': ('email', 'username', 'first_name', 'last_name', 'website', 'photo')}),
        ('Adres', {'fields': ('postcode', 'address',)}),
        ('Konto', {'fields': ('user_type',)}),
        ('Uprawnienia', {'fields': ('is_staff', 'is_active', 'is_superuser', 'user_permissions', 'groups',)}),
    )

    # Add user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff')
        }),
    )


admin.site.register(User, UserAdmin)
