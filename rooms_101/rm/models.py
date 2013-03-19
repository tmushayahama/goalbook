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

class RmUser(models.Model):
    user = models.ForeignKey(User, unique=True, related_name ="foo")
    gender = models.CharField(max_length=3)
    class Meta:
        db_table = u'rm_user'
    def __unicode__(self):
        return u'%s' % (self.user)

class RmTaskCategory(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=3000, blank=True)
    class Meta:
        db_table = u'rm_task_category'
    def __unicode__(self):
        return u'%s %s' % (self.name, self.description)

class RmTaskType(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=3000, blank=True)
    class Meta:
        db_table = u'rm_task_type'

class RmPrivilegeType(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=3000, blank=True)
    class Meta:
        db_table = u'rm_privilege_type'

class RmGroupCategory(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=3000, blank=True)
    class Meta:
        db_table = u'rm_group_category'

class RmTask(models.Model):
    name = models.CharField(max_length=150)
    is_group_task = models.IntegerField()
    task_type = models.ForeignKey(RmTaskType)
    task_category = models.ForeignKey(RmTaskCategory)
    points_awarded = models.IntegerField(null=True, blank=True)
    award = models.CharField(max_length=765, blank=True)
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'rm_task'

class RmGroup(models.Model):
    name = models.CharField(max_length=150, unique=True)
    founder = models.ForeignKey(RmUser)
    group_category = models.ForeignKey(RmGroupCategory)
    founded = models.DateTimeField()
    decription = models.CharField(max_length=3000, blank=True)
    class Meta:
        db_table = u'rm_group'

class RmGroupMonitor(models.Model):
    user = models.ForeignKey(RmGroup, related_name="groupMonitorUser")
    monitor = models.ForeignKey(RmGroup, related_name="groupMonitorMonitor")
    task = models.ForeignKey(RmTask)
    class Meta:
        db_table = u'rm_group_monitor'

class RmGroupTask(models.Model):
    taskee = models.ForeignKey(RmGroup, db_column='taskee', related_name="groupTaskTaskee")
    tasker = models.ForeignKey(RmGroup, db_column='tasker', related_name="groupTaskTasker")
    task = models.ForeignKey(RmTask)
    class Meta:
        db_table = u'rm_group_task'

class RmIsMember(models.Model):
    user = models.ForeignKey(RmUser)
    group = models.ForeignKey(RmGroup)
    privilege_type = models.ForeignKey(RmPrivilegeType)
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'rm_is_member'



class RmUserMonitor(models.Model):
    user = models.ForeignKey(RmUser, related_name="userMonitorUser")
    monitor = models.ForeignKey(RmUser, related_name="userMonitorMonitor")
    task = models.ForeignKey(RmTask)
    class Meta:
        db_table = u'rm_user_monitor'

class RmUserTask(models.Model):
    taskee = models.ForeignKey(RmUser, db_column='taskee', related_name="UserTaskTaskee")
    tasker = models.ForeignKey(RmUser, db_column='tasker', related_name="UserTaskTasker")
    task = models.ForeignKey(RmTask)
    class Meta:
        db_table = u'rm_user_task'

class RmFollow(models.Model):
    user = models.ForeignKey(RmUser, related_name="followUser")
    friend = models.ForeignKey(RmUser, related_name="followFollow")
    class Meta:
        db_table = u'rm_follow'

class RmFriend(models.Model):
    user = models.ForeignKey(RmUser, related_name="friendUser")
    friend = models.ForeignKey(RmUser, related_name="friendFriend")
    privilege_type = models.ForeignKey(RmPrivilegeType)
    class Meta:
        db_table = u'rm_friend'

class RmTaskHistory(models.Model):
    task = models.ForeignKey(RmTask)
    date_done = models.DateTimeField()
    class Meta:
        db_table = u'rm_task_history'


