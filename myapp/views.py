# from django.shortcuts import render
from . import models 
from .forms import UserForm, RegisterForm, DateForm
import json

from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def home(request):
    print('0000')
    if request.method == "POST":
        print('7878')
        date_form = DateForm(request.POST)
        print('9090')
        if not request.session.get('is_signin', None):
            message = '未登录！'
            return render(request, 'home.html', {"date_form": date_form, "message": message})
        else:
            if date_form.is_valid(): 
                # date = request.POST.get('date')
                print('1212')
                date = date_form.cleaned_data['date']
                print(date)
                if date[5:] == '01-01':
                    message = '元旦'
                elif date[5:] == '10-01':
                    message = '国庆节'
                elif date[5:] == '12-25':
                    message = '圣诞节'
                else:
                    message = ''
                return render(request, 'home.html', {"date_form": date_form, "message": message})
    date_form = DateForm()
    return render(request, 'home.html', {"date_form": date_form})

def signin(request):
    print('1111')
    if request.method == "POST":
        reply = {'status': False, 'msg': None}
        print('3434')
        print(fib(32)) # delay
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # print(username, password)
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            # print(username, password)
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    request.session['is_signin'] = True
                    request.session['user_name'] = user.name
                    reply['status'] = True
                    reply['msg'] = 'Sign in successfully'
                    return HttpResponse(json.dumps(reply))
                else:
                    reply['status'] = False
                    reply['msg'] = 'Incorrect password'
            except:
                reply['status'] = False
                reply['msg'] = 'Invalid username'
        return HttpResponse(json.dumps(reply))
    return render(request, 'signin.html')

def signup(request):
    print('3333')
    if request.method == "POST":
        if 'signup' in request.POST:
            print(fib(33)) # delay
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():  # 获取数据
                username = register_form.cleaned_data['username']
                password = register_form.cleaned_data['password']
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = 'error'
                    return render(request, 'signup.html', {"register_form": register_form, "message": message})
                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = password
                new_user.save()
                message = 'success'
                return render(request, 'signup.html', {"register_form": register_form, "message": message})
        # elif 'del-message' in request.POST:
        #     print('9999')
        #     message = ''
        #     register_form = RegisterForm(request.POST)
        #     return render(request, 'signin.html', {"register_form": register_form, "message": message})
    register_form = RegisterForm()
    return render(request, 'signup.html', {"register_form": register_form})

def logout(request):
    print('5555')
    if not request.session.get('is_signin', None): # 如果本来就未登录，也就没有登出一说
        return redirect("/")
    request.session.flush() # 或者使用下面的方法
    # del request.session['is_signin']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/")
