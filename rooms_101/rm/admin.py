from django.contrib import admin
from rm.models import RmUser, RmTask, RmTaskCategory, RmPrivilegeType, RmTaskType, RmGroupCategory, RmGroup, RmGroupMonitor, RmGroupTask, RmIsMember, RmUserMonitor, RmFollow, RmFriend, RmTaskHistory, RmUserTask

admin.site.register(RmUser)
admin.site.register(RmTaskCategory)
admin.site.register(RmPrivilegeType)
admin.site.register(RmTaskType)
admin.site.register(RmTask)
admin.site.register(RmGroupCategory)
admin.site.register(RmGroup)
admin.site.register(RmGroupMonitor)
admin.site.register(RmGroupTask)
admin.site.register(RmIsMember)
admin.site.register(RmUserMonitor)
admin.site.register(RmFollow)
admin.site.register(RmFriend)
admin.site.register(RmTaskHistory)
admin.site.register(RmUserTask)
