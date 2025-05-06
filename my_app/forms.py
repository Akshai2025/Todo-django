from django import forms
from my_app.models import User,TaskModel



class Userregistration(forms.ModelForm):

    class Meta:

        model=User

        fields=['username','password','email']

        widgets={"username":forms.TextInput(attrs={"class": "form-control w-50 mx-auto","placeholder":"Enter your Username "}),
                "password":forms.PasswordInput(attrs={"class": "form-control w-50 mx-auto","placeholder":"Enter your password "}),
                "email":forms.EmailInput(attrs={"class":"form-control w-50 mx-auto","placeholder":"Enter your email"})

        }

class Loginform(forms.Form):

    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control w-50 mx-auto","placeholder":"Enter your Username "}
    ))

    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control w-50 mx-auto","placeholder":"Enter your Password  "}))

class Taskform(forms.ModelForm):

    class Meta:

        model=TaskModel

        exclude=['created_date','completed_status','user_id']

class Forgotform(forms.Form):

    email=forms.CharField(max_length=100)

class OtpVerifyform(forms.Form):

    otp=forms.CharField(max_length=100)

class ResetPasswordform(forms.Form):

    password=forms.CharField(max_length=100)

    confirm_password=forms.CharField(max_length=100)  