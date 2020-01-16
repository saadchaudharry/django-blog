from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import Usercreate,log
from django.contrib.auth import authenticate
# Create your views here.


def register(request):
    if request.method == 'POST':
        f = Usercreate(request.POST)
        if f.is_valid():
            is_staff = request.POST.get(True)
            f.save()
            # messages.success(request, 'Account created successfully')
            return redirect('home')
    else:
        f = Usercreate()
    return render(request, 'register.html', {'form':f})


def loogin(request):
    form = log(request.POST or None)
    context = {'form': form}
    print("User Logged in")
    print(request.user.is_authenticated)
    if form.is_valid():
        username = form.cleaned_data.get("Username")
        password = form.cleaned_data.get("Password")
        user = authenticate(request, username=username, password=password)
        print(request.user.is_authenticated)
        if user is not None:
            print(request.user.is_authenticated)
            log(request, user)
            # context['form'] = LoginForm()
            return (redirect('home'))
        else:
            # Return an 'Invalid login' error message
            print("error")
    return render(request,'uttar.html', context)

 # form =log(request.POST or None)
 #    context={'form':form}
 #    if form.is_valid():
 #        username = form.cleaned_data.get("username")
 #        password = form.cleaned_data.get("password")
 #        user = authenticate(request, username=username, password=password)
 #        print(request.user.is_authenticated)
 #        if user is not None:
 #            print(request.user.is_authenticated)
 #            log(request, user)
 #            # context['form'] = LoginForm()
 #            return (redirect("home"))
 #        else:
 #            # Return an 'Invalid login' error message
 #            print("error")
 #    return render(request,'uttar.html',context)