from django.db import models

# Create your models here.

class ModelClassName(models.Model):

    class Meta:
        app_label = 'address' # <-- this label was wrong before.

    field_name = models.FloatField()
    ...