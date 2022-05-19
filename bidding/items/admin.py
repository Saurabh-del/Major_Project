from django.contrib import admin

# Register your models here.
from . models import Item
from accounts.models import Detail, UserOTP

admin.site.register(Item)
admin.site.register(Detail)
admin.site.register(UserOTP)