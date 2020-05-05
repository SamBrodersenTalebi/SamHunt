from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def signup(request):
  if request.method == 'POST':
    #The user wants to signup
    #check to see if passwords match
    if request.POST['password1'] == request.POST['password2']:
      try:
        #check to see if username exists
        user = User.objects.get(username = request.POST['username'])
        # return signup page again but with error dic
        return render(request, 'account/signup.html', {'error':'Username has already been taken'})
      except User.DoesNotExist:
        #make new user object if user does not exists
        user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
        #login with the user
        auth.login(request, user)
        #then redirect to homepage
        return redirect('home')
    else:
      #password does not match error
      return render(request, 'account/signup.html', {'error':'Passwords does not match'})
  else:
    #The user want to info
    return render(request, 'account/signup.html')
  

def login(request):
  if request.method == 'POST':
    user = auth.authenticate(username=request.POST['username'] , password=request.POST['password'])
    if user is not None:
      #if we get user then is not none, and we'll login
      auth.login(request, user)
      #redirect homepage
      return redirect('home')
    else:
      return render(request, 'account/login.html', {'error': 'Wrong credentials'})
  else:
    return render(request, 'account/login.html')


def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    return redirect('home')