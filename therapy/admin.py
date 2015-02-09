from django.contrib import admin
from therapy.models import Service, Schedule, UserProfile

admin.site.register(Service)
admin.site.register(Schedule)
admin.site.register(UserProfile)

