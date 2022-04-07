from django.shortcuts import render
from django.views import View
from django import http

# Create your views here.
class IndexView(View):
    # 首页广告
    def get(self, request):
        return render(request, 'index.html')

class VersionView(View):
    # 返回版本号
    def get(self, request):
        """
        :return: JSON
        """
        # 实现业务逻辑，使用username查询对应记录的条数。
        version = "CI_COMMIT_TAG"
        # 响应结果
        return http.JsonResponse({'version': version})
