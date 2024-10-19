from django.contrib import admin
from menu import models as m

admin.site.register(m.Category)
admin.site.register(m.Meals)
admin.site.register(m.Review)
admin.site.register(m.Gallery)