"""college URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views
urlpatterns = [
    # path('',views.home,name="home"),
    
    path('home/',views.home,name="home"),
    path('home/<int:num>',views.home,name="homefilter"),
    path('home/<int:num>/<str:topic>',views.topics,name="hometopic"),
    path('myprofile/',views.myprofile,name="myprofile"),
    path('signup/',views.signup,name="signup"),
    path('signup_student/',views.signup_student,name="signup_student"),
    path('signup_teacher/',views.signup_teacher,name="signup_teacher"),
    path('login/',views.login,name="login"),
    path('createproject/',views.createproject,name="createproject"),
    path('createresearch/',views.createresearch,name="createresearch"),
    path('logout/',views.logout,name="logout"),
    path('delete/',views.delete,name="delete")
]
