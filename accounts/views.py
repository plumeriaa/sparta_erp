from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# SIGN UP
def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'accounts/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        email = request.POST.get('email', '')

        if password != password2:
            return render(request, 'accounts/signup.html', {'error': '패스워드를 다시 입력해 주세요.'})
        else:
            if username == '' or password == '':
                return render(request, 'accounts/signup.html', {'error': '아이디와 비밀번호는 필수 값 입니다.'})

            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'accounts/signup.html', {'error': '사용자가 존재합니다.'})
            else:
                UserModel.objects.create_user(username=username, password=password, email=email)
                return redirect('/login')


# LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if username == '' or password == '':
            return render(request, 'accounts/login.html', {'error': '아이디와 비밀번호를 입력해주세요.'})
        else:
            me = auth.authenticate(request, username=username, password=password)
            if me is not None:
                auth.login(request, me)
                return redirect('/')
            else:
                return render(request, 'accounts/login.html', {'error': '아이디 혹은 비밀번호를 확인해주세요.'})
    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'accounts/login.html')


@login_required()
def logout_view(request):
    auth.logout(request)
    return redirect('/')
