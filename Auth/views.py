from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.template.base import Template
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

def sign_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password =  request.POST.get('password')
        errors = {}

        try:
            user = User.objects.get(email = email)
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
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')

        password = request.POST.get('password')
        password_validation = request.POST.get('password_validation')

        errors = {}
        if not name:
            errors['name'] = 'Укажите ваше имя'
        if not surname:
            errors['surname'] = 'Укажите вашу фамилию'
        if password != password_validation:
            errors['password_validation'] = 'Пароли не совпадают'
        if not email:
            errors['email'] = 'Укажите email'
        if email and User.objects.filter(email = email).all().count() > 0:
            errors['email'] = 'Такой Email уже используется'
        if len(password) < 8:
            errors['password_validation'] = 'Пароль не должен быть меньше 8 символов'

        if not errors:
            user = User.objects.create_user(username=email, password=password, first_name = name, last_name = surname, email = email)
            user.save()

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
