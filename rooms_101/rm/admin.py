from django.contrib import admin
from rm.models import *

admin.site.register(GbUser)
admin.site.register(GbType)
admin.site.register(GbCategory)
admin.site.register(GbTask)
admin.site.register(GbGroup)
admin.site.register(GbGroupMonitor)
admin.site.register(GbGroupTask)
admin.site.register(GbIsMember)
admin.site.register(GbUserMonitor)
admin.site.register(GbRelationship)
admin.site.register(GbTaskTimeline)
admin.site.register(GbUserTask)
admin.site.register(GbUserGoalList)
admin.site.register(GbGroupGoalList)
admin.site.register(GbUserProfile)
admin.site.register(GbGroupProfile)
