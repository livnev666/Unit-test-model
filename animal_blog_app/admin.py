from django.contrib import admin
from .models import Animal

# Register your models here.


@admin.register(Animal)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'breed', 'nickname', 'age', 'email']
    list_display_links = ['nickname']
    ordering = ['id']
