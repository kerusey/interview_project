from django.db import models


class Polls(models.Model):
    topic = models.CharField(max_length=60)
    publication_date = models.DateTimeField('date published')
    expiry_date = models.DateTimeField('date poll expires')
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.topic


class Choice(models.Model):
    question = models.ForeignKey(Polls, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
