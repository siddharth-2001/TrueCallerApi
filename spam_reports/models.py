from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class SpamReport(models.Model):
    
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(blank=True, max_length=120)
    phone = models.CharField(max_length=20)
    reported_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [models.Index(fields=["phone"])]
    def __str__(self):
        return f"Reported by {self.reported_by.username} for {self.phone_number}"