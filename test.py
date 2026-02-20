import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE","job_application.settings")
django.setup()
from jobapi.models import Job, JobUser, JobApplication

user = JobUser(
    name = "Julia Johnson",
    email = "julia@example.com",
    phone = "8976543210",
    is_admin = True,
    password = "hadif098a73"
)
user.save()

for i in JobUser.objects.all():
    print(i)
    
job = Job(title="jdladHelajdf", description="Need a good work!", created_by = user)
job.save()
for i in Job.objects.all():
    print(i)
    
application = JobApplication(job=job, user=user)
application.save()
for i in JobApplication.objects.all():
    print(i)