from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField("用户名", max_length=30, unique=True)
    password = models.CharField("密码", max_length=32)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table ='user'
        # 下述修改 對應到admin後台有用
        verbose_name='使用者'
        verbose_name_plural=verbose_name

    def __str__(self):
        return "%s|%s|%s"%(self.username,self.created_time,self.updated_time)
                              