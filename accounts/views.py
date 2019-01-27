# accounts/views.py

from django.conf import settings
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignupForm


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