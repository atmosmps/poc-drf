from django.contrib import admin

from .models import Review


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'approved']
    actions = [reprove_comments, aprove_comments]

    def reprove_comments(modeladmin, queryset):
        queryset.update(approved=False)

    def aprove_comments(modeladmin, queryset):
        queryset.update(approved=True)


reprove_comments.short_description = "Reprova comentários"
aprove_comments.short_description = "Aprova comentários"


admin.site.register(Review, CommentsAdmin)
