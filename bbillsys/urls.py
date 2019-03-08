"""bbillsys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from bbillsysapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),
    path('accounts/profile/',views.home,name='home'),
    # path('search/',views.query,name='search'),
    # path('makeinvoice/',views.barcode,name='barcode'),
    path('makeinvoice/',views.query,name='query'),
    path('makeinvoice/',views.makeinvoice,name='minvoice'),
    # path('barcode/',views.query,name='bs'),
    path('barcode/',views.barcode,name='barcode'),
    path('viewinvoice/',views.viewinvoice,name='vinvoice'),
    path('detailinvoice/<pk>',views.detailinvoice,name='dinvoice'),
    path('updateinvoice/<pk>',views.updateinvoice,name='uinvoice'),
    path('deleteinvoice/<pk>',views.deleteinvoice,name='deinvoice'),
    path('mail/<pk>',views.sendemail,name='semail'),
    path('addproduct/',views.addproduct,name='aproduct'),
    path('view/',views.product_query,name='view'),
    # path('view/',views.viewcatquery,name='vproduct'),
    path('updateproduct/<int:pk>',views.updateproduct,name='uproduct'),
    path('deleteproduct/<int:pk>',views.delproduct,name='dproduct'),
    path('load/',views.load_category,name='csd'),
    path('loadd/',views.load_brand,name='bcd'),
    path('pdf/<pk>',views.GeneratePdf.as_view(),name='genpdf'),

    # path('extendproduct/',views.extendproduct,name='exproduct'),
    path('', include('django.contrib.auth.urls')),
    path('userapp/',include('userapp.urls')),
    path('ticketapp/',include('ticketapp.urls',namespace="tic")),
    path('chatapp/',include('chatapp.urls')),

    path('category/',views.addcategory,name='category'),
    path('viewcat/',views.viewcategory,name='viewcat'),
    path('<int:pk>',views.updatecategory,name='updatecat'),
    path('delcat/<int:pk>',views.delcategory,name='delcat'),
    path('subcategory/',views.addsubcategory,name='subcategory'),
    path('viewsubcat/',views.viewsubcategory,name='viewsubcat'),
    path('updatesubcat/<int:pk>',views.updatesubcat,name='updatesubcat'),
    path('delsubcat/<int:pk>',views.delsubcat,name='delsubcat'),
    path('brand/',views.addbrand,name='brand'),
    path('viewbrand/',views.viewbrand,name='viewbrand'),
    path('updatebrand/<int:pk>',views.updatebrand,name='updatebrand'),
    path('delbrand/<int:pk>',views.delbrand,name='delbrand'),
    path('catalog/',views.addcatalog,name='catalog'),
    path('viewcatalog/',views.viewcatalog,name='viewcatalog'),
    path('updatecatalog/<int:pk>',views.updatecatalog,name='ucatlog'),
    path('delcatalog/<int:pk>',views.delcatalog,name='delcatalog'),

    path('store/',views.addstore,name='store'),
    path('viewstore/',views.viewstore,name='viewstore'),
    path('updatestore/<int:pk>',views.updatestore,name='upstore'),
    path('delstore/<int:pk>',views.delstore,name='delstore'),

    path('assignstore/',views.assignstore, name='assign'),
    path('viewassignstore/',views.viewassignstore, name='vassign'),
    path('updateassignstore/<int:pk>',views.updateassign,name='uassign'),
    path('delassign/<int:pk>',views.delassign,name='dassign'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
