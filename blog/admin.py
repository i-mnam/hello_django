# blog/admin.py

from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Comment, Tag


# admin.site.register(Post)
# 장식자 형태로 지원
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size', 'status', 'created_at', 'updated_at']
    actions = ['make_draft', 'make_published']

    def content_size(self, post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    content_size.short_description = '글자수'

    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='d')
        self.message_user(request, '{}건의 포스팅을 Draft상태로 변경'.format(updated_count))
    make_draft.short_description = '지정 포스팅을 Draft상태로 변경합니다.'

    def make_published(self, request, queryset): # 어떠한 데이터가 선택되었는지 알 수 있게 queryset 인자가 있어야해.
        published_count = queryset.update(status='p')
        self.message_user(request, '{}건의 포스팅을 Published상태로 변경'.format(published_count))
    make_published.short_description = '지정 포스팅을 Published상태로 변경합니다.'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']