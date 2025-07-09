from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm  # Форма для СОЗДАНИЯ пользователя
    form = CustomUserChangeForm # Форма для РЕДАКТИРОВАНИЯ пользователя
    model = CustomUser  # Указываем кастомную модель пользователя
    list_display = ["email", "username", "name", "is_staff",]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),) # стандартные группы полей (логин, права, группы и т.д.).
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),) # Аналогично fieldsets, но для формы создания пользователя. Добавляет поле name при регистрации нового пользователя через админку.

admin.site.register(CustomUser, CustomUserAdmin)