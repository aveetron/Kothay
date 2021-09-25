from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    status = models.BooleanField(default=True)

class OperationStatus(BaseModel):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Service(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    details = models.TextField(null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)

    def __str__(self):
        return self.name + '-' + self.cost


class Designation(BaseModel):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

