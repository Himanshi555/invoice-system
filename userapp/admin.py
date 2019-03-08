from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile,Employee,Customer
from django.contrib.auth.admin import UserAdmin

class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User
        verbose_name_plural = 'Profile'

admin.site.register(Profile,UserAdmin)
admin.site.register(Employee)
admin.site.register(Customer)
