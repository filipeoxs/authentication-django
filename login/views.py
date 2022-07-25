from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, authenticate, logout
from .form import UserForm,UpdateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def registration_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            messages.add_message(request, messages.SUCCESS,f'Usuário criado.')
            return redirect('login')
    else:
        form = UserForm
    return render(request, 'registration/registration.html', {'form':form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            messages.add_message(request, messages.SUCCESS,f'Usuário validado.')
            return redirect('home')
        else:
            messages.add_message(request, messages.INFO,f'Usuário não encontrado.')
            # Return an 'invalid login' error message.
            return redirect('registration')
    else:
        form = UserForm
        return render(request,'registration/login.html',{'form':form})
    
def logout_user(request):
    logout(request)
    return redirect('login')

def delete_user(request,id):
    user = get_object_or_404(User, id=id)
    user.delete()
    messages.add_message(request, messages.SUCCESS,f'Usuário excluido.')
    return redirect('home')

def update_user(request,id):
    user = User.objects.get(id=id)
    user = UpdateUserForm(request.POST or None, instance=user)
    if user.is_valid():
        user.save()
        messages.add_message(request, messages.SUCCESS,f'Dados alterados.')
        return redirect('home')
    return render(request,'registration/update_user.html',{'user':user})

@login_required
def home_page(request):
    users = User.objects.all().order_by('username')
    return render(request,'registration/home.html',{'users':users})

