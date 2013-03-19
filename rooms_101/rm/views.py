from django.http import HttpResponse
from django.template import Context, loader

from rm.models import RmUser

def index(request):
    latest_poll_list = RmUser.objects.all()
    template = loader.get_template('rm/index.html')
    context = Context({
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(template.render(context))
