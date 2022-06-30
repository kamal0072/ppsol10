from django.http import HttpResponse
from django.shortcuts import render
from .models import School,Student

def home(request):
    qs1=School.objects.all()
    qs2=Student.objects.all()
    unn=qs1.union(qs2).values('name')[2:]
    print(unn.count())
    # q=data.query
    # return render(request,'home.html',{'data':data,"query":q})
    return render(request,'home.html',{'data':unn})

def detail_home(request,pk):
    try:
        data=School.objects.get(id=pk)
    except School.DoesNotExist as errr:
        return HttpResponse("The user is not available!!")
    return render(request,'home.html',{'detail':data})


def index(request):
    c_name="Django"
    addres="Pune"
    data={
        'nm':c_name,
        'add':addres,
    }
    return render(request,'index.html',data)

def page(request):
    c_name="Html"
    addres="Kolkata"
    data={
        'nm':c_name,
        'add':addres,
    }
    return render(request,'page.html',data)