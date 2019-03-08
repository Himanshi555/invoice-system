from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
from smart_selects.db_fields import ChainedForeignKey
from userapp.models import Employee
# Create your models here.

# SIZE_CHOICES = (
#     ('s','S'),
#     ('m','M'),
#     ('l','L'),
#     ('xl','XL'),
#     ('xxl','XXL'),
# )

Product_type_CHOICES = (
    ('Deals of the Day', 'Deals of the Day'),
    ('Latest Designer Dresses', 'Latest Designer Dresses'),
    ('Recommended by we', 'Recommended by we'),
    ('Top Rated Product', 'Top Rated Product'),
)
# Product_Category = (
#     ('Home Needs', 'Home Needs'),
#     ('Grocery Staples and More','Grocery Staples and More'),
#     ('Fruits and Vegetables', 'Fruits and Vegetables'),
#     ('Beverages', 'Beverages'),
#     ('Bread Dairy and Eggs','Bread Dairy and Eggs'),
#     ('Personal Care','Personal Care'),
#     ('Kids Utilities','Kids Utilities'),
# )

class make_invoice(models.Model):
    order_number = models.CharField(max_length=50,unique=True)
    invoice_number = models.CharField(max_length=50,unique=True)
    user_full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=40)
    contact_number = PhoneNumberField()
    discount = models.PositiveIntegerField()
    address = models.TextField(max_length=100)
    shipping_user_full_name = models.CharField(max_length=50)
    shipping_user_contact_no = PhoneNumberField()
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=10)
    client_gst = models.CharField(max_length=20)
    mode_of_payment = models.CharField(max_length=20)
    date_and_time = models.DateTimeField(default=datetime.today(),blank=True)
    shipping_cost = models.CharField(max_length=10)


    def __str__(self):
        return self.order_number + ' - ' + self.invoice_number

class product(models.Model):
    minvoice = models.ForeignKey(make_invoice, on_delete='DO_NOTHING')
    product_name = models.CharField(max_length=50)
    product_id = models.CharField(max_length=50,unique=True)
    quantity = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=6)

    def __str__(self):
        return self.product_id




class Prod_Category(models.Model):
    Category = models.CharField(max_length=265)
    image = models.ImageField(upload_to='category_img/', null=True, blank=True)
    Meta_Title = models.CharField(max_length=128)
    Meta_Keyword = models.CharField(max_length=128)
    Meta_Desc = models.CharField(max_length=128)

    def __str__(self):
        return self.Category

class Prod_subcategory(models.Model):
    Category = models.ForeignKey(Prod_Category,on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=265)
    image = models.ImageField(upload_to='subcat_img/', null=True, blank=True)
    Meta_Title = models.CharField(max_length=128)
    Meta_Keyword = models.CharField(max_length=128)
    Meta_Desc = models.CharField(max_length=128)

    def __str__(self):
        return self.subcategory

class Prod_Brand(models.Model):
    Brand = models.CharField(max_length=265)
    image = models.ImageField(upload_to='brand_img/', null=True, blank=True)
    Meta_Title = models.CharField(max_length=128)
    Meta_Keyword = models.CharField(max_length=128)
    Meta_Desc = models.CharField(max_length=128)

    def __str__(self):
        return self.Brand




class Prod_Catalog(models.Model):
    Brand = models.ForeignKey(Prod_Brand,on_delete=models.CASCADE)
    catalog = models.CharField(max_length=264)
    image = models.ImageField(upload_to='catalog_img/', null=True, blank=True)
    Meta_Title = models.CharField(max_length=128)
    Meta_Keyword = models.CharField(max_length=128)
    Meta_Desc = models.CharField(max_length=128)

    def __str__(self):
        return self.catalog

class add_product(models.Model):
    Product_No = models.CharField(max_length=128)
    Title = models.CharField(max_length=128)
    image = models.ImageField(upload_to='product_img/', null=True, blank=True)
    Price = models.PositiveIntegerField()
    Offer = models.PositiveIntegerField()
    Brand = models.ForeignKey(Prod_Brand, on_delete=models.CASCADE)
    catalog = models.ForeignKey(Prod_Catalog, on_delete=models.CASCADE)
    Size = models.CharField(max_length=50)
    Weight_per_kg = models.PositiveIntegerField(default='1')
    Category = models.ForeignKey(Prod_Category, on_delete=models.CASCADE)
    SubCategory = models.ForeignKey(Prod_subcategory, on_delete=models.CASCADE)
    Product_Type = models.CharField(max_length=100, choices=Product_type_CHOICES)
    Quantity = models.CharField(max_length=128)
    Product_Description = models.TextField(max_length=128)
    Details = models.TextField(max_length=128)
    Meta_Title = models.CharField(max_length=128)
    Meta_Keyword = models.CharField(max_length=128)
    Meta_Desc = models.CharField(max_length=128)


class create_store(models.Model):
    select_brand = models.ForeignKey(Prod_Brand, on_delete=models.CASCADE)
    store_no = models.PositiveIntegerField()
    Title = models.CharField(max_length=255)
    Image = models.ImageField(upload_to='create_store/', null=True, blank=True)
    Category = models.ForeignKey(Prod_Category, on_delete=models.CASCADE)
    SubCategory = models.ForeignKey(Prod_subcategory, on_delete=models.CASCADE)
    Details = models.TextField(max_length=255)
    Store_description = models.TextField(max_length=255)
    Meta_Title = models.CharField(max_length=128)
    Meta_Keyword = models.CharField(max_length=128)
    Meta_Desc = models.CharField(max_length=128)

    def __str__(self):
       return self.Title


class assign_store(models.Model):
    select_store = models.ForeignKey(create_store,on_delete=models.CASCADE)
    select_employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
