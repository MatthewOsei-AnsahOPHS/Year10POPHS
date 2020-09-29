q1=input("Is it raining ").lower()
q2=input("Is it windy? ").lower()

if q1==("yes") and q2==("yes"):
    print("It is too windy for an umbrella")

elif q1==("yes") and q2==("no"):
    print("You should probally take an umbrella today")

elif q1==("no") and q2==("yes"):
    print("Take caution when travelling it is going to be very windy")

else:
    print("Enjoy your day")
