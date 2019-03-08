from django.db import models
from datetime import datetime

class User_chat(models.Model):
    sender_id = models.PositiveIntegerField()
    reciever_id = models.PositiveIntegerField()
    date_and_time = models.DateTimeField(default=datetime.today())
    message = models.TextField()
