from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Recipepost(models.Model):
    sno=models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    recipe = models.TextField()
    photos = models.ImageField(default="p1.png",upload_to="images2/%y",null=True, blank=True)
    date_created = models.DateTimeField(default=now)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title