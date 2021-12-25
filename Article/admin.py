from django.contrib import admin
from .models import articlesModel


class articlesAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'genre']


admin.site.register(articlesModel, articlesAdmin)
