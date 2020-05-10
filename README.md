# <font face="Consolas" size=7>说明</font>

<font face="Consolas">韩佳乐 PB16051152</font>

***

## <font face="Consolas" size=5>工具</font>

<font face="Consolas">

*python == 3.7*<br>
*Django == 2.2*<br>
*mysqlclient >= 1.3.13*<br>
*mysql == 8.0.20*<br>

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
