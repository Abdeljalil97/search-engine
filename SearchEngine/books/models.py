from django.db import models

class Ieee(models.Model):
    title = models.TextField()
    abstract = models.TextField()
    published_date = models.TextField()
    published_by = models.TextField()
    def __str__(self) -> str:
        return self.title