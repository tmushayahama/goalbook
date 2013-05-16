from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template import Context, loader, RequestContext
from rm.forms import RegistrationForm, LoginForm, CommitGoalForm

from rm.models import *
import json

def index(request):
    latest_poll_list = GbUser.objects.all()
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
            gb_user = GbUser(user=user)
            gb_user.gender = form.cleaned_data['gender']
            gb_user.birthdate = form.cleaned_data['birthdate']
            gb_user.save()
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
    context = get_home_profile(request)
    return render(request, 'home.html', context)

@login_required
def commit_goal(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    if (request.method == 'POST'):
        form = CommitGoalForm(request.POST)
        if form.is_valid():
            task_type = RmTaskType.objects.get(name="Goal")
            task_category=RmTaskCategory.objects.get(name="other")
            rm_user = request.user
            goal_name=form.cleaned_data['goal']
            start_date=form.cleaned_data['start_date']
            end_date=form.cleaned_data['end_date']
            task = RmTask(name=goal_name,
                          is_group_task=0,
                          task_type=task_type,
                          task_category=task_category,
                          begin_date=start_date,
                          end_date=end_date)
            task.save();
            rm_user=RmUser.objects.get(user=rm_user)
            user_task = RmUserTask(taskee=rm_user, tasker=rm_user, task=task)
            user_task.save()
    
    return HttpResponse(json.dumps({"commitment":goal_name,
                                    "taskee_name":user_task.taskee.user.first_name}))
  
@login_required
def send_request(request, friend, purpose):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    if (request.method == 'POST'):
        return HttpResponse(json.dumps({"commitment":True}))
       
          
@login_required
def profile_page(request, username):
    if request.user.is_authenticated():
        gb_user = request.user
        if username == gb_user.username:
            context = {'authorization':'owner',
                       'commit_goal_form':CommitGoalForm()}
            context.update(get_home_profile(request))
            return render(request, 'profile.html', context)
        else:
            if is_friend(gb_user, username):
                context = {'authorization':'friend'}
                return render(request, 'profile.html', context)
            else:
                gb_user=GbUser.objects.get(user__username=username)
                context = {'authorization':'non_friend',
                           'username':username,
                           'first_name':gb_user.user.first_name,
                           'last_name':gb_user.user.last_name}
                return render(request, 'profile_non_friend.html', context)

def logout_user (request):
    logout(request)
    return HttpResponseRedirect('/login')

def is_friend(user, friend_username):
    try:
        GbRelationship.objects.get(user=user, friend__username=friend_username)
    except GbRelationship.DoesNotExist:
        return False
    return True

def get_home_profile(request):
    gb_user = request.user
    friends = GbRelationship.objects.filter(user=gb_user)
    goals = GbUserTask.objects.filter(taskee=gb_user)
    suggested_friends = GbUser.objects.exclude(user=request.user)#exclude(user=rm_user)
    suggested_friends_list = []
    goals_list = []
    friends_list = [] #create list
    for row in goals: #populate list
        goals_list.append({'task_name':row.task.name})
    
    for row in friends: #populate list
        friends_list.append({'first_name':row.friend.user.first_name, 'last_name': row.friend.user.last_name})
        suggested_friends = suggested_friends.exclude(user=row.friend.user)

    for row in suggested_friends: #populate list
        suggested_friends_list.append({"username":row.user.username, "first_name":row.user.first_name, "last_name": row.user.last_name})
    
        
    friends = json.dumps(friends_list) #dump list as JSON
    goals = json.dumps(goals_list)
       # return HttpResponse(recipe_list_json, 'application/javascript')
    return {'friends':friends, 
            'goals':goals,
            'suggested_friends':json.dumps(suggested_friends_list),
            'commit_goal_form':CommitGoalForm()}
