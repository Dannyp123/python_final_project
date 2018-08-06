import disk


def here_is_the_inventory(inventory):
    for item in inventory.values():
        print(
            '\n\n\t{} \nIn-Stock: {} \nRental Cost: ${} \nReplacement Cost: ${}'.
            format(
                item['name'],
                item['stock'],
                item['rental cost'],
                item['replacement cost'],
            ))


def business_hours():
    print('''Business Hours:

        Mon-Fri: 7:00 am to 6:00 pm
        Sat: 8:00 am to 5:00 pm
        Sun: Closed''')
