from django.contrib import admin
from petstagram.pets.models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


# Register your models here.
admin.site.register(Pet)
