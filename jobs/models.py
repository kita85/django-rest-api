from django.db import models


class Job(models.Model):
    batch_number = models.IntegerField()
    submitted_at = models.DateTimeField(blank=True, null=True)
    nodes_used = models.IntegerField(null=True)
