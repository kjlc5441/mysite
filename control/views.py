from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Flag
from django.http import JsonResponse
import json


# Create your views here.

def  flag_list(request):
    status = Flag.objects.all()
    # status = Book.objects.filter(is_active=True)
    print(status)
    # return HttpResponse("status views is ok")
    return render(request, "status.html", locals())


def  flag_json(request):
    status = Flag.objects.all()
    status=status[0]
    print('status:',status)
    # return JsonResponse(status)
    return HttpResponse(status)


def update_status(request):
    # return HttpResponse('id=1')
    # 修改models資料步驟 1.查
    try:
        flag = Flag.objects.get(id=1) #flag= 001|001|001|
        print("flag=",flag)
    except Exception as e:
        print("--update id error %s" % (e))
        return HttpResponse("--update id error")

    if request.method == "GET":
        return render(request, "update.html", locals())
        # locals()為某一個id編號的對象,是一組字典,傳到模板取出各字段

    elif request.method == "POST":
        gbpay = request.POST["gbpay"]
        uupay = request.POST["uupay"]
        twpay = request.POST["twpay"]
        # 2.改
        flag.gbpay = gbpay
        flag.uupay = uupay
        flag.twpay = twpay
        # 3.保存
        flag.save()
        return HttpResponseRedirect("/index")

