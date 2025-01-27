from django.urls import path
from . import views
urlpatterns=[
    path('',views.movie_list,name='movie_list'),
    path('<int:movie_id>/theaters',views.theater_list,name='theater_list'),
    path('theater/<str:theater_id>/seats/book/',views.book_seats,name='book_seats'),
      path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]