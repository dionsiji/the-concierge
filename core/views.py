import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal
from .models import Restaurant, Table, Reservation, MenuItem, PreOrder
from django.contrib import messages

def loading(request):
    return render(request, 'loading.html')

def landing(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'landing.html', {'restaurants': restaurants})

def restaurant_detail(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    return render(request, 'restaurant_detail.html', {'restaurant': restaurant})

def public_menu(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    menu_items = restaurant.menu_items.all()
    categories = list(set([item.category for item in menu_items]))
    return render(request, 'public_menu.html', {
        'restaurant': restaurant,
        'menu_items': menu_items,
        'categories': categories,
    })

@login_required
def book_seats(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    return render(request, 'book_seats.html', {'restaurant': restaurant})

@login_required
def get_tables(request, restaurant_id):
    tables = Table.objects.filter(restaurant_id=restaurant_id)
    tables_data = []
    for t in tables:
        tables_data.append({
            'id': t.id,
            'table_number': t.table_number,
            'type': t.table_type,
            'capacity': t.capacity,
            'price': str(t.price),
            'is_booked': t.is_booked,
            'demand_level': t.demand_level,
        })
    return JsonResponse({'tables': tables_data})

@login_required
@csrf_exempt
def confirm_booking(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        restaurant_id = data.get('restaurant_id')
        table_id = data.get('table_id')
        people = data.get('people')
        date = data.get('date')
        time = data.get('time')
        price = data.get('price')

        if Reservation.objects.filter(user=request.user, date=date).exists():
            return JsonResponse({'success': False, 'message': 'You already have another reservation at that time so unable to proceed with your request. Perhaps choose a different date or timing?'})

        table = get_object_or_404(Table, id=table_id)
        if table.is_booked:
            return JsonResponse({'success': False, 'message': 'Table already booked!'})
        
        table.is_booked = True
        table.save()

        reservation = Reservation.objects.create(
            user=request.user,
            restaurant_id=restaurant_id,
            table=table,
            date=date,
            time=time,
            people_count=people,
            booking_price=Decimal(price)
        )

        return JsonResponse({'success': True, 'reservation_id': reservation.id})
    return JsonResponse({'success': False})

@login_required
def menu(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    menu_items = reservation.restaurant.menu_items.all()
    categories = list(set([item.category for item in menu_items]))
    
    return render(request, 'menu.html', {
        'reservation': reservation,
        'menu_items': menu_items,
        'categories': categories,
    })

@login_required
@csrf_exempt
def save_preorder(request, reservation_id):
    if request.method == 'POST':
        reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
        data = json.loads(request.body)
        cart = data.get('cart', [])

        for item in cart:
            try:
                mi = MenuItem.objects.get(id=item['id'])
                PreOrder.objects.create(
                    reservation=reservation,
                    menu_item=mi,
                    quantity=item['quantity']
                )
            except MenuItem.DoesNotExist:
                continue

        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def user_login(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'landing')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone') # we can store phone in profile, but mostly using basic User
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = phone  # hack: storing phone in first_name for simplicity
            user.save()
            login(request, user)
            return redirect('landing')
    return render(request, 'signup.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('landing')

@login_required
def profile(request):
    reservations = Reservation.objects.filter(user=request.user).order_by('-date', '-time')
    return render(request, 'profile.html', {'reservations': reservations})

@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('landing')
    
    reservations = Reservation.objects.all().order_by('-date', '-time')
    restaurants = Restaurant.objects.all()
    
    # Simple stats
    total_res = reservations.count()
    today_res = reservations.filter(date=Decimal('2026-03-04') if False else '2026-03-04').count() # Mocking today for now
    
    return render(request, 'admin_dashboard.html', {
        'reservations': reservations,
        'restaurants': restaurants,
        'total_res': total_res,
        'today_res': today_res
    })
