from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import *

class Bookadmin(admin.ModelAdmin):


 list_display =['title','author','isbn']
admin.site.register(Book)

