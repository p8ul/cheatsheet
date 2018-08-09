__author__ = 'p8ul'

from urlparse import urlparse

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from django.conf import settings
from django.contrib.auth.models import User, Group
from django.core.cache import cache

from bs4 import BeautifulSoup

from model_mommy import mommy


class CheatSheet(TestCase):
    def setUp(self):
        cache.clear()
        group = Group.objects.create(name=u'HTS Superuser')

        self.test_password = '123456789'

        self.user = mommy.make(User, username='test_user', email='test@test.com', is_superuser=True)
        self.user.set_password(self.test_password)
        self.user.groups.add(group)
        self.user.save()

    def login(self, user):
        client = Client()
        result = client.login(username=user.username, password=self.test_password)
        self.assertEqual(result, True)
        return client

    def test_get(self):
        client = self.login(self.user)

        response = client.get(reverse('my_url'))

        # Inspect status code
        self.assertEqual(response.status_code, 200)

        # Where are we? After status code 200
        target_url = 'my url'
        self.assertEqual(target_url, response.request[u'PATH_INFO'])

        # Where are we? After status code 302
        target_url = 'my url'
        self.assertEqual(target_url, urlparse(response.url)[2])

        # Looking in HTML. Not sure why, but assertInHTML does not work
        self.assertIn('id_department', response.content)
        self.assertNotIn('id_location', response.content)
        
        # Want more detailed info about the HTML?
        # For example: make sure field is hidden
        soup = BeautifulSoup(response.content, 'html.parser')
        the_field = soup.find(id='id_the_field')
        self.assertEqual(the_field.attrs[u'type'], u'hidden')
        
    def test_post(self):
        """
        How to set empty fields:
            models.ForeignKey: exclude from post data
            models.DecimalField: exclude from post data
        """

        client = self.login(self.user)

        initial_objects_list = list(MyModel.objects.all())  # convert to list to force evaluation
        new_MyModel_data = {
            'field_1': 'abc',
            'field_2': 5,
        }
        response = client.post(post_url, new_MyModel_data)
        
        # Look for errors: https://docs.djangoproject.com/en/1.8/topics/testing/tools/#django.test.SimpleTestCase.assertFormError
        # For a non-field error
        field = None
        self.assertFormError(self.response, 'form', field, u'An error message.')
        
        # For a field
        field = 'user_name'
        self.assertFormError(self.response, 'form', field, u'An error message.')

        # Should go to list page
        self.assertEqual(response.status_code, 302)
        self.assertEqual(success_url, urlparse(response.url)[2])

        final_object_list = list(MyModel.objects.all())
self.assertEqual(len(final_object_list), len(initial_object_list) + 1)
