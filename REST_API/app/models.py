from django.db import models

class ModelDataTables (models.Model):

    user = models.CharField(max_length=5)
    item_name = models.CharField(max_length=20)