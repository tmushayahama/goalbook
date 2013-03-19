# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class RmFollow(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(RmUser)
    friend = models.ForeignKey(RmUser)
    class Meta:
        db_table = u'rm_follow'

class RmFriend(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(RmUser)
    friend = models.ForeignKey(RmUser)
    privilege_type = models.ForeignKey(RmPrivilegeType)
    class Meta:
        db_table = u'rm_friend'

class RmGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    founder = models.ForeignKey(RmUser)
    group_category = models.ForeignKey(RmGroupCategory)
    founded = models.DateTimeField()
    decription = models.CharField(max_length=3000, blank=True)
    class Meta:
        db_table = u'rm_group'

class RmGroupCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=3000, blank=True)
    class Meta:
        db_table = u'rm_group_category'

class RmGroupMonitor(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(RmGroup)
    monitor = models.ForeignKey(RmGroup)
    task = models.ForeignKey(RmTask)
    class Meta:
        db_table = u'rm_group_monitor'

class RmGroupTask(models.Model):
    id = models.IntegerField(primary_key=True)
    taskee = models.ForeignKey(RmGroup, db_column='taskee')
    tasker = models.ForeignKey(RmGroup, db_column='tasker')
    task = models.ForeignKey(RmTask)
    class Meta:
        db_table = u'rm_group_task'

class RmIsMember(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(RmUser)
    group = models.ForeignKey(RmGroup)
    privilege_type = models.ForeignKey(RmPrivilegeType)
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'rm_is_member'

class RmPrivilegeType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=3000, blank=True)
    class Meta:
        db_table = u'rm_privilege_type'

class RmTask(models.Model):
    id = models.IntegerField(primary_key=True)
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

class RmTaskCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=3000, blank=True)
    class Meta:
        db_table = u'rm_task_category'

class RmTaskHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    task = models.ForeignKey(RmTask)
    date_done = models.DateTimeField()
    class Meta:
        db_table = u'rm_task_history'

class RmTaskType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=3000, blank=True)
    class Meta:
        db_table = u'rm_task_type'

class RmUser(models.Model):
    id = models.IntegerField(primary_key=True)
    user_password = models.CharField(max_length=60)
    email = models.CharField(max_length=150, unique=True)
    f_name = models.CharField(max_length=150)
    l_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=3)
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'rm_user'

class RmUserMonitor(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(RmUser)
    monitor = models.ForeignKey(RmUser)
    task = models.ForeignKey(RmTask)
    class Meta:
        db_table = u'rm_user_monitor'

class RmUserTask(models.Model):
    id = models.IntegerField(primary_key=True)
    taskee = models.ForeignKey(RmUser, db_column='taskee')
    tasker = models.ForeignKey(RmUser, db_column='tasker')
    task = models.ForeignKey(RmTask)
    class Meta:
        db_table = u'rm_user_task'

