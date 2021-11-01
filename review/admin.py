from django.contrib import admin

from .actions import reprove_comments, aprove_comments
from .models import Review


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'approved']
    actions = [reprove_comments, aprove_comments]


admin.site.register(Review, CommentsAdmin)
