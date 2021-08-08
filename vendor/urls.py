from django.urls import path
from .views import  dashboardPreviewView, dashboardNewView, dashboardProductListView

app_name = 'vendor'


urlpatterns = [
    path('dashboard/', dashboardPreviewView, name = 'dashboardPreviewView'),
    path('dashboard/new/', dashboardNewView, name = 'dashboardNewView'),
    path('dashboard/products/', dashboardProductListView, name = 'dashboardProductListView'),
]