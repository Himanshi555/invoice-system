from django.shortcuts import render,render_to_response,redirect
from .forms import make_invoiceform,add_productform,productform
from .forms import categoryform,subcatform,brandform,catalogform
from .models import make_invoice,product
from .models import add_product
from .models import Prod_Category,Prod_subcategory,Prod_Brand,Prod_Catalog
from django.contrib import messages
#mailing import files
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string, get_template
from django.template import Context
from bbillsysapp.barcode import MyBarcodeDrawing
import random
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from .utils import Render
from django.views.generic import View
#Search
import django_filters
from django.db.models import Q

from .forms import createstoreform,assignstoreform
from .models import create_store,assign_store
# Create your views here.

def home(request):
    return render(request,'home.html')

def makeinvoice(request):
    form = make_invoiceform()
    form1 = productform()

    if request.method == 'POST' and 'submitbutton2' in request.POST :
        form = make_invoiceform(request.POST)
        form1 = productform(request.POST)

        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
            return HttpResponseRedirect(reverse(vinvoice))
        else:
            print("Error in form")
    return render(request,'makeinvoice.html',{'form':form,'form1':form1})

def viewinvoice(request):
    vinvoice = make_invoice.objects.order_by()
    context = {'v_invoice':vinvoice}
    return render(request,'viewinvoice.html',context)

def detailinvoice(request,pk):
    dinvoice = make_invoice.objects.get(pk=pk)
    pinvoice = product.objects.get(pk=pk)
    context = {'d_invoice':dinvoice,'p_invoice':pinvoice}
    return render(request,'detailinvoice.html',context)

def updateinvoice(request,pk):
    uinvoice = make_invoice.objects.get(pk=pk)
    form = make_invoiceform(request.POST,instance=uinvoice)

    if form.is_valid():
        form.save()
        return viewinvoice(request)
    else:
        print("Update Error")
    return render(request,'updateinvoice.html',{'form':form,'uinvoice':uinvoice})

def deleteinvoice(request,pk):
    deinvoice = make_invoice.objects.get(pk=pk)
    deinvoice.delete()
    return viewinvoice(request)


#Mailing

    # send_mail('Success pk method',
    # 'Hello there. This is an 2automated message.',
    # 'swst2146@gmail.com',
    # [sendinvoice.email],
    # fail_silently=False)
    #
    # subject = 'Thank you'
    # message = 'hello bro'
    # from_email = settings.EMAIL_HOST_USER
    # to_list = [sendinvoice.email, settings.EMAIL_HOST_USER]
    # attach = request.
    # send_mail(subject,message,from_email,to_list,fail_silently=True)

    # email = EmailMessage('Subject here', 'Here is the message', settings.EMAIL_HOST_USER, [sendinvoice.email])
    # email.attach_file(Render.render_to_pdf('detailinvoice1.html'))
    # email.send()
def sendemail(request,pk):

    dinvoice = make_invoice.objects.get(pk=pk)
    pinvoice = product.objects.get(pk=pk)
    subject = 'Thank you'

    from_email = settings.EMAIL_HOST_USER
    to_list = [dinvoice.email]

    ctx = {
       'order_number': dinvoice.order_number,
       'invoice_number': dinvoice.invoice_number,
       'product_name':pinvoice.product_name,
       'product_id':pinvoice.product_id,
       'quantity':pinvoice.quantity,
       'price':pinvoice.price,
       'size':pinvoice.size,
       'user_full_name':dinvoice.user_full_name,
       'email':dinvoice.email,
       'contact_number':dinvoice.contact_number,
       'address':dinvoice.address,
       'shipping_user_full_name':dinvoice.shipping_user_full_name,
       'shipping_user_contact_no':dinvoice.shipping_user_contact_no,
       'city':dinvoice.city,
       'country':dinvoice.country,
       'zipcode':dinvoice.zipcode,
       'client_gst':dinvoice.client_gst,
       'mode_of_payment':dinvoice.mode_of_payment,
       'date_and_time':dinvoice.date_and_time,
       'shipping_cost':dinvoice.shipping_cost,
    }
    message = render_to_string('detailinvoice1.html',ctx)
    # message = get_template('detailinvoice1.html').render(Context(ctx))

    # pdf = Render.render_to_pdf('detailinvoice1.html',context_dict)
    # msg = EmailMessage("title","content",to=["singhal121997@gmail.com"])
    # msg.attach('my_pdf.pdf',pdf,'application/pdf')
    # msg.content_subtype = "html"
    # msg.send()
    # send_mail(subject,message,from_email,to_list,fail_silently=True)
    # return HttpResponse("Sent an email!!")
    msg = EmailMessage(subject,message,to=to_list,from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()
    return render(request,'sendemail.html')

# add product

def addproduct(request):
    form = add_productform()

    if request.method == 'POST':
        form = add_productform(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            # return HttpResponse("Product Added successfully!")
            # return redirect('viewproduct')
            return HttpResponseRedirect(reverse(view))
        else:
            print("Error in form")
    return render(request,'addproduct.html',{'form':form})

def viewproduct(request):
    viewp = product.objects.all()
    return render(request,'product_query.html',{'viewp':viewp})

def updateproduct(request,pk):
    upro = add_product.objects.get(pk=pk)
    form = add_productform(request.POST,instance=upro)
    if form.is_valid():
        form.save()
        return viewproduct(request)
    else:
        print('Update error!!!')
    return render(request,'updateproduct.html',{'form':form, 'upro':upro})

def delproduct(request,pk):
    delpro = add_product.objects.get(pk=pk)
    delpro.delete()
    return viewproduct(request)


def load_category(request):
    Category_id = request.GET.get('Category')
    subc = Prod_subcategory.objects.filter(Category_id=Category_id).order_by('Category')
    return render(request, 'csd.html', {'subc': subc})

def load_brand(request):
    Brand_id = request.GET.get('Brand')
    catl = Prod_Catalog.objects.filter(Brand_id=Brand_id).order_by('Brand')
    return render(request,'bcd.html',{'catl':catl})

# pdf generator

class GeneratePdf(View):
    def get(self, request, pk):
        dinvoice = make_invoice.objects.get(pk=pk)
        pinvoice = product.objects.get(pk=pk)
      #     [{% for s in d_invoice.product_set.all %}
      #   {{s.price}},
      # {% endfor %}]
        context_dict = {
           'order_number': dinvoice.order_number,
           'invoice_number': dinvoice.invoice_number,
           'product_name':pinvoice.product_name,
           'product_id':pinvoice.product_id,
           'quantity':pinvoice.quantity,
           'price':pinvoice.price,
           'size':pinvoice.size,
           'user_full_name':dinvoice.user_full_name,
           'email':dinvoice.email,
           'contact_number':dinvoice.contact_number,
           'address':dinvoice.address,
           'shipping_user_full_name':dinvoice.shipping_user_full_name,
           'shipping_user_contact_no':dinvoice.shipping_user_contact_no,
           'city':dinvoice.city,
           'country':dinvoice.country,
           'zipcode':dinvoice.zipcode,
           'client_gst':dinvoice.client_gst,
           'mode_of_payment':dinvoice.mode_of_payment,
           'date_and_time':dinvoice.date_and_time,
           'shipping_cost':dinvoice.shipping_cost,

        }
        return Render.render_to_pdf('detailinvoice1.html', context_dict)


#barcode gen

def barcode(request):
    #instantiate a drawing object
    for i in range(3):
        x = random.randrange(100,100000000000,12)
    d = MyBarcodeDrawing(x)
    print(x)
    binaryStuff = d.asString('gif')
    d.save(formats=['gif'],outDir='bbillsysapp/static/barcode',fnRoot='barcode')
    barcodePicUrl = "barcode/barcode.gif"
    return render(request,'barcode.html',{'x':x})


def query(request):
    if request.method == 'POST' and 'submitbutton1' in request.POST :
        search = request.POST['search']
        if search:
            m = product.objects.filter(Q(product_id__icontains=search))
            if m:
                return render(request,'makeinvoice.html',{'srch':m})

    return render(request,'makeinvoice.html',{'query':query})

# def viewcatquery(request):
#     view = Prod_Category.objects.all()
#     return render(request,'product_query.html',{'view':view})

def product_query(request):
    view = Prod_Category.objects.all()
    # v = add_product.objects.all()
    if request.method == 'POST':
        search = request.POST['search']
        if search:
            catg = add_product.objects.filter(Q(Category__Category__icontains=search))
            # for vi in view:
            #     for w in v:
            #         if int(w.Quantity) <= 35 and vi.Category == 'A':
            # messages.info(request,'Your Quantity is below 35!!!')
                    # elif int(w.Quantity) >35:
                    #     break
            if catg:
                return render(request,'product_query.html',{'category':catg,'view':view})

    return render(request,'product_query.html',{'product_query':product_query,'view':view})



def addcategory(request):
    form = categoryform()

    if request.method == 'POST':
        form = categoryform(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('viewcat'))
            # return redirect('viewcategory')
        else:
            print("Error in form")
    return render(request,'addcategory.html',{'form':form})

def viewcategory(request):
    view = Prod_Category.objects.all()
    return render(request,'viewcategory.html',{'view':view})



def updatecategory(request,pk):
    ucat = Prod_Category.objects.get(pk=pk)
    form = categoryform(request.POST,instance=ucat)
    if form.is_valid():
        form.save()
        return viewcategory(request)
    else:
        print("Error in form")
    return render(request,'updatecategory.html',{'form':form,'ucat':ucat})

def delcategory(request,pk):
    delcat = Prod_Category.objects.get(pk=pk)
    delcat.delete()
    return viewcategory(request)


def addsubcategory(request):
    form = subcatform()

    if request.method == 'POST':
        form = subcatform(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            # return HttpResponse("Subcategory Added successfully!")
            return HttpResponseRedirect(reverse('viewsubcat'))
            # return redirect('viewsubcategory')
        else:
            print("Error in form")
    return render(request,'addsubcategory.html',{'form':form})

def viewsubcategory(request):
    view = Prod_subcategory.objects.all()
    return render(request,'viewsubcategory.html',{'view':view})

def updatesubcat(request,pk):
    uscat = Prod_subcategory.objects.get(pk=pk)
    form = subcatform(request.POST,instance=uscat)
    if form.is_valid():
        form.save()
        return viewsubcategory(request)
    else:
        print("Update errors!!!")
    return render(request,'updatesubcat.html',{'form':form,'uscat':uscat})

def delsubcat(request,pk):
    uscat = Prod_subcategory.objects.get(pk=pk)
    uscat.delete()
    return viewsubcategory(request)

def addbrand(request):
    form = brandform()

    if request.method == 'POST':
        form = brandform(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            # return HttpResponse("Brand Added successfully!")
            return HttpResponseRedirect(reverse('viewbrand'))
            # return redirect('viewbrand')
        else:
            print("Error in form")
    return render(request,'addbrand.html',{'form':form})



def viewbrand(request):
    view = Prod_Brand.objects.all()
    return render(request,'viewbrand.html',{'view':view})


def updatebrand(request,pk):
    ubrand = Prod_Brand.objects.get(pk=pk)
    form = brandform(request.POST,instance=ubrand)
    if form.is_valid():
        form.save()
        return viewbrand(request)
    else:
        print("Update error!!!")
    return render(request,'updatebrand.html',{'form':form,'ubrand':ubrand})

def delbrand(request,pk):
    dbrand = Prod_Brand.objects.get(pk=pk)
    dbrand.delete()
    return viewbrand(request)

def addcatalog(request):
    form = catalogform()

    if request.method == 'POST':
        form = catalogform(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('viewcatalog'))
            # return HttpResponse("Catalog Added successfully!")
            # return redirect('viewcatalog')
        else:
            print("Error in form")
    return render(request,'addcatalog.html',{'form':form})


def viewcatalog(request):
    view = Prod_Catalog.objects.all()
    return render(request,'viewcatalog.html',{'view':view})

def updatecatalog(request,pk):
    ucatalog = Prod_Catalog.objects.get(pk=pk)
    form = catalogform(request.POST,instance=ucatalog)
    if form.is_valid():
        form.save()
        return viewcatalog(request)
    else:
        print("Update error!!!")

    return render(request,'updatecatalog.html',{'form':form,'ucatalog':ucatalog})

def delcatalog(request,pk):
    upcatl = Prod_Catalog.objects.get(pk=pk)
    upcatl.delete()
    return viewcatalog(request)

def addstore(request):
    form = createstoreform()
    if request.method == 'POST':
        form = createstoreform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('viewstore')
            return HttpResponseRedirect(reverse('viewstore'))
            # return HttpResponse('store created!!')
        else:
            print("Error in form")
    return render(request,'addstore.html',{'form':form})

def viewstore(request):
    viewstore = create_store.objects.all()
    return render(request,'viewstore.html',{'viewstore':viewstore})

def updatestore(request,pk):
    view = create_store.objects.get(pk=pk)
    form = createstoreform(request.POST, instance=view)
    if form.is_valid():
        form.save()
        return viewstore(request)
    else:
        print('Error while update store!!')

    return render(request,'updatestore.html',{'view':view, 'form':form})

def delstore(request,pk):
    view = create_store.objects.get(pk=pk)
    view.delete()
    return viewstore(request)


def assignstore(request):
    form = assignstoreform()
    if request.method == 'POST':
        form = assignstoreform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vassign'))
            # return redirect('viewassign')
        else:
            print('Error while assigning')
    return render(request,'assignstore.html',{'form':form})

def viewassignstore(request):
    view = assign_store.objects.all()
    return render(request,'viewassignstore.html',{'view':view})

def updateassign(request,pk):
    view = assign_store.objects.get(pk=pk)
    form = assignstoreform(request.POST,instance=view)
    if form.is_valid():
        form.save()
        return viewassignstore(request)
    else:
        print('Error while update store!!')

    return render(request,'updateassignstore.html',{'view':view, 'form':form})

def delassign(request,pk):
    delas = assign_store.objects.get(pk=pk)
    delas.delete()
    return viewassignstore(request)
