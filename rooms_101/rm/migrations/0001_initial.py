# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GbUser'
        db.create_table(u'gb_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('birthdate', self.gf('django.db.models.fields.DateTimeField')()),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('rm', ['GbUser'])

        # Adding model 'GbCategory'
        db.create_table(u'gb_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=3000, blank=True)),
        ))
        db.send_create_signal('rm', ['GbCategory'])

        # Adding model 'GbType'
        db.create_table(u'gb_type', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rm.GbCategory'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=3000, blank=True)),
        ))
        db.send_create_signal('rm', ['GbType'])

        # Adding model 'GbTask'
        db.create_table(u'gb_task', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=3000, blank=True)),
            ('task_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='taskType', to=orm['rm.GbType'])),
            ('task_category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='taskCategory', to=orm['rm.GbType'])),
            ('points_awarded', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('award', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('assign_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('begin_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('rm', ['GbTask'])

        # Adding model 'GbUserGoalList'
        db.create_table(u'gb_user_goal_list', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('date_listed', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('rm', ['GbUserGoalList'])

        # Adding model 'GbUserProfile'
        db.create_table(u'gb_user_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('welcome_note', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('cover_goal_1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='UserProfileGoal1', null=True, to=orm['rm.GbUserGoalList'])),
            ('cover_goal_2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='UserProfileGoal2', null=True, to=orm['rm.GbUserGoalList'])),
            ('cover_goal_3', self.gf('django.db.models.fields.related.ForeignKey')(related_name='UserProfileGoal3', null=True, to=orm['rm.GbUserGoalList'])),
        ))
        db.send_create_signal('rm', ['GbUserProfile'])

        # Adding model 'GbGroup'
        db.create_table(u'gb_group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('founder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('group_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='groupType', to=orm['rm.GbType'])),
            ('group_category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='groupCategory', to=orm['rm.GbType'])),
            ('founded', self.gf('django.db.models.fields.DateTimeField')()),
            ('decription', self.gf('django.db.models.fields.CharField')(max_length=3000, blank=True)),
        ))
        db.send_create_signal('rm', ['GbGroup'])

        # Adding model 'GbGroupGoalList'
        db.create_table(u'gb_group_goal_list', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rm.GbGroup'], unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('date_listed', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('rm', ['GbGroupGoalList'])

        # Adding model 'GbGroupProfile'
        db.create_table(u'gb_group_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rm.GbGroup'], unique=True)),
            ('welcome_note', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('cover_goal_1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='GroupProfileGoal1', null=True, to=orm['rm.GbGroupGoalList'])),
            ('cover_goal_2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='GroupProfileGoal2', null=True, to=orm['rm.GbGroupGoalList'])),
            ('cover_goal_3', self.gf('django.db.models.fields.related.ForeignKey')(related_name='GroupProfileGoal3', null=True, to=orm['rm.GbGroupGoalList'])),
        ))
        db.send_create_signal('rm', ['GbGroupProfile'])

        # Adding model 'GbIsMember'
        db.create_table(u'gb_is_member', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rm.GbGroup'])),
            ('member_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rm.GbType'])),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('rm', ['GbIsMember'])

        # Adding model 'GbGroupTask'
        db.create_table(u'gb_group_task', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('taskee', self.gf('django.db.models.fields.related.ForeignKey')(related_name='groupTaskTaskee', db_column='taskee', to=orm['rm.GbGroup'])),
            ('tasker', self.gf('django.db.models.fields.related.ForeignKey')(related_name='groupTaskTasker', db_column='tasker', to=orm['rm.GbGroup'])),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rm.GbTask'])),
        ))
        db.send_create_signal('rm', ['GbGroupTask'])

        # Adding model 'GbGroupMonitor'
        db.create_table(u'gb_group_monitor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='groupMonitorUser', to=orm['rm.GbGroup'])),
            ('monitor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='groupMonitorMonitor', to=orm['rm.GbGroup'])),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rm.GbTask'])),
            ('monitor_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='groupMonitorType', to=orm['rm.GbType'])),
            ('monitor_status', self.gf('django.db.models.fields.related.ForeignKey')(related_name='groupMonitorStatus', to=orm['rm.GbType'])),
        ))
        db.send_create_signal('rm', ['GbGroupMonitor'])

        # Adding model 'GbUserMonitor'
        db.create_table(u'gb_user_monitor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='userMonitorUser', to=orm['auth.User'])),
            ('monitor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='userMonitorMonitor', to=orm['auth.User'])),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rm.GbTask'])),
            ('monitor_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='userMonitorType', to=orm['rm.GbType'])),
            ('monitor_status', self.gf('django.db.models.fields.related.ForeignKey')(related_name='userMonitorStatus', to=orm['rm.GbType'])),
        ))
        db.send_create_signal('rm', ['GbUserMonitor'])

        # Adding model 'GbUserTask'
        db.create_table(u'gb_user_task', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('taskee', self.gf('django.db.models.fields.related.ForeignKey')(related_name='UserTaskTaskee', db_column='taskee', to=orm['auth.User'])),
            ('tasker', self.gf('django.db.models.fields.related.ForeignKey')(related_name='UserTaskTasker', db_column='tasker', to=orm['auth.User'])),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rm.GbTask'])),
        ))
        db.send_create_signal('rm', ['GbUserTask'])

        # Adding model 'GbRelationship'
        db.create_table(u'gb_relationship', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='friendUser', to=orm['auth.User'])),
            ('friend', self.gf('django.db.models.fields.related.ForeignKey')(related_name='friendFriend', to=orm['auth.User'])),
            ('friendship_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='friendshipType', to=orm['rm.GbType'])),
            ('friendship_status', self.gf('django.db.models.fields.related.ForeignKey')(related_name='statusType', to=orm['rm.GbType'])),
            ('request_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('accepted_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('rm', ['GbRelationship'])

        # Adding model 'GbTaskTimeline'
        db.create_table(u'gb_task_timeline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rm.GbTask'])),
            ('entry_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('entry_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('rm', ['GbTaskTimeline'])


    def backwards(self, orm):
        # Deleting model 'GbUser'
        db.delete_table(u'gb_user')

        # Deleting model 'GbCategory'
        db.delete_table(u'gb_category')

        # Deleting model 'GbType'
        db.delete_table(u'gb_type')

        # Deleting model 'GbTask'
        db.delete_table(u'gb_task')

        # Deleting model 'GbUserGoalList'
        db.delete_table(u'gb_user_goal_list')

        # Deleting model 'GbUserProfile'
        db.delete_table(u'gb_user_profile')

        # Deleting model 'GbGroup'
        db.delete_table(u'gb_group')

        # Deleting model 'GbGroupGoalList'
        db.delete_table(u'gb_group_goal_list')

        # Deleting model 'GbGroupProfile'
        db.delete_table(u'gb_group_profile')

        # Deleting model 'GbIsMember'
        db.delete_table(u'gb_is_member')

        # Deleting model 'GbGroupTask'
        db.delete_table(u'gb_group_task')

        # Deleting model 'GbGroupMonitor'
        db.delete_table(u'gb_group_monitor')

        # Deleting model 'GbUserMonitor'
        db.delete_table(u'gb_user_monitor')

        # Deleting model 'GbUserTask'
        db.delete_table(u'gb_user_task')

        # Deleting model 'GbRelationship'
        db.delete_table(u'gb_relationship')

        # Deleting model 'GbTaskTimeline'
        db.delete_table(u'gb_task_timeline')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'rm.gbcategory': {
            'Meta': {'object_name': 'GbCategory', 'db_table': "u'gb_category'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '3000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
        'rm.gbgroup': {
            'Meta': {'object_name': 'GbGroup', 'db_table': "u'gb_group'"},
            'decription': ('django.db.models.fields.CharField', [], {'max_length': '3000', 'blank': 'True'}),
            'founded': ('django.db.models.fields.DateTimeField', [], {}),
            'founder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'group_category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'groupCategory'", 'to': "orm['rm.GbType']"}),
            'group_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'groupType'", 'to': "orm['rm.GbType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
        'rm.gbgroupgoallist': {
            'Meta': {'object_name': 'GbGroupGoalList', 'db_table': "u'gb_group_goal_list'"},
            'date_listed': ('django.db.models.fields.DateTimeField', [], {}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rm.GbGroup']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'rm.gbgroupmonitor': {
            'Meta': {'object_name': 'GbGroupMonitor', 'db_table': "u'gb_group_monitor'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monitor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'groupMonitorMonitor'", 'to': "orm['rm.GbGroup']"}),
            'monitor_status': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'groupMonitorStatus'", 'to': "orm['rm.GbType']"}),
            'monitor_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'groupMonitorType'", 'to': "orm['rm.GbType']"}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rm.GbTask']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'groupMonitorUser'", 'to': "orm['rm.GbGroup']"})
        },
        'rm.gbgroupprofile': {
            'Meta': {'object_name': 'GbGroupProfile', 'db_table': "u'gb_group_profile'"},
            'cover_goal_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'GroupProfileGoal1'", 'null': 'True', 'to': "orm['rm.GbGroupGoalList']"}),
            'cover_goal_2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'GroupProfileGoal2'", 'null': 'True', 'to': "orm['rm.GbGroupGoalList']"}),
            'cover_goal_3': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'GroupProfileGoal3'", 'null': 'True', 'to': "orm['rm.GbGroupGoalList']"}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rm.GbGroup']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'welcome_note': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'rm.gbgrouptask': {
            'Meta': {'object_name': 'GbGroupTask', 'db_table': "u'gb_group_task'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rm.GbTask']"}),
            'taskee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'groupTaskTaskee'", 'db_column': "'taskee'", 'to': "orm['rm.GbGroup']"}),
            'tasker': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'groupTaskTasker'", 'db_column': "'tasker'", 'to': "orm['rm.GbGroup']"})
        },
        'rm.gbismember': {
            'Meta': {'object_name': 'GbIsMember', 'db_table': "u'gb_is_member'"},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rm.GbGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rm.GbType']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'rm.gbrelationship': {
            'Meta': {'object_name': 'GbRelationship', 'db_table': "u'gb_relationship'"},
            'accepted_date': ('django.db.models.fields.DateTimeField', [], {}),
            'friend': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'friendFriend'", 'to': "orm['auth.User']"}),
            'friendship_status': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'statusType'", 'to': "orm['rm.GbType']"}),
            'friendship_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'friendshipType'", 'to': "orm['rm.GbType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request_date': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'friendUser'", 'to': "orm['auth.User']"})
        },
        'rm.gbtask': {
            'Meta': {'object_name': 'GbTask', 'db_table': "u'gb_task'"},
            'assign_date': ('django.db.models.fields.DateTimeField', [], {}),
            'award': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'begin_date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '3000', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'points_awarded': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'task_category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taskCategory'", 'to': "orm['rm.GbType']"}),
            'task_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taskType'", 'to': "orm['rm.GbType']"})
        },
        'rm.gbtasktimeline': {
            'Meta': {'object_name': 'GbTaskTimeline', 'db_table': "u'gb_task_timeline'"},
            'entry_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'entry_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rm.GbTask']"})
        },
        'rm.gbtype': {
            'Meta': {'object_name': 'GbType', 'db_table': "u'gb_type'"},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rm.GbCategory']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '3000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
        'rm.gbuser': {
            'Meta': {'object_name': 'GbUser', 'db_table': "u'gb_user'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'birthdate': ('django.db.models.fields.DateTimeField', [], {}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'rm.gbusergoallist': {
            'Meta': {'object_name': 'GbUserGoalList', 'db_table': "u'gb_user_goal_list'"},
            'date_listed': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'rm.gbusermonitor': {
            'Meta': {'object_name': 'GbUserMonitor', 'db_table': "u'gb_user_monitor'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monitor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'userMonitorMonitor'", 'to': "orm['auth.User']"}),
            'monitor_status': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'userMonitorStatus'", 'to': "orm['rm.GbType']"}),
            'monitor_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'userMonitorType'", 'to': "orm['rm.GbType']"}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rm.GbTask']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'userMonitorUser'", 'to': "orm['auth.User']"})
        },
        'rm.gbuserprofile': {
            'Meta': {'object_name': 'GbUserProfile', 'db_table': "u'gb_user_profile'"},
            'cover_goal_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'UserProfileGoal1'", 'null': 'True', 'to': "orm['rm.GbUserGoalList']"}),
            'cover_goal_2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'UserProfileGoal2'", 'null': 'True', 'to': "orm['rm.GbUserGoalList']"}),
            'cover_goal_3': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'UserProfileGoal3'", 'null': 'True', 'to': "orm['rm.GbUserGoalList']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'welcome_note': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'rm.gbusertask': {
            'Meta': {'object_name': 'GbUserTask', 'db_table': "u'gb_user_task'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rm.GbTask']"}),
            'taskee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'UserTaskTaskee'", 'db_column': "'taskee'", 'to': "orm['auth.User']"}),
            'tasker': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'UserTaskTasker'", 'db_column': "'tasker'", 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['rm']