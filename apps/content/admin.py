from django.contrib import admin
from .models import *


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_date', 'trailer_link', 'description', 'cover_image']
    search_fields = ['title']
    list_filter = ['genres']
admin.site.register(Episode)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Favorite)
admin.site.register(Rating)
admin.site.register(Genre)
admin.site.register(Season)
admin.site.register(Age)