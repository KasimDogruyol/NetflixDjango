from math import fabs
from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def userRegister(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        email = request.POST['email']
        resim = request.FILES['resim']
        tel = request.POST['tel']
        sifre1 = request.POST['sifre1']
        sifre2 = request.POST['sifre2']
        
        if sifre1 == sifre2:
            if User.objects.filter(username=kullanici).exists():
                messages.error(request,'Kullanıcı Adı Kullanımda')
                return redirect ('register')
            elif User.objects.filter(email = email).exists():
                messages.error(request,'Email Kullanımda')
                return redirect('register')
            elif kullanici in sifre1:
                messages.error(request,'Kullanıcı Adı İle Şifre Benzer Olamaz')
                return redirect('register')
            elif len(sifre1) < 6:
                messages.error(request,'Şifre En az 6 Karakterden Oluşmalı')
                return redirect('register')
            else:
                user = User.objects.create_user(username =kullanici, email = email,password =sifre1)
                Account.objects.create(user = user,resim = resim,tel = tel)
                subject = 'Netflix'
                message = 'Bu Netflix Projesini Kasım Doğruyol Yaptı İncelediğiniz İçin Teşekkürler'
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=False,
                )
                
                user.save()
                messages.success(request,'Kullanıcı Başarı İle Oluşturuldu')
                return redirect('index')

    return render(request,'user/register.html')

def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        
        user = authenticate(request, username = username, password =password)
        
        if user is not None:
            login(request,user)
            messages.success(request,'Giriş Yapıldı')
            return redirect('profile')
        else:
            messages.error(request,'Kullanıcı Adı Veya Şifre Hatalı')
            return redirect('login')
    return render(request,'user/login.html')

def userLogout(request):
    logout(request)
    messages.success(request,'Çıkış Yapıldı')
    return redirect('index')

def profile(request):
    profiles = Profile.objects.filter(user = request.user)
    context = {
        'profiles':profiles
    }
    return render(request,'browse.html',context)

def createProfile(request):
    form = ProfileForm()
    profile = Profile.objects.filter(user= request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if len(profile) <4:
            try:
                if form.is_valid():
                    profile = form.save(commit=False)
                    profile.user = request.user
                    profile.save()
                    messages.success(request,'Profil Başarıyla Oluşturuldu')
                    return redirect('profile')
            except:
                messages.error(request,'Profil Oluşturulamadı Bu Profil Adı Mevcut')
                return redirect('create')
        else:
            messages.error(request,'Profil Sayısı 4 den Fazla Olamaz')
            return redirect('profile')
    context = {
        'form':form
    }
    return render(request,'createProfile.html',context)

def hesap(request):
    user = request.user.account
    context = {
        'user':user
    }
    return render(request,'user/hesap.html',context)

def userDelete(request):
    user = request.user
    user.delete()
    messages.success(request,'Kullanıcı Silindi')
    return redirect('index')

def update(request):
    user= request.user.account
    form = AccountForm(instance=user)
    if request.method == 'POST':
        form = AccountForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'Profil Güncellendi')
            return redirect('hesap')
    context = {
        'form':form
    }
    return render(request,'user/update.html',context)