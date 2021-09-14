from django.http.request import HttpHeaders
from oauth2_provider.views.generic import ProtectedResourceView
from django.core import serializers
from django.http import response


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        resp = response.HttpResponse(
            serializers.serialize("json", [request.user])[1:-1]
        )
        resp.headers["content-type"] = "application/json"
        return resp
