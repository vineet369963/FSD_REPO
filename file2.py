# Temperature check
temp = float(input("Enter temperature in °C: "))
if temp < 15:
    print("Cold")
elif 15 <= temp <= 25:
    print("Warm")
else:
    print("Hot")
