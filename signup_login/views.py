from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import new_user_form, user_profile_form
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User


def homepage(request):
    return render(request, "home.html")

@cache_page(60 * 15)
@csrf_protect
def signup(request):
    form = new_user_form()
    profile_form = user_profile_form()
    if request.method == "POST":
        try:
            user_instance = User.objects.get(username =request.user)
        except User.DoesNotExist:
            user_instance = User(username = request.user)
        form = new_user_form(request.POST)
        profile_form = user_profile_form(request.POST or None, request.FILES or None, instance=user_instance)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = User
            profile.save()
            username = form.cleaned_data.get("username")
            user.userprofile.avatar = profile_form.cleaned_data.get("avatar")
            messages.success(request, f"Welcome {username}, Your account was created successfully.")
            login(request, user)
            return redirect("homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")

            return render(request, "signup.html", {"form":form, "profile_form": profile_form})

    context = {
        "form": form,
        "profile_form": profile_form
    }
    return render(request, 'signup.html', context)

def login_req(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request=request, data= request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in Successfully, { username }")
                return redirect('/')
            else:
                messages.error(request, f"Invalid Username or Password !!!")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")

            return render(request, "login.html", {"form":form})

    return render(request, "login.html", {"form":form})

def logout_req(request):
    logout(request)
    messages.info(request, f"Logged Out Successfully !!!")
    return redirect("homepage")

