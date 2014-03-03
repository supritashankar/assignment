from django.test import TestCase

# Create your tests here.

class RetrieveColorsViewTestCase(TestCase):

  def test_viewing_retrieve_colors_page(self):
    """ Initial test to make sure colors
        selection page is loading """

    response = self.client.get('/clientui/colors/')
    self.assertEqual(response.status_code, 200)
