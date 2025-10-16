import os

customers = []
smallPizza = 3.00
largePizza = 5.00

def pizzaFunc(quantity,size):
    if size == "large":
        cost = round(largePizza * quantity,2)
        print(f"Your total is ${cost}.")
        return cost
    elif size == "small":
        cost = round(smallPizza * quantity,2)
        print(f"Your total is ${cost}.")
        return cost

print("Daniels Dodgy Pizza")

while True:
    try:
        quantity = int(input("How many pizzas would u like?"))
        if quantity <= 0:
            print("Please enter a positive number!")
            continue 
    except ValueError:
        print("Enter nmumerical values only")
        continue 

    size = input("What size pizza would u like?(Small Large)").strip().lower()

    pizzaFunc(quantity,size)

    name = input("What is the name of this order?")
    customers.append([name,size,quantity])
    
    f = open("Customers.txt", "w")
    f.write(str(customers))
    f.close()
    break











    


    



