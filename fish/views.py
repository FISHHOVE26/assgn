from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreateForm,inquire
from .models import  Inquiry

def inquiry(request):
    if request.method == 'POST':
           inq = Inquiry.objects.create(name=request.POST['name'], email=request.POST['email'],
           inquiry=request.POST['memo'], number=request.POST['number'])
           inq.save()
           return redirect('settings')

    else:
        return render(request,'fish/Enquiries.html',{'form':inquire})

    return render(request,'fish/Enquiries.html',{'form':inquire})


def settings(request):
    return render(request,'fish/settings.html')


def dup(request):
    return render(request,'fish/dup.html')


def login(request):

    return render(request,'inquiry/login.html',{'form':AuthenticationForm()})

def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')

    else:
     form =  UserCreateForm
    return render(request,'fish/register.html',{'form':form})


def login(request):

    return render(request,'fish/login.html',{'form':AuthenticationForm()})


