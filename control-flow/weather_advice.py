quiz = input ("What's the weather like today? (sunny/rainy/cold): ").lower()

if quiz == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif quiz == "rainy":
    print(" Don't forget your umbrella and a raincoat.")
elif quiz == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
    
