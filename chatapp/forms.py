from django import forms
from .models import User_chat

class User_chat_form(forms.ModelForm):
    class Meta():
        model = User_chat
        fields = ['sender_id','reciever_id','date_and_time','message']
        widgets = {'reciever_id':forms.HiddenInput(),'date_and_time':forms.HiddenInput()}
