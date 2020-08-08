from django.db import models


class News(models.Model):
    url = models.CharField(max_length=256)
    title = models.CharField(max_length=64)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'news'