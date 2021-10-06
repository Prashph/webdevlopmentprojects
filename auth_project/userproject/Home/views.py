from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login

#password Prashant@143

# Create your views here.
def index(request): 
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def loginuser(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(username=username, password=password)
        print(username,password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/index")
        else:
            return render(request, 'login.html')
            # No backend authenticated the credentials
        
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")