from django.contrib import admin
from .models import CustomUser, UserProfile
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
# User = get_user_model()
# admin.site.unregister(User)


class UserProfileInLine(admin.StackedInline):
    model = UserProfile



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'title')
            }
         ),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions'),
            }
        ),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'is_staff')
    inlines = [UserProfileInLine]



admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(CustomUser)

