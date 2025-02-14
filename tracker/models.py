from django.db import models

# Create your models here.

class HealthRecord(models.Model):
    date = models.DateField(unique=True)
    weight = models.FloatField(null=True, blank=True)
    temperature = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    menstruation = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.date} - Weight: {self.weight}kg, temperature: {self.temperature}°C"