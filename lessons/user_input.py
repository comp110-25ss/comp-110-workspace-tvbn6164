"""Practice user input, elif, and variable assignment."""

forcast: str = input("What is the weather?")
forcast = input("Double checking.... what is the weather?")
hot_day: str = "sunny"
if forcast == "rainy":
    print("Bring a jacket!")
elif forcast == hot_day:
    print("Bring sunglasses!")
else:
    print("I don't have any advice for you. :)")
