from django.urls import path
from chatapp import views

urlpatterns=[
path('chat/<int:pk>',views.chat,name='chat'),
path('users/',views.all_user,name='users'),
path('showchat/<int:pk>',views.show_chat,name='show_chat'),


]
