from django.db import models

#Definiujemy modele dla naszej DB
class Post (models.Model):
    title = models.CharField()
    content = models.TextField()

    def __str__(self):
        return self.title

class Comment (models.Model):
    title = models.CharField()
    content = models.TextField()

    def __str__(self):
        return self.title
