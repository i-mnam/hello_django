# dojo.views.py

from django.http import HttpResponse
from django.shortcuts import render


def mysum(request, numbers):
    # numbers = "1/4526/231/3/252/457"
    # return HttpResponse(numbers)
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    # s가 거짓일 때 (or의 뜻) 0으로 치환
    print("result:", result)
    return HttpResponse(result)