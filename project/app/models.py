from django.db import models
from datetime import datetime



class video(models.Model):
    title= models.CharField(max_length=30)
    description = models.TextField(max_length=30)
    image = models.ImageField(upload_to="images/")
    datetime= models.DateTimeField(default=datetime.now)
    video= models.FileField(upload_to="videos/")


    def _str_(self):
     return self.tittle
    
    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos' 


 



