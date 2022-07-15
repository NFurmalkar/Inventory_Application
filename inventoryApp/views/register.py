from django.shortcuts import render,redirect
from django.core.mail import send_mail
from inventoryApp.forms import registerForm
from inventoryApp.models import registerModel
import random
from django.contrib import messages

# Create your views here.
def login(request):
    request.session.clear()
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        userdata = registerModel.objects.filter(email=email,password=password)
        #print(bool(userdata),userdata)
        if userdata:
            request.session['email'] = email
            request.session['password'] = password
            return redirect('/home')
        else:
            messages.error(request,'Invalid Username or password')
            return redirect('/')
    return render(request,'inventory/login.html')

def register(request):
    global GETOTP
    OTP = []
    OTP.clear()
    for i in range(4):
        num = random.randint(0,9)
        OTP.append(str(num))
    OTPNum = ''.join(OTP)
    GETOTP = OTPNum
    print("GETOTP is:",GETOTP)
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastName = form.cleaned_data['lastName']
            email = form.cleaned_data['email']
            gender = form.cleaned_data['gender']
            password = form.cleaned_data['password']
            print(firstname,lastName,email,gender,password)
            formData = {'firstname':firstname,'lastName':lastName,'email':email,'gender':gender}

            verifyEmail = registerModel.objects.filter(email=email)
            #print("email is",email,"verifyEmail",verifyEmail,bool(verifyEmail))
            if verifyEmail:
                messages.error(request,'Email Already Exists')
                return render(request,'inventory/register.html',{'formData':formData})
        #----------save data in session--------------
            request.session['firstname'] = firstname
            request.session['lastName'] = lastName
            request.session['email'] = email
            request.session['gender'] = gender
            request.session['password'] = password

        #--------send mail----------------
            msg = f"Your OTP is {GETOTP}"
            sendEmail(email,msg)

            return redirect('/otp')

    data = {'OTP':OTPNum}
    return render(request,'inventory/register.html',data)

def sendEmail(email,msg):
    to = email
    subject = "Inventory Application"
    message = msg
    send_mail(subject, message, 'gavarthor@gmail.com', [to])

def otp(request):
    #-------------------collect session data-----------------
    fname = request.session.get('firstname')
    lname = request.session.get('lastName')
    email = request.session.get('email')
    gender = request.session.get('gender')
    password = request.session.get('password')
    print(fname,lname,email,gender,password)

    if fname is None or lname is None or email is None or gender is None or password is None:
        messages.error(request, 'register Please')
        return redirect('/register')
    myOTP =None
    try:
        myOTP = GETOTP
        print("myotp",myOTP)
    except Exception as e:
        return redirect('/register')


    if request.method == 'POST':
        otp = request.POST.get('otp')
        if otp == myOTP:
            FormData = registerModel(firstname=fname,lastName=lname,email=email,gender=gender,password=password)
            FormData.save()
            messages.success(request, 'successfully Register')
            msg = "Thank you for Using our application"
            sendEmail(email,msg)
            request.session.clear()
            return redirect('/')
        else:
            messages.error(request,'Invalid OTP')
        print("otp is",otp,"myotp",myOTP)

    return render(request,'inventory/otp.html')