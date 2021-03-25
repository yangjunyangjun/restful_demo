import os
import re
import django
from celery import Celery

# 创建celery实例对象
app = Celery("desk")

# 把celery和django进行组合，识别和加载django的配置文件
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")
django.setup()

# 通过app对象加载配置
app.config_from_object("celery_task.config")
celery_list = []


def find_task(path):
    for f in os.listdir(path):
        file_path = os.path.join(path, f)
        ##判断当目下是否是文件
        if os.path.isfile(file_path):
            if f == "tasks.py":
                tmp = re.sub('[/\\\]+', '.', file_path)
                f = re.findall(".*demo.(.*?).tasks.py", tmp, re.IGNORECASE)
                celery_list.append(f[0])
        else:
            find_task(file_path)  # 文件夹，递归查找该文件夹下的所有文件


find_task(os.getcwd())

# 加载任务
app.autodiscover_tasks(celery_list)
#