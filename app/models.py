from django.db import models

#Definiujemy modele dla naszej DB
class Post (models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title

class Comment (models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    post = models.ForeignKey("Post",on_delete=models.CASCADE) 

    def __str__(self):
        return self.title
