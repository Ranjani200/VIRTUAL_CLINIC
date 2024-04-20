from django.shortcuts import render
import google.generativeai as genai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from twilio.rest import Client


# Create your views here.
GOOGLE_API_KEY='AIzaSyARwRyEByZcvGVbkopD6pa4uqdVrYDNNKQ'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

@csrf_exempt
@login_required
def home(req):
    return render(req, 'home.html')

@csrf_exempt
def index(req):
    return render(req, 'index.html', {})
def pharmacy(req):
    return render(req, 'pharmacy.html', {})
@csrf_exempt
def smartcard(req):
    return render(req, 'smartcard.html', {})

# def login(req):
#     return render(req, 'login.html', {})


@csrf_exempt
def auth_login(request):
    context = {}
    
    if request.user.is_authenticated:    
        return redirect('/')
    else:
        pass

    if request.method == 'POST':
        username = request.POST['emailid'] #username
        password = request.POST['password'] #password
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            print("loggedin")
            return redirect('home')
        else:
            context = {"error":"error"}
            print("error1")
    else:
        print("error2")
    return render(request,'login.html',context)


@csrf_exempt
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["emailid"]
        password = request.POST["password"]      
        user = User.objects.create_user(email, email, password)
        user.first_name = username
        user.is_active = False
        user.save()
    return render(request, 'register.html', {})

@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        input_val = request.POST.get('message')  # Assuming 'message' is the key sent in AJAX data
        print("Input value:", input_val)
        response = model.generate_content(input_val)
        print(response.text)
        # Perform any processing here based on the input value
        # Return JSON response
        return JsonResponse({'message': response.text}, status=200)
    else:
        # Handle other HTTP methods or return an error response
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)