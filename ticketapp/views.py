from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket, Comment
from .forms import Ticket_form, CommentForm
from django.views.generic import  ListView
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    form = Ticket_form()
    if request.method == 'POST':
        form = Ticket_form(request.POST)
        if form.is_valid():
            c=form.save()
            c.user = request.user
            c.save()
            return HttpResponseRedirect(c.get_absolute_url())

    return render(request,'ticket/index.html',{'form':form})

class ticketview(ListView):
    model =Ticket
    template_name= 'ticket/list.html'
    context_object_name = "listticket"


def Detail_view(request,pk):
    c_form = CommentForm()
    ticket = get_object_or_404(Ticket, pk=pk)
    # comments = Comment.objects.filter(ticket=ticket)
    comments = Comment.objects.filter(ticket=ticket, reply=None)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            description = request.POST.get('description')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(pk=reply_id)
            comment=Comment.objects.create(ticket=ticket, user=request.user, description=description, reply=comment_qs)
            comment.save()
            return HttpResponseRedirect(ticket.get_absolute_url())
        else:
            c_form = CommentForm()
    context = {
       'ticket':ticket,
       'comments':comments,
       'c_form':c_form,
    }
    return render(request,'ticket/showview.html',context)
