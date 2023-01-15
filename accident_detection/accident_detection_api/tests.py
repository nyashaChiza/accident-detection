from django.test import TestCase
from accident_detection_api.models.responders import Responder
# Create your tests here.

class ResponderTestCase(TestCase):
    def setUp(self):
        Responder.objects.create(first_name="Test name", last_name="Test surname",longitude="40.714", latitude="-74.006")
    
    
    def test_is_responder_active(self):
        """test if responder is active"""
        responder = Responder.objects.get(first_name="Test name")
            
        self.assertEqual(responder.is_active, True)