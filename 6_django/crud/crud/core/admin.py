from django.contrib import admin
from .models import UserModel
# Register your models here.

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "user_name", "phone_number"]