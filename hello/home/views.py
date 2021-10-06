from django.shortcuts import render,redirect
from home.models import Contact
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    context = {
        'veriable':'this is sent'
    }
    return render(request,'index.html',context)
    # return HttpResponse('this is index page')

def about(request):
    return render(request,'about.html')

def services(request):
        return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        decs=request.POST.get('decs')
        contact=Contact
        contact.save()

    return render(request,'contact.html')
    
def loginUser(request):
    if request.POST=="POST":
       username = request.POST['username']
       password = request.POST['password']
       user = authenticate(request, username=username, password=password)
       if user is not None:
            login(request, user)
            return redirect('/index')
        # Redirect to a success page.

       else:
        # Return an 'invalid login' error message.
            return render(request,'login.html')
        
    return render(request,'login.html')