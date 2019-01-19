# dojo/forms.py

from django import forms
from .models import Post


'''
def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요.')
'''

class PostForm(forms.Form):
    #title = forms.CharField(validators=[min_length_3_validator])
    #not 함수 호출! 리스트로 함수를 연결한 것. python은 일급객체를 지원하기 때문에 함수를 위와같이 넘겨 연결시킨다.
    content = forms.CharField(widget=forms.Textarea)
    #class로 지정하면 django가 알아서 인스턴스로 제공 / .Textarea()라고 인스턴스로 적어도 됨..
    # python입장에서는 문자열에 길이 제한이 있던 없던 상관없다. 타입은 같지만 widget은 다르게 보여줄 수 있다.

    def save(self, commit=True):
        post = Post(**self.cleaned_data) # self.* self.incetance.*
        if commit:
            post.save()
        return post



# 생성되는 Form Field는 PostForm과 거의 동일
class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content'] #'ip']