from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from control.models import Flag, Cos
from control.views import cos_status

# Create your views here.

def index_view(request):
    status = Flag.objects.all()
    cos_data = Cos.objects.all()
    # cos_data = cos_data[0]
    print("status:",status,"cos_data:",cos_data)
    # return render(request, "status.html", locals())
    return render(request,'index.html',locals())
