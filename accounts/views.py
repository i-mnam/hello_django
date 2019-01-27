# accounts/views.py

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() #return user
            return redirect(settings.LOGIN_URL) # default: "/accounts/login"
    else :
        form = UserCreationForm()
        
    return render(request, 'accounts/signup_form.html', {
        'form' : form,
    })
@login_required # 로그아웃 상태일 때, 해당 뷰에 접근하면 settings.LOGIN_URL 로 이동 # @user_passes_test()
def profile(request):
    return render(request, 'accounts/profile.html')