from django.db import models

class LandOwner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    registered_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class LandRecord(models.Model):
    owner = models.ForeignKey(LandOwner, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    size_in_acres = models.DecimalField(max_digits=10, decimal_places=4)
    land_type = models.CharField(max_length=100, choices=[('Residential', 'Residential'), ('Commercial', 'Commercial')])
    price = models.FloatField()
    image = models.ImageField(upload_to='land_images/', null=True, blank=True)
    purchase_date = models.DateField()

    def __str__(self):
        return f"{self.location} - {self.size_in_acres} acres"
