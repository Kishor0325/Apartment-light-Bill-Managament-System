from django.db import models

# Create your models here.
class Bill(models.Model):
    apartment_number = models.CharField(max_length=10)
    resident_name = models.CharField(max_length=100)
    units_consumed = models.PositiveIntegerField()
    bill_date = models.DateField()
    
    PER_UNIT_RATE = 5  # ₹5 per unit
    
    @property
    def total_bill(self):
        return self.units_consumed * self.PER_UNIT_RATE

    def __str__(self):
        return f"Apt {self.apartment_number} - {self.resident_name}"