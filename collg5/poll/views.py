from django.shortcuts import render
# Create your views here.
def home(request):
    name="Manisha"
    age=23
    data={
        'nm':name,
        "ag":age,
    }
    return render(request,'poll/home.html',data)