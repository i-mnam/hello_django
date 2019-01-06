# dojo.views.py

import os
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


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
    return render(request, 'post_list.html', {'name':name})
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