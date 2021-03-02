from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import UpdateView
from .forms import UserRegistrationForm ,ContactForm
from django.contrib.auth.forms import AuthenticationForm
from products.models import Tags
from products.models import Products

def home(request):
    signupform = UserRegistrationForm()
    form = AuthenticationForm()
    tags = Tags.objects.all()
    context = {'signupform':signupform,
    'loginform':form,'tags1':tags[0:3],'tags2':tags[3:6],
    'tags3':tags[6:9]}
    return render(request,'user/home.html',context)
def handle_signup(request):
    if request.method =="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'account created')
        else:
            messages.warning(request,'enter proper credentials')     
    return redirect('home')
def loginuser(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usr = form.get_user()
            login(request,usr)
            messages.success(request,'sucessfully logged-in as ')
            return redirect('home')
        else:
            messages.warning(request, 'incorrect username or password')
            return redirect('home')
    else:
        messages.warning(request,'login to access parsonalised features')
        return redirect('/')

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request,'you reached us, we will get back to you soon')
        return redirect('/')
    form = ContactForm()
    return render(request,'user/contact.html',{'contactform':form})
def search(request):
    query = request.GET['search']
    search_results = Products.objects.filter(name__icontains= query)
    context = {'allproducts':search_results}
    return render(request,'search.html',context)

def new_arraivals(request):
    products= Products.objects.all()
    return render(request,'new_arraivals.html',{"products":products})

def logingout(request):
    logout(request)
    messages.success(request, 'logout sucessfull ')
    return redirect('home')

class UserAccount(UpdateView,LoginRequiredMixin,UserPassesTestMixin):
    model = User
    success_url = '/'
    template_name = 'user/user_account.html'
    fields =['username','email','first_name','last_name']
    def test_func(self):
        user = self.get_object()
        if user == self.request.user:
            return True
        return False

    