# blog/views.py

from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm


def post_list(request):
    print(repr(request.user))
    # <SimpleLazyObject: <function AuthenticationMiddleware.process_request.<locals>.<lambda> at 0x1105afb70>>

    qs = Post.objects.all() # django.db.models.query.QuerySet
    q = request.GET.get('q', '') # str
    '''
    QueryDict.get(key, default=None)
    Uses the same logic as __getitem__()
    , with a hook for returning a default value if the key doesn’t exist.
    '''
    
    if q:
        qs = qs.filter(title__icontains=q) # _ * 2 !! not once!!!

    # message test
    # messages.error(request, 'error test')

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


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()

            # message framework
            messages.success(request, '새 포스팅을 저장했습니다.')
            return redirect(post) 
            # get_absolute_url() 설정을 model에 해놔서 => post_detail.html

    else:
        form = PostForm()
        return render(request, 'blog/post_form.html', {
            'form' : form,
        })


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, '포스팅을 수정했습니다.')
            return redirect(post) 
            # get_absolute_url() 설정을 model에 해놔서 => post_detail.html

    else:
        form = PostForm(instance=post)
        return render(request, 'blog/post_form.html', {
            'form' : form,
        })


def comment_list(request):
    # comment_list = Comment.objects.all()
    comment_list = Comment.objects.all().select_related('post')
    return render(request, 'blog/comment_list.html', {
        'comment_list' : comment_list,
    })
    '''
    from blog.models import Post, Comment
    Post.objects.all()
    
    post_list = list(Post.objects.all())
    post_list

    import random
    random.choice(post_list)

    Comment??

    for i in range(100):
        comment = Commnet()
        comment.post = random.choice(post_list)
        comment.author = 'i-mnam'
        comment.message = 'bulk add content'
        comment.save()
    '''

    '''
    	
    SELECT ••• FROM "blog_post" WHERE "blog_post"."id" = '407'
    106 similar queries.
    Comment.objects.all().count()
    49.73ms
    '''