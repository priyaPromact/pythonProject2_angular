from django.conf.urls import *
from rest_framework import routers
from therapy import views

router = routers.DefaultRouter()
router.register(r'schedule', views.ScheduleViewSet)
router.register(r'service', views.ServiceViewSet)


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add_service/$', views.add_service, name='add_service'),
    url(r'^add_schedule/$', views.add_schedule, name='add_schedule'),
    url(r'^schedule_detail/$', views.schedule_detail, name='schedule_detail'),
    url(r'^home/$', views.home, name='home'),
    url(r'^view_schedules/$', views.view_schedules, name='view_schedules'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^api/', include(router.urls))
)
