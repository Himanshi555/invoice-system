from django import forms
from . models import Ticket, Comment

class Ticket_form(forms.ModelForm):
    class Meta():
        model = Ticket
        fields = ('subject', 'description',)
        widgets = {
            'description': forms.Textarea(attrs={'class':'form-control','placeholder':'text goes here!!!!', 'rows':'7', 'cols':'40'})
                  }

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('description', )
        widgets = {
            'description': forms.Textarea(attrs={'class':'form-control','placeholder':'text goes here!!!!', 'rows':'4', 'cols':'50'})
                  }
