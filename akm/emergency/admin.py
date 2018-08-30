from django.contrib import admin
from akm.emergency.models import Emergency

class EmergencyAdmin(admin.ModelAdmin):
    list_display = ('contact','phone',)

admin.site.register(Emergency)


