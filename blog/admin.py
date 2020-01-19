from django.contrib import admin

from .models import Post


@admin.register(Post)
class  PostAdmin(admin.ModelAdmin):
    list_display= ["pk",'title','author_name','content']
    list_display_links = ['title']
    search_fields = ['title']
    list_filter = ['updated_at']

