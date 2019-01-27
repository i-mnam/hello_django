# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        #fields = ('username', 'email') # fields만 재정의하겠다.
        # ModelForm has no model class specified.
        # 기존 meta class를 재정의 하는바람에 기존 것을 다 날림.. 그래서 이런 오류남
        fields = UserCreationForm.Meta.fields + ('email',)
        # 더하는 방식이 매우 독특함..
        # TypeError: can only concatenate tuple (not "str") to tuple