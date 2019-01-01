# dojo/urls.py

from django.conf.urls import url
from . import views

urlpatterns = [ # 패턴과 주소가 꼭 1:1대응일 필요 없다!!
    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum), 
    # 끝에 왜 /$ 인지 "/"이게 없으면 왜 안되는지 모르겠다.
]