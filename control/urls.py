from django.urls import path

from . import views

urlpatterns =[

    path('status',views.flag_list),

    path('status_json',views.flag_json),

    path('update/1',views.update_status),

]