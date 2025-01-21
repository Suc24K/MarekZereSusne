def vypocet_bmr(hmotnost, vyska, vek):
    bmr = 66.473 + (13.7516 * hmotnost) + (5.0033 * vyska) - (6.755 * vek)
    return bmr

# Příklad použití
hmotnost = float(input("Zadejte svou hmotnost v kg: "))
vyska = float(input("Zadejte svou výšku v cm: "))
vek = int(input("Zadejte svůj věk v letech: "))

bmr = vypocet_bmr(hmotnost, vyska, vek)
print(f"Váš bazální metabolismus (BMR) je: {bmr:.2f} kcal/den")
