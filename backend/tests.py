"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.http import HttpResponse

from django.test.client import Client
from django.test import TestCase
from django.core import serializers
from backend.models import Message

class SimpleTest(TestCase):
    def canPostAndRetrieveMessage(self):
        textToPost = 'a fun text message to Gleet!'

        c = Client()

        response = c.post("/messages", {'text' : textToPost})
        self.assertEqual(200, response.status_code)

        response = c.get("/messages")
        for message in serializers.deserialize("json", response.content):
            self.assertEqual(textToPost, message.object.text)

        response = c.delete("/messages")
        self.assertEqual(200, response.status_code)