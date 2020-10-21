from django.contrib import admin

# Register your models here.
from posts.models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "updated", "timestamp"]
    list_display_links = ["__str__"]
    list_filter = ["title"]
    search_fields = ["title"]
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)