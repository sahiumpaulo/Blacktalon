from django.db import models

class Relics(models.Model):
    name = models.CharField(max_length=50)
    mod_type = models.CharField(max_length=30)
    tier_1 = models.DecimalField(max_digits=5, decimal_places=2)
    tier_2 = models.DecimalField(max_digits=5, decimal_places=2)
    tier_3 = models.DecimalField(max_digits=5, decimal_places=2)
    method = models.CharField(max_length=50)