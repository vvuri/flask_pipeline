from django.contrib import admin
from news.models import Movies, News


class NewsAdmin(admin.ModelAdmin):  # View list in admin panel
    list_display = ('id', 'title', 'create_at', 'update_at', 'is_publish')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


admin.site.register(Movies)
admin.site.register(News, NewsAdmin)
