from django.db import models


# Create your models here.
class Flag(models.Model):
    # models模組 會自行增加id欄位
   
    gbpay = models.CharField('呷霸卡', max_length=3)
    uupay = models.CharField('悠遊卡', max_length=3)
    twpay = models.CharField('台灣pay', max_length=3)
 
    # 下述修改 對應到admin後台有用
    class Meta:
        db_table ='flag'
        verbose_name='燈號'
        verbose_name_plural=verbose_name

    # 增加類方法 ：for查詢,列印時可看到明細
    def __str__(self):
        return '%s|%s|%s|'%(self.gbpay,self.uupay,self.twpay)

class Lan(models.Model):
   
    lan_status = models.CharField('網路檢測', max_length=4)
    
    # 下述修改 對應到admin後台有用
    class Meta:
        db_table ='lan_status'
        verbose_name='網路檢測'
        verbose_name_plural=verbose_name

    # 增加類方法 ：for查詢,列印時可看到明細
    def __str__(self):
        return '%s'%(self.lan_status)

class Cos(models.Model):
   
    cos_db = models.CharField('雲端訂單', max_length=4)
    
    # 下述修改 對應到admin後台有用
    class Meta:
        db_table ='cos_db'
        verbose_name='雲端訂單'
        verbose_name_plural=verbose_name

    # 增加類方法 ：for查詢,列印時可看到明細
    def __str__(self):
        return '%s'%(self.cos_db)