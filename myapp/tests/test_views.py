from django.test import TestCase

# Create your tests here.
class HomeViewTestCase(TestCase):
    def test_home_status_code(self):
        response = self.client.get('/')
        print('####calling test_home_status_code')
        self.assertEqual(response.status_code,200)

    def test_home_template_content(self):
        response = self.client.get('/home/')
        print('####calling test_home_template_content')
        self.assertContains(response,'<title>') # or any string you have in your template