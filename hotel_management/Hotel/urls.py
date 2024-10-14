from django.urls import path
from . import views

urlpatterns = [
    path('', views.HotelListView.as_view(), name='hotel_list'),
    path('<int:pk>/', views.HotelDetailView.as_view(), name='hotel_detail'),
    path('create/', views.HotelCreateView.as_view(), name='hotel_create'),
    path('update/<int:pk>/', views.HotelUpdateView.as_view(), name='hotel_update'),
    path('delete/<int:pk>/', views.HotelDeleteView.as_view(), name='hotel_delete'),

    # Room URLs
    path('rooms/', views.RoomListView.as_view(), name='room_list'),
    path('rooms/<int:pk>/', views.RoomDetailView.as_view(), name='room_detail'),
    path('rooms/create/<int:hotel_id>/', views.RoomCreateView.as_view(), name='room_create'),
    path('rooms/update/<int:pk>/', views.RoomUpdateView.as_view(), name='room_update'),
    path('rooms/delete/<int:pk>/', views.RoomDeleteView.as_view(), name='room_delete'),

    # Reservation URLs
    path('reservations/', views.ReservationListView.as_view(), name='reservation_list'),
    path('reservations/<int:pk>/', views.ReservationDetailView.as_view(), name='reservation_detail'),

    # Payment URLs
    path('payments/', views.PaymentListView.as_view(), name='payment_list'),
    path('payments/<int:pk>/', views.PaymentDetailView.as_view(), name='payment_detail'),

    # Expense URLs
    path('expenses/', views.ExpenseListView.as_view(), name='expense_list'),
    path('expenses/<int:pk>/', views.ExpenseDetailView.as_view(), name='expense_detail'),

    # Income URLs
    path('incomes/', views.IncomeListView.as_view(), name='income_list'),
    path('incomes/<int:pk>/', views.IncomeDetailView.as_view(), name='income_detail'),

    # Budget URLs
    path('budgets/', views.BudgetListView.as_view(), name='budget_list'),
    path('budgets/<int:pk>/', views.BudgetDetailView.as_view(), name='budget_detail'),
]