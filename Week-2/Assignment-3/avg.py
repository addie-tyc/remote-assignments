def avg(data): 
    price = []
    for dic in data["products"]:
        price.append(dic["price"])
    avg_price = round(sum(price)/len(price), 3)
    return avg_price
