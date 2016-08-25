from django.http import HttpResponse
from django.views.generic import View

# Create your views here.


class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')
