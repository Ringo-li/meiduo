from django.shortcuts import render
from django.views import View
from django import http
import re

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
        if not re.match(r'^[a-zA-Z0-9]{8,20}$', username):
            return http.HttpResponseForbidden('请输入8-20个字符的用户名')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')