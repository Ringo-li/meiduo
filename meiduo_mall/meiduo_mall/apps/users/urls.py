from django.urls import path, re_path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('user_info_center/', views.UserInfoCenterView.as_view(), name='user_info_center'),
]