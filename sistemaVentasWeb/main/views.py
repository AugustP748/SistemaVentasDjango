from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        #return render(request,'registration/login.html')
        if user is not None:
            login(request,user)
            return render(request,'main/index.html')
        else:
            return render(request,"registration/login.html",{
                'error_message':"El usuario o contraseña no es correcto."
                })
    else:
        return render(request,'registration/login.html')
        
        
def logout_view(request):
    logout(request)