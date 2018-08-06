import disk
import core
import time

# {
#         '1': {
#             'name': 'Hammer',
#             'stock': 17,
#             'rental cost': 10,
#             'replacement cost': 45
#         },
#         '2': {
#             'name': 'Drill',
#             'stock': 10,
#             'rental cost': 30,
#             'replacement cost': 100
#         },
#         '3': {
#             'name': 'Chop-Saw',
#             'stock': 5,
#             'rental cost': 115,
#             'replacement cost': 450
#         },
#         '4': {
#             'name': 'Screwdriver Set',
#             'stock': 18,
#             'rental cost': 26,
#             'replacement cost': 35
#         }
#     }

# def load_inventory():

#     return inventory


def employee_side(who_are_you, name, inventory):
    if who_are_you == '2':
        print()
        print('How you doing', name)
        print()
        print('Type 1 for yes and 2 for no!')
        employee = input('\nWould you like to see the inventory? ')
        print()
        if employee == '1':
            print()
            print(
                inventory['1']['name'] + '\n' + '\n',
                '\nStock: ',
                inventory['1']['stock'],
                '\nRental Cost: ',
                inventory['1']['rental cost'],
                '\nReplacement Cost:',
                inventory['1']['replacement cost'],
                '\n' + inventory['2']['name'] + '\n',
                '\nStock: ',
                inventory['2']['stock'],
                '\nRental Cost: ',
                inventory['2']['rental cost'],
                '\nReplacement Cost:',
                inventory['2']['replacement cost'],
                '\n' + inventory['3']['name'] + '\n',
                '\nStock: ',
                inventory['3']['stock'],
                '\nRental Cost: ',
                inventory['3']['rental cost'],
                '\nReplacement Cost:',
                inventory['3']['replacement cost'],
                '\n' + inventory['4']['name'] + '\n',
                '\nStock: ',
                inventory['4']['stock'],
                '\nRental Cost: ',
                inventory['4']['rental cost'],
                '\nReplacement Cost:',
                inventory['4']['replacement cost'],
            )
            print('Type 1 for yes and 2 for no!')
            print()
            revenue = input('\nWould you like to see the revenue? ')
            print()
            if revenue == '1':
                with open('history.txt') as file:
                    print()
                    file_information = file.read()
                    time.sleep(1)

                    print(file_information)
                    print('Have a blessed day', name)
            if revenue == '2':
                print('Have a blessed day', name)

        if employee == '2':
            print('Goodbye', name)


def here_is_the_inventory(inventory):
    for item in inventory.values():
        print('\n{}: Stock: {} Rental Cost: {} Replacement Cost: {}'.format(
            item['name'],
            item['stock'],
            item['rental cost'],
            item['replacement cost'],
        ))


def load_inventory():
    with open('inventory.txt', 'r') as file:
        line = file.readlines()
    inventory = {}
    for info in line:
        items = info.split(',')
        tool_name = items[0].strip()
        rental_cost = int(items[1].strip())
        stock = int(items[2].strip())
        replacement_cost = int(items[3].strip())
        inventory[tool_name] = {
            'name': tool_name,
            'rental cost': rental_cost,
            'stock': stock,
            'replacement cost': replacement_cost
        }
    return inventory


def main():

    inventory = load_inventory()

    here_is_the_inventory(inventory)

    print("Welcome to Daniel's Tool Rental!")
    print()
    print('''Bussiness Hours:

        Mon-Fri: 7:00 am to 6:00 pm
        Sat: 8:00 am to 5:00 pm
        Sun: Closed''')
    print()
    name = input("What is the name on this rental? ").strip()
    print()

    while True:
        who_are_you = input(
            "Are you a Customer(1) or Employee(2)? ").strip().title()
        if who_are_you == '1':
            returning = input(
                'Are you returning a tool yes(1),No(2)? ').strip()
            print()
            if returning == '1':
                what_tool = input('What tool did you have? ')
                if what_tool in ['Hammer', 'hammer']:
                    inventory['stock'] += 1

                    print('\nIn-Stock: ', inventory['1']['stock'])
                    print('\nHere is your refund for returning item ${:.2f}'.
                          format(inventory['1']['replacement cost'] * 0.10))

                elif what_tool in ['Drill', 'drill']:
                    inventory['2']['stock'] += 1

                    print('\nIn-Stock: ', inventory['2']['stock'])
                    print('\nHere is your refund for returning item ${:.2f}'.
                          format(inventory['2']['replacement cost'] * 0.10))

                elif what_tool in [
                        'Chop-Saw', 'Chop saw', 'Chop Saw', 'chop-saw',
                        'chopsaw', 'chop saw'
                ]:
                    inventory['3']['stock'] += 1

                    print('\nIn-Stock: ', inventory['3']['stock'])
                    print('\nHere is your refund for returning item ${:.2f}'.
                          format(inventory['3']['replacement cost'] * 0.10))

                elif what_tool in [
                        'Screwdriver set', 'screwdriver set', 'Screwdriver Set'
                ]:
                    inventory['4']['stock'] += 1
                    print('\nIn-Stock: ', inventory['4']['stock'])
                    print('\nHere is your refund for returning item ${:.2f}'.
                          format(inventory['4']['replacement cost'] * 0.10))

                print('\t\nThank You for returning your tool!')
                print()
                print('\tHave a blessed day.')
                break
            help = input(
                "Would you like to rent a Tool or q for quit? ").strip()

            if help == 'q':
                print()
                print('Have a blessed day', name, 'Come back soon')
                break

            if help in ['rent', 'rent a tool', 'rent a Tool', 'Rent']:
                print()
                print('Here is our inventory:')
                here_is_the_inventory(inventory)

            tool = input('OK, what tool would you like to rent? ').strip()
            print('\nRentals are only up to 5 days')
            print()
            print(
                "\nWith each rental, there is a 10% fee of product replacement value."
            )
            print()
            rental_rate = int(
                input('How many days do you want to rent a tool for? '))

            if tool in ['Hammer', 'hammer']:
                print()
                if rental_rate > 5:
                    print('Can not rent for more than 5 days!')
                    break
                inventory['Hammer']['stock'] -= 1
                print(tool,
                      'has a rental cost of $ 10.0 plus tax for one day.')

                print()

                print()
                print('In-stock: ', inventory['Hammer']['stock'])
                print()

                if rental_rate == 1:
                    print('Rental Fee: ', '$',
                          inventory['Hammer']['rental cost'])
                if rental_rate == 2:
                    print('Rental Fee: ', '$',
                          inventory['Hammer']['rental cost'] * 2)
                if rental_rate == 3:
                    print('Rental Fee: ', '$',
                          inventory['Hammer']['rental cost'] * 3)
                if rental_rate == 4:
                    print('Rental Fee: ', '$',
                          inventory['Hammer']['rental cost'] * 4)
                if rental_rate == 5:
                    print('Rental Fee: ', '$',
                          inventory['Hammer']['rental cost'] * 5)
                with open('history.txt', 'a') as file:
                    file.write('\n$' + str(
                        round(
                            inventory['Hammer']['rental cost'] * 1.07 +
                            inventory['Hammer']['replacement cost'] * 0.10 +
                            inventory['Hammer']['rental cost'] * rental_rate)))

                print(
                    '''Cost plus Tax: ${:.2f}\nReplacement Deposit: ${:.2f}'''.
                    format(inventory['Hammer']['rental cost'] * 1.07,
                           inventory['Hammer']['replacement cost'] * 0.10))

                print('Total: ${:.2f}\n'.format(
                    inventory['Hammer']['rental cost'] * 1.07 +
                    inventory['Hammer']['replacement cost'] * 0.10 +
                    inventory['Hammer']['rental cost'] * rental_rate))

            elif tool in ['Drill', 'drill']:
                if rental_rate > 5:
                    print('Can not rent for more than 5 days!')
                    break

                inventory['Drill']['stock'] -= 1
                print(tool, 'has a rental cost of $ 30.0 plus tax per day.')

                print()
                print()
                print('In-stock: ', inventory['Drill']['stock'])
                print()
                if rental_rate == 1:
                    print('Rental Fee: ', '$',
                          inventory['Drill']['rental cost'])
                if rental_rate == 2:
                    print('Rental Fee: ', '$',
                          inventory['Drill']['rental cost'] * 2)
                if rental_rate == 3:
                    print('Rental Fee: ', '$',
                          inventory['Drill']['rental cost'] * 3)
                if rental_rate == 4:
                    print('Rental Fee: ', '$',
                          inventory['Drill']['rental cost'] * 4)
                if rental_rate == 5:
                    print('Rental Fee: ', '$',
                          inventory['Drill']['rental cost'] * 5)
                with open('history.txt', 'a') as file:
                    file.write('\n$' + str(
                        round(inventory['Drill']['rental cost'] * 1.07 +
                              inventory['Drill']['replacement cost'] * 0.10 +
                              inventory['Drill']['rental cost'] * rental_rate))
                               )

                print(
                    '''Cost plus Tax: ${:.2f}\nReplacement Deposit: ${:.2f}'''.
                    format(inventory['Drill']['rental cost'] * 1.07,
                           inventory['Drill']['replacement cost'] * 0.10))

                print('Total: ${:.2f}\n'.format(
                    inventory['Drill']['rental cost'] * 1.07 +
                    inventory['Drill']['replacement cost'] * 0.10 +
                    inventory['Drill']['rental cost'] * rental_rate))

            elif tool in [
                    'Chop-Saw', 'chop-saw', 'chop saw', 'chopsaw', 'Chop Saw'
            ]:
                if rental_rate > 5:
                    print('Can not rent for more than 5 days!')
                    break
                inventory['Chop-Saw']['stock'] -= 1
                print(tool, 'has a rental cost of $ 115 plus tax per day.')

                print()
                print()
                print('In-stock: ', inventory['Chop-Saw']['stock'])
                print()
                if rental_rate == 1:
                    print('Rental Fee: ', '$',
                          inventory['Chop-Saw']['rental cost'])
                if rental_rate == 2:
                    print('Rental Fee: ', '$',
                          inventory['Chop-Saw']['rental cost'] * 2)
                if rental_rate == 3:
                    print('Rental Fee: ', '$',
                          inventory['Chop-Saw']['rental cost'] * 3)
                if rental_rate == 4:
                    print('Rental Fee: ', '$',
                          inventory['Chop-Saw']['rental cost'] * 4)
                if rental_rate == 5:
                    print('Rental Fee: ', '$',
                          inventory['Chop-Saw']['rental cost'] * 5)
                with open('history.txt', 'a') as file:
                    file.write(
                        '\n$' + str(
                            round(inventory['Chop-Saw']['rental cost'] * 1.07 +
                                  inventory['Chop-Saw']['replacement cost'] *
                                  0.10 + inventory['Chop-Saw']['rental cost'] *
                                  rental_rate)), )

                print(
                    '''Cost plus Tax: ${:.2f}\nReplacement Deposit: ${:.2f}'''.
                    format(inventory['Chop-Saw']['rental cost'] * 1.07,
                           inventory['Chop-Saw']['replacement cost'] * 0.10))

                print('Total: ${:.2f}\n'.format(
                    inventory['Chop-Saw']['rental cost'] * 1.07 +
                    inventory['Chop-Saw']['replacement cost'] * 0.10 +
                    inventory['Chop-Saw']['rental cost'] * rental_rate))

            elif tool in [
                    'Screwdriver Set', 'screwdriver set', 'screwdrivers',
                    'Screwdrivers'
            ]:
                if rental_rate > 5:
                    print('Can not rent for more than 5 days!')
                    break
                inventory['Screwdriver Set']['stock'] -= 1
                print(tool, 'has a rental cost of $ 26.0 plus tax per day.')

                print()
                print()
                print('In-stock: ', inventory['Screwdriver Set']['stock'])
                print()
                if rental_rate == 1:
                    print('Rental Fee: ', '$',
                          inventory['Screwdriver Set']['rental cost'])
                if rental_rate == 2:
                    print('Rental Fee: ', '$',
                          inventory['Screwdriver Set']['rental cost'] * 2)
                if rental_rate == 3:
                    print('Rental Fee: ', '$',
                          inventory['Screwdriver Set']['rental cost'] * 3)
                if rental_rate == 4:
                    print('Rental Fee: ', '$',
                          inventory['Screwdriver Set']['rental cost'] * 4)
                if rental_rate == 5:
                    print('Rental Fee: ', '$',
                          inventory['Screwdriver Set']['rental cost'] * 5)

                with open('history.txt', 'a') as file:
                    file.write('\n$' + str(
                        round(inventory['Screwdriver Set']['rental cost'] *
                              1.07 + inventory['Screwdriver Set']
                              ['replacement cost'] * 0.10 +
                              inventory['Screwdriver Set']['rental cost'] *
                              rental_rate)))

                print(
                    '''Cost plus Tax: ${:.2f}\nReplacement Deposit: ${:.2f}'''.
                    format(
                        inventory['Screwdriver Set']['rental cost'] * 1.07,
                        inventory['Screwdriver Set']['replacement cost'] *
                        0.10))

                print('Total: ${:.2f}\n'.format(
                    inventory['Screwdriver Set']['rental cost'] * 1.07 +
                    inventory['Screwdriver Set']['replacement cost'] * 0.10 +
                    inventory['Screwdriver Set']['rental cost'] * rental_rate))
        employee_side(who_are_you, name, inventory)


if __name__ == '__main__':
    main()
