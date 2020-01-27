from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('profile/', views.profile, name="profile"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.signup, name='signup'),

    # path('password_change/',
    #      auth_views.PasswordChangeView.as_view(
    #          success_url=reverse_lazy('profile'),
    #          template_name='accounts/password_change_form.html'),
    #      name="password_change"),

    path('password_change/',views.MyPasswordChangeView.as_view(),name="password_change"),
    # path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),name="password_change_done")
    # 위에꺼를 안쓰고 views안에다가 success_url을 사용해서 가능!
]
