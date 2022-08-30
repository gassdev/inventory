from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import (
    CreateUserForm,
    UpdateUserForm,
    UpdateProfileForm
)

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard:index')
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=CreateUserForm()

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    return render(request, "users/profile.html")

@login_required
def profile_update(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    
    context = {
        'user_form':user_form,
        'profile_form':profile_form,
    }
    return render(request, "users/profile_update.html", context)