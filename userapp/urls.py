from django.contrib import admin
from django.urls import path, include
from . import views

app_name  = 'userapp'

urlpatterns = [

path('register/',views.register,name='register'),
# path('accounts/login', include('django.contrib.auth.urls')),
path('add/',views.add,name='employee'),
path('viewemp/',views.viewemp,name='viewemp'),
path('updateemp/<int:pk>',views.upemp, name='uemployee'),
path('delemp/<int:pk>',views.delemp,name='delemp'),
path('login/',views.user_login,name='login'),
path('logout/',views.user_logout,name='logout'),
path('customer/',views.customer,name='customer'),
path('viewcustomer/',views.viewcustomer,name='vcustomer'),
path('updatecustomer/<int:pk>',views.upcustomer,name='ucustomer'),
path('delcustomer/<int:pk>',views.delcustomer,name='dcustomer'),


]
