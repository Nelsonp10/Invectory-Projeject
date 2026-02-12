from django.contrib import admin
from .models import product, oder
from django.contrib.auth.models import Group


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')

    list_filter = ('category',)


# Register your models here.
admin.site.register(product, ProductAdmin)
admin.site.register(oder)
admin.site.site_header = 'Invectory Admin'
admin.site.site_title = 'Invectory Admin Portal'
admin.site.index_title = 'Welcome to Invectory Admin Portal'
#admin.site.unregister(Group)
