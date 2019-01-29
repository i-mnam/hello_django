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
    # pass
    list_display = ['id', 'author', 'post_content_len']
    # list_display = ['post'] # post의 __str__ 으로 'POST'항목에 출력됨.
    def post_content_len(self, comment):
        return '{}글자'.format(len(comment.post.content))
    '''
    SELECT
    "blog_comment"."id", "blog_comment"."post_id", "blog_comment"."author"
    , "blog_comment"."message", "blog_comment"."created_at"
    , "blog_comment"."updated_at"
    FROM "blog_comment" ORDER BY "blog_comment"."id" DESC LIMIT 100
    1.8005134478540292%
    0.25	
    Sel Expl



    SELECT
    "blog_post"."id", "blog_post"."user_id", "blog_post"."title"
    , "blog_post"."content", "blog_post"."photo", "blog_post"."created_at"
    , "blog_post"."updated_at", "blog_post"."tags", "blog_post"."lnglat"
    , "blog_post"."status"
    FROM "blog_post" WHERE "blog_post"."id" = '1003'
    3 similar queries.   Duplicated 2 times. # 이렇게 중복될 수도 있지 Comment에서는! 
    '''
    # 105, 13ms   5, 1ms
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # return qs
        return qs.select_related('post')
    '''
    FROM "blog_comment" INNER JOIN "blog_post" 
    ON ("blog_comment"."post_id" = "blog_post"."id") 
    ORDER BY "blog_comment"."id" DESC LIMIT 100
    '''

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']