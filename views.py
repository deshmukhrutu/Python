from django.shortcuts import render
from .models import Employee,Event,EmailTemplate
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import date
# Create your views here.
@csrf_exempt
def send_emails(r):
    if r.method == 'POST':
        today=date.today()
        events=Event.objects.filter(event_date=today)

        for event in events:
            employee=event.employee
            event_type=event.event_type

            try:
                template=EmailTemplate.objects.get(event_type=event_type)
            except EmailTemplate.DoesNotExist:
                return JsonResponse({'message':f"No template found for(event_type"},status=400)
            email_content=template.template.replace('{{employee_name}}',employee.name)
            send_mail(f'Event Reminder:{event_type}',email_content,'sender@example.com',[employee.email],fail_silently=False)
            return JsonResponse({'message':'Email send Successfully'})
        else:
                 return JsonResponse({'message':'Invalid request'},status=405)

