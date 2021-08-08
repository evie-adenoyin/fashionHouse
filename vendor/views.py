from django.shortcuts import render
from .forms import  editProfileForm, newProductForm
# Create your views here.


def dashboardPreviewView(request):
    form = editProfileForm()
    context = {
        'form': form
    }
    return render (request, 'vendor/dashboard/dashboard_preview.html', context)


def dashboardNewView(request):
    form = newProductForm()
    context = {
        'form': form
    }
    return render (request, 'vendor/dashboard/dashboard_new.html', context)


def dashboardProductListView(request):
    return render (request, 'vendor/dashboard/dashboard_product_list.html')


