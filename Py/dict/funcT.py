def mark ():
    market = {}
    value =0
    num = int(input("How much supplies you want to buy: "))
    for i in range(num):
        prod = input(f"The {i+1} item ? : ")
        market[prod] = int(input(f"\n The price of the {i+1} item : "))
    for value in market.values():
        value =+ value
    print(f"The totale is {value}")

