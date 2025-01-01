import uuid
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    referral_code = models.CharField(max_length=8, unique=True)
    referred_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.referral_code:
            self.referral_code = str(uuid.uuid4())[:8]
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'users'

class LeaderboardEntry(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField()
    referrals = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
