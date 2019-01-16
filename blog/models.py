# blog/models.py

import re
from django.db import models
from django.forms import ValidationError



def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100, verbose_name='제목',
        help_text='포스팅 제목을 입력해주세요. 최대 100자 내외.')  # 길이 제한이 있는 문자열
    content = models.TextField(verbose_name='내용')        # 길이 제한이 없는 문자열
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True,
        validators=[lnglat_validator], help_text='경도/위도 포맷으로 입력')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    # add!
    tag_set = models.ManyToManyField('Tag', blank=True) #class 형태로 입력하지 않는 이유: Tag가 Post 보다 하위에 정의되어 있어서.
    class Meta:
        ordering = ['-id'] # ['-id']

    def __str__(self): # don't need to migrate
        return self.title 


class Comment(models.Model):
    post = models.ForeignKey(Post) 
    # POINT! 실제 DB에는 post_id 라고 저장됨. # blog_post라는 table도 만들어지나 보다.
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #def __str__(self):
    #    return self.message # print by title


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
'''
 Post.objects.filter(tag_set__name__in=['puttyTeaRi', 'YeJi_Putty'])
Out[4]: <QuerySet [<Post: 제목 #999>, <Post: 제목 #999>, <Post: 제목 #997>]>
'''