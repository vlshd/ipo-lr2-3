import math
volume = float(input("Введите объем шара: "))
radius = ((3 * volume) / (4 * math.pi)) ** (1/3)
print(f"Радиус шара: {radius} единиц")