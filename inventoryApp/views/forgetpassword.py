from django.shortcuts import render,redirect
from inventoryApp.models import registerModel
from django.contrib import messages
from django.core.mail import send_mail

def forgetPassword(request):
    if request.method == "POST":
        data = None
        userEmail = request.POST.get("forgetEemail")
        try:
            data = registerModel.objects.get(email=userEmail)
        except:
            messages.success(request, "Invalid Email")
            data = {'email':userEmail}
            return render(request,'inventory/forgetpassword.html',data)

        mess = f"Your email is {data.email} and password is {data.password}"
        sub = "Inventory Application"
        print(mess)
        if data is None:
            messages.success(request,"Invalid data")
            return redirect('/forgetpassword')
        sendMail(request,sub,mess,userEmail)

    return render(request,'inventory/forgetpassword.html')

def sendMail(request,sub,mess,to):
    subject = sub
    message = mess
    to = to
    print(subject,message,to)
    res = None
    try:
        res = send_mail(subject, message, 'gavarthor@gmail.com', [to])
        print(res)
    except Exception as e:
        print(e)
        messages.error(request,"check connection!")
    if res == 1:
        messages.success(request,"please Check your email")

