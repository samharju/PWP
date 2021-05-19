from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core import models

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Rule)
admin.site.register(models.Game)
