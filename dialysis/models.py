from django.db import models


class DialysisRecord(models.Model):

    date = models.DateField()
    patient_id = models.CharField(max_length=20)
    name = models.CharField(max_length=50)

    weight = models.FloatField()
    dw = models.FloatField()
    time = models.FloatField()

    uf = models.FloatField()
    rate = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
