# restful_demo
django

#### swagger 


##项目结构

```
demo--| 
      |--api--|--desk---|---url
      |       |         |---model
      |       |         |---views
      |       |         |---filter
      |       |         |---serializer
      |       |         |---tool
      |       |---app1...
      |
      |--celery_task--|---task
      |               |---crontab
      |
      |--conf
      |
      |--pkg
      |
      |--script
      |
      |--tools
      | 
      |
```


####启动celery

```json
启动celery定时任务
    celery -A celery_task.main beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
启动work
    celery -A celery_task.main  worker -l info  --pool=solo
```


