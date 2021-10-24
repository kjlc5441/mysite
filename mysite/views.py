from django.http import HttpResponse
from django.shortcuts import render




def index_view(request):
    html = '<h1>這是 mysite的首頁</h1>'
    # return HttpResponse(html)
    return render(request, "portal.html")



def pos_sign(request):
    html = '<h1>這是 possign頁面</h1>'
    return HttpResponse(html)

