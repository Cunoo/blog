from django.db import models

# Create your models here.

class BlogPost(models.Model):
    text = models.CharField(max_length=200) # for store names max length 200
    date_added = models.DateTimeField(auto_now_add=True) # for time when user create a blogPOST

    def __str__(self): # return name of the blogpost
        return self.text

class BlogEntry(models.Model):
    topic = models.ForeignKey(BlogPost, on_delete=models.CASCADE) # on delete tells django when topic is deleted all data connected to topic are deleted too
    textentry = models.TextField() # just normal Text field with unlimited letters
    date_added = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self): #return entry text
        return self.textentry 