from django.contrib import admin
from . models import UserProfile

# Register your models here.
admin.site.register(UserProfile)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']