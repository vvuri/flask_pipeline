from django.contrib import admin
from news.models import Movies, News, Category


class NewsAdmin(admin.ModelAdmin):  # View list in admin panel
    list_display = ('id', 'title', 'category_id', 'create_at', 'update_at', 'is_publish')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_publish',)
    list_filter = ('category_id', 'is_publish')


class CategoryAdmin(admin.ModelAdmin):  # View list in admin panel
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Movies)
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
