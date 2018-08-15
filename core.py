def loading_inventory(line):
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


def totals(inventory, tool, rental_rate):
    total = 0
    total = (float(total + inventory[tool]['rental cost'] * 0.07 +
                   inventory[tool]['replacement cost'] * 0.10 +
                   inventory[tool]['rental cost'] * rental_rate))
    return total
