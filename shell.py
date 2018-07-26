import disk
import core


def main():
    # inventory_raw_info = disk.open_file('inventory.txt')
    # inventory_dictionary = core.create_inventory_dictionary(inventory_raw_info)
    inventory = {
        '1': {
            'name': 'Hammer',
            'stock': 17,
            'rental cost': 24,
            'replacement cost': 34
        },
        '2': {
            'name': 'Drill',
            'stock': 10,
            'rental cost': 55,
            'replacement cost': 100
        },
        '3': {
            'name': 'Saw',
            'stock': 18,
            'rental cost': 15,
            'replacement cost': 25
        },
        '4': {
            'name': 'Screwdriver',
            'stock': 18,
            'rental cost': 5,
            'replacement cost': 10
        }
    }

    print("Welcome to Daniel's Tool Rental!")

    name = input("What is the name for this rental? ")
    who_are_you = input("Are you a Employee or a Customer? ").strip().title()
    while True:
        if who_are_you == 'Employee':
            print('Checking the inventory!')
        elif who_are_you == 'Customer':
            help = input(
                "Would you like to rent a Tool , see our inventory, or quit? "
            ).strip()
            if help in ['Quit', 'quit']:
                break

        if help in [
                'See our inventory', 'see our inventory', 'see inventory',
                'Inventory', 'inventory'
        ]:
            print(
                'Choose of tools:',
                inventory['1']['name'],
                inventory['2']['name'],
                inventory['3']['name'],
                inventory['4']['name'],
            )
        if help in ['rent', 'rent a tool', 'rent a Tool', 'rent']:
            print(
                'Here is our inventory:',
                inventory['1']['name'],
                inventory['2']['name'],
                inventory['3']['name'],
                inventory['4']['name'],
            )

            tool = input('OK, what tool would you like to rent? ').strip()

            if tool in ['Hammer', 'hammer']:
                inventory['1']['stock'] -= 1
                print()
                print(tool, 'has a rental cost of $ 24.0 plus tax.')
                print()
                print('In-stock: ', inventory['1']['stock'])
                print()
                print('''Total: {}'''.format(
                    inventory['1']['rental cost'] * 1.07))

            elif tool in ['Drill', 'drill']:
                inventory['2']['stock'] -= 1
                print()
                print(tool, 'has a rental cost of $ 55.0 plus tax.')
                print()
                print('In-stock: ', inventory['2']['stock'])
                print()
                print('''Total: {}'''.format(
                    inventory['2']['rental cost'] * 1.07))

            elif tool in ['Saw', 'saw']:
                inventory['3']['stock'] -= 1
                print()
                print(tool, 'has a rental cost of $ 15.0 plus tax.')
                print()
                print('In-stock: ', inventory['3']['stock'])
                print()
                print(
                    '''Total: {}'''.format(
                        round(inventory['3']['rental cost'] * 1.07, 3)), )

            elif tool in ['Screwdriver', 'screwdriver']:
                inventory['4']['stock'] -= 1
                print()
                print(tool, 'has a rental cost of $ 20.0 plus tax.')
                print()
                print('In-stock: ', inventory['4']['stock'])
                print()
                print(
                    '''Total: {}'''.format(
                        round(inventory['4']['rental cost'] * 1.07, 3)), )

    with open('history.txt', 'a') as file:
        file.write('\n' + str(inventory) + '\n')


if __name__ == '__main__':
    main()
