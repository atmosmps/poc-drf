
def reprove_comments(modeladmin, request, queryset):
    queryset.update(approved=False)


def aprove_comments(modeladmin, request, queryset):
    queryset.update(approved=True)


reprove_comments.short_description = "Reprova comentários"
aprove_comments.short_description = "Aprova comentários"
