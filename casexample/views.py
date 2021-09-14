from oauth2_provider.views.generic import ProtectedResourceView
from django.core import serializers
from django.http import HttpResponse
import json


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        self.head
        return serializers.serialize("json", [request.user])[1:-1]
