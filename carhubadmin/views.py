from django.shortcuts import render

# Create your views here.
def admin_login(request):
    return render(request,'carhubadmin/login.html')
    