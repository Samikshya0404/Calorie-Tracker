from django.db import models

class CalorieEntry(models.Model):
    date = models.DateField()
    meal = models.CharField(max_length=100)
    calorie_count = models.PositiveIntegerField()
