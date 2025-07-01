from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from job.models import Job

def frontpage(request):
  jobs = Job.objects.all()


  return render(request, 'core/frontpage.html', {
    'jobs': jobs
  })

def signup(request):

  if request.method == 'POST':
    form=UserCreationForm(request.POST)

    if form.is_valid():
      user = form.save()

      account_type = request.POST.get('account_type', 'jobseeker')

      if account_type == 'employer':
        user.userprofile.is_employer = True
        user.userprofile.save()
      login(request, user)

      return redirect('frontpage')
  else:
    form = UserCreationForm()
  return render(request, 'core/signup.html', {
    'form': form
  })