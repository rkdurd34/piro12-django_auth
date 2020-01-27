from django.conf import settings
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.http import Http404
from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login as auth_login
from accounts.forms import SignupForm


@login_required
def profile(request):
    # django.contrib.auth.models.User/AnonymousUser
    return render(request, 'accounts/profile.html')



#함수 기반뷰
'''
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # 로그인 처리
            next_url =  request.GET.get("next") or 'profile'
            return redirect("profile")
            #next_url을 사용 하면 return redirect(next_url) 
            #return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {
        'form': form,
    })
'''
#클래스 기반 뷰
class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = "accounts/signup.html"
    def get_success_url(self):
        next_url = self.GET.get("next") or 'profile'
        return resolve_url(next_url)
        #return resolve_url('profile')
        #next_url이 없을시에는 위에와 같이 활동
    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect(self.get_success_url())


signup = SignupView.as_view()
# SignupForm 이름을 사용하는 이유는 앱내 forms.py 에서 UserCreationForm을 상속 받았기 떄문에 원래는 이거를 통해서 필드 수정 할려구함!
class MyPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('profile')
    template_name = "accounts/password_change_form.html"

    def form_valid(self, form):
        messages.info(self.request,"암호변경을 완료했습니다.")
        return super().form_valid(form)
#-----22--------이거는 url에서 길게 안하고!!!!!!!!클래스로 커스터마이