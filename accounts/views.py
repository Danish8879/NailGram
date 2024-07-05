from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
#from accounts.forms import CustomAuthenticationForm, SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


from django.http import HttpResponseRedirect #used to redirect from same page

from .models import Profile


# Create your views here.

def login_page(request):
    if request.method=="POST":
        email =  request.POST.get("email")
        password =  request.POST.get("password")

        user_obj = User.objects.filter(username = email) 

        if not user_obj.exists():
            #print(" email already registered ", email)
            messages.warning( request, 'Account not found.' ) 
            return HttpResponseRedirect(request.path_info)

        #print ("first_name=",first_name,"last name = ",last_name,"email=",email)

        if not user_obj[0].profile.is_email_verified:
            messages.warning( request, 'Your account is not verified, Please check your email for the verification link' ) 
            return HttpResponseRedirect(request.path_info)


        user_obj= authenticate(username=email,password=password)
        if user_obj:
            login(request,user_obj)
            return redirect('/')
        
        messages.success(request, 'Incorrect username or password')
        return HttpResponseRedirect(request.path_info)

    return render(request, "accounts/login.html")


# class CustomLoginView(LoginView):
#     template_name = 'accounts/login.html'
#     authentication_form = CustomAuthenticationForm

#     def get_success_url(self):
#         return reverse_lazy('home_page')

#     def form_valid(self, form):
#         print("Authentication successful for user:", form.get_user())
#         return super().form_valid(form)

#     def form_invalid(self, form):
#         print("Authentication failed. Invalid credentials.")
#         return super().form_invalid(form)



def registerPage(request):
    if request.method=="POST":
        first_name = request.POST.get("first_name")
        last_name =  request.POST.get("last_name")
        mobile = request.POST.get('mobile')
        email =  request.POST.get("email")
        password =  request.POST.get("password")

        user_obj = User.objects.filter(username = email) 

        if user_obj.exists():
            print(" email already registered ", email)
            messages.warning( request, 'Email is already registered' ) 
            return HttpResponseRedirect(request.path_info)

        print ("first_name=",first_name,"last name = ",last_name,"email=",email,"mobile=",mobile)

        user_obj= User.objects.create(first_name= first_name,last_name=last_name,email=email,username=email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'Please check your email for the registration link')
        return HttpResponseRedirect(request.path_info)

    return render(request, "accounts/register.html")


def activate_email(request, email_token):
    try:
        user = Profile.objects.get(email_token= email_token)
        user.is_email_verified = True
        user.save()
        return redirect("/")
    except Exception as e:
        return HttpResponse("Invalid Email Token")
