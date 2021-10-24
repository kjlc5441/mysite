from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from control.models import Flag

# Create your views here.

def index_view(request):
    status = Flag.objects.all()
    # status = Book.objects.filter(is_active=True)
    print(status)
    # return render(request, "status.html", locals())
    return render(request,'index.html',locals())
