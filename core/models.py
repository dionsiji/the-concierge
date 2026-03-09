from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    theme = models.CharField(max_length=200)
    cuisine = models.CharField(max_length=200)
    image = models.ImageField(upload_to='restaurants/', null=True, blank=True)

    def __str__(self):
        return self.name

class RestaurantImage(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='restaurants/')

    def __str__(self):
        return f"Image for {self.restaurant.name}"

class Table(models.Model):
    TABLE_TYPES = (
        ('standard', 'Standard Table'),
        ('window', 'Window Table'),
        ('premium', 'Premium Table'),
        ('private', 'Private Dining Table'),
    )
    
    DEMAND_LEVELS = (
        ('low', 'Low'),
        ('normal', 'Normal'),
        ('high', 'High'),
    )

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='tables')
    table_number = models.CharField(max_length=20)
    table_type = models.CharField(max_length=20, choices=TABLE_TYPES, default='standard')
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_booked = models.BooleanField(default=False)
    demand_level = models.CharField(max_length=20, choices=DEMAND_LEVELS, default='normal')

    def __str__(self):
        return f"{self.restaurant.name} - Table {self.table_number} ({self.get_table_type_display()})"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    people_count = models.IntegerField()
    booking_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation for {self.user.username} at {self.restaurant.name} on {self.date}"

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu_items/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.restaurant.name})"

class PreOrder(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='preorders')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity}x {self.menu_item.name} for {self.reservation.user.username}"
