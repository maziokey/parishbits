from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Reflection, HomeBanners, AdBannerOne, AdBannerTwo, HomeWelcomeImage

# Register your models here.
class Reflection_Admin(SummernoteModelAdmin):
    summernote_fields = ("content",)
    list_display = (
        "title",
        "name",
    )
    prepopulated_fields = {"slug": ("title",)}


class HomeBanners_Admin(admin.ModelAdmin):
    list_display = (
        "title",
        "subtitle",
        "slide",
    )

class AdBannerOne_Admin(admin.ModelAdmin):
    list_display = ("id", "banner",)

class AdBannerTwo_Admin(admin.ModelAdmin):
    list_display = ("id", "banner",)

class HomeWelcomeImage_Admin(admin.ModelAdmin):
    list_display = ("id", "image",)

admin.site.register(Reflection, Reflection_Admin)
admin.site.register(HomeBanners, HomeBanners_Admin)
admin.site.register(AdBannerOne, AdBannerOne_Admin)
admin.site.register(AdBannerTwo, AdBannerTwo_Admin)
admin.site.register(HomeWelcomeImage, HomeWelcomeImage_Admin)
