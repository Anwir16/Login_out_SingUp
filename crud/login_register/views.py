from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(f'username: {username}')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
    
def loginViews(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            #thong bao loi
            error = 'Invalid username or password'
            form = AuthenticationForm()
            return render(request, 'login.html', {'form': form, 'error': error})
    else:
        print("loi roi")
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    return render(request, 'login.html')

def logoutViews(request):
    logout(request)
    return redirect('login')
