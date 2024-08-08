from django.db import models

class Relics(models.Model):
    name = models.CharField(max_length=50)
    mod_type = models.CharField(max_length=30)
    tier_1 = models.CharField(max_length=20)
    tier_2 = models.CharField(max_length=20, null=True, blank=True)
    tier_3 = models.CharField(max_length=20, null=True, blank=True)
    method = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return f"{self.name}"