from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
import requests
from .models import ContactModel, User
from django.core.mail import send_mail
from django.contrib import messages


from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request,"home.html")

def weatherinfo(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = 'b0197d10a56c3ed637801d7b54edb0bb'
        url =  f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(data)
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1 = round(temperature - 273.15, 2)
            return render(request, 'weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})
    return render(request,"weatherappinput.html")

def contactmail(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        comment = request.POST['comment']
        email = request.POST['email']
        subject = "If you have any query regarding TTMS"
        comment1 = comment + " This is System generated mail. So donot respond to this mail"

        data = ContactModel(firstname=firstname,lastname=lastname,comment=comment,email=email)
        data.save()
        send_mail(
            subject,
            comment1,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently= False
        )
        return HttpResponse("<h1 align=center>Mail Sent Successfully</h1>")
    return render(request,"Contact.html")

def login(request):
   return render(request,"login.html")
def bhargav(request):
    username = request.POST["username"]
    password = request.POST["password"]
    if(username =="2200090120" and password=="123"):
        return render(request,"home.html")
    elif(username =="klu2200090120" and password=="123123"):
        return render(request, "home.html")
    elif (username == "2200090050" and password == "qwertyuiop"):
        return render(request, "home.html")
    elif (username == "karthikmani" and password == "123123"):
        return render(request, "home.html")
    elif (username == "karthikmani" and password == "123"):
        return render(request, "home.html")
    else:
        return HttpResponse("<h1> password Incorrect <h1>")
def Signup(request):
    if request.method== "POST":
        username= request.POST["username"]
        password= request.POST["password"]
        password1= request.POST["confirm_password"]
        email= request.POST["email"]

        if password1!= password:
            messages.error("Passwords do not match! uwu")
            return redirect('Signup')
        user= User.objects.create(username= username, password= password, email= email)
        user.save()
        return redirect("login")

    return render(request,'SignUp.html')