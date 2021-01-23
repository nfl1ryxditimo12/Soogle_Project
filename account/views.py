from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import RegisterForm


def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            nickname = form.cleaned_data.get('nickname')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, nickname=nickname, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form': form})


@login_required(login_url='account:login')
def profile(request):

    return render(request, 'account/profile.html')

def page_not_found(request, exception):

    return render(request, 'account/404.html', {})