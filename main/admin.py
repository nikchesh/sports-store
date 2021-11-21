from django.contrib import admin

# Register your models here.

from .models import Task
from .models import Sales, Shortages, Clients

admin.site.register(Task)
admin.site.register(Sales)
admin.site.register(Shortages)
admin.site.register(Clients)