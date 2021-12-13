from django.shortcuts import render,redirect
from django.views import View
from django import http
import re
from django.db import DatabaseError
from django.urls import reverse

from users.models import User

# Create your views here.
class RegisterView(View):
    """用户注册"""

    def get(self, request):
        """提供用户注册页面"""
        return render(request, 'register.html')

    def post(self, request):
        """实现用户注册业务逻辑"""
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        mobile = request.POST.get("mobile")
        allow = request.POST.get("allow")

        # 校验参数：前后端要分开，避免恶意请求绕过前端直接请求后端
        # 判断参数是否齐全，all([列表])，只有有一个为空，返回false
        if not all([username, password, password2, mobile, allow]):
            return http.HttpResponseForbidden('缺少必传参数')
        # 判断用户名是否是5-20个字符
        if not re.match(r'^[a-zA-Z0-9]{5,20}$', username):
            return http.HttpResponseForbidden('请输入5-20个字符的用户名')
        # 判断密码是不是8-20位
        if not re.match(r'[a-zA-Z0-9]{8,20}$', password):
            return http.HttpResponseForbidden('请输入8-20个字符的密码')
        # 判断两次密码是否一致
        if password2 != password:
            return http.HttpResponseForbidden('两次密码输入不一致')
        # 判断手机号是否合法：
        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return http.HttpResponseForbidden('请输入正确的电话号码')
        # 判断是否勾选用户协议
        if allow != "on":
            return http.HttpResponseForbidden('请勾选用户协议')
        # 保存注册数据，是注册业务的核心
        try:
            User.objects.create_user(username=username, password=password, mobile=mobile)
        except DatabaseError:
            return "告诉用户注册失败"
        # 响应结果
        # return http.HttpResponse("注册成功，重定向到首页")
        return redirect(reverse('contents:index'))

class UserInfoCenterView(View):
    def get(self, request):
        return render(request, 'user_info_center.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

class LogoutView(View):
    def get(self, request):
        return redirect(reverse('contents:index'))