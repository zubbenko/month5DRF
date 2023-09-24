from django.contrib import admin
from .models import Ads, Category, HashTag, AdsImage
admin.site.register(Ads)
admin.site.register(HashTag)
admin.site.register(Category)
admin.site.register(AdsImage)