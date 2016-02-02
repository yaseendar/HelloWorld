from django.contrib import admin
from models import Name


# Register your models here.

class NameAdmin(admin.ModelAdmin):
    list_display = ('name', 'saved_on')
    order_by = ('saved_on',)


admin.site.register(Name, NameAdmin)
