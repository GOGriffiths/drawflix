from django.contrib import admin
from drawflix.models import Film, Drawing, Like, UserProfile


class FilmAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(UserProfile)
admin.site.register(Film, FilmAdmin)
admin.site.register(Drawing)
admin.site.register(Like)
