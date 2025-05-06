"""
URL configuration for Todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from my_app.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView.as_view(),name='index'),
    path('todo/signup/',RegistrationView.as_view(),name="Signup"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('login/',LoginView.as_view(),name="login"),
    path('addTask/',AddtaskView.as_view(),name="create"),
    path('listTask/',TaskReadView.as_view(),name="tasklist"),
    path('updateTask/<int:pk>',TaskUpdateView.as_view(),name="update"),
    path('deleteTask/<int:pk>',TaskdeleteView.as_view()),
    path('detailsview/<int:pk>',TaskdetailsView.as_view(),name="detail"),
    path('editTask/<int:pk>',Taskedit.as_view(),name="taskedit"),
    path('ForgotPassword/',ForgotpasswordView.as_view(),name="forgot"),
    path('otpverify/',OtpVerifyView.as_view(),name="otpverify"),
    path('resetPassword/',ResetpasswordView.as_view(),name="resetpass"),
    path('Filter/',TaskfilterView.as_view()),
]
