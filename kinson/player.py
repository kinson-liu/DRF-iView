from libs import iView
from django_filters import FilterSet
from django.db import models
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response

class Player(models.Model):

    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=20)
    level = models.IntegerField(default=1)
    profession = models.CharField(max_length=20)
    golds = models.IntegerField(default=0)
    diamonds = models.IntegerField(default=0)
    # 默认字段
    is_delete = models.BooleanField(default= 0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class PlayerFilter(FilterSet):
    class Meta:
        model = Player
        fields = '__all__'

class player(iView):
    # 默认认证校验类
    authentication_classes = []
    # 默认权限校验类
    permission_classes = []
    # 权限校验名称
    # perms_map = { 
    #   'get':    '*',
    #   'post':   '*',
    #   'put':    '*',
    #   'delete': '*'
    # }
    # 数据库模型
    queryset = Player
    # 序列化器
    serializer = PlayerSerializer
    # 过滤器
    filter_class = (PlayerFilter)
    # def get(self,request):
    #     1/0
    #     return Response()