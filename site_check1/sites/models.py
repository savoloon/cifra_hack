from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class SiteUserProfile(models.Model):  # Изменено имя класса
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    response_content = models.CharField(max_length=255)
