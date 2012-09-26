"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test.client import Client
from django.test import TestCase

class SimpleTest(TestCase):
    def canPostAndRetrieveMessage(self):
        c = Client()

        response = c.post("/messages", {'message' : 'This is my first Gleet!'})
        self.assertEqual(response.status_code, 200)

        response = c.get("/messages")
        self.assertEqual(response._body['message'], 'This is my first Gleet!')