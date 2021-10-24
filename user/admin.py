from django.contrib import admin
from .models import User

# Register your models here.

class UserManager(admin.ModelAdmin):
    # 列表頭出現的欄位名稱
    list_display = ['username','created_time','updated_time']

    # 控制超連接的欄位
    # list_display_links = ["username"]

    # 添加過濾器
    # list_filter = ['username']

    # 添加搜索框
    # search_fields = ['username']

    # 添加可在列表頁編輯的欄位
    # list_editable = ['price','market_price']

admin.site.register(User,UserManager)