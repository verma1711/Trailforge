from django.contrib import admin
from .models import *

admin.site.register(trackModel)
admin.site.register(eventModel)
admin.site.register(bookingModel)