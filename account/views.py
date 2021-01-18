from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import RegisterForm


def register(request):
    """
    계정생성
    """
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


