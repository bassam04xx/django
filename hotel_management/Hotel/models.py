from django.db import models

# Create your models here.
class Hotel(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=255)
    address = models.TextField()
    capacity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

class Room(models.Model):
    ROOM_TYPES =[
        ('standard', 'Standard'),
        ('deluxe', 'Deluxe'),
        ('suite', 'Suite'),
    ]
    id = models.AutoField(primary_key=True)
    number =models.IntegerField(blank=False)
    type = models.CharField(
        max_length=10, 
        choices=ROOM_TYPES,
        default='standard',)
    rate = models.DecimalField(max_digits=10,decimal_places=2)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')


    def __str__(self):
        return self.number
class Guest(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)  # Optional email field
    phone_number = models.CharField(max_length=20, blank=True)  # Optional phone number

    def __str__(self):
        return self.name

class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='reservations')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations') 
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # ... other fields and methods

    def __str__(self):
        return f"Reservation {self.id} for {self.guest.name}"

    def calculate_total_amount(self):
        # Assuming some calculation logic here, including room rate, duration, etc.
        # Example:
        duration = (self.check_out_date - self.check_in_date).days
        self.total_amount = self.room.rate * duration
        self.save()  # Update the total_amount field

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    reservation = models.ForeignKey(
        Reservation,
        on_delete=models.CASCADE,
        related_name='payments'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment {self.id} for Reservation {self.reservation}"
    

class Expense(models.Model):
    id = models.AutoField(primary_key=True)
    CATEGORY_CHOICES = [
        ('utilities', 'Utilities'),
        ('salaries', 'Salaries'),
        ('maintenance', 'Maintenance'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
    rooms = models.ManyToManyField(Room, related_name='expenses', blank=True)

    def __str__(self):
        return f"Expense {self.id} - {self.category}"


class Income(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"Income {self.id} - {self.source}"


class Budget(models.Model):
    id = models.AutoField(primary_key=True)
    PERIOD_CHOICES = [
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    ]
    period = models.CharField(max_length=50, choices=PERIOD_CHOICES)
    expense_budget = models.DecimalField(max_digits=10, decimal_places=2)
    income_budget = models.DecimalField(max_digits=10, decimal_places=2)
    expenses = models.ManyToManyField(Expense, related_name='budgets', blank=True)
    incomes = models.ManyToManyField(Income, related_name='budgets', blank=True)

    def __str__(self):
        return f"Budget {self.id} for {self.period}"