from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    userIP = models.CharField(max_length=16)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="messages"
    )
    text = models.TextField(blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    isOffensiveInModelView=models.BooleanField(null=True)
    isOffensiveInUserView=models.BooleanField(null=True)

    def __str__(self):
        return self.text