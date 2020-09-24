from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

class AuthMiddleWare(MiddlewareMixin):
    white_list = [
        '/api/user/vcode/fetch',
        '/api/user/vcode/submit',
        'qiniu/callback',
    ]
    def process_request(self,request):
        if request.path not in self.white_list:
            uid = request.session.get('uid')
            if not uid:
                data={
                    'code':1002,
                    'data':'用户未登录'
                }
                return JsonResponse(data)
