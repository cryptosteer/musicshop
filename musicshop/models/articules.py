from django.db import models


class Articule(models.Model):
    TYPES_ARTICULES = (
        ('CASSETE', 'CASSETE'),
        ('LP', 'LP'),
        ('LP', 'VHS'),
        ('LP', 'DVD')
    )
    name = models.CharField(max_length=25, null=True)
    type = models.CharField(max_length=25,choices=TYPES_ARTICULES)
    genere = models.CharField(max_length=25)
    album =models.CharField(max_length=25)
    artist = models.CharField(max_length=25)
    year = models.DateTimeField()
    value = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.name)




