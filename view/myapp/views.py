from django.http import HttpResponse
from django.views.generic import View, TemplateView

# Create your views here.

# base view example
class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

class MyTemplateView(TemplateView):
    template_name = 'template.html'
    myteststring = 'i am a variable from object:MyTemplateView'

    def get_context_data(self, **kwargs):
        context = super(MyTemplateView, self).get_context_data(**kwargs)
        return  context