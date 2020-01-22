from django.urls import path,include
from . import views

app_name = 'blog'

urlpatterns =[
    #path('accounts/', include('django.contrib.auth.urls')),
    path('',views.post_list, name="post_list"),
    path('<int:pk>/', views.post_detail, name = "post_detail"),

]