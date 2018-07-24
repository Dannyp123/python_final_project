import disk


def create_inventory_dictionary(inventory_list):
    inventory_dictionary = {}
    for inventory_info in inventory_list:
        items = inventory_info.split(',')
        key = items[0].strip()
        value = float(items[1].strip())
        inventory_dictionary[key] = value
    return inventory_dictionary
