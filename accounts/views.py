from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

from accounts.forms import SignupForm


@login_required
def profile(request):
    # django.contrib.auth.models.User/AnonymousUser
    return render(request, 'accounts/profile.html')


# def signup(request):
#     if request.method == "POST":
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             return redirect(settings.LOGIN_URL)
#     else:
#         form = SignupForm()
#     return render(request,"accounts/signup.html",{
#         'form': form,
#     })

signup = CreateView.as_view(model = User, form_class=SignupForm, template_name='accounts/signup.html', success_url=settings.LOGIN_URL)
#SignupForm 이름을 사용하는 이유는 앱내 forms.py 에서 UserCreationForm을 상속 받았기 떄문에 원래는 이거를 통해서 필드 수정 할려구함!
