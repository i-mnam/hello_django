# blog/view_cbv.py

from django import forms
from django.core.urlresolvers import reverse, reverse_lazy
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
#post_delete = DeleteView.as_view(model=Post, success_url='/blog/')
post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('blog:post_list'))# reverse
'''  현재 프로젝트가 초기화 되는 시점에 reverse를 수행하려 해서 error나는 것. 초기화 후에 실행되어야 하므로 > reverse_lazy
django.core.exceptions.ImproperlyConfigured: The included URLconf 'askdjango.urls' does not appear to have any patterns in it. If you see valid patterns in the file then the issue is probably caused by a circular import.
'''