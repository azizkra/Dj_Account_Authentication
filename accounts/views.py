#authenticate => رح تتاكد ازا اليوزر موجود فعلا عندي
from django.shortcuts import render, redirect
from .models import Profile
from .forms import SignupForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth import authenticate, login
# Create your views here.

def signup(request):
    if request.method == 'POST': # SAVE
        form = SignupForm(request.POST)# request.POST => this is data from user
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/accounts/profile')
            
    
    else: # SHOW FORM
        form = SignupForm()
    
    return render(request, 'registration/signup.html', {'form':form})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile/profile.html', {'profile':profile})


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        
        u_form = UserUpdateForm(request.POST,  instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save() 
            myform = p_form.save(commit=False)
            myform.save()
            return redirect('/accounts/profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)
    
    context ={'u_form':u_form, 'p_form':p_form}
    return render(request, 'profile/profile_edit.html', context)