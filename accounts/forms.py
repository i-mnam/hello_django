# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignupForm(UserCreationForm):
    phone_number = forms.CharField() # 이 줄만 추가한다고 전화번호가 저장되지 않음. 
    # 현재 폼은 UserCreationForm으로 되어 있어 추가필드는 직접 저장해줘야 한다.
    address = forms.CharField()
    
    class Meta(UserCreationForm.Meta):
        #fields = ('username', 'email') # fields만 재정의하겠다.
        # ModelForm has no model class specified.
        # 기존 meta class를 재정의 하는바람에 기존 것을 다 날림.. 그래서 이런 오류남
        fields = UserCreationForm.Meta.fields + ('email',)
        # 더하는 방식이 매우 독특함..
        # TypeError: can only concatenate tuple (not "str") to tuple

    def save(self):
        user = super().save()
        profile = Profile.objects.create(
            user = user,
            phone_number = self.cleaned_data['phone_number'],
            address = self.cleaned_data['address']
        )
        return user