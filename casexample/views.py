from oauth2_provider.views.generic import ProtectedResourceView
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
import json


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return json.dumps(request.user, serializer=DjangoJSONEncoder)
