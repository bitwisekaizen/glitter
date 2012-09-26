"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test.client import Client
from django.test import TestCase
from django.core import serializers

class SimpleTest(TestCase):

    def setUp(self):
        self.client = Client()

    def canPostAndRetrieveMessage(self):
        textToPost = 'a fun text message to Gleet!'

        response = self.client.post("/messages", {'message' : textToPost})
        self.assertEqual(200, response.status_code)

        response = self.client.get("/messages")
        for message in serializers.deserialize("json", response.content):
            self.assertEqual(textToPost, message.object.message)

        response = self.client.delete("/messages")
        self.assertEqual(200, response.status_code)

    def successResponseOnNavigationToHomePage(self):
        response = self.client.get("/")

        self.assertEqual(200, response.status_code)