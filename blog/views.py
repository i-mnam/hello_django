# blog/views.py

from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    qs = Post.objects.all() # django.db.models.query.QuerySet
    q = request.GET.get('q', '') # str
    '''
    QueryDict.get(key, default=None)
    Uses the same logic as __getitem__()
    , with a hook for returning a default value if the key doesn’t exist.
    '''
    
    if q:
        qs = qs.filter(title__icontains=q) # _ * 2 !! not once!!!

    return render(request, 'blog/post_list.html', {
        'post_list' : qs,
        'q' : q,
    })


def post_detail(request, id):
    '''
    python3.6 manager.py shell
    from blog.models import Post
    Post.objects.filter(id=1002).delete()  
    '''

    '''
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404
    이렇게 404예외처리 안해주면 디버그모드로 매우 안예쁘게 나온다.
    지정 Record가 없는 것은 서버오류가 아닙니다 (!= 500)
    '''

    post = get_object_or_404(Post, id=id)

    return render(request, 'blog/post_detail.html', {
        'post': post,
    })