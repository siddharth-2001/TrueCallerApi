from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class Contact(models.Model):

    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    name  = models.CharField(max_length=128, default="")
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(blank = False, max_length=20)

    class Meta:
        indexes = [models.Index(fields=["phone"])]
    def __str__ (self):

        return self.name