from django.contrib import admin

# Register your models here.
from posts.models import Post


class PostsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostsAdmin)