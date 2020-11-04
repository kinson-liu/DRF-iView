# from django.contrib.auth.models import User
import json
from .models import RolePerms,UserRoles,User,Permission
from django.contrib.auth import authenticate
from rest_framework.views import APIView
# from utils.common import JsonResponse
from libs.authtication import TokenAuthtication
from django.core import serializers
from rest_framework.response import Response
from libs.exceptions import LoginFailed,UserNotExist
# Create your views here.
class login(APIView):
    """
    用户登录
    """
    authentication_classes = []
    permission_classes = []
    def post(self,request,*args,**kwargs):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            role_ids = []
            permission_ids = []
            perms = {
                'platform':[],
                'list':[],
                'menu':[],
                'interface':[],
            }
            recv = json.loads(serializers.serialize("json",UserRoles.objects.filter(user_id=user.id)))
            for item in recv:
                role_ids.append(item['fields']['role_id'])
            recv = json.loads(serializers.serialize("json",RolePerms.objects.filter(role_id__in=role_ids)))
            for item in recv:
                permission_ids.append(item['fields']['permission_id'])
            recv = json.loads(serializers.serialize("json",Permission.objects.filter(id__in=permission_ids)))
            for item in recv:
                if item['fields']['type'] == '平台':
                    perms['platform'].append(item['fields']['method'])
                elif item['fields']['type'] == '目录':
                    perms['list'].append(item['fields']['method'])
                elif item['fields']['type'] == '菜单':
                    perms['menu'].append(item['fields']['method'])
                elif item['fields']['type'] == '接口':
                    perms['interface'].append(item['fields']['method'])
            data = {
                "username":user.username,
                "name":user.name,
                "token":TokenAuthtication().create_token(request.data['username'],perms)
            }
            return Response(data= data)
        else:
            raise LoginFailed()

class account(APIView):
    """
    get     获取账户
    post    创建账户
    put     重置账户
    delete  注销账户
    """
    permission_classes = []
    def get(self,request,*args,**kwargs):
        """
        获取账户
        :param  username;
        """
        try:
            user = User.objects.get(username=request.user)
        except Exception:
            raise UserNotExist()
        
        data = {
            "username":user.username,
            "name":user.name,
            "email":user.email,
            "perms":request.auth
        }
        return Response(data= data)


