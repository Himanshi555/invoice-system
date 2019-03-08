from django import forms
from .models import Employee,Customer
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User



class User_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    #role = forms.ModelChoiceField(queryset=Group.objects.all())


    class Meta:

        model = User
        fields = ['first_name', 'last_name',
                  'email','username',
                  'password','confirm_password']
                     # excludes = ['']

        label = {
            'password': 'Password'
            # 'confirm_password': 'Password'
        }



    def clean(self):
        cleaned_data = super(User_form, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("password and confirm_password does not match...")

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, *kwargs)




        if kwargs.get('instance'):
            initial = kwargs.setdefault('initial', {})
            if kwargs['instance'].groups.all():
                initial['role'] = kwargs['instance'].groups.all()[0]
            else:
                initial['role'] = None

        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class':'form-control'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control'})
        self.fields['email'].widget.attrs.update({'class':"form-control"})
        self.fields['username'].widget.attrs.update({'class':'form-control'})
        self.fields['password'].widget.attrs.update({'class':"form-control"})



    def save(self):
        password=self.cleaned_data.pop('password')
        u=super().save()
        u.set_password(password)
        u.save()
        return u



class Employeeform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['Name','Email','Address','Image','Position','salary','date_added']
        def __str__(self):
            self.fields['salary'].widget.attrs.update({'class':'form-control'})
            return self.name



class Customerform(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['Name','Email','Address','Wallet']
    



































# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
#
#
#
# class User_form(UserCreationForm):
#     username = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     # password = forms.CharField(widget=forms.PasswordInput(),min_length=6)
#     # confirm_password = forms.CharField(widget=forms.PasswordInput(),min_length=6)
