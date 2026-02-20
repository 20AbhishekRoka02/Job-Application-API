from django.core.exceptions import ValidationError
from django.db import models
import uuid

def validate_minimum_name_length(value):
    if len(value) < 3:
        raise ValidationError(
            (f"{value} is not long enough for name. Minimum lenght for name is 5")
            )

def validate_phone_number(value):
    if len(value) != 10:
        raise ValidationError(
            (f"Phone number of 10 characters long are valid.")
            )
# Create your models here.
class JobUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    name = models.CharField(max_length=200, blank=False, null=False, validators=[validate_minimum_name_length])
    
    email = models.EmailField(max_length=254, unique=True, blank=False, null=False, help_text="Enter a valid email address")
    
    phone = models.CharField(max_length=10, blank=False, null=False, validators=[validate_phone_number])
    
    is_admin = models.BooleanField(default=False, blank=False, null=False)
    
    password = models.CharField(max_length=128, null=False, blank=False)
    
    def __str__(self):
        return f"User with email {self.email} created with id {self.id}"
    
    # Overriding save
    def save(self, *args, **kwargs):
        self.full_clean() # To trigger validators
        super().save(*args, **kwargs)

class Job(models.Model):
    job_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    title = models.CharField(blank=False, null=False, max_length=250, validators=[validate_minimum_name_length])
    
    description = models.TextField(blank=False, null=False, max_length=500)
    
    created_on = models.DateTimeField(auto_now=True)
    
    created_by = models.ForeignKey(JobUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Job with title {self.title} created with id {self.job_id} by {self.created_by} on {self.created_on}"
    
    # Overriding save
    def save(self, *args, **kwargs):
        self.full_clean() # To trigger validators
        super().save(*args, **kwargs)
        
    class Meta:
        ordering = ["-created_on"] # Newest job first on query



class JobApplication(models.Model):
    application_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
        
    user = models.ForeignKey(JobUser, on_delete=models.CASCADE)
        
    applied_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Job Application with id {self.application_id} on {self.applied_on}"
    
    # Overriding save
    def save(self, *args, **kwargs):
        self.full_clean() # To trigger validators
        super().save(*args, **kwargs)
        
    class Meta:
        ordering = ["-applied_on"] # Newest job first on query

        