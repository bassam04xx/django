from django.contrib import admin
from .models import Hotel, Room, Reservation, Payment, Expense, Income, Budget

admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(Payment)
admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(Budget)
