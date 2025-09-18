from django.contrib import admin
from petstagram.pets.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "date_of_birth", "slug")

    search_fields = ("name", "slug")
    list_filter = ("date_of_birth",)