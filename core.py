import disk


def here_is_the_inventory(inventory):
    for item in inventory.values():
        print('\n\t{} \nStock: {} \nRental Cost: ${} \nReplacement Cost: ${}'.
              format(
                  item['name'],
                  item['stock'],
                  item['rental cost'],
                  item['replacement cost'],
              ))
