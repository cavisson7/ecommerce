from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Banner
from .models import ContactDetails
from .models import socialIcon

# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')

def home(request):
    

    banner = Banner.objects.all()
    social = socialIcon.objects.all()


    #login module
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            request.session.set_expiry(30)
            return redirect('/')
        else:
            messages.info(request,'invalid User name or Password Please try Again')
            return redirect('home')
    else:
        return render(request,'index.html',{'banner':banner,'social':social})
   

    # Rgister module here 

    if request.method == 'POST':
        first_name = request.POST['first_name'] 
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User Taken')
                return redirect('home')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email taken")
                return redirect('home')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print("User created ")
                return redirect('home')
        else:
            messages.info(request,'Password Not matched')
            return redirect('home')
        return redirect('/')
    else:

        return render(request,'index.html') 


# Class for update banner 
    
def contact (request):

    contacts = ContactDetails.objects.all()

    social = socialIcon.objects.all()
    
    return render(request,'contact.html',{'contacts':contacts,'social':social}) 