def load_inventory():
    with open('inventory.txt', 'r') as file:
        line = file.readlines()
    inventory = {}
    for info in line:
        items = info.split(',')
        tool_name = items[0].strip()
        rental_cost = int(items[2].strip())
        stock = int(items[1].strip())
        replacement_cost = int(items[3].strip())
        inventory[tool_name] = {
            'name': tool_name,
            'rental cost': rental_cost,
            'stock': stock,
            'replacement cost': replacement_cost
        }
    return inventory
