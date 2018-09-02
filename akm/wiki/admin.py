from django.contrib import admin
from akm.wiki.models import Section

class SectionAdmin(admin.ModelAdmin):
    list_display=('title','description',)
    search_fields=('title',)

admin.site.register(Section, SectionAdmin)
