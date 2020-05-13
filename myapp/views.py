# from django.shortcuts import render
from . import models 
from .forms import SigninForm, SignupForm, DateForm
import json

from django.shortcuts import render, redirect, HttpResponse

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
        message = None
        print('3434')
        print(fib(33)) # delay
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        signin_form = SigninForm(request.POST)
        if signin_form.is_valid():
            username = signin_form.cleaned_data['username']
            password = signin_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    request.session['is_signin'] = True
                    request.session['user_name'] = user.name
                    return redirect("/")
                else:
                    message = 'Incorrect password'
            except:
                message = 'Invalid username'
        return render(request, 'signin.html', {"signin_form": signin_form, "message": message})
    signin_form = SigninForm()
    return render(request, 'signin.html', {"signin_form": signin_form})

def signup(request):
    print('3333')
    if request.method == "POST":
        if 'signup' in request.POST:
            print(fib(33))
            signup_form = SignupForm(request.POST)
            if signup_form.is_valid():
                username = signup_form.cleaned_data['username']
                password = signup_form.cleaned_data['password']
                try:
                    new_user = models.User.objects.create()
                    new_user.name = username
                    new_user.password = password
                    new_user.save()
                    return redirect("/user/signin/")
                except:
                    message = 'Error occured when creating account.'
                    return render(request, 'signup.html', {"signup_form": signup_form, "message": message})
        else:
            reply = {'status': True, 'msg': None}
            print(fib(28))
            username = request.POST.get('username')
            same_name_user = models.User.objects.filter(name=username)
            if same_name_user:
                reply['status'] = False
            return HttpResponse(json.dumps(reply))
    signup_form = SignupForm()
    return render(request, 'signup.html', {"signup_form": signup_form})

def logout(request):
    print('5555')
    if not request.session.get('is_signin', None): # 如果本来就未登录，也就没有登出一说
        return redirect("/")
    request.session.flush() # 或者使用下面的方法
    # del request.session['is_signin']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/")
