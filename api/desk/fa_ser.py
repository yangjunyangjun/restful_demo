'''
@Project ：desk_demo
@File    ：fa_ser.py
@Author  ：ex_yangjun2
@Date    ：2021/03/19 15.18
'''
from rest_framework import serializers
from .models import Fa


class FaSerializer(serializers.Serializer):
    fa_name = serializers.CharField(required=True)
    master_ip = serializers.CharField(required=True)
    slave_ip = serializers.CharField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    remark = serializers.CharField(required=True)
    region = serializers.CharField(required=True)

    def create(self, validated_data):
        Fa.objects.create(**validated_data)
