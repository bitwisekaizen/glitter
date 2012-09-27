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
        message = list(serializers.deserialize("json", response.content))[0]
        self.assertEqual(textToPost, message.object.message)

        response = self.client.get("/messages")
        deserializedMessage = None
        messages = serializers.deserialize("json", response.content)
        for message in messages:
            deserializedMessage = message.object
            self.assertEqual(textToPost, deserializedMessage.message)
            self.assertNotEqual(None, deserializedMessage.timestamp)

        response = self.client.delete("/messages", {'id' : deserializedMessage.id})
        self.assertEqual(200, response.status_code)

        messages = serializers.deserialize("json", self.client.get("/messages").content)
        self.assertEqual(0, len(list(messages)))

    def successResponseOnNavigationToHomePage(self):
        response = self.client.get("/")

        self.assertEqual(200, response.status_code)