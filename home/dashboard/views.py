from dashboard.models import ContactUs
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
# Create your views here.

# def index(request):
#     if request.user.is_authenticated:
#         html_template = 'dashboard/index.html'
#         return render(request,html_template)
#     else:
#         return redirect('login/')

@login_required()
def index(request):
    html_template = 'dashboard/index.html'
    return render(request,html_template)

@login_required()
def details(request):
    html_template = 'dashboard/details.html'
    return render(request,html_template)

@login_required()
def myservices(request):
    html_template = 'dashboard/services.html'
    return render(request,html_template)

@login_required()
def contactus(request):
    if request.method == 'POST':
        print("------------------------------",request.POST)
        print("first name",request.POST.get('first_name',"shreyash"))
        print("last name",request.POST['last_name'])
        print("email",request.POST['email'])
        print("phone",request.POST['phone'])
        print("address",request.POST['address'])
        obj,created=ContactUs.objects.get_or_create(first_name = request.POST.get('first_name'),last_name= request.POST['last_name'],email=request.POST['email'],phone=request.POST['phone'],address = request.POST['address'])
        print('obj and created',obj,created)
        
        if created:
            messages.success(request, 'New entry created')
        else:
            messages.info(request, 'Entry already exist')
    html_template = 'dashboard/contact.html'
    return render(request,html_template)

def loginUser(request):
    html_template = 'dashboard/login.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
           messages.warning(request, 'Username/Password does not exist') 
    
    return render(request,html_template)

def logoutUser(request):
    html_template = 'dashboard/login.html'
    logout(request)
    return render(request,html_template)