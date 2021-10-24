from django.contrib import admin
from .models import Flag

# Register your models here.

# 此區 為後台admin綁定模組的用途['gbpay','uupay','twpay']

class FlagManager(admin.ModelAdmin):
    # 列表頭出現的欄位名稱
    list_display =['gbpay','uupay','twpay']

    # 控制超連接的欄位
    # list_display_links =['gbpay','uupay','twpay']

    # 添加過濾器
    # list_filter = ['gbpay','uupay','twpay']

    # 添加搜索框
    # search_fields = ['gbpay','uupay','twpay']

    # 添加可在列表頁編輯的欄位
    # list_editable =  ['gbpay','uupay','twpay']

admin.site.register(Flag,FlagManager)
