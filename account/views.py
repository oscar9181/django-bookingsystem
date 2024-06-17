from django.shortcuts import render, redirect
from.forms import RegisterUserForm
from django.contrib.auth import authenticate,login as auth_login
from django.contrib import messages

# Create your views here.
def register(request):
    form=RegisterUserForm()
    if request.method == 'POST':
       form =RegisterUserForm(request.POST)
       if form.is_valid:
           form.save()
           return redirect('home')   
       else:
           form =RegisterUserForm()
    
    return render(request,'accounts/register.html',{'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(user)
            auth_login(request,user)
            messages.success(request,'login successful')
            return redirect('home')
        else:
            messages.error(request,'Username or Password is incorrect')
            return render(request,'accounts/login.html')
    
        
    return render(request,'accounts/login.html')