from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from job.models import Application

# Create your views here.
@login_required
def dashboard(request):
  return render(request, 'userprofile/dashboard.html', {'userprofile':request.user.userprofile})

def view_application(request, application_id):
  application = Application.objects.get(id=application_id)

  return render(request, 'userprofile/view_application.html',{
    'application': application
  })