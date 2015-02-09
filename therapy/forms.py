from django import forms
from therapy.models import Service, Schedule, UserProfile
from django.contrib.auth.models import User

class ServiceForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Service name:")
    min_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), initial="10:00",help_text="Starting time:")
    max_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), initial="17:00",help_text="Ending Time:")
    price = forms.DecimalField(max_digits=5,decimal_places=2,help_text="Price:")

    def is_valid(self):
	valid = super(ServiceForm, self).is_valid()
        if not valid:
            return valid
	
	if self.cleaned_data['min_time'] > self.cleaned_data['max_time']:
		self._errors["min_time"] = 'min time should be less then max time'
		return False
	
	return True

    class Meta:
        model = Service

class ScheduleForm(forms.ModelForm):
	service=forms.ModelChoiceField(required=True, queryset= Service.objects.all(),help_text="Select a service:")
	date=forms.SplitDateTimeField(required = True,help_text="Enter a date:") 
     	class Meta:
            model = Schedule

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
