from django.http import HttpResponse
import datetime

def hello_world(request):
    now = datetime.datetime.now()
    html = "<html><body>Hello, It is now %s.</body></html>" % now
    return HttpResponse(html)