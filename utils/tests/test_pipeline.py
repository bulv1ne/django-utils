from io import StringIO

from django.core.management import call_command
from django.test import TestCase


class PipelineTestCase(TestCase):

    def test_success(self):
        call_command('collectstatic', '--noinput', stdout=StringIO())
        call_command('clean_staticfilesjson', stdout=StringIO())
