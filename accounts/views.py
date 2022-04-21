from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from accounts.forms import LoginForm
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required


class LoginView(View):
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password']
            )
            if user is None:
                return HttpResponse('Неправильный логин и/или пароль')

            if not user.is_active:
                return HttpResponse('Ваш аккаунт заблокирован')

            login(request, user)
        return render(request, 'accounts/login.html', {"form": form})

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'accounts/login.html', {"form": form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()

            return render(request, "accounts/registration_complete.html",
                              {"new_user": new_user})
    else:
        form = RegistrationForm()

    return render(request, "accounts/register.html", {"user_form": form})


@login_required
def about_us(request):
    user_form = request.user
    return render(request, "accounts/about_us.html", {"user_form": user_form})
