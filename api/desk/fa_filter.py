'''
@Project ：desk_demo
@File    ：fa_filter.py
@Author  ：ex_yangjun2
@Date    ：2021/03/19 15.18
'''
import django_filters
from .models import Fa


class FaFilter(django_filters.FilterSet):
    fa_name = django_filters.CharFilter(field_name="fa_name")
    master_ip = django_filters.CharFilter(field_name="master_ip")

    class Meta:
        model = Fa
        fields = ['fa_name', 'master_ip']
