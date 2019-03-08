from django import forms
from .models import make_invoice,add_product,product,Prod_Category,Prod_subcategory,Prod_Brand,Prod_Catalog
from .models import create_store,assign_store

class make_invoiceform(forms.ModelForm):
    class Meta():
        model = make_invoice
        fields = '__all__'

class productform(forms.ModelForm):
    class Meta():
        model = product
        fields = '__all__'


class add_productform(forms.ModelForm):
    class Meta():
        model = add_product
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['SubCategory'].queryset = Prod_subcategory.objects.none()
        if 'Category' in self.data:
            try:
                Category_id = int(self.data.get('Category'))
                self.fields['SubCategory'].queryset = Prod_subcategory.objects.filter(Category_id=Category_id).order_by('Category')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['SubCategory'].queryset = self.instance.Category.SubCategory_set.order_by('SubCategory')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['catalog'].queryset = Prod_Catalog.objects.none()
        if 'Brand' in self.data:
            try:
                Brand_id = int(self.data.get('Brand'))
                self.fields['catalog'].queryset = Prod_Catalog.objects.filter(Brand_id=Brand_id).order_by('Brand')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['catalog'].queryset = self.instance.Brand.catalog_set.order_by('catalog')



class categoryform(forms.ModelForm):
    class Meta():
        model = Prod_Category
        fields = '__all__'


class subcatform(forms.ModelForm):
    class Meta():
        model = Prod_subcategory
        fields = '__all__'

class brandform(forms.ModelForm):
    class Meta():
        model = Prod_Brand
        fields = '__all__'

class catalogform(forms.ModelForm):
    class Meta():
        model = Prod_Catalog
        fields = '__all__'


class createstoreform(forms.ModelForm):
    class Meta():
        model = create_store
        fields='__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['SubCategory'].queryset = Prod_subcategory.objects.none()
        if 'Category' in self.data:
            try:
                Category_id = int(self.data.get('Category'))
                self.fields['SubCategory'].queryset = Prod_subcategory.objects.filter(Category_id=Category_id).order_by('Category')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['SubCategory'].queryset = self.instance.Category.SubCategory_set.order_by('SubCategory')


class assignstoreform(forms.ModelForm):
    class Meta():
        model = assign_store
        fields ='__all__'
