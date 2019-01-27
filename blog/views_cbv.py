# blog/view_cbv.py

from django import forms
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Post

post_list = ListView.as_view(model=Post, paginate_by=10)
# http://localhost:8080/blog/?page=2
post_detail = DetailView.as_view(model=Post, pk_url_kwarg='id')

'''
# blog/forms.py
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    # success_url = '/...'
'''
#post_new = PostCreateView.as_view()
post_new = CreateView.as_view(model=Post)

post_edit = UpdateView.as_view(model=Post, fields='__all__')
post_delete = DeleteView.as_view(model=Post, success_url='/blog/')