from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'department')

admin.site.register(CustomUser, CustomUserAdmin)
