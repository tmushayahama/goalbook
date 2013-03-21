from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate, login
from django.template import Context, loader

from rm.models import RmUser

def index(request):
    latest_poll_list = RmUser.objects.all()
    template = loader.get_template('rm/index.html')
    context = Context({
            'latest_poll_list': latest_poll_list, 
    })
    return HttpResponse(template.render(context))


    
def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "Welcome "+user.first_name
                name=user.first_name
                return render(request, 'home.html',{'name':name, 'username': username})
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    
    return render(request, 'login.html',{'state':state, 'username': username})



def homekk(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    
    return render(request, 'login.html',{'state':state, 'username': username})


   # return render_to_response('login.html',{'state':state, 'username': username})
