import jwt
import datetime
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

SECRET_KEY = settings.SECRET_KEY  

def home(request):
    return render(request, 'admin_page/index.html')

def Login(request):
    return render(request, 'admin_page/login.html')

@csrf_exempt
def handleLogin(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            if email == "admin@example.com" and password == "admin123":
                # Create a JWT token 
                payload = {
                    'email': email,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),  # Token expires in 1 hour
                    'iat': datetime.datetime.utcnow() 
                }

                # Generate JWT token
                token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

                return JsonResponse({'success': True, 'message': 'Login successful', 'token': token})

            else:
                return JsonResponse({'success': False, 'message': 'Invalid email or password'})

        except Exception as e:
            return JsonResponse({'success': False, 'message': 'Invalid request', 'error': str(e)})

    return JsonResponse({'success': False, 'message': 'Only POST requests are allowed'})
