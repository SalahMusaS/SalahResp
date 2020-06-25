from django.shortcuts import render

# Create your views here.
from .models import Job


def job_list(request):
    job_list = Job.objects.all()
    print(job_list)
    context = {'jobs': job_list}
    return render(request, 'job/job_list.htm', context)


def job_details(request):
    pass
