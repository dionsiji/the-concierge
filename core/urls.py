from django.urls import path
from . import views

urlpatterns = [
    path('', views.loading, name='loading'),
    path('home/', views.landing, name='landing'),
    path('restaurant/<int:id>/', views.restaurant_detail, name='restaurant_detail'),
    path('restaurant/<int:restaurant_id>/menu/', views.public_menu, name='public_menu'),
    path('book/<int:restaurant_id>/', views.book_seats, name='book_seats'),
    path('api/tables/<int:restaurant_id>/', views.get_tables, name='get_tables'),
    path('menu/<int:reservation_id>/', views.menu, name='menu'),
    path('confirm_booking/', views.confirm_booking, name='confirm_booking'),
    path('save_preorder/<int:reservation_id>/', views.save_preorder, name='save_preorder'),
    
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('concierge-admin/', views.admin_dashboard, name='admin_dashboard'),
]
