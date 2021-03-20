'''
@Project ：desk_demo
@File    ：views.py
@Author  ：ex_yangjun2
@Date    ：2021/03/19 15.18
'''
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .fa_filter import FaFilter
from .fa_ser import FaSerializer
from .models import Fa


# Create your views here.


class FaViews(GenericViewSet):
    queryset = Fa.objects.filter(is_delete=0)
    serializer_class = FaSerializer
    search_fields = ('fa_name', 'master_ip')
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_class = FaFilter

    def create(self, request, *args, **kwargs):
        '''
        后台管理-系统管理-FA配置
        :param
        ------fa_name fa名(必填)
        ------master_ip 主ip(必填)
        ------slave_ip 备ip(必填)
        ------user_name 账号(选填)
        ------password 密码(选填)
        ------remark 备注(选填)
        ------region 地区(选填)
        :return
        '''
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"code": 20000, "msg": "success"})

    def list(self, request, *args, **kwargs):
        '''
        后台管理-系统管理-FA配置
        :param
        :return
            ------fa_name fa名
            ------master_ip 主ip
            ------slave_ip 备ip
            ------user_name 账号
            ------password 密码
            ------remark 备注
            ------region 地区
        '''
        queryset = Fa.objects.filter(is_delete=0).values()
        return Response({"code": 20000, "msg": "success", "data": queryset})

    def update(self, request, *args, **kwargs):
        '''
        后台管理-系统管理-FA配置
        :param
        ------fa_name fa名(必填)
        ------master_ip 主ip(必填)
        ------slave_ip 备ip(必填)
        ------user_name 账号(选填)
        ------password 密码(选填)
        ------remark 备注(选填)
        ------region 地区(选填)
        :return
        '''
        pk = kwargs.get('pk')
        try:
            fa = Fa.objects.get(id=pk)
        except Fa.DoesNotExist as e:
            return Response({"code": 50000, "msg": str(e)})
        serializer = self.get_serializer(fa, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"code": 20000, "msg": "success"})

    def destroy(self, request, *args, **kwargs):
        '''
        后台管理-系统管理-FA配置
        :param
        :return
        '''
        pk = kwargs.get('pk')
        try:
            flow = Fa.objects.get(id=pk)
        except Fa.DoesNotExist as e:
            return Response({"code": 50000, "msg": str(e)})
        flow.delete()
        return Response({"code": 20000, "msg": "success"})
