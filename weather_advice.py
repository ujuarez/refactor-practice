def weather_advice(weather):
    weather = "rainy"
    if weather == "rainy":
        print("Take an umbrella.")
    elif weather == "sunny":
        print("Wear sunglasses.")
    elif weather == "cold":
        print("Wear a jacket.")
    else:
        print("Weather unknown. Dress comfortably.")