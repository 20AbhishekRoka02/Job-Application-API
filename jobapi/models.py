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

# class JobUser(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
#     name = models.CharField(max_length=200, blank=False, null=False, validators=[validate_minimum_name_length])
    
#     email = models.EmailField(max_length=254, unique=True, blank=False, null=False, help_text="Enter a valid email address")
    
#     phone = models.CharField(max_length=10, blank=False, null=False, validators=[validate_phone_number])
    
#     is_admin = models.BooleanField(default=False, blank=False, null=False)
    
#     password = models.CharField(max_length=128, null=False, blank=False)
    
#     def __str__(self):
#         return f"User with email {self.email} created with id {self.id}"
    
#     # Overriding save
#     def save(self, *args, **kwargs):
#         self.full_clean() # To trigger validators
#         super().save(*args, **kwargs)
        