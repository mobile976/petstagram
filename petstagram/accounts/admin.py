from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "gender",
    )
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("gender",)
