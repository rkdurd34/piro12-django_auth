from django.contrib import admin

from .models import Post, Comment


@admin.register(Post)
class  PostAdmin(admin.ModelAdmin):
    list_display= ["pk",'title','author_name','content']
    list_display_links = ['title']
    search_fields = ['title']
    list_filter = ['updated_at']

@admin.register(Comment)
class  CommentAdmin(admin.ModelAdmin):
    list_display= ["pk",'post','message']
    list_display_links = ['post']
    search_fields = ['post']
    list_filter = ['message']

