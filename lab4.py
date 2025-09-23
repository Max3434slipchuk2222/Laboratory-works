store = {
    "телефон": 10000.00,
    "зубна щітка": 91.50,
    "банан": 44.12,
    "чай": 120.00,
    "зошит": 31.30,
    "ручка": 10.00
}


def convertator(price):
    return f'ціна: {price:.2f} грн'
def availability(*products):
    result = {}
    for product in products:
        result[product] = product in store
    return result
def check_order(order, option):
    if not order:
        return "Немає товарів у замовленні."
    not_available = []
    for product in order:
        if product not in store:
            not_available.append(product)
    if not_available:
        return f"Данних товарів немає у наявності: {', '.join(not_available)}"
        
    total = 0
    for product in order:
        total += store[product]

    if option == "price":
        return "Загальна " + convertator(total)
    elif option == "buy":
        return "Ви купили " + ", ".join(order) + " " + convertator(total)
    else:
        return "Ви вказали невідому опцію"
        
print(convertator(100))
print(convertator(23.98763))  
print(convertator(83282.2))  

print(availability("хліб", "чай", "робот", "ручка"))

print(check_order(["чай", "зубна щітка"], "price"))

print(check_order(["телефон", "зубна щітка"], "buy"))

print(check_order(["телефон", "кетчуп"], "buy"))
        
        
        
