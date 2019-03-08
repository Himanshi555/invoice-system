from django.shortcuts import render,redirect
from .forms import User_form,Employeeform,Customerform
from .models import Employee,Customer
from django.contrib.auth.models import User

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from django.views.generic import View, DeleteView
# from rest_framework.response import Response
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.sessions.models import Session

def register(request):
    form = User_form()
    if request.method == 'POST':
        form = User_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return HttpResponseRedirect(reverse('login'))

    else:
        form = User_form()
    return render(request,'register.html',{'form':form})

def add(request):
    if request.method=='POST':
        form=Employeeform(request.POST, request.FILES)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect(reverse('userapp:viewemp'))
    else:
        form =Employeeform()

    context = {'form':form}

    return render(request, 'data.html', context)

def viewemp(request):
    view = Employee.objects.all()
    return render(request,'viewemployee.html',{'view':view})

def upemp(request,pk):
    view = Employee.objects.get(pk=pk)
    form = Employeeform(request.POST,instance=view)
    if form.is_valid():
        form.save()
        return viewemp(request)
    else:
        print("Error in Update!!")
    return render(request,'updateemp.html',{'view':view,'form':form})

def delemp(request,pk):
    delem = Employee.objects.get(pk=pk)
    delem.delete()
    return viewemp(request)

def customer(request):
    if request.method=='POST':
        form=Customerform(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect(reverse('userapp:vcustomer'))
    else:
        form =Customerform()

    context = {'form':form}

    return render(request, 'customer.html', context)

def viewcustomer(request):
    view = Customer.objects.all()
    return render(request,'viewcustomer.html',{'view':view})

def upcustomer(request,pk):
    view = Customer.objects.get(pk=pk)
    form = Customerform(request.POST,instance=view)
    if form.is_valid():
        form.save()
        return viewcustomer(request)
    else:
        print("Error in Update!!")
    return render(request,'updatecustomer.html',{'view':view,'form':form})

def delcustomer(request,pk):
    delcus = Customer.objects.get(pk=pk)
    delcus.delete()
    return viewcustomer(request)

def user_login(request):
    # context = {}
    if  request.method == 'POST':
        username = request.POST.get('username')
        password   = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        user.is_staff == True

        if user is not None:
            if user.is_active:
                login(request, user)
                # request.session['user'] = usr + 1
                session = Session.objects.get('key',0)
                request.session['key'] = key + 1
                session_data = session.get_decoded()
                uid = session_data.get('_auth_user_id')
                user = User.objects.get(id=uid)

                context = {'user':user}
                return HttpResponseRedirect(reverse('home'))
            else:
                # context["error"] =  "Provide valid credentials !!!"
                return HttpResponse("You're account is disabled.")
        else:
            print("invalid login details " + username + " " + password)
            return render(request,'login.html', context,{'key':key})
    else:
        return render(request,'login.html', context,{'key':key})


@login_required
def user_logout(request):
    logout(request)
    try:
        del request.session['key']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('home'))
