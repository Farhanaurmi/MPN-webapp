from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


#        ----------Log-in & Sign-up api----------

def home(request):
    return render(request, 'app1/home.html')

def signupuser(request):
    if request.method=='GET':
        return render(request, 'app1/signupuser.html',{'form':UserCreationForm})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'app1/signupuser.html', {'form':UserCreationForm,'error':'username has been already taken'})
        else:
            return render(request, 'app1/signupuser.html', {'form':UserCreationForm,'error':'password did not match'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'app1/login.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'app1/login.html', {'form':AuthenticationForm(), 'error':'Error! Try again with correct username & password'})
        else:
            login(request, user)
            return redirect('home')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

#----------------------------------------------




