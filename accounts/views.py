# accounts/views.py

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login as auth_login
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from .forms import SignupForm, LoginForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST) # UserCreationForm
        if form.is_valid():
            user = form.save() #return user
            return redirect(settings.LOGIN_URL) # default: "/accounts/login"
    else :
        form = SignupForm()
        
    return render(request, 'accounts/signup_form.html', {
        'form' : form,
    })


@login_required # 로그아웃 상태일 때, 해당 뷰에 접근하면 settings.LOGIN_URL 로 이동 # @user_passes_test()
def profile(request):
    return render(request, 'accounts/profile.html')


def login(request):
    providers = []
    for provider in get_providers():# settings/INSTALLED_APPS 내에서 활성화된 목록
        # social_app속성은 provider에는 없는 속성입니다.
        try:
            # 실제 Provider 별 Client id/secret 이 등록이 되어있는가?
            provider.socail_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.socail_app = None
        providers.append(provider)

    return auth_login(request,
        authentication_form=LoginForm,
        template_name='accounts/login_form.html',
        extra_context={'providers':providers})