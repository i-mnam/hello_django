# dojo/models.py

from django import forms
from django.db import models


def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요.')


class Post(models.Model):
    title = models.CharField(max_length=100, validators=[min_length_3_validator])
    content = models.TextField()
    ip = models.CharField(max_length=15) 
    # '' user로 부터 입력받는 정보 아님!
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
