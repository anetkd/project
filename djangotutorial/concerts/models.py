from django.db import models

class Concert(models.Model):
    artist = models.CharField(max_length=100)  # Исполнитель
    date = models.DateTimeField()               # Дата и время концерта
    venue = models.CharField(max_length=200)    # Место проведения
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена билета

    def __str__(self):
        return f"{self.artist} - {self.date.strftime('%Y-%m-%d %H:%M')}"

