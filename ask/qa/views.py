from django.http import HttpResponseRedirect, Http404, HttpResponse
from qa.models import Question,Answer

def test(request, *args, **kwargs):
    return HttpResponse('OK')
