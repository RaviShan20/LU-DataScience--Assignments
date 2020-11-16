cost_price=int(input())
selling_price=int(input())
if selling_price > cost_price:
    print("Profit")
elif selling_price < cost_price:
    print("Loss")
else:
    print("Neither")
