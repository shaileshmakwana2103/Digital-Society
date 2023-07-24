from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Chairman)
admin.site.register(Societymember)
admin.site.register(Notice)
admin.site.register(NoticeViewDetails)
admin.site.register(Events)
admin.site.register(EventsViewDetails)
admin.site.register(Complaints)
admin.site.register(ComplaintsViewDetails)
admin.site.register(Maintainance)
