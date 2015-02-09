from django.test import TestCase
from therapy.models import Service
from django.core.urlresolvers import reverse
from django.test.utils import setup_test_environment

class ServiceMethodTests(TestCase):
	
	#service model testing
	def test_check_service(self):
		test_time = Service(name='test',min_time='17:00',max_time='10:00',price='0')
		self.assertEqual(test_time.save(commit=True),False)

class ServiceViewTests(TestCase):

	def test_add_service_view(self):
		response = self.client.get(reverse('therapy:add_service'))
		self.assertEquals(response.status_code,200)
		self.assertContains(response, "Access denied.")
	
