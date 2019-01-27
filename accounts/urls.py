# account/urls.py

from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login'
        , kwargs={'template_name': 'accounts/login_form.html'}),
    url(r'^logout/$', auth_views.logout, name='logout'
       , kwargs={'next_page': settings.LOGIN_URL }), 
       # default '/accounts/logout' << admin mode..
       # kwargs의 next_page지정으로 인해 LOGIN_URL = '/accounts/login/' 로 리다이렉트
    url(r'^profile/$', views.profile, name='profile'), 
    # ep32 p4  관련 default settings 
    # LOGIN_REDIRECT_URL = '/accounts/profile/'
]