from django.db import models
from django.utils import timezone

# Create your models here.
class BoastOrRoast(models.Model):
    boast_or_roast = models.BooleanField()
    title = models.CharField(max_length=30)
    post = models.CharField(max_length=280)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    submit_time = models.DateTimeField(default=timezone.now)
    score = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title
    

    def score(self):
        score = self.up_votes - self.down_votes
        return score