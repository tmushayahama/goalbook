# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

class GbUser(models.Model):
    user = models.ForeignKey(User, unique=True)
    gender = models.CharField(max_length=3)
    birthdate = models.DateTimeField()
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'gb_user'
        
        def __unicode__(self):
            return u'%s' % (self.user)
        


#Task
class GbCategory(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=3000, blank=True)
    class Meta:
        db_table = u'gb_category'
    def __unicode__(self):
        return u'%s' % (self.name)

class GbType(models.Model):
    name = models.CharField(max_length=150, unique=True)
    category=models.ForeignKey(GbCategory);
    description = models.CharField(max_length=3000, blank=True)
    class Meta:
        db_table = u'gb_type'
    def __unicode__(self):
        return u'%s' % (self.name)


class GbTask(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=3000, blank=True)
    task_type = models.ForeignKey(GbType, related_name="taskType")
    task_category = models.ForeignKey(GbType, related_name="taskCategory")
    points_awarded = models.IntegerField(null=True, blank=True)
    award = models.CharField(max_length=765, blank=True)
    assign_date = models.DateTimeField()
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'gb_task'
    def __unicode__(self):
        return u'%s' % (self.name)

class GbUserGoalList(models.Model):
    user = models.ForeignKey(User, unique=True)
    name = models.CharField(max_length=150)
    date_listed = models.DateTimeField()
    class Meta:
        db_table = u'gb_user_goal_list'
        
    def __unicode__(self):
        return u'%s' % (self.user)
class GbUserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    welcome_note= models.CharField(max_length=150)
    cover_goal_1 = models.ForeignKey(GbUserGoalList, related_name="UserProfileGoal1", null=True)
    cover_goal_2 = models.ForeignKey(GbUserGoalList, related_name="UserProfileGoal2", null=True)
    cover_goal_3 = models.ForeignKey(GbUserGoalList, related_name="UserProfileGoal3",  null=True)
    class Meta:
        db_table = u'gb_user_profile'
        
    def __unicode__(self):
        return u'%s' % (self.user)

class GbGroup(models.Model):
    name = models.CharField(max_length=150, unique=True)
    founder = models.ForeignKey(User)
    group_type = models.ForeignKey(GbType, related_name="groupType")
    group_category = models.ForeignKey(GbType, related_name="groupCategory")
    founded = models.DateTimeField()
    decription = models.CharField(max_length=3000, blank=True)
    class Meta:
        db_table = u'gb_group'
    def __unicode__(self):
        return u'%s' % (self.name)

class GbGroupGoalList(models.Model):
    group = models.ForeignKey(GbGroup, unique=True)
    name = models.CharField(max_length=150)
    date_listed = models.DateTimeField()
    class Meta:
        db_table = u'gb_group_goal_list'
        
    def __unicode__(self):
        return u'%s' % (self.user)

class GbGroupProfile(models.Model):
    group = models.ForeignKey(GbGroup, unique=True)
    welcome_note= models.CharField(max_length=150)
    cover_goal_1 = models.ForeignKey(GbGroupGoalList, related_name="GroupProfileGoal1", null=True)
    cover_goal_2 = models.ForeignKey(GbGroupGoalList, related_name="GroupProfileGoal2", null=True)
    cover_goal_3 = models.ForeignKey(GbGroupGoalList, related_name="GroupProfileGoal3", null=True)
    class Meta:
        db_table = u'gb_group_profile'
        
    def __unicode__(self):
        return u'%s' % (self.group)

class GbIsMember(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(GbGroup)
    member_type = models.ForeignKey(GbType)
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'gb_is_member'

class GbGroupTask(models.Model):
    taskee = models.ForeignKey(GbGroup, db_column='taskee', related_name="groupTaskTaskee")
    tasker = models.ForeignKey(GbGroup, db_column='tasker', related_name="groupTaskTasker")
    task = models.ForeignKey(GbTask)
    class Meta:
        db_table = u'gb_group_task'

class GbGroupMonitor(models.Model):
    user = models.ForeignKey(GbGroup, related_name="groupMonitorUser")
    monitor = models.ForeignKey(GbGroup, related_name="groupMonitorMonitor")
    task = models.ForeignKey(GbTask)
    monitor_type = models.ForeignKey(GbType, related_name="groupMonitorType")
    monitor_status = models.ForeignKey(GbType, related_name="groupMonitorStatus")
    class Meta:
        db_table = u'gb_group_monitor'
    def __unicode__(self):
        return u'%s' % (self.task)

class GbUserMonitor(models.Model):
    user = models.ForeignKey(User, related_name="userMonitorUser")
    monitor = models.ForeignKey(User, related_name="userMonitorMonitor")
    task = models.ForeignKey(GbTask)
    monitor_type = models.ForeignKey(GbType, related_name="userMonitorType")
    monitor_status = models.ForeignKey(GbType, related_name="userMonitorStatus")
    class Meta:
        db_table = u'gb_user_monitor'

class GbUserTask(models.Model):
    taskee = models.ForeignKey(User, db_column='taskee', related_name="UserTaskTaskee")
    tasker = models.ForeignKey(User, db_column='tasker', related_name="UserTaskTasker")
    task = models.ForeignKey(GbTask)
    class Meta:
        db_table = u'gb_user_task'
    def __unicode__(self):
        return u'%s %s %s' % (self.taskee, self.tasker, self.task)

class GbRelationship(models.Model):
    user = models.ForeignKey(User, related_name="friendUser")
    friend = models.ForeignKey(User, related_name="friendFriend")
    friendship_type = models.ForeignKey(GbType, related_name="friendshipType")
    friendship_status = models.ForeignKey(GbType, related_name="statusType")
    request_date = models.DateTimeField()
    accepted_date = models.DateTimeField()
    class Meta:
        db_table = u'gb_relationship'
    def __unicode__(self):
        return u'%s %s %s' % (self.user, self.friend, self.friendship_type)

class GbTaskTimeline(models.Model):
    task = models.ForeignKey(GbTask)
    entry_name = models.CharField(max_length=150, unique=True)
    entry_time = models.DateTimeField()
    class Meta:
        db_table = u'gb_task_timeline'
    def __unicode__(self):
        return u'%s %s %s' % (self.task, self.entry_name, self.entry_time)
