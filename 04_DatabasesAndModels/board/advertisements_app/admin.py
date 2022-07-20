from django.contrib import admin
from advertisements_app.models import Advertisement, AdvertisementCategory, AdvertisementStatus, AdvertisementAuthor


# Register your models here.
@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    pass

# @admin.register(AdvertisementCategory)
# class AdvertisementCategoryAdmin(admin.ModelAdmin):
#     pass

# @admin.register(AdvertisementStatus)
# class AdvertisementStatusAdmin(admin.ModelAdmin):
#     pass

# @admin.register(AdvertisementStatus)
# class AdvertisementAuthorAdmin(admin.ModelAdmin):
#     pass
