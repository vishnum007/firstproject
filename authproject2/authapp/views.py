from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authapp.forms import SignupForm
from django.http import HttpResponseRedirect

# Create your views here.

def home_view(request):
    return render(request,'authapp/home.html')

@login_required
def java_view(request):
    return render(request,'authapp/java.html')

def logout_view(request):
    return render(request,'authapp/logout.html')

def signup_view(request):
    form=SignupForm()
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'authapp/signup.html',{'form':form})
