from django.shortcuts import render,redirect
from my_app.forms import *
from my_app.models import User,Otpmodel
# Create your views here.
from django.views.generic import View
from django.contrib.auth import authenticate,login,logout
import random
from django.core.mail import send_mail
from django.utils.decorators import method_decorator
# key =  nyon xsuj icva pvhe

def is_user(fn):

    def wrapper(request,**kwargs):

        id=kwargs.get("pk")

        item=TaskModel.objects.get(id=id)

        if item.user_id==request.user:

            return fn(request,**kwargs)
        return redirect("login")
    return wrapper





class RegistrationView(View):

    def get(self,request):

        form=Userregistration
        
        return render(request,'signup.html',{"form":form})
    
    def post(self,request):

        form=Userregistration(request.POST)

        if form.is_valid():

            print(form.cleaned_data)

            username=form.cleaned_data.get('username')

            password=form.cleaned_data.get('password')

            email=form.cleaned_data.get('email')

            User.objects.create_user(username=username,password=password,email=email)

        # return render(request,"signup.html",{"form":form})
        return redirect("login")
    

class LoginView(View):

    def get(self,request):

        form=Loginform

        return render(request,'login.html',{"form":form})
    
    def post(self,request):

        form=Loginform(request.POST)

        if form.is_valid():

            username=form.cleaned_data.get('username')

            password=form.cleaned_data.get('password')

            user_obj= authenticate(request,username=username,password=password)

            if user_obj:

                login(request,user_obj)
                
                print(request.user)

                return render(request,'index.html')
                
            else:

                

                return render (request,"login.html",{"form":form})
            
class LogoutView(View):

    def get(self,request):

        logout(request)

        return redirect("login")
    
class AddtaskView(View):

    def get (self,request):

        form=Taskform
        return render(request,'addtask.html',{'form':form})
    
    def post(self,request):

        form=Taskform(request.POST)

        if form.is_valid():

            TaskModel.objects.create(user_id=request.user,**form.cleaned_data)
        return render(request,"addtask.html",{'form':form})
    
class TaskReadView(View):

    def get (self,request):

        # items=TaskModel.objects.all()
        items=TaskModel.objects.filter(user_id=request.user)#filtering tasks which are added by the logged in user

        return render (request,'tasklist.html',{'items':items})
    
@method_decorator(decorator=is_user,name="dispatch")
class TaskUpdateView(View):
    
    def get(self,request,**kwargs):

        id=kwargs.get('pk')

        item=TaskModel.objects.get(id=id)

        form=Taskform(instance=item)

        return render (request,"update.html",{"form":form})
    
    def post(self,request,**kwargs):

        id=kwargs.get('pk')

        item=TaskModel.objects.get(id=id)

        form=Taskform(request.POST,instance=item)

        if form.is_valid():

            form.save()
            

        form=Taskform

        return render(request,'update.html',{"form":form})
    
@method_decorator(decorator=is_user,name="dispatch")
class TaskdeleteView(View):

    def get(self,request,**kwargs):

        id=kwargs.get("pk")

        TaskModel.objects.get(id=id).delete()

        return redirect("tasklist")
    
@method_decorator(decorator=is_user,name="dispatch")
class TaskdetailsView(View):

    def get( self,request,**kwargs):

        id=kwargs.get("pk")

        item=TaskModel.objects.get(id=id)

        return render(request,"details.html",{"item":item})
    
class Taskedit(View):

    def get (self,request,**kwargs):

        id=kwargs.get("pk")

        data=TaskModel.objects.get(id=id)

        data.completed_status=True

        data.save()

        return redirect("tasklist")
    
class ForgotpasswordView(View):

    def get(self,request):

        form=Forgotform

        return render(request,"forgotpswd.html",{"form":form})
    
    def post(self,request):

        form=Forgotform(request.POST)

        if form.is_valid():

            
            email=form.cleaned_data.get('email')

            user=User.objects.get(email=email)

            otp=random.randint(1000,9999)

            Otpmodel.objects.create(user_id=user,otp=otp)

            send_mail(subject="otp for password reset",message=str(otp),from_email="akshains333@gmail.com",
                      recipient_list=[email])
            
            return redirect("otpverify")
            

class OtpVerifyView(View):

    def get (self,request):

        form=OtpVerifyform

        return render(request,"otpverify.html",{"form":form})
    
    def post(self,request):

        form=OtpVerifyform(request.POST)

        if form.is_valid():

            otp=form.cleaned_data.get("otp")

            item=Otpmodel.objects.get(otp=otp)

            user_id=item.user_id
            user=User.objects.get(id=user_id)
            username= user.username


            if item:

                request.session["user"] = username

                return redirect("resetpass")
            
        return render(request,"otpverify.html",{"form":form})
    
class ResetpasswordView(View):

    def get(self,request):

        form=ResetPasswordform
        return render(request,"resetpswd.html",{"form":form})
    
    def post(self,request):

        form=ResetPasswordform(request.POST)

        if form.is_valid():

            password=form.cleaned_data.get("password")

            confirm_password=form.cleaned_data.get("confirm_password")

            if password==confirm_password:

                item=request.session.get('user')

                user=User.objects.get(id=item.user_name)

                user.set_password(password)

                user.save()

                return redirect("login")


class TaskfilterView(View):

    def get(self,request):

        category=request.GET.get('category')

        Task=TaskModel.objects.filter(user_id=request.user)

        tasks=Task.filter(task_category=category)

        return render(request,"filter.html",{"tasks":tasks})

class IndexView(View):

    def get(self,request):

        return render(request,"index2.html")








        




            
        
        



