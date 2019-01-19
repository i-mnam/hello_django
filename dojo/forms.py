# dojo/forms.py

from django import forms


def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요.')


class PostForm(forms.Form):
    title = forms.CharField(Validator=[min_length_3_validator])
    content = forms.CharField(widget=forms.Textarea)
    #class로 지정하면 django가 알아서 인스턴스로 제공 / .Textarea()라고 인스턴스로 적어도 됨..
    # python입장에서는 문자열에 길이 제한이 있던 없던 상관없다. 타입은 같지만 widget은 다르게 보여줄 수 있다.