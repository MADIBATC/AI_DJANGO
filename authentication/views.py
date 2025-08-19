from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.contrib.auth import authenticate, login as auth_login, logout
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from .models import CustomUser
import json

@csrf_exempt
def loginView(request):
    if request.method == 'POST':
        data =  json.loads(request.body)
        
        email = data.get("email", "").strip()
        password = data.get("password", "").strip()

        if not email or not password:
            return JsonResponse({"error": "Email and password required"}, status=400)

        # Authenticate user
        user = authenticate_user(email=email, password=password)

        if user is not None:
            if user.is_active:
                auth_login(request, user)  # start session
                return JsonResponse({"success": True, "message": "Login successful"}, status=200)
            else:
                return JsonResponse({"error": "Account is disabled"}, status=403)
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=401)
    return render(request, 'login.html')

def authenticate_user(email, password):
    try:
        user_data = CustomUser.objects.get(email = email)
    except Exception as e:
        return None
    else:
       if user_data.check_password(password):
           return user_data
    return None


def signup(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # parse JSON payload
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        # Pass the parsed data into the form
        form = CustomUserCreationForm(data)

        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # log the user in after signup (optional)
            return JsonResponse({"success": True, "message": "User created successfully"}, status=201)
        else:
            return JsonResponse({"success": False, "errors": form.errors}, status=400)
    return render(request, 'SignUp.html')


@login_required
def logOut(request):
    logout(request)
    return redirect('authentication:login')