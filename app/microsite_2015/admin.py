from django.contrib import admin
from microsite_2015.models import Page
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class PageAdmin(SummernoteModelAdmin):
    # fields display on change list
    list_display = ['title']
    # fields to filter the change list with
    save_on_top = True
    # fields to search in change list
    search_fields = ['title', 'text']
    # prepopulate the slug from the title - big timesaver!
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Page, PageAdmin)
