from django.shortcuts import render
from .forms import User_chat_form
from django.http import HttpResponse
from .models import User_chat
from django.contrib.auth.models import User
from userapp.forms import User_form
from django.contrib.auth.forms import UserCreationForm

def chat(request,pk):
    form = User_chat_form()
    if request.method == 'POST':
        form = User_chat_form(request.POST)
        if form.is_valid():
            form.save()
            HttpResponse("your message is send")
    user = User.objects.get(pk=pk)
    return render(request,'chat.html',{'form':form, 'user':user})


def all_user(request):
    users = User.objects.all()
    return render(request,'users.html',{'users':users})

def show_chat(request,pk):
    all = User_chat.objects.get(pk=pk)
    return render(request,'show_chat.html',{'all':all})
