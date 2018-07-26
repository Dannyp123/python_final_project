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
            'name': 'Chop-Saw',
            'stock': 5,
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
            break

        elif who_are_you == 'Customer':

            help = input("Would you like to rent a Tool or quit? ").strip()
            print('must return with-in 5 days!')
            if help in ['Quit', 'quit']:
                break

            if help in ['rent', 'rent a tool', 'rent a Tool', 'rent']:
                print()
                print(
                    'Here is our inventory:',
                    inventory['1']['name'],
                    inventory['2']['name'],
                    inventory['3']['name'],
                    inventory['4']['name'],
                )

            tool = input('OK, what tool would you like to rent? ').strip()

            rental_rate = input(
                'How many days do you want to rent a tool for? ')

            if tool in ['Hammer', 'hammer']:
                inventory['1']['stock'] -= 1

                print()
                print(tool, 'has a rental cost of $ 24.0 plus tax.')
                print()
                print('In-stock: ', inventory['1']['stock'])
                print()
                if rental_rate == '1':
                    print(
                        'Rental Fee: ',
                        '$',
                        inventory['1']['rental cost'],
                    )
                if rental_rate == '2':
                    print('Rental Fee: ', '$',
                          inventory['1']['rental cost'] * 2)
                if rental_rate == '3':
                    print('Rental Fee: ', '$',
                          inventory['1']['rental cost'] * 3)
                if rental_rate == '4':
                    print('Rental Fee: ', '$',
                          inventory['1']['rental cost'] * 4)
                if rental_rate == '5':
                    print('Rental Fee: ', '$',
                          inventory['1']['rental cost'] * 5)

                print('''Total: {}'''.format(
                    inventory['1']['rental cost'] * 1.07))

            elif tool in ['Drill', 'drill']:
                inventory['2']['stock'] -= 1

                print()
                print(tool, 'has a rental cost of $ 55.0 plus tax.')
                print()
                print('In-stock: ', inventory['2']['stock'])
                print()
                if rental_rate == '1':
                    print('Rental Fee: ', '$', inventory['2']['rental cost'])
                if rental_rate == '2':
                    print('Rental Fee: ', '$',
                          inventory['2']['rental cost'] * 2)
                if rental_rate == '3':
                    print('Rental Fee: ', '$',
                          inventory['2']['rental cost'] * 3)
                if rental_rate == '4':
                    print('Rental Fee: ', '$',
                          inventory['2']['rental cost'] * 4)
                if rental_rate == '5':
                    print('Rental Fee: ', '$',
                          inventory['2']['rental cost'] * 5)

                print('''Total: {}'''.format(
                    inventory['2']['rental cost'] * 1.07))

            elif tool in ['Chop-Saw', 'chop-saw', 'chop saw', 'chopsaw']:
                inventory['3']['stock'] -= 1

                print()
                print(tool, 'has a rental cost of $ 15.0 plus tax.')
                print()
                print('In-stock: ', inventory['3']['stock'])
                print()
                if rental_rate == '1':
                    print('Rental Fee: ', '$', inventory['1']['rental cost'])
                if rental_rate == '2':
                    print('Rental Fee: ', '$',
                          inventory['3']['rental cost'] * 2)
                if rental_rate == '3':
                    print('Rental Fee: ', '$',
                          inventory['3']['rental cost'] * 3)
                if rental_rate == '4':
                    print('Rental Fee: ', '$',
                          inventory['3']['rental cost'] * 4)
                if rental_rate == '5':
                    print('Rental Fee: ', '$',
                          inventory['3']['rental cost'] * 5)
                print('''Total: {}'''.format(
                    round(inventory['3']['rental cost'] * 1.07, 3)))

            if tool in ['Screwdriver', 'screwdriver']:
                inventory['4']['stock'] -= 1

                print()
                print(tool, 'has a rental cost of $ 5.0 plus tax.')
                print()
                print('In-stock: ', inventory['4']['stock'])
                print()
                if rental_rate == '1':
                    print('Rental Fee: ', '$', inventory['1']['rental cost'])
                if rental_rate == '2':
                    print('Rental Fee: ', '$',
                          inventory['4']['rental cost'] * 2)
                if rental_rate == '3':
                    print('Rental Fee: ', '$',
                          inventory['4']['rental cost'] * 3)
                if rental_rate == '4':
                    print('Rental Fee: ', '$',
                          inventory['4']['rental cost'] * 4)
                if rental_rate == '5':
                    print('Rental Fee: ', '$',
                          inventory['4']['rental cost'] * 5)

                print('''Total: {}'''.format(
                    round(inventory['4']['rental cost'] * 1.07, 3)))

            returning = input('Are you returning a tool? ').strip()

            if returning == 'yes':
                what_tool = input('What tool(s) did you have? ')
                if what_tool in ['Hammer', 'hammer']:
                    inventory['1']['stock'] += 1

                    print('In-Stock: ', inventory['1']['stock'])

                elif what_tool in ['Drill', 'drill']:
                    inventory['2']['stock'] += 1

                    print('In-Stock: ', inventory['2']['stock'])

                elif what_tool in ['Chop-Saw', 'chop-saw']:
                    inventory['3']['stock'] += 1
                    print('In-Stock: ', inventory['3']['stock'])

                elif what_tool in ['Screwdriver', 'screwdriver']:
                    inventory['4']['stock'] += 1
                    print('In-Stock: ', inventory['4']['stock'])

                print('Thank You for returning, have a blessed day!')

    with open('history.txt', 'a') as file:
        file.write('\n' + str(inventory) + '\n')


if __name__ == '__main__':
    main()
