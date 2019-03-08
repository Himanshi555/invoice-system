from django.urls import path
from ticketapp import views
app_name = 'tic'
urlpatterns=[
path('index',views.index,name='index'),
path('list/',views.ticketview.as_view(),name='ticketview'),
path('detail/<int:pk>',views.Detail_view,name='Detail_view'),

]
