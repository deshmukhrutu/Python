from django.test import TestCase
from .models import Employee, Event,EmailTemplate
# Create your tests here.
class EventEmailTestCase(TestCase):
    def setup(self):
        self.employee=Employee.objects.create(name='Rutuja Deshmukh',email='rutujadeshmukh9919@gmail.com')
        self.template=EmailTemplate.objects.create(event_type='birthday',template="Happy BirthDay,{{employee_name}}!!!")


    def test_send_emails(self):
        Event.objects.create(employee=self.employee,event_type='birthday',event_date=date.today())
        response=self.client.post('/send_emails')
        self.asserEqual(response.status.code,200)
        self.assertContains(response,'Emails send successfully')
