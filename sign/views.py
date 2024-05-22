from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login

from .forms import LoginUserForm, RegisterUserForm


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            print(request)
            print(cd['username'], cd['password'])
            login(request, user)

            return HttpResponseRedirect(reverse('card_list'))
    else:
        form = LoginUserForm()
    return render(request, 'sign/login.html', {'form': form})


def registers(request):
    print(request)
    if request.method == "POST":
        print(request)
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)

            return HttpResponseRedirect(reverse('card_list'))

    form = RegisterUserForm()
    return render(request, 'sign/signup.html', {'form': form})
