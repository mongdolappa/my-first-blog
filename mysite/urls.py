"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.contrib import admin
from django.urls import path, include
#from django.urls 행을 찾아 import 뒤에 include 함수를 추가하세요.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    #지금 장고는 http://127.0.0.1:8000/ 로 들어오는 모든 접속 요청을 blog.urls로 전송해 추가 명령을 찾을 거예요.
]
