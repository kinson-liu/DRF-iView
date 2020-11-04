import json
from rest_framework.views import APIView
from rest_framework.response import Response
from .pagination import CustomPagination
from .filter import CustomFilter

class iView(APIView):
    queryset = None
    serializer = None
    filter_class = None
    def __init__(self,**kwargs):
        self.soft_delete = hasattr(self.queryset,'is_delete')
        # TODO 添加传入参数校验，为空抛出异常
        super().__init__(**kwargs)

    def get(self,request):
        if 'ordering' in request.query_params:
            ordering = request.query_params['ordering'].split(',')
        else:
            ordering = ['id']
        queryset = self.queryset.objects.order_by(*ordering)
        if self.soft_delete:
            queryset = queryset.filter(is_delete=False)
        queryset = CustomFilter().filter_queryset(request=request,queryset=queryset, view=self)
        pg = CustomPagination()
        page = pg.paginate_queryset(queryset=queryset, request=request,view=self)
        serializer = self.serializer(instance=page,many= True)
        return Response(pg.get_paginated_response(serializer.data))
    
    def post(self,request):
        serializer = self.serializer(data= request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def put(self,request):
        queryset = self.queryset.objects.get(id= request.data['id'])
        serializer = self.serializer(instance=queryset,data= request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def delete(self,request):
        queryset = self.queryset.objects.get(id= request.data['id'])
        if self.soft_delete:
            queryset.is_delete = True
            queryset.save()
        else:
            queryset.delete()
        return Response()