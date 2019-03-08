from django.contrib import admin
from .models import make_invoice,add_product,product
from .models import Prod_Category,Prod_subcategory,Prod_Brand,Prod_Catalog
from .models import create_store,assign_store
# Register your models here.
admin.site.register(make_invoice)
admin.site.register(add_product)
admin.site.register(product)
admin.site.register(Prod_Category)
admin.site.register(Prod_subcategory)
admin.site.register(Prod_Brand)
admin.site.register(Prod_Catalog)
admin.site.register(create_store)
admin.site.register(assign_store)


# class Prod_BrandAdmin(admin.ModelAdmin):
#     fields = ['image_tag']
#     readonly_fields = ['image_tag']
#     def image_tag(self):
#         return mark_safe('<img src="{url}" widht="{width}" height="{height}"/>'.format(
#         url = obj.image.url,
#         width =100,
#         height=100,
#         )
#         )
