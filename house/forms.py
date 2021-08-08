from django import forms


class contactForm(forms.Form):
    name = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control', 'type':"text", 'name':"name", 'placeholder':"Name"}),  max_length=1500, required=True)
    email = forms.EmailField(widget = forms.TextInput(attrs = {'class': 'form-control', 'type':"email", 'name':"email", 'placeholder':"Email"}),  max_length=1500, required=True)
    message = forms.CharField(widget = forms.Textarea(attrs = {'class': 'form-control', 'type':"text", 'name':"message", 'placeholder':"Message", 'rows':"14"}), max_length=2000, required=True)