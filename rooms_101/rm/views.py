from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.template import Context, loader, RequestContext
from rm.forms import RegistrationForm

from rm.models import RmUser

def index(request):
    latest_poll_list = RmUser.objects.all()
    template = loader.get_template('rm/index.html')
    context = Context({
            'latest_poll_list': latest_poll_list, 
    })
    return HttpResponse(template.render(context))

def register_user(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile')
    if (request.method == 'POST'):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['email'],
                                            email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password'])
            user.first_name=form.cleaned_data['first_name']
            user.last_name=form.cleaned_data['last_name']
            user.save()
            #user = user.get_profile()
            #rm_user.gender= for.cleaned_data['gender']
            #user= request.user.get_profile();
            #rm_user.save()
            return HttpResponseRedirect('/profile')
        else:
            context ={'form':form}
            return render(request, 'register.html', context)

    else :
        '''show a blank form '''
        form = RegistrationForm()
        context ={'form':form}
        return render(request, 'register.html', context)
        

    
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



def home(request):
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
