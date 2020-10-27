from django.shortcuts import render

# Create your views here.
import datetime
def Filter(request):
    date1=datetime.datetime.now()
    return render(request,'filter.html',context={'data':'hai HELLO django','date1':date1,'count':1})


def user_defined_filter(request):
    return render(request,'usdfilter.html',context={'data':'hai hellO Python'})