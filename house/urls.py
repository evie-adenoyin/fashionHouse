from django.urls import path
from .views import  homeView, storeView, aboutView, contactFormView

app_name = 'house'


urlpatterns = [
    path('fashionhouse/home/', homeView, name = 'homeView'),
    path('fashionhouse/store/', storeView, name = 'storeView'),
    path('fashionhouse/about/', aboutView, name = 'aboutView'),
    path('fashionhouse/contact/', contactFormView, name = 'contactFormView'),
]