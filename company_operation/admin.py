from django.contrib import admin
from .models import OperationStatus, Service, Designation

# Register your models here.
admin.site.register(OperationStatus)
admin.site.register(Service)
admin.site.register(Designation)