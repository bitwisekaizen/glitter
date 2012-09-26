# Create your views here.
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render_to_response
from backend.models import Message

from simple_rest import Resource

def index(request):
    messages = Message.objects.all()
    return render_to_response('backend/index.html', {'messages': messages})

class Messages(Resource):
    def get(self, request, *args, **kwargs):
        messages = serializers.serialize("json", Message.objects.all())
        return HttpResponse(messages, content_type='application/json', status=200)

    def post(self, request, *args, **kwargs):
        Message.objects.create(text = request.POST.get('text'))
        return HttpResponse(status=200)

    def delete(self, request, *args, **kwargs):
        for message in Message.objects.all():
            message.delete()
        return HttpResponse(status=200)