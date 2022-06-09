from django.shortcuts import render

# Create your views here.
def home(request):
    cname="Django"
    c_fees=12000
    c_addres="Pune"
    data={
        "cn":cname,
        "cf":c_fees,
        'cd':c_addres,
    }
    return render(request,'poll/home.html',data)

def show(request):
    cname="React"
    c_fees=11300
    c_addres="Delhi"
    data={
        "cn":cname,
        "cf":c_fees,
        'cd':c_addres,
    }
    return render(request,'poll/show.html',data)

def page(request):
    cname="Java script"
    c_fees=12560
    c_addres="Kolkata"
    data={
        "cn":cname,
        "cf":c_fees,
        'cd':c_addres,
    }
    return render(request,'poll/page.html',data)

def site(request):
    cname="Django Rest"
    c_fees=11130
    c_addres="Mumbai"
    data={
        "cn":cname,
        "cf":c_fees,
        'cd':c_addres,
    }
    return render(request,'poll/site.html',data)