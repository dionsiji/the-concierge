import os
from django.core.management.base import BaseCommand
from django.core.files import File
from core.models import Restaurant, Table, MenuItem

class Command(BaseCommand):
    help = 'Seeds the database with initial restaurants, tables, and menu items'

    def handle(self, *args, **kwargs):
        # Clean current if needed
        Restaurant.objects.all().delete()

        r1 = Restaurant.objects.create(
            name='The Capital',
            location='Trivandrum',
            description='Luxury 5-star hotel restaurant serving authentic Kerala cuisine.',
            theme='Royal heritage hotel + fine dining',
            cuisine='Kerala Special'
        )
        try:
            r1.image.save('the_capital.png', File(open(r"C:\Users\Dion\.gemini\antigravity\brain\0f8a97b1-c1dd-4a1b-b5a1-a820a3140cf8\the_capital_hotel_1772602359907.png", 'rb')))
        except: pass

        r2 = Restaurant.objects.create(
            name='The Horizon',
            location='Varkala Beach',
            description='Beach-view fine dining with indoor + ocean-facing experience.',
            theme='Oceanic / beach view',
            cuisine='Seafood + Indian'
        )
        try:
            r2.image.save('the_horizon.png', File(open(r"C:\Users\Dion\.gemini\antigravity\brain\0f8a97b1-c1dd-4a1b-b5a1-a820a3140cf8\the_horizon_hotel_1772602388341.png", 'rb')))
        except: pass

        r3 = Restaurant.objects.create(
            name='The Continental',
            location='Calicut',
            description='Premium standalone restaurant offering international cuisines.',
            theme='Modern fine dining',
            cuisine='Multi-cuisine'
        )
        try:
            r3.image.save('the_continental.png', File(open(r"C:\Users\Dion\.gemini\antigravity\brain\0f8a97b1-c1dd-4a1b-b5a1-a820a3140cf8\the_continental_hotel_1772602440700.png", 'rb')))
        except: pass

        self.stdout.write('Created 3 Restaurants.')

        # Seeding Tables based on specific restaurant requirements
        self.stdout.write('Seeding tailored tables...')
        
        # 1. The Capital: 20% 2s, 60% 4s, 20% 6-8s (No window)
        # 50 tables total
        for i in range(1, 11): # 10 tables (20%)
            demand = 'high' if i <= 3 else 'low'
            Table.objects.create(restaurant=r1, table_number=str(i), table_type='standard', capacity=2, price=2000, demand_level=demand)
        for i in range(11, 41): # 30 tables (60%)
            demand = 'high' if i >= 35 else 'normal'
            Table.objects.create(restaurant=r1, table_number=str(i), table_type='standard', capacity=4, price=3000, demand_level=demand)
        for i in range(41, 46): # 5 tables (10%)
            Table.objects.create(restaurant=r1, table_number=str(i), table_type='premium', capacity=6, price=5000, demand_level='high')
        for i in range(46, 51): # 5 tables (10%)
            Table.objects.create(restaurant=r1, table_number=str(i), table_type='private', capacity=8, price=8000, demand_level='high')

        # 2. The Horizon: 40% 2s (Beach View + Normal), 60% 4s
        # 50 tables total
        for i in range(1, 11): # 10 tables (20%) Beach View 2-seater
            Table.objects.create(restaurant=r2, table_number=str(i), table_type='window', capacity=2, price=4000, demand_level='high')
        for i in range(11, 21): # 10 tables (20%) Normal 2-seater
            demand = 'high' if i >= 18 else 'normal'
            Table.objects.create(restaurant=r2, table_number=str(i), table_type='standard', capacity=2, price=2500, demand_level=demand)
        for i in range(21, 51): # 30 tables (60%) 4-seater
            demand = 'high' if i % 5 == 0 else 'normal'
            Table.objects.create(restaurant=r2, table_number=str(i), table_type='standard', capacity=4, price=3500, demand_level=demand)

        # 3. The Continental: 15% 2s, 50% 4s, 35% 6-8s (40% window)
        # 50 tables total. 40% window = 20 tables.
        # 2-seaters (15% of 50 = 8 tables): 4 Window, 4 Standard
        for i in range(1, 5):
            Table.objects.create(restaurant=r3, table_number=str(i), table_type='window', capacity=2, price=4500, demand_level='high')
        for i in range(5, 9):
            Table.objects.create(restaurant=r3, table_number=str(i), table_type='standard', capacity=2, price=2800, demand_level='normal')
        # 4-seaters (50% of 50 = 25 tables): 10 Window, 15 Standard
        for i in range(9, 19):
            Table.objects.create(restaurant=r3, table_number=str(i), table_type='window', capacity=4, price=5500, demand_level='high')
        for i in range(19, 34):
            demand = 'high' if i % 4 == 0 else 'normal'
            Table.objects.create(restaurant=r3, table_number=str(i), table_type='standard', capacity=4, price=3800, demand_level=demand)
        # 6-8-seaters (35% of 50 = 17 tables): 6 Window (all 6s), 6 Standard 6s, 5 Private 8s
        for i in range(34, 40):
            Table.objects.create(restaurant=r3, table_number=str(i), table_type='window', capacity=6, price=7000, demand_level='high')
        for i in range(40, 46):
            Table.objects.create(restaurant=r3, table_number=str(i), table_type='premium', capacity=6, price=6000, demand_level='high')
        for i in range(46, 51):
            Table.objects.create(restaurant=r3, table_number=str(i), table_type='private', capacity=8, price=9500, demand_level='high')

        self.stdout.write('Created Tables.')

        # Menu Items for The Capital (Kerala)
        MenuItem.objects.create(restaurant=r1, name='Karimeen Pollichathu', category='Mains', description='Pearl spot fish marinated in Kerala spices and wrapped in banana leaf.', price=1200)
        MenuItem.objects.create(restaurant=r1, name='Appam & Mutton Stew', category='Mains', description='Soft rice hoppers with rich coconut milk and mutton.', price=850)
        MenuItem.objects.create(restaurant=r1, name='Thalassery Biryani', category='Mains', description='Fragrant short-grain rice cooked with spiced chicken.', price=650)
        MenuItem.objects.create(restaurant=r1, name='Kerala Beef Roast', category='Mains', description='Slow-roasted beef with coconut slices and curry leaves.', price=750)
        MenuItem.objects.create(restaurant=r1, name='Malabar Fish Curry', category='Mains', description='Tangy fish curry made with kokum and coconut milk.', price=900)
        MenuItem.objects.create(restaurant=r1, name='Parippu Vada', category='Starters', description='Crispy lentil fritters.', price=300)
        MenuItem.objects.create(restaurant=r1, name='Chicken 65', category='Starters', description='Spicy, deep-fried chicken prepared with red chilies and yogurt.', price=450)
        MenuItem.objects.create(restaurant=r1, name='Palada Payasam', category='Desserts', description='Classic sweet milk pudding with rice flakes.', price=400)
        MenuItem.objects.create(restaurant=r1, name='Vattayappam', category='Desserts', description='Steamed rice cake sweetened with jaggery and coconut.', price=350)
        
        # Add Drinks
        MenuItem.objects.create(restaurant=r1, name='Kulukk Sarbath', category='Beverages', description='Traditional shaken lemonade with sweet basil seeds.', price=150)
        MenuItem.objects.create(restaurant=r1, name='Filter Coffee', category='Beverages', description='Authentic South Indian strong coffee.', price=200)

        # Menu Items for The Horizon (Seafood)
        MenuItem.objects.create(restaurant=r2, name='Lobster Thermidor', category='Mains', description='Creamy lobster meat stuffed back into the shell, baked with cheese.', price=3500)
        MenuItem.objects.create(restaurant=r2, name='Grilled Jumbo Prawns', category='Mains', description='Fresh sea prawns grilled with garlic butter.', price=2200)
        MenuItem.objects.create(restaurant=r2, name='Seafood Risotto', category='Mains', description='Italian rice dish cooked with mixed oceanic seafood.', price=1800)
        MenuItem.objects.create(restaurant=r2, name='Pan-Seared Scallops', category='Mains', description='Fresh scallops perfectly seared with lemon butter sauce.', price=2600)
        MenuItem.objects.create(restaurant=r2, name='Calamari Rings', category='Starters', description='Crispy fried squid rings with tartar sauce.', price=800)
        MenuItem.objects.create(restaurant=r2, name='Crab Cakes', category='Starters', description='Lump crab meat cakes with signature remoulade.', price=1200)
        MenuItem.objects.create(restaurant=r2, name='Ocean Sky Mousse', category='Desserts', description='Blueberry and vanilla layered mousse.', price=600)
        MenuItem.objects.create(restaurant=r2, name='Lemon Tart', category='Desserts', description='Zesty lemon filling in a buttery pastry crust.', price=550)
        
        MenuItem.objects.create(restaurant=r2, name='Blue Lagoon Mocktail', category='Beverages', description='Refreshing blue curacao and lemonade blend.', price=400)
        MenuItem.objects.create(restaurant=r2, name='Sparkling Water', category='Beverages', description='Premium imported sparkling water.', price=250)

        # Menu Items for The Continental (Multi-cuisine)
        MenuItem.objects.create(restaurant=r3, name='Wagyu Beef Steak', category='Mains', description='Premium Japanese wagyu cooked to perfection.', price=6000)
        MenuItem.objects.create(restaurant=r3, name='Truffle Pasta', category='Mains', description='Handmade pasta with black truffle shavings.', price=2400)
        MenuItem.objects.create(restaurant=r3, name='Herb-Crusted Rack of Lamb', category='Mains', description='New Zealand lamb served with mint jus and roasted vegetables.', price=4200)
        MenuItem.objects.create(restaurant=r3, name='Chicken Cordon Bleu', category='Mains', description='Breaded chicken breast stuffed with ham and swiss cheese.', price=1800)
        MenuItem.objects.create(restaurant=r3, name='Sushi Platter', category='Starters', description='Assortment of fresh sashimi and maki rolls.', price=3200)
        MenuItem.objects.create(restaurant=r3, name='Bruschetta', category='Starters', description='Toasted bread topped with tomatoes, garlic, and basil.', price=500)
        MenuItem.objects.create(restaurant=r3, name='French Onion Soup', category='Starters', description='Classic savory soup topped with a gruyere crouton.', price=850)
        MenuItem.objects.create(restaurant=r3, name='Tiramisu', category='Desserts', description='Classic Italian coffee-flavored dessert.', price=750)
        MenuItem.objects.create(restaurant=r3, name='Crème Brûlée', category='Desserts', description='Vanilla custard base with a hardened caramelized sugar crust.', price=800)
        
        MenuItem.objects.create(restaurant=r3, name='Aged Pinot Noir (Glass)', category='Beverages', description='Exquisite red wine imported from France.', price=1500)
        MenuItem.objects.create(restaurant=r3, name='Crafted Mojito', category='Beverages', description='Classic mint and lime crushed cooler.', price=500)

        self.stdout.write('Created Menu Items.')

        # Adding Gallery Images
        from core.models import RestaurantImage
        try:
            ri1 = RestaurantImage.objects.create(restaurant=r1)
            ri1.image.save('the_capital_2.png', File(open(r"C:\Users\Dion\.gemini\antigravity\brain\0f8a97b1-c1dd-4a1b-b5a1-a820a3140cf8\the_capital_2_1772603178783.png", 'rb')))
            ri2 = RestaurantImage.objects.create(restaurant=r1)
            ri2.image.save('the_capital_3.png', File(open(r"C:\Users\Dion\.gemini\antigravity\brain\0f8a97b1-c1dd-4a1b-b5a1-a820a3140cf8\the_capital_3_1772603194835.png", 'rb')))
        except Exception as e:
            self.stdout.write(f"Image 1 setup failed: {e}")

        try:
            ri3 = RestaurantImage.objects.create(restaurant=r2)
            ri3.image.save('the_horizon_2.png', File(open(r"C:\Users\Dion\.gemini\antigravity\brain\0f8a97b1-c1dd-4a1b-b5a1-a820a3140cf8\the_horizon_2_1772603232734.png", 'rb')))
            
            # Since quota exhausted, we reuse main Continental image as Continental 2
            ri4 = RestaurantImage.objects.create(restaurant=r3)
            ri4.image.save('the_continental_2.png', File(open(r"C:\Users\Dion\.gemini\antigravity\brain\0f8a97b1-c1dd-4a1b-b5a1-a820a3140cf8\the_continental_hotel_1772602440700.png", 'rb')))
            
        except Exception as e:
            self.stdout.write(f"Image 2 setup failed: {e}")

        self.stdout.write(self.style.SUCCESS('Successfully seeded database!'))
