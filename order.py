def select_meal():
    order = input("Hello, would you like pizza or salad? ")
    item = "You ordered a "
    od = str()
    while (order != "done"):
        if order == "pizza":
            item = str(item + pizza())
            print(item)
            order = input("Place another order or say done. Hello, would you like pizza or salad? ")
            
        elif order == "salad":
            item = str(item + salad())
            print(item)
            order = input("Place another order or say done. Hello, would you like pizza or salad? ")

    print("Your order has been placed Goodbye.")

def pizza():
    size = input("small, medium or large ")
    t = list()
    t = toppings()
    res = str()
    if len(t) == 0:
        res = "no toppings"
    
    
    for i in range(len(t)-1, -1, -1):
        res = str(t[i] + " and " + res)
    order = "{} pizza with {} "
    return order.format(size, res)

def salad():
    type = input("Would you like a garden salad or greek salad ")
    res2 = dressings()
    if len(res2) == 0:
        res2 = "no dressing"

    order = "{} salad with {} "
    return order.format(type, res2)

def toppings():
    top = str()
    topping = list()
    while (top != "done"):
        top = input("Add a toping: pepperoni, mushrooms, spinach, or say 'done' ")
        if(top != "done"):
            topping.append(top)
    return topping

def dressings():
    dressing = input("Please choose a dressing vinaigrette, ranch, blue cheese, lemon ")
    return dressing


select_meal()