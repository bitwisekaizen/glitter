# Create your views here.
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render_to_response
from backend.models import Gleet

from simple_rest import Resource

def index(request):
    messages = Gleet.objects.all()
    return render_to_response('index.html', {'messages': messages})

class Messages(Resource):
    def get(self, request, *args, **kwargs):
        messages = serializers.serialize("json", Gleet.objects.all())
        return HttpResponse(messages, content_type='application/json', status=200)

    def post(self, request, *args, **kwargs):
        message = serializers.serialize("json", [Gleet.objects.create(message = request.POST.get('message'))])
        return HttpResponse(message, content_type='application/json', status=200)

    def delete(self, request, id=None, **kwargs):
        if id:
            Gleet.objects.filter(id=id).delete()
        else:
            for message in Gleet.objects.all():
                message.delete()
        return HttpResponse(status=200)