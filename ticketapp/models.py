from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.conf import settings
from django.urls import reverse
import random

class TicketManager(models.Manager):
    def get_queryset(self):
        return super(TicketManager, self).get_queryset().filter(status='token')

class Ticket(models.Model):
    def tid():
        num = random.randrange(50000,1000000)
        return num
    id = models.CharField(max_length=10,primary_key=True,default=tid,editable=False,unique=True)
    objects = models.Manager()
    token = TicketManager()
    user = models.ForeignKey(User,settings.AUTH_USER_MODEL, null=True, blank=True,)
    subject = models.CharField(max_length=200)
    description = models.TextField()
    date_and_time = models.DateTimeField(default=datetime.today())

    def get_absolute_url(self):
        return reverse("tic:Detail_view", args=[self.pk])


class Comment(models.Model):
    user = models.ForeignKey(User,settings.AUTH_USER_MODEL, default=1)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    reply = models.ForeignKey('Comment', on_delete=models.SET_NULL, null=True, related_name="replies")
    description = models.TextField()
    date_and_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.user.username)
