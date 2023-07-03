from django.contrib import admin
from .models import AndroidApp,UserApp,Profile

# Register your models here.
admin.site.register(AndroidApp)
admin.site.register(UserApp)
admin.site.register(Profile)