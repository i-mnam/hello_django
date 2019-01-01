# dojo/urls.py

from django.conf.urls import url
from . import views

urlpatterns = [ # 패턴과 주소가 꼭 1:1대응일 필요 없다!!
    url(r'^sum/(?P<x>\d+)/$', views.mysum), 
    # 주의 여기서 "$"가 없었으면 ~/sum/01/23/4134 가 들어오더라도 
    # # 모두 첫번쨰 패턴으로 잡힌다. 끝니없으니까!
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum),
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum),
]