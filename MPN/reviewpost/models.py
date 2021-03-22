from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Reviewpost(models.Model):
    sno=models.AutoField(primary_key=True)
    content_name = models.CharField(max_length=150, null=True)
    content = models.TextField()
    photos = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(default=now)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

	