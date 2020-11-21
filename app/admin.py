from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class PostImportExport(admin.ModelAdmin):
    list_display = [
        'operation_number',
        'author',

    ]
    list_filter = ['shop']
    search_fields = ['shop', 'operation_number','author']

class Pos(admin.ModelAdmin):
    list_display = [
        'title',
        'num',
        'mobile'

    ]
    search_fields = ['title', 'num','mobile']




admin.site.register(Shop,Pos)
admin.site.register(Bond, PostImportExport)
admin.site.unregister(Group)
admin.site.site_header = 'لوحة التحكم'
admin.site.site_title = 'شركة هاني حسن رضا ابو عبدالله وشركاه'
admin.site.index_title = 'شركة هاني حسن رضا ابو عبدالله وشركاه'
admin.site.site_url="/disclosures"






