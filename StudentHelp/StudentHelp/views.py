from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.
def index(request):
    return render(request, 'signIn.html')

def register(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            #user = authenticate(username=username, password=password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, f'bienvenue, {username}')# not showing
            return redirect('acceuil')
    else:
        form = UserCreationForm()
    return render(request,'signUp.html',{'form' : form})