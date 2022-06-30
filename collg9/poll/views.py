from django.shortcuts import redirect, render
from .forms import StudentModelForm
from .models import StudentModel
def home(request):
    stu_data=StudentModel.objects.all()
    if request.method=='POST':
        form=StudentModelForm(request.POST)
        if form.is_valid():
            nm=form.cleaned_data['name']
            roll=form.cleaned_data['roll_no']
            add=form.cleaned_data['address']
            email=form.cleaned_data['email']
            color=form.cleaned_data['color']
            pwd1=form.cleaned_data['pwd1']
            pwd2=form.cleaned_data['pwd2']
            state=form.cleaned_data['state']
            stu_model=StudentModel(
                name=nm,roll_no=roll,address=add,email=email,color=color,pwd1=pwd1,pwd2=pwd2,
                state=state)
            stu_model.save()
            return redirect('/home/')
    else:
        form=StudentModelForm()
    return render(request,'home.html',{'form':form,"data":stu_data})

    