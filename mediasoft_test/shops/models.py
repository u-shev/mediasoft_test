from django.db import models


class City(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(max_length=150)
    city = models.ForeignKey(City, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=150)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    street = models.ForeignKey(Street, on_delete=models.PROTECT)
    house = models.PositiveIntegerField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.name
