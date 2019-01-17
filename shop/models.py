# shop/models.py

from django.conf import settings
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
    # related_name = '+' : user.post_set.all() 방식의 접근을 포기하겠다는 것
    # shop.models.Post.objects.filter(user=user) 여전히 유효
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)