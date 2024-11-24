from django.db import models
from django.utils.crypto import get_random_string

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    referral_code = models.CharField(max_length=10, unique=True)
    referrals_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.referral_code:
            self.referral_code = get_random_string(8).upper()  
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
