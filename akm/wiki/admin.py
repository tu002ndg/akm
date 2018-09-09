from django.contrib import admin
from akm.wiki.models import Section, Group, Part, Category, Article, Detail
#from django.utils.translation import gettext_lazy as _
#from django.core.exceptions import ObjectDoesNotExist


class SectionInlineAdmin(admin.StackedInline):
    model = Section
    fk_name="group"
    extra=0
    fields = (('ordnum','title'),'description')
    

class GroupAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'description',)
    fields = ['title','description']
    list_display_links=('title',)
    inlines = (SectionInlineAdmin,)
    #filter_horizontal = ('sections',)
    def save_model(self, request, obj, form, change):
        if not hasattr(obj,'author'):
             obj.author = request.user
        obj.save()


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
                instance.save()

    def save_model(self, request, obj, form, change):
        if (not obj.author):
            obj.author = request.user
        obj.save()

class CategoryAdmin(admin.ModelAdmin):
   list_display=('title', 'description','slug','importance',)
   fields = (('importance','part',),'title','description')
   search_fields = ('title',)
   list_filter = ('part',)
   
   def save_model(self, request, obj, form, change):
        if (not obj.author):
            obj.author = request.user
        obj.save()

class PartListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = ('разделы')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'part'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return Part.objects.order_by('id').values_list('id','title')

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value
        # to decide how to filter the queryset.
        if self.value():
            categories = Category.objects.all().filter(part=self.value())
            return queryset.filter(category__in=[current.id for current in categories])
        else:
            return queryset

from django.forms.models import BaseInlineFormSet

class DetailFormSet(BaseInlineFormSet):

    GROUP_CODE = 3

    def __init__(self, *args, **kwargs):
        super(DetailFormSet, self).__init__(*args, **kwargs)

        self.can_delete = False
        self.initial=[]
        ps=Section.objects.filter(group=self.GROUP_CODE)
        for item in ps.values():
            self.initial.append({'ordnum':item['ordnum'], 
            'title_section': item['title'], })

 


class DetailInlineAdmin(admin.StackedInline):
    model = Detail
    fk_name = "article"
     
    formset = DetailFormSet
    EXTRA_NUM = Section.objects.filter(group=formset.GROUP_CODE).count()


    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        else: 
            return self.EXTRA_NUM
    
    #def has_add_permission(self, request):
    #    return False

    fields = (('ordnum','title_section'),
    'markdown_content', 'file_to','html_content')
    

class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','category','slug','author','modified_by')
    fields = (('status','view_count',),
    'category', 'title', 'abstract', ('uploaded',),)
    search_fields = ('title',)
    list_filter =  (PartListFilter,'status',)

    inlines = (DetailInlineAdmin,)
    
    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if isinstance(instance, Detail): #Check if it is the correct type of inline
                instance.html_content = instance.markdown_content
                instance.save()

    def save_model(self, request, obj, form, change):
        obj.modified_by =  request.user
        if not hasattr(obj,'author'):
             obj.author = request.user
        obj.save()

admin.site.register(Group, GroupAdmin)
admin.site.register(Part, PartAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)


