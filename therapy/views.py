from django.shortcuts import render, render_to_response
from therapy.forms import ServiceForm, UserForm, UserProfileForm, ScheduleForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from therapy.models import Service, Schedule, UserProfile
import psycopg2
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from therapy.serializers import ScheduleSerializer,ServiceSerializer
from therapy.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets, generics

class JSONResponse(HttpResponse):
   
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class ServiceViewSet(viewsets.ModelViewSet) :
	queryset = Service.objects.all()
	serializer_class = ServiceSerializer

	def list(self, request):
            queryset = Service.objects.all()
	    serializer = ServiceSerializer(queryset, many=True)
            return JSONResponse(serializer.data)	

	def pre_save(self,obj) :
	    obj.owner = self.request.user

class ScheduleViewSet(viewsets.ModelViewSet) :
	queryset = Schedule.objects.all()
	serializer_class = ScheduleSerializer

	def list(self, request):
            queryset = Schedule.objects.all()
	    serializer = ScheduleSerializer(queryset, many=True)
            return JSONResponse(serializer.data)	

	def pre_save(self,obj) :
	    obj.owner = self.request.user
	
	def put(request):
    	    if request.method == 'PUT':
	       serializer = ScheduleSerializer(request.PUT)
	       if serializer.is_valid():
		  serializer.save()
       

class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView) :
	queryset = Schedule.objects.all()
	serializer_class = ScheduleSerializer

def index(request):
	return render(request,'therapy/index.html') 

def home(request):
	return render(request,'therapy/home.html') 

def schedule_detail(request):
	return render(request,'therapy/schedule_detail.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
            'therapy/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
		if request.user.is_authenticated() and request.user.has_perm('therapy.add_schedule') \
                        and request.user.has_perm('therapy.add_service') :
                	return HttpResponseRedirect('/therapy/home')
		if request.user.is_authenticated() and not request.user.has_perm('therapy.add_service') \
			and not request.user.has_perm('therapy.add_service') :
			return HttpResponseRedirect('/therapy/view_schedules')
		else :
			return HttpResponseRedirect('/therapy/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request,'therapy/login.html',{})

def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/therapy/')

def add_service(request):
    if request.user.is_authenticated() and request.user.has_perm('therapy.add_service') :
    	if request.method == 'POST':
	    form = ServiceForm(request.POST)
	    message = ""
	    if form.is_valid():
	       form.save(commit=True)
	       message = "data entered successfully"

	       return render(request,'therapy/home.html',{"message":message})
	    else:
	       print form.errors
        else:
	   form = ServiceForm()

        return render(request,'therapy/add_service.html', {'form': form})
    else :
        return HttpResponse("Access denied.")


def view_schedules(request):
    list_all_schedules = Schedule.objects.all()
    return render(request,'therapy/view_schedules.html',{"list_all_schedules":list_all_schedules})

def add_schedule(request):
    if request.user.is_authenticated() and request.user.has_perm('therapy.add_schedule') :
    	if request.method == 'POST':
	    form = ScheduleForm(request.POST)
	    message = ""
	    if form.is_valid():
	       form.save(commit=True)
	       message = "data entered successfully"

	       return render(request,'therapy/home.html',{"message":message})
	    else:
	       print form.errors
        else:
	   form = ScheduleForm()

        return render(request,'therapy/add_schedule.html', {'form': form})
    else :
        return HttpResponse("Access denied.")
