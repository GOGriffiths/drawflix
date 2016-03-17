from django.contrib import admin

from drawflix.models import Drawing


class DrawingAdmin(admin.ModelAdmin):

    list_display = ('film', 'user', 'likes', 'date')

admin.site.register(Drawing, DrawingAdmin)
