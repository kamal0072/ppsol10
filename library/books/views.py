from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Books
from .forms import BookModelform

#show all books view----- 
def show_books(request):
    books=Books.objects.all()
    return render(request,'detail.html',{'books':books})

#book upload view
def upload_book(request):
    if request.method=='POST':
        form=BookModelform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/books')
    else:
        form=BookModelform()
    return render(request,'upload_form.html',{'form':form})

#book update view
def update_book(request,pk):
    try:
        data=Books.objects.get(id=pk)
    except:
        # return redirect('/books')
        return HttpResponse("Records Not Found!!")
    if request.method=='POST':
        form=BookModelform(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/books')
    else:
        form=BookModelform(instance=data)
    return render(request,'update_book.html',{'form':form})


#book delete view...
def delete_book(request,pk):
    try:
        get_data=Books.objects.get(id=pk)
    except:
        return HttpResponse("Records Not Found!")
    get_data.delete()
    return render(request,'delete.html',{'delete_data':get_data})

#view all detail of user
def get_detail(request,pk):
    try:
        detail_data=Books.objects.get(id=pk)
    except:
        return redirect('/books')
    return render(request,'info.html',{'detail':detail_data})