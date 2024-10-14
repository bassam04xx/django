from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Hotel, Room, Reservation, Payment, Expense, Income, Budget

# Hotel Views
class HotelListView(ListView):
    model = Hotel
    template_name = 'hotel/hotel_list.html'
    context_object_name = 'hotels'

class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'hotel/hotel_detail.html'
    context_object_name = 'hotel'

class HotelCreateView(CreateView):
    model = Hotel
    fields = ['name', 'address', 'capacity']
    template_name = 'hotel/hotel_form.html'
    success_url = reverse_lazy('hotel_list')

class HotelUpdateView(UpdateView):
    model = Hotel
    fields = ['name', 'address', 'capacity']
    template_name = 'hotel/hotel_form.html'
    success_url = reverse_lazy('hotel_list')

class HotelDeleteView(DeleteView):
    model = Hotel
    template_name = 'hotel/hotel_confirm_delete.html'
    success_url = reverse_lazy('hotel_list')

# Room Views
class RoomListView(ListView):
    model = Room
    template_name = 'room/room_list.html'
    context_object_name = 'rooms'

class RoomDetailView(DetailView):
    model = Room
    template_name = 'room/room_detail.html'
    context_object_name = 'room'

class RoomCreateView(CreateView):
    model = Room
    fields = ['number', 'type', 'rate']  # Ensure 'hotel' is not in fields here
    template_name = 'room/room_form.html'

    def form_valid(self, form):
        hotel_id = self.kwargs['hotel_id']
        form.instance.hotel = get_object_or_404(Hotel, id=hotel_id)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('hotel_detail', kwargs={'pk': self.kwargs['hotel_id']})
class RoomUpdateView(UpdateView):
    model = Room
    fields = ['number', 'type', 'rate', 'hotel_id']
    template_name = 'room/room_form.html'
    success_url = reverse_lazy('room_list')

class RoomDeleteView(DeleteView):
    model = Room
    template_name = 'room/room_confirm_delete.html'
    success_url = reverse_lazy('room_list')
# Reservation Views
class ReservationListView(ListView):
    model = Reservation
    template_name = 'reservation/reservation_list.html'
    context_object_name = 'reservations'

class ReservationDetailView(DetailView):
    model = Reservation
    template_name = 'reservation/reservation_detail.html'
    context_object_name = 'reservation'

# Payment Views
class PaymentListView(ListView):
    model = Payment
    template_name = 'payment/payment_list.html'
    context_object_name = 'payments'

class PaymentDetailView(DetailView):
    model = Payment
    template_name = 'payment/payment_detail.html'
    context_object_name = 'payment'

# Expense Views
class ExpenseListView(ListView):
    model = Expense
    template_name = 'expense/expense_list.html'
    context_object_name = 'expenses'

class ExpenseDetailView(DetailView):
    model = Expense
    template_name = 'expense/expense_detail.html'
    context_object_name = 'expense'

# Income Views
class IncomeListView(ListView):
    model = Income
    template_name = 'income/income_list.html'
    context_object_name = 'incomes'

class IncomeDetailView(DetailView):
    model = Income
    template_name = 'income/income_detail.html'
    context_object_name = 'income'

# Budget Views
class BudgetListView(ListView):
    model = Budget
    template_name = 'budget/budget_list.html'
    context_object_name = 'budgets'

class BudgetDetailView(DetailView):
    model = Budget
    template_name = 'budget/budget_detail.html'
    context_object_name ='budget'