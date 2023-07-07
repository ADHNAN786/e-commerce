from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView
from django.urls import reverse_lazy
from .forms import LoginForm,RegistrationForm
from django.contrib.auth import authenticate,login,logout


# Create your views here.

# class LoginPage(View):
#     def get(self,request):
#         form=LoginForm()
#         return render(request,'login.html',{'form':form})
#     def post(self,request):
#         form_data=LoginForm(data=request.POST)
#         if form_data.is_valid:
#             return redirect('home')
#         else:
#             return render(request,'login.html',{'form':form_data})


class LoginPage(FormView):
    template_name='login.html'
    form_class=LoginForm
    def post(self,request):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            uname=form_data.cleaned_data.get('username')
            pswd=form_data.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
            if user:
                login(request,user)
                return redirect('home')
            else:
                return render(request,'login.html',{'form':form_data})

# class RegistraionView(View):
#     template_name='Registration.html'
#     form_class=RegistrationForm
#     success_url='login'

#     def get(self,request):
#         form=self.form_class()
#         return render(request,self.template_name,{'form':form})
#     def post(self,request):
#         form_data=self.form_class(data=request.POST)
#         if form_data.is_valid():
#             form_data.save()
#             return redirect(self.form_class)
#         else:
#             return render(request,self.template_name,{'form':form_data})
        
class RegistrationView(CreateView):
    template_name='Registration.html'
    form_class=RegistrationForm
    success_url=reverse_lazy('login')

class LogOut(View):
    def get(self,request):
        logout(request)
        return redirect('login')


    
