inputs = input("Please enter a string: ")


if(len(inputs) < 6):
    print("Dick is too short")
    print("Call me")
elif(len(inputs) > 6 and len(inputs) < 10):
    print("She is happy")
else:
    print("She is crying or She is African")