from django.test import TestCase, Client
import json
import unittest

from .models import Job


class JobModelTests(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_latest_jobs(self):
        """
        index.html should return the latest 5 jobs
        """

        # Issue a GET request.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        self.assertEqual(response.context['count'], 5)

    def test_batch_jobs(self):
        """
        batch_jobs filters should return jobs containing min and max nodes
        """

        # Issue a GET request.
        response = self.client.get('/batch_jobs/?filter[max_nodes]=200&filter[min_nodes]=2')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains expected filters
        self.assertIn("[min_nodes]=2", response.context['jobs'])
        self.assertIn("[max_nodes]=200", response.context['jobs'])