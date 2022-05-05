from django.shortcuts import render, redirect
from .models import Posts, Contact
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.


def index(request):
    zz = Posts.objects.all()
    yy = Contact.objects.all()
    return render(request, 'index.html', {'post': zz, 'contactss': yy})


def post(request, pk):
    posts = Posts.objects.get(id=pk)
    return render(request, 'posts.html', {'posts': posts})


def contactform(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')
        if name == "":
            messages.info(request, 'Name Empty')
            return redirect('/#contact')
        elif email == "":
            messages.info(request, 'Email Empty')
            return redirect('/#contact')
        elif number == "":
            messages.info(request, 'Number Empty')
            return redirect('/#contact')
        elif message == "":
            messages.info(request, 'Message Empty')
            return redirect('/#contact')
        else:
            contact.name = name
            contact.number = number
            contact.email = email
            contact.message = message
            contact.save()
            return redirect('/')
    return redirect('/')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def createform(request):
    if request.method == 'POST':
        post = Posts()
        name = request.POST.get('name')
        content = request.POST.get('content')
        y = 1
        for x in Posts.objects.all():
            if x.id == y:
                y = y+1
            else:
                post.id = y
        post.title = name
        post.content = content
        post.save()
        messages.info(request, 'Post Created')
        return redirect('/#mess')
    return redirect('/')


def delete(request, pk):
    Posts.objects.filter(id=pk).delete()
    messages.info(request, 'Post Deleted')
    return redirect('/#mess')


def delcon(request, sk):
    Contact.objects.filter(id=sk).delete()
    messages.info(request, 'Contact Deleted')
    return redirect('/#mess')

