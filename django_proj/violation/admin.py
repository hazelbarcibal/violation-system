from django.contrib import admin

# Register your models here.
from .models import Records
from .models import customUser

admin.site.register(Records)
admin.site.register(customUser)
