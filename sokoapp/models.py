from django.db import models

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
