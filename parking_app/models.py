from django.db import models

class Parking(models.Model):

    state = models.CharField(max_length=4)
    vehicle_no = models.CharField(max_length=6, unique=True)
    vehicle_type = models.CharField(max_length=5)
    park_time = models.TimeField()
    park_date = models.DateField()
    park_price = models.IntegerField(default=20)

    def __str__(self):
        return self.vehicle_no
    
#for demo
class ParkingSpace(models.Model):
    number = models.IntegerField(unique=True)
    x_coordinate = models.IntegerField()
    y_coordinate = models.IntegerField()

    def __str__(self):
        return str(self.number)

class ParkingSlot(models.Model):
    space = models.ForeignKey(ParkingSpace, on_delete=models.CASCADE)
    slot_number = models.CharField(max_length=50, unique=True)
    is_vacant = models.BooleanField(default=True)

    def __str__(self):
        return f"Slot {self.slot_number} - Parking Space {self.space.number}"

class Distance(models.Model):
    source = models.ForeignKey(ParkingSpace, related_name='distances_from', on_delete=models.CASCADE)
    destination = models.ForeignKey(ParkingSpace, related_name='distances_to', on_delete=models.CASCADE)
    distance = models.FloatField()

    def __str__(self):
        return f'Distance from {self.source} to {self.destination}: {self.distance}'