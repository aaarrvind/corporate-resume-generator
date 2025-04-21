import jwt
import datetime
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import hashlib
from django.db import connection
from employees.models import Employee
from django.db.models.functions import TruncMonth
from django.db.models import Count
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.db.models.functions import TruncMonth
from django.db.models import Count
from admin_page.models import Company
import calendar

SECRET_KEY = settings.SECRET_KEY  

from django.shortcuts import render
from .models import Company
from django.db.models import Count
from django.db import connection

# Delete company data
def deleteData(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        company_id = data['company_id']

        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM employee WHERE company_id = %s", [company_id])
            
            # Then delete the company
            cursor.execute("DELETE FROM companies WHERE id = %s", [company_id])
            connection.commit()
            print('executed')

        return JsonResponse({'status': 'success'}, status=200)
    else:

        return JsonResponse({'status': 'invalid method'}, status=405)

def getCompany(request):
    active = request.GET.get('active')
    is_active = active == 'true'   
    companies = Company.objects.filter(is_active=is_active)
    return render(request, 'admin_page/getCompany.html', {'companies': companies})


def customer(request):
    # Count active and inactive companies
    status_data = Company.objects.values('is_active') \
        .annotate(count=Count('id')) \
        .order_by('is_active')
    
    # Convert the QuerySet to a list of dictionaries (JSON serializable)
    status_data_list = list(status_data)

    # Prepare the data to be passed into the template
    context = {
        'status_data': status_data_list
    }

    return render(request, 'admin_page/index.html', context)


def Login(request):
    return render(request, 'admin_page/login.html')

def Dashboard(request):
    return render(request,'admin_page/dashboard.html')



def companyHistory(request, company_id):
    # Get the company object
    company = get_object_or_404(Company, id=company_id)

    # Monthly Hiring Data
    monthly_queryset = (
        Employee.objects.filter(company=company, is_deleted=False)
        .annotate(month=TruncMonth('created_date'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )
    monthly_data = [
        {"month": calendar.month_name[item['month'].month], "count": item['count']}
        for item in monthly_queryset
    ]

    # Designation Data
    designation_queryset = (
        Employee.objects.filter(company=company, is_deleted=False)
        .values('designation')
        .annotate(count=Count('id'))
    )
    designation_data = [
        {"designation": item['designation'], "count": item['count']}
        for item in designation_queryset
    ]

    # Status Data
    status_queryset = (
        Employee.objects.filter(company=company, is_deleted=False)
        .values('status')
        .annotate(count=Count('id'))
    )
    status_data = [
        {"status": item['status'], "count": item['count']}
        for item in status_queryset
    ]

    return render(request, 'admin_page/companyChart.html', {
        'company_id': company_id,
        'company_name': company.name,
        'monthly_hiring_data': monthly_data,
        'designation_data': designation_data,
        'status_data': status_data
    })


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


import datetime


@csrf_exempt
def handleLogin(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            if email == "admin@example.com" and password == "admin123":
                email = "admin@example.com"
                payload = {
                    'email': email,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
                    'iat': datetime.datetime.utcnow()
                }

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


def updatCompanyData(request):
    if request.method == 'POST':
        data =  json.loads(request.body)
        company_id = data.get('company_id')
        
        cursor = connection.cursor()
        query = 'SELECT * from companies where id = %s'
        cursor.execute(query,[company_id])
        row = cursor.fetchone()

        if row:
            columns = [col[0] for col in cursor.description]
            company_data = dict(zip(columns, row))

            # Exclude password
            if 'password' in company_data:
                del company_data['password']

            print(company_data)
            return JsonResponse({'status': 'success', 'data': company_data})
        else:
            return JsonResponse({'status': 'error', 'message': 'Company not found'}, status=404)

    return JsonResponse({'error': 'Invalid method'}, status=405)


def update_company(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        data = data['updatedData']
        
        company_id = data.get('company_id')
        company_name = data.get('companyName')
        company_email = data.get('companyEmail')
        companyPassword = data.get('companyPassword')
        
        hashed_password = hashlib.sha256(companyPassword.encode()).hexdigest()
        cursor = connection.cursor()
        query = "UPDATE companies SET name = %s ,email = %s,password = %s WHERE id = %s"
        cursor.execute(query,[company_name,company_email,hashed_password,company_id])
        connection.commit()
        cursor.close()

        return JsonResponse({'status': 'success', 'message': 'Company updated successfully'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)