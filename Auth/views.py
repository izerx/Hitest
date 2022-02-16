from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.template.base import Template
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =  request.POST.get('password')
        errors = {}

        try:
            user = User.objects.get(username = username)
        except Exception:
            errors['user'] = 'Пользователь не найден'
            context = {'errors': errors}
            return render(request, 'Auth/login.html', context)

        if user.check_password(password):
            login(request, user)
            return redirect('/')
        else:
            errors['password'] = 'Пароль введен не верно'
            context = {'errors': errors}
            return render(request, 'Auth/login.html', context)

    return render(request, 'Auth/login.html')

def sign_up(request):

    if request.method == 'POST':
        fio = request.POST.get('fio')
        username = request.POST.get('username')
        group = request.POST.get('group')

        password = request.POST.get('password')
        password_validation = request.POST.get('password_validation')

        errors = {}
        if not fio:
            errors['fio'] = 'Укажите ваше фио'
        if password != password_validation:
            errors['password_validation'] = 'Пароли не совпадают'
        if not username:
            errors['username'] = 'Укажите имя пользователя'
        if username and User.objects.filter(username = username).all().count() > 0:
            errors['email'] = 'Такой имя пользователя уже используется'
        if len(password) < 8:
            errors['password_validation'] = 'Пароль не должен быть меньше 8 символов'

        if not errors:
            user = User.objects.create_user(username=username, password=password)
            user.profile.group = group
            user.profile.fio = fio
            user.save()
            user.profile.save()

            login(request, user)

            return redirect('/')
        else:
            print(2)
            context = {
                'errors': errors
            }
            return render(request, 'Auth/register.html', context)

    return render(request, 'Auth/register.html')

def sign_out(request):
    logout(request)
    return redirect('/accounts/login/')
