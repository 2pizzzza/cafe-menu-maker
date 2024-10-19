from django.contrib import admin

from event import models as m

admin.site.register(m.Event)
admin.site.register(m.ImageForEvent)
