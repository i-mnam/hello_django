# account/urls.py

from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views


urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login'
        , kwargs={
            'authentication_form' : LoginForm,
            'template_name': 'accounts/login_form.html'
            }),
    url(r'^logout/$', auth_views.logout, name='logout'
       , kwargs={'next_page': settings.LOGIN_URL }), 
       # default '/accounts/logout' << admin mode..
       # kwargs의 next_page지정으로 인해 LOGIN_URL = '/accounts/login/' 로 리다이렉트
       # next인자가 있으면 next인자로 지정된게 우선순위가 위의 값보다 높음.
    url(r'^profile/$', views.profile, name='profile'), 
    # ep32 p4  관련 default settings 
    # LOGIN_REDIRECT_URL = '/accounts/profile/'
]