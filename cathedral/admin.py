from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Reflection

# Register your models here.
class Reflection_Admin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ("title", "name",)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Reflection, Reflection_Admin)