from django.shortcuts import render
from django.views import View

# Create your views here.
class ImageCodeView(View):
    def get(self, request, uuid):
        """
        返回图形验证码
        :param request:网页请求信息
        :param uuid:通用唯一识别码，标识图形验证码属于哪个用户
        :return:image/jpg
        """
        pass