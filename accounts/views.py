from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.decorators import login_required
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
            return redirect("profile")
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
        return resolve_url('profile')
    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect(self.get_success_url())


signup = SignupView.as_view()
# SignupForm 이름을 사용하는 이유는 앱내 forms.py 에서 UserCreationForm을 상속 받았기 떄문에 원래는 이거를 통해서 필드 수정 할려구함!
