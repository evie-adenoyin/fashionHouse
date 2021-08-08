from django.shortcuts import render
from django.http import HttpResponse
from .forms import contactForm
from .models import Post
# Create your views here.


def homeView(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render (request, 'house/home_page.html', context)


def storeView(request):
    return render (request, 'house/stores_page.html')


def aboutView(request):
    return render (request, 'house/about_page.html')


def contactFormView(request):
    if request.method == "POST":
        form = contactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name, email, message)
    else:
        form = contactForm()
    context = {
        'form': form
    }
    return render (request, 'house/contact_form_page.html', context)