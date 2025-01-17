from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'status', 'created_date', 'is_admin')
    list_filter = ('is_admin', 'status', 'created_date')
    fieldsets = (
        (None, {'fields': (
            'password',
            'username',
            'phone_number',
            'email',
            'status',)}),
        ('Permissions', {'fields': ('is_admin', )}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'phone_number',
                'status',
                'password1',
                'password2'),
        }),
    )
    search_fields = ('phone_number', 'username', 'email')
    ordering = ('phone_number', 'created_date')
    filter_horizontal = ()


admin.site.register(User, UserAdmin)