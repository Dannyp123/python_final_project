def loading_inventory(line):
    inventory = {}
    for info in line:
        items = info.split(',')
        tool_name = items[0].strip()
        stock = int(items[1].strip())
        rental_cost = int(items[2].strip())
        replacement_cost = int(items[3].strip())
        inventory[tool_name] = {
            'name': tool_name,
            'rental cost': rental_cost,
            'stock': stock,
            'replacement cost': replacement_cost
        }
    return inventory


def rental_sales(inventory, tool, rental_rate):
    total = 0
    total = (float(total + inventory[tool]['rental cost'] * 0.07 +
                   inventory[tool]['replacement cost'] * 0.10 +
                   inventory[tool]['rental cost'] * rental_rate))
    return total


def salestax(inventory, tool):
    sales_tax = 0
    sales_tax = (float(sales_tax + inventory[tool]['rental cost'] * 0.07))
    return sales_tax


def replacementdeposit(inventory, tool):
    replacement_deposit = 0
    replacement_deposit = (float(replacement_deposit +
                                 inventory[tool]['replacement cost'] * 0.10))
    return replacement_deposit
