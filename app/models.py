from django.db import models

#Definiujemy modele dla naszej DB
class Article (models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title

class Comment (models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    article = models.ForeignKey("Article",on_delete=models.CASCADE) 

    def __str__(self):
        return self.title
