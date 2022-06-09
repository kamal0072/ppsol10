from django.shortcuts import render
def enroll_view(request):
    name="python"
    age=23
    address="delhi"
    data={
        'nm':name,
        'ag':age,
        'add':address,
    }
    return render(request,'enroll/enroll.html',data)