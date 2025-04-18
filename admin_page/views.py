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

def companyHistory(request,company_id):
    return render(request,'admin_page/companyChart.html',{'company_id':company_id})

# handle company active and deactive button
def handleActivity(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            Company_id = data['id']
            is_active = 0
            if(data['is_active']):
                is_active = 1

            cursor =connection.cursor()
            query = 'UPDATE companies SET is_active = %s WHERe id = %s'
            cursor.execute(query,[is_active,Company_id])
            connection.commit()
            cursor.close()

            return JsonResponse({'success':True,'message':'data updated correctly'})
        
        except Exception as e:
            return JsonResponse({'success':False,'message':'Error in updating the data'})
    return JsonResponse({'success':False,'message':'Error in updating the data'})
    

# import company mode
from .models import Company
def HandleCompanyData(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from request body
            data = json.loads(request.body)

            companyName = data.get('companyName')
            companyEmail = data.get('companyEmail')
            companyPassword = data.get('companyPassword')
            planType = data.get('planType', None)
            subStart = data.get('subscriptionStart', None)
            subEnd = data.get('subscriptionEnd', None)
            isActive = data.get('isActive', False)

            # Hash the password (use Django's built-in hasher for best security)
            hashed_password = hashlib.sha256(companyPassword.encode()).hexdigest()

            # Create a new Company object and save to the DB
            company = Company(
                name=companyName,
                email=companyEmail,
                password=hashed_password,
                plan_type=planType,
                subscription_start=subStart,
                subscription_end=subEnd,
                is_active=isActive
            )

            company.save()

            return JsonResponse({
                'success': True,
                'message': 'Company data saved successfully.'
            })

        except Exception as e:
            print("Error:", str(e))
            return JsonResponse({
                'success': False,
                'message': f'Error: {str(e)}'
            })

    return JsonResponse({
        'success': False,
        'message': 'Only POST requests are allowed.'
    })


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
