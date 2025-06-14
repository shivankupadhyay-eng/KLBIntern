from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    telegram_id=models.BigIntegerField(blank=True,null=True,unique=True)
    telegram_username=models.CharField(max_length=120,blank=False,null=False)


    def __str__(self):
        return self.username
    