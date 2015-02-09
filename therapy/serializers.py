from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from therapy.models import Schedule, Service
from django.contrib.auth.models import User

class ServiceSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Service
        fields = ('id','name','min_time','max_time','price')

class ScheduleSerializer(serializers.ModelSerializer):   
    service = ServiceSerializer() 
    class Meta:
        model = Schedule
        fields = ('id','service','date')

    def update(self, instance, validated_data):	
	print  validated_data.pop('service')  
	instance.date = validated_data.get('date')
	instance.save()
	return instance
