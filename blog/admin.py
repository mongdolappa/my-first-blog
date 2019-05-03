from django.contrib import admin
from .models import Post, Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)

#@admin.register(Post)
#class PostAdmin(admin.ModelAdmin):
#    list_display = ['id', 'title','is_public', 'created_date']
#    list_display_links = ['title']
#    list_editable = ['is_public']

