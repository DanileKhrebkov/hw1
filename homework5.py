
def add_product(inventory, product_id, name, category, price, quantity):
    if product_id in inventory:  
        inventory[product_id]["quantity"] += quantity  
    else:
        inventory[product_id] = {
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity
        }


def remove_product(inventory, product_id):

    if product_id in inventory:  
        del inventory[product_id]  
    else:
        print(f"Ошибка: Товар с ID {product_id} не существует.")


def update_quantity(inventory, product_id, quantity):
    if product_id in inventory:  
        if quantity <= 0: 
            del inventory[product_id]
        else: 
            inventory[product_id]["quantity"] = quantity
    else:
        print(f"Ошибка: Товар с ID {product_id} не существует.")


def get_unique_categories(inventory):
    return {product["category"] for product in inventory.values()}

inventory = {
    101: {"name": "Смартфон", "category": "Электроника", "price": 29999, "quantity": 50},
    102: {"name": "Ноутбук", "category": "Электроника", "price": 54999, "quantity": 30},
    103: {"name": "Кофеварка", "category": "Бытовая техника", "price": 7999, "quantity": 20},
}




add_product(inventory, 104, "Телевизор", "Электроника", 45000, 15)
remove_product(inventory, 101)
update_quantity(inventory, 102, 25)
categories = get_unique_categories(inventory)
print(categories)
