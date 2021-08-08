from django import forms


class editProfileForm(forms.Form):
    full_name = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control', 'type':"text", 'name':"fullname"}),  max_length=1500, required=True)
    brand_name = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control', 'type':"text", 'name':"brandname"}),  max_length=1500, required=True)
    phone = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control', 'type':"tel", 'name':"phone"}),  max_length=1500, required=True)
    whatsapp = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control', 'type':"tel", 'name':"whatsapp"}),  max_length=1500, required=True)
    location = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control', 'type':"text", 'name':"location"}),  max_length=1500, required=True)
    
 

class newProductForm(forms.Form):
    name = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control', 'type':"text", 'name':"name"}), max_length=1500, required=True)
    Design_Description = forms.CharField(widget = forms.Textarea(attrs = {'name':"desc" ,'id':"description" ,'cols':"40", 'rows':"5" ,'class':"desc" ,'placeholder':"40 words max"}), max_length=2000, required=True)