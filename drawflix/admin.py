from django.contrib import admin
from drawflix.models import Film, Drawing, Like, UserProfile


admin.site.register(UserProfile)
admin.site.register(Film)
admin.site.register(Drawing)
admin.site.register(Like)
