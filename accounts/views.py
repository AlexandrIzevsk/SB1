from django.contrib.auth.models import User, Group
from serviceBook.models import RegUser
from django.views.generic.edit import CreateView
from django.shortcuts import redirect, render

from .forms import SignUpForm


# class SignUpView(CreateView):
#     model = RegUser
#     form_class = SignUpForm
#     success_url = '/accounts/login'
#     template_name = 'registration/signup.html'
#
#     def post(self,request,*args,**kwargs):
#         pass
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.save()
#             if user.serviceCompany:
#                 user_group = Group.objects.get(name="ServiceCompany")
#                 user.groups.add(user_group)
#                 return redirect("login")
#             elif user.manager:
#                 user_group = Group.objects.get(name="Manager")
#                 user.groups.add(user_group)
#                 return redirect("login")
#             else:
#                 user_group = Group.objects.get(name="Client")
#                 user.groups.add(user_group)
#                 return redirect("login")
#         else:
#             return render(request,self.template_name)
