from django.core.management import call_command
from django.test import TestCase


class PipelineTestCase(TestCase):

    def test_success(self):
        call_command('collectstatic', '--noinput')
        call_command('clean_staticfilesjson')
