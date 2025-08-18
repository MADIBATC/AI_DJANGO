from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data =  json.loads(request.body)
        print(data.get('email',''))
        return JsonResponse({'success':True}, status = 200)
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        
        return JsonResponse({'success': True}, status=200)
    return render(request, 'SignUp.html') 