from django.contrib import admin
from .models import Restaurant, Table, Reservation, MenuItem, PreOrder

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'cuisine', 'theme')

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'table_number', 'table_type', 'capacity', 'price', 'is_booked')
    list_filter = ('restaurant', 'is_booked', 'table_type')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'restaurant', 'date', 'time', 'table', 'people_count', 'booking_price', 'created_at')
    list_filter = ('date', 'restaurant')
    search_fields = ('user__username', 'restaurant__name')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'category', 'price')
    list_filter = ('restaurant', 'category')

@admin.register(PreOrder)
class PreOrderAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'menu_item', 'quantity')
