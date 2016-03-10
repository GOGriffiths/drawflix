from django.contrib import admin
from drawflix.models import Drawing, Like


class FilmAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Drawing)
admin.site.register(Like)

# put this in one line
