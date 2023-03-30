from django.db import models

# Weak entity
class Amount(models.Model):
    unities = models.IntegerField()

    def __str__(self):
        return self.unities

class Country(models.Model):
    id_country = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    # Available sanctuaries in the country

    def __str__(self):
        return self.name
    

class Sanctuary(models.Model):
    id_sanctuary = models.AutoField(primary_key=True)
    fk_amount = models.ForeignKey(Amount, on_delete=models.CASCADE)
    fk_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name