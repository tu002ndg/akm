from django.contrib import admin
from akm.wiki.models import Section, Group, Part, Category #, Pattern

#class SectionAdmin(admin.ModelAdmin):
#    list_display=('title','description',)
#    search_fields=('title',)

class SectionInlineAdmin(admin.StackedInline):
    #model = Group.sections.through
    model = Section
    fk_name="group"
    extra=0
    fields = (('ordnum','title'),'description')
    

class GroupAdmin(admin.ModelAdmin):
    list_display=('title', 'description',)
    fields = ['title','description']
    inlines = (SectionInlineAdmin,)
    #filter_horizontal = ('sections',)
    def save_model(self, request, obj, form, change):
        if (not obj.author):
            obj.author = request.user
        obj.save()

#class PatternAdmin(admin.ModelAdmin):
#    list_display=('group','ordnum','section',)

class CategoryInlineAdmin(admin.StackedInline):
    model = Category
    fk_name = "part"
    extra=0
    fields = (('importance','title'),'description')

class PartAdmin(admin.ModelAdmin):
    list_display=('importance', 'acronym','title', )
    list_display_links = ('acronym','title', )
    fieldsets = (
        ('название раздела', 
        {'fields': ('acronym','title',)}),
        ('Примечание', 
        {'fields': ('description',)}),
        ('дополнительно',
        {'fields': (('importance','logo'),)}),
    )
    inlines = (CategoryInlineAdmin,)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if isinstance(instance, Category): #Check if it is the correct type of inline
                if(not instance.author):
                    instance.author = request.user
#                else:
#                    instance.modified_by = request.user            
                instance.save()

    def save_model(self, request, obj, form, change):
        if (not obj.author):
            obj.author = request.user
        obj.save()

#class CategoryAdmin(admin.ModelAdmin):
#    list_display=('part','title', 'description','slug','importance',)

#admin.site.register(Section, SectionAdmin)
admin.site.register(Group, GroupAdmin)
#admin.site.register(Pattern, PatternAdmin)
admin.site.register(Part, PartAdmin)
#admin.site.register(Category, CategoryAdmin)
