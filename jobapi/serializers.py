from rest_framework import serializers
from models import JobUser, Job, JobApplication

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobUser
        fields = ['name', 'email', 'phone', 'password']
        