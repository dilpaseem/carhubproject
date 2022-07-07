from django.shortcuts import render

# Create your views here.
def user_login(request):
    return render(request,'carhubuser/login.html')

def user_signup(request):
    return render(request,'carhubuser/signup.html') 
    
def user_home(request):
    return render(request,'carhubuser/home.html')

           