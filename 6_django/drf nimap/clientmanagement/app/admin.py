from django.contrib import admin
from .models import Client
# Register your models here.

# admin.site.register(Client)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["id", "client_name", "created_by", "created_at", "updated_at"]