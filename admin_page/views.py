import jwt
import datetime
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import hashlib
from django.db import connection

SECRET_KEY = settings.SECRET_KEY  

def customer(request):
    return render(request, 'admin_page/index.html')

def Login(request):
    return render(request, 'admin_page/login.html')

def Dashboard(request):
    return render(request,'admin_page/dashboard.html')


def HandleCompanyData(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            companyName = data.get('companyName')
            companyEmail = data.get('companyEmail')
            companyPassword = data.get('companyPassword')

            # Hash the password using SHA-256
            hashed_password = hashlib.sha256(companyPassword.encode()).hexdigest()

            print(f"Data received: {companyName}, {companyEmail}, {hashed_password}")  # Debugging line

            cursor = connection.cursor()

            # Insert query with automatic timestamps
            insert_query = """
                INSERT INTO companies (name, email, password, created_at, updated_at)
                VALUES (%s, %s, %s, NOW(), NOW())
            """
            print(f"Executing query: {insert_query}")  # Debugging line
            cursor.execute(insert_query, (companyName, companyEmail, hashed_password))
            connection.commit()
            cursor.close()

            return JsonResponse({
                'success': True,
                'message': 'Data stored in the database successfully...'
            })
        
        except Exception as e:
            print(f"Error: {str(e)}")  # Debugging line
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Only POST requests are allowed'})



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


# Fetch company data from the database when page is loaded
def fetchCompanyData(request):
    if request.method == 'GET':
        cursor = connection.cursor()
        cursor.execute('SELECT id,name,email,password,is_active FROM companies')

        rows =  cursor.fetchall()
        companies =  [{'id':row[0],'name':row[1] , 'email':row[2],'password':row[3],'is_active':row[4]} for row in rows]


        return JsonResponse(companies,safe=False)

    return JsonResponse({'success':400,'message':'Error in fetching the data'})
