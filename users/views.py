from django.shortcuts import render,redirect
from .forms import UserRegisterForm #UserLoginForm,
from django.contrib.auth import login as auth_login

# def login_view(request):
#     if request.method == "POST":
#         form = UserLoginForm(request,data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request,user)
#             if user:
#                 auth_login(request,user)
#                 return redirect('index')
#         else:
#             form = UserLoginForm(request)
#     context = {'form':form}
#     return render(request,'users/login.html',context)
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('index')
    else:
        form = UserRegisterForm()

    return render(request,'users/register.html',{'form':form,'title':'Registration'})
