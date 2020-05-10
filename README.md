# <font face="Consolas" size=7>说明</font>

<font face="Consolas">韩佳乐 PB16051152</font>

***

## <font face="Consolas" size=5>工具</font>

<font face="Consolas">

*python==3.7*<br>
*Django==2.2*<br>
*mysqlclient>=1.3.13*<br>
*mysql==8.0.20*<br>

</font>

## <font face="Consolas" size=5>部署</font>

<font face="Consolas">

1. 安装 django

```c
pip install django==2.2
```

2. 安装 mysqlclient

```c
pip install mysqlclient
```

3. 修改 `DjangoDemo\settings.py` 数据库配置。使用 `root` 账户登录 `mysql` ，新建数据库 `django_mysql`（数据库名可以修改，但应和 `NAME` 保持一致）。其次，将 `PASSWORD` 修改为你的数据库密码。`HOST` 和 `PORT` 无需改动。

```c
DATABASES = { 'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'django_mysql',  #  --> 新建数据库
    'USER': 'root',
    'PASSWORD': '',          #  --> 修改为你的密码
    'HOST': '127.0.0.1',
    'PORT': '3306',
    }
}
```

4. 数据库迁移。在 `DjangoDemo` 目录下执行

```c
python manage.py makemigrations
python manage.py migrate
```

5. 运行项目。在 `DjangoDemo` 目录下执行

```c
python manage.py runserver
```

</font>

## <font face="Consolas" size=5>代码风格约定</font>

<font face="Consolas">

*pylint==2.5.0*

</font>

## <font face="Consolas" size=5>接口说明</font>

1. /，home 页面接口名为 `DjangoDemo\myapp\forms.py` 中自定义表单 `DateForm` 中的 `date`，接受的参数为 `YY-MM-DD` 格式的字符串，返回格式为字符串，在后端使用 `session` 判断用户是否处于登录状态。

    <center><img src="https://img-blog.csdnimg.cn/20200510120640461.PNG" width="70%"></img></center>

2. /user/login/，继承 home 页面，login 页面接口名为 `DjangoDemo\myapp\forms.py` 中自定义表单 `UserForm` 中的 `username` 和 `password`，接受的参数为非空字符串，返回格式为字符串。若登录失败，后端返回 `Incorrect username or password.`；若登录成功，后端通过 `session` 设置用户处于登录状态，并直接跳转至 `home` 页面，右上角显示用户信息。

    <center><img src="https://img-blog.csdnimg.cn/20200510120640465.PNG" width="70%"></img></center>

3. /user/signup/，继承 home 页面，signup 页面接口名为 `DjangoDemo\myapp\forms.py` 中自定义表单 `RegisterForm` 中的 `username` 和 `password`，接受的参数为非空字符串，返回格式为字符串。若注册失败，后端返回 `Username is already taken`；若注册成功，后端返回 `Sign up successfully!`。

    <center><img src="https://img-blog.csdnimg.cn/20200510120640490.PNG" width="70%"></img></center>
