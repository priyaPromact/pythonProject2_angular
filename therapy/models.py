from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
	name=models.CharField(max_length=50)
	min_time=models.TimeField(("minimum time"),blank=True)
	max_time=models.TimeField(("maximum time"),blank=True)
	price=models.DecimalField(max_digits=5,decimal_places=2)
	
	def save(self, *args, **kwargs):
		if self.min_time > self.max_time:
		    return False
		else: 
		    super(Service, self).save(*args, **kwargs)
	
	def __str__(self):
		return self.name

class Schedule(models.Model):  
	service=models.ForeignKey(Service)
	date=models.DateTimeField()
	def __str__(self):
		return "%s Schedule for %s" % (self.service,self.date)

class UserProfile(models.Model):
    	user = models.OneToOneField(User)
    	picture = models.ImageField(upload_to='profile_images', blank=True)

    	def __str__(self):
        	return self.user.username


