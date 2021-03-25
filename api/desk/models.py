from django.db import models


# Create your models here.

class Fa(models.Model):
    # fa_name = models.CharField(max_length=128, unique=True)  # FA名称
    master_ip = models.CharField(max_length=128)  # 主ip
    slave_ip = models.CharField(max_length=128)  # 备ip
    user_name = models.CharField(max_length=128)  # FA用户名
    password = models.CharField(max_length=128)  # FA密码
    remark = models.CharField(max_length=128, null=True, blank=True)  # 备注
    region = models.CharField(max_length=128, )  # 备注
    is_delete = models.IntegerField(default=0)  # 是否删除

    class Meta:
        db_table = 'fa'
