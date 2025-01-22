def check_weather(temperature):
    if temperature >= 25:
        return "Det er varmt."
    elif temperature == 10 and temperature < 25:
        return "Det er mildt."
    elif temperature == 0 and temperature < 10:
        return "Det er kjølig."
    else:
        return "Det er kaldt."

print(check_weather(15))
