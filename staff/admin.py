from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Staff)
# admin.site.register(tss)

class tssInline(admin.StackedInline):
    model = tss

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    inlines = [tssInline]