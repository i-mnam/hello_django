# blog/forms.py

from django import forms
from .models import Post
from askdjango.widgets.google_map_point_widget import LocationWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'lnglat' : LocationWidget,
        }