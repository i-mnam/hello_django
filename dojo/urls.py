# dojo/urls.py

from django.conf.urls import url
from . import views, views_cbv

urlpatterns = [ # 패턴과 주소가 꼭 1:1대응일 필요 없다!!
    url(r'^new/$', views.post_new), # ep21. form용
    url(r'^(?P<id>\d+)/edit/$', views.post_edit), # ep22 form 수정용

    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum), 
    # 끝에 왜 /$ 인지 "/"이게 없으면 왜 안되는지 모르겠다.
    url(r'^hello/(?P<name>[a-zA-Z]+)/(?P<age>\d+)/$', views.hello),

    url(r'^list1/$', views.post_list1),
    url(r'^list2/$', views.post_list2),
    url(r'^list3/$', views.post_list3),
    url(r'^excel/$', views.excel_download),

    url(r'^cbv/list1/$', views_cbv.post_list1),
    url(r'^cbv/list2/$', views_cbv.post_list2), # AttributeError: module 'dojo.views_cbv' has no attribute 'post_list2'
    url(r'^cbv/list3/$', views_cbv.post_list3),
    url(r'^cbv/excel$', views_cbv.excel_downlaod),
]