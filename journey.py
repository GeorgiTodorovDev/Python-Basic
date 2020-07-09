budget = float(input())
season = input()

total_price = 0.0
room_type = ""
destination = ""

"""    
• При 100 лв. или по-малко – някъде в България:
        ◦ Лято – 30% от бюджета;
        ◦ Зима – 70% от бюджета.
    • При 1000 лв. или по малко – някъде на Балканите:
        ◦ Лято – 40% от бюджета;
        ◦ Зима – 80% от бюджета.
    • При повече от 1000 лв. – някъде из Европа:
        ◦ При пътуване из Европа, независимо от сезона, ще похарчи 90% от бюджета.
    
    Ако е лято ще почива на къмпинг, а зимата в хотел. Ако е в Европа, независимо от сезона, ще почива в хотел.
    
    • "Somewhere in [дестинация]" измежду "Bulgaria", "Balkans" и "Europe"
    • "{Вид почивка} – {Похарчена сума}":
        ◦ Почивката може да е между "Camp" и "Hotel";
        ◦ Сумата трябва да е закръглена с точност до вторият знак след запетаята.
"""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        total_price = budget * 0.30
    else:
        total_price = budget * 0.70
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        total_price = budget * 0.40
    else:
        total_price = budget * 0.80
else:
    destination = "Europe"
    total_price = budget * 0.90

if season == "summer" and (not destination == "Europe"):
    room_type = "Camp"
else:
    room_type = "Hotel"

print(f'Somewhere in {destination}\n{room_type} - {total_price:.2f}')