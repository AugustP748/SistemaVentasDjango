from django.shortcuts import redirect, render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required(login_url="/")
def home(request):
    return render(request,'main/index.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            #return render(request,'main/index.html')
            #return home(request)
            return redirect('main:home')
            
        else:
            return render(request,"registration/login.html",{
                'error_message':"El usuario o contraseña no es correcto."
                })
    else:
        return render(request,'registration/login.html')
        

def logout_view(request):
    logout(request)
    messages.success(request,("Cerraste sesión!"))
    return redirect('main:login_view')