from django.shortcuts import render
from django.views import View

# Create your views here.
class RegisterView(View):
    """用户注册"""

    def get(self, requets):
        """提供用户注册页面"""
        return render(requets, 'register.html')

class LoginView(View):
    def get(self, requets):
        return render(requets, 'login.html')