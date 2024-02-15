from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from . import views
from . models import Member
# Create your views here.

def home(request):
    return render(request,"index.html")

def dummy(request):
    mem = Member.objects.all()
    return render(request,"dummy.html",{'mem':mem})

def add(request):
    return render(request,'update.html')

def addrec(request):
    if request.method == 'POST':
        firstname= request.POST['firstname']
        lastname= request.POST['lastname']
        country= request.POST['country']
        mem=Member(firstname=firstname,lastname=lastname,country=country)
        mem.save()
    return redirect('/')

# def delete(request,id):
#     mem=Member.objects.get(id=id)
#     mem.delete()
#     return redirect('/')

# def update(request,id):
#     mem=Member.objects.get(id=id)
#     return render(request,'update.html',{'mem':mem})

def uprec(request,id):
    x= request.POST['firstname']
    y= request.POST['lastname']
    z= request.POST['country']
    mem=Member.objects.get(id=id)
    mem.firstname=x
    mem.lastname=y
    mem.country=z

    mem.save()
    return redirect('/')