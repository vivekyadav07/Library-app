from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import *
@admin.register(Book)
class Bookadmin(admin.ModelAdmin):


 list_display =['title','author','isbn']


