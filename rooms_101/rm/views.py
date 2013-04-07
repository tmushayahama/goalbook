from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template import Context, loader, RequestContext
from rm.forms import RegistrationForm, LoginForm

from rm.models import *
import json

def index(request):
    latest_poll_list = RmUser.objects.all()
    template = loader.get_template('index.html')
    context = Context({
            'latest_poll_list': latest_poll_list, 
    })
    return HttpResponse(template.render(context))

def register_user(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')
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
            rm_user = RmUser(user=user)
            rm_user.save()
            user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home/')
        else:
            context ={'form':form}
            return render(request, 'register.html', context)
    else :
        '''show a blank form '''
        form = RegistrationForm()
        context ={'form':form}
        return render(request, 'register.html', context)
        
def login_user(request):
    if request.user.is_authenticated():
       return HttpResponseRedirect('/home/')
    if (request.method == 'POST'):
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
               # state = "Welcome "+user.first_name
               # name=user.first_name
                return render(request, 'login.html',{'form':form})
        else:
            return render(request, 'login.html',{'form':form})
    else:
        form = LoginForm()
        context ={'form':form}
        return render(request, 'login.html', context)

@login_required 
def home_page(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    rm_user = request.user.get_profile
    friends = RmFriend.objects.filter(user=rm_user)
    goals = RmUserTask.objects.filter(taskee=rm_user)
    goals_list = []
    friends_list = [] #create list
    for row in goals: #populate list
        goals_list.append({'task_name':row.task.name})
    
    for row in friends: #populate list
        friends_list.append({'first_name':row.friend.user.first_name, 'last_name': row.friend.user.last_name})
    
    friends = json.dumps(friends_list) #dump list as JSON
    goals = json.dumps(goals_list)
       # return HttpResponse(recipe_list_json, 'application/javascript')
    context = {'friends':friends, 'goals':goals}
    return render(request, 'home.html', context)

@login_required 
def profile_page(request):
    if request.user.is_authenticated():
        #return HttpResponseRedirect('/profile')
        return render(request, 'profile.html')


def logout_user (request):
    logout(request)
    return HttpResponseRedirect('/login')
