from django.test import TestCase

class StudentModelTestCase(TestCase):
    def test_homeall_status_code(self):
        response=self.client.get('/all/')
        print(response)
        self.assertEqual(response.status_code,200)
    