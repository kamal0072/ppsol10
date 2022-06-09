from django.shortcuts import render
def home(request):
    c_name="Python"
    addres="delhi"
    data={
        'nm':c_name,
        'add':addres,
    }
    return render(request,'home.html',data)

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