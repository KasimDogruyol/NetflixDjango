from django.contrib import admin

from movies.models import Kategori, Movie

# Register your models here.
admin.site.register(Movie)
admin.site.register(Kategori)