from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import login ,logout,authenticate
#from django.contrib.auth.forms import  UserCreationForm
from .forms import CustomUserCreationForm
import random
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']

        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!",extra_tags='success')

            # Role based redirect
            if user.is_superuser:
                return redirect('admin_dashboard')   # for Admin
            elif user.is_staff:
                return redirect('dashboard')   # for Staff
            else:
                return redirect('home')              # for Normal User

        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'AuthApp/login.html')

def register_view(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!",extra_tags='success')
            return redirect('login')
    context = {'form':form}
    return render(request, 'AuthApp/register.html',context)

def logout_view(request):
    logout(request)
    return redirect('login')

def forget_pass(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        otp=request.POST.get('otp')
        if email:
            user=User.objects.filter(email=email).first()
            if user:
                gen_otp = str(random.randint(1000,9999))
                #store otp and id
                request.session['reset_otp'] = gen_otp
                request.session['reset_user_id'] = user.id
                send_mail(
                    'Resset Password',
                    f'Your OTP is {gen_otp}',
                    'gopalpatil03709@gmail.com',
                    [user.email],
                )
                messages.success(request, "OTP sent successfully!",extra_tags='success')
                return render(request, 'AuthApp/forget.html',{'show_otp':True})
            else:
                return redirect('login')
        elif otp:
            session_otp = request.session.get('reset_otp')
            if otp == session_otp:
                return redirect('new-pass')
            else:
                messages.error(request,'Invalid OTP!.',extra_tags='danger')
                return render(request, 'AuthApp/forget.html',{'show_otp':True})
    return render(request,'AuthApp/forget.html')



def set_new_password(request):
    user_id = request.session.get('reset_user_id')
    if not user_id:
        return redirect('login')

    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            user.set_password(password2)
            user.save()
            # clear session
            del request.session['reset_otp']
            del request.session['reset_user_id']
            return redirect('login')
        else:
            return redirect('new-pass')
    return render(request,'AuthApp/new-password.html')
