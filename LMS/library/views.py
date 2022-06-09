from django.shortcuts import redirect, render
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .forms import BookModel
from django.contrib.auth.models import User
#user account creation form
def sign_up(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Account has been created!!')
            return redirect('/signup')
    else:
        form=SignUpForm()
    return render(request,'signup.html',{'form':form})


#user login view
def user_login(request):
    if request.method=='POST':
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            user_name=form.cleaned_data['username']
            user_pass=form.cleaned_data['password']
            user=authenticate(username=user_name,password=user_pass)
            if user is not None:
                login(request,user)
                messages.success(request,'logged-In sucess!!!')
                return redirect("/profile")
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})

from .models import Books
def profile_view(request):
    # user=User.objects.get(id=pk)
    detail=Books.objects.all()
    if request.method=='POST':
        form=BookModel(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'logged-In sucess!!!')
            return redirect('/profile')
    else:
        form=BookModel()
    return render(request,'profile.html',{'data':detail,'form':form})

def delete_data(request,pk):
    detail=Books.objects.get(id=pk)
    detail.delete()
    messages.success(request,'item deleted successfully!!!')
    return redirect('/profile')

def update_books(request,pk):
    books=Books.objects.get(id=pk)
    form=BookModel(request.POST or None,instance=books)
    if form.is_valid():
        form.save()
        return redirect('/profile')
    return render(request,'update.html',{'form':form})

def logout_view(request):
    logout(request=request)
    return redirect('/login/')