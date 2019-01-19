# dojo.views.py

import os
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) 
        #order! 이 form은 인자를 받았으니,       사용자가 입력한 데이터를 알 수 있게됨.
        if form.is_valid(): # form에 걸려있는 validations 모두 호출, 하나라도 false면 false
            #print("cleaned_data :",form.cleaned_data) # user가 입력한 값을 사전형으로 받음.
            
            # 방법1)
            # post = Post()
            # post.title = form.cleaned_data['title']
            # post.content = form.cleaned_data['content']
            # post.save()

            # 방법2)
            '''
            post = Post(title=form.cleaned_data['title'],
                        content = form.cleaned_data['content'])
            post.save()
            '''

            # 방법3)
            '''
            post = Post.objects.create(title=form.cleaned_data['title'],
                                       content = form.cleaned_data['content'])
            '''

            # 방법4)
            #post = Post.objects.create(**form.cleaned_data)

            # last)
            post = form.save()
            return redirect('/dojo/') # namespace:name을 사용해도 됨. 뭘하고 싶든 여동생 마음
        else:
            form.errors
    else:
        form = PostForm()
    
    return render(request, 'dojo/post_form.html', {
        'form':form
    })


def mysum(request, numbers):
    # numbers = "1/4526/231/3/252/457"
    # return HttpResponse(numbers)
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    # s가 거짓일 때 (or의 뜻) 0으로 치환
    print("result:", result)
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse('안녕하세요. {}씨. {}살 이시네요.'.format(name, age))


def post_list1(request):
    name="S.Yeji"
    return HttpResponse('''
        <h1>putty YEJI</h1>
        <p>{name}</p>
        <p>예쁜 서예지 배우</p>
    '''.format(name=name))


def post_list2(request):
    name="K.Teari"
    return render(request, 'dojo/post_list.html', {'name':name})
    # dojo/post_list.html은 탬플릿을 아예 못찾음..


def post_list3(request):
    return JsonResponse({
        'message': 'Hello, Teari & Yeji',
        'items' : ['Python', 'Django', 'Celery', 'Azure', 'AWS']
    }, json_dumps_params={'ensure_ascii': False})


def excel_download(request):
    # filepath = '/Users/naami/git/hello_django/sample.xlsx'
    filepath = os.path.join(settings.BASE_DIR, 'sample.xlsx')
    filename = os.path.basename(filepath)
    
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel') #text/html
        response['Content-Disposition'] = 'attachment; filename{}'.format(filename)
        return response