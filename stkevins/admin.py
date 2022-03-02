from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Event

# Register your models here.
class Event_Admin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ("title", "date",)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Event, Event_Admin)

"""
class Sacrament_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class Community_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class Society_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class Parishioner_Admin(admin.ModelAdmin):
    list_display = ("name", "id_number",)
    prepopulated_fields = {'slug': ('name', 'id_number')}

class Levy_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class Contribution_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Sacrament, Sacrament_Admin)
admin.site.register(Community, Community_Admin)
admin.site.register(Society, Society_Admin)
admin.site.register(Parishioner, Parishioner_Admin)
admin.site.register(Levy, Levy_Admin)
admin.site.register(Contribution, Contribution_Admin)

"""