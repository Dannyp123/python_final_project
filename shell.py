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
            'rental cost': 45,
            'replacement cost': 95
        },
        '4': {
            'name': 'Screwdriver Set',
            'stock': 18,
            'rental cost': 5,
            'replacement cost': 16
        }
    }

    print("Welcome to Daniel's Tool Rental!")
    print()
    print(
        'Bussiness Hours: \nMon-Fri: 7:00 am to 6:00 pm \nSat: 8:00 am to 5:00 pm \nSun: Closed'
    )
    print()
    name = input("What is the name on this rental? ")

    who_are_you = input("Are you a Employee or a Customer? ").strip().title()
    while True:
        if who_are_you == 'Employee':
            print('How you doing', name)
            employee = input('Would you like to see the inventory? ')
            if employee == 'yes':
                print(
                    inventory['1']['name'],
                    inventory['1']['stock'],
                    inventory['1']['rental cost'],
                    inventory['1']['replacement cost'],
                    inventory['3']['name'],
                    inventory['3']['stock'],
                    inventory['3']['rental cost'],
                    inventory['3']['replacement cost'],
                    inventory['4']['name'],
                    inventory['4']['stock'],
                    inventory['4']['rental cost'],
                    inventory['4']['replacement cost'],
                )
                revenue = input('Would you like to see the revenue? ')
                if revenue == 'yes':
                    with open('history.txt') as file:
                        file_information = file.readlines()
                        items = str(file_information).split('\n')

                        print(file_information)
                if revenue == 'no':
                    print('Have a blessed day', name)
                break

            if employee == 'no':
                print('Goodbye', name)
                break

        elif who_are_you == 'Customer':

            help = input("Would you like to rent a Tool or quit? ").strip()

            if help in ['Quit', 'quit']:
                print()
                print('Have a blessed day', name, 'Come back soon')
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
            print('\nRentals are only up to 5 days')
            print()
            print("\nWith each rental, there is a 10% replacement fee")
            print()
            rental_rate = int(
                input('How many days do you want to rent a tool for? '))

            if tool in ['Hammer', 'hammer']:
                print()
                if rental_rate > 5:
                    print('Can not rent for more than 5 days!')
                    break
                inventory['1']['stock'] -= 1
                print(tool,
                      'has a rental cost of $ 24.0 plus tax for one day.')

                print()

                print()
                print('In-stock: ', inventory['1']['stock'])
                print()

                if rental_rate == 1:
                    print('Rental Fee: ', '$', inventory['1']['rental cost'])
                if rental_rate == 2:
                    print('Rental Fee: ', '$',
                          inventory['1']['rental cost'] * 2)
                if rental_rate == 3:
                    print('Rental Fee: ', '$',
                          inventory['1']['rental cost'] * 3)
                if rental_rate == 4:
                    print('Rental Fee: ', '$',
                          inventory['1']['rental cost'] * 4)
                if rental_rate == 5:
                    print('Rental Fee: ', '$',
                          inventory['1']['rental cost'] * 5)
                with open('history.txt', 'a') as file:
                    file.write('\n' + str(
                        round(inventory['1']['rental cost'] * 1.07 +
                              inventory['1']['replacement cost'] * 0.10 +
                              inventory['1']['rental cost'] * rental_rate)))

                print(
                    '''Cost plus Tax: ${:.2f}\nReplacement Deposit: ${:.2f}'''.
                    format(inventory['1']['rental cost'] * 1.07,
                           inventory['1']['replacement cost'] * 0.10))

                print('Total: ${:.2f}\n'.format(
                    inventory['1']['rental cost'] * 1.07 +
                    inventory['1']['replacement cost'] * 0.10 +
                    inventory['1']['rental cost'] * rental_rate))

            elif tool in ['Drill', 'drill']:
                if rental_rate > 5:
                    print('Can not rent for more than 5 days!')
                    break
                inventory['2']['stock'] -= 1
                print(tool, 'has a rental cost of $ 55.0 plus tax per day.')

                print()

                print()
                print('In-stock: ', inventory['2']['stock'])
                print()
                if rental_rate == 1:
                    print('Rental Fee: ', '$', inventory['2']['rental cost'])
                if rental_rate == 2:
                    print('Rental Fee: ', '$',
                          inventory['2']['rental cost'] * 2)
                if rental_rate == 3:
                    print('Rental Fee: ', '$',
                          inventory['2']['rental cost'] * 3)
                if rental_rate == 4:
                    print('Rental Fee: ', '$',
                          inventory['2']['rental cost'] * 4)
                if rental_rate == 5:
                    print('Rental Fee: ', '$',
                          inventory['2']['rental cost'] * 5)
                with open('history.txt', 'a') as file:
                    file.write('\n' + str(
                        round(inventory['2']['rental cost'] * 1.07 +
                              inventory['2']['replacement cost'] * 0.10 +
                              inventory['2']['rental cost'] * rental_rate)))

                print(
                    '''Cost plus Tax: ${:.2f}\nReplacement Deposit: ${:.2f}'''.
                    format(inventory['2']['rental cost'] * 1.07,
                           inventory['2']['replacement cost'] * 0.10))

                print('Total: ${:.2f}\n'.format(
                    inventory['2']['rental cost'] * 1.07 +
                    inventory['2']['replacement cost'] * 0.10 +
                    inventory['2']['rental cost'] * rental_rate))

            elif tool in [
                    'Chop-Saw', 'chop-saw', 'chop saw', 'chopsaw', 'Chop Saw'
            ]:
                if rental_rate > 5:
                    print('Can not rent for more than 5 days!')
                    break
                inventory['3']['stock'] -= 1
                print(tool, 'has a rental cost of $ 45 plus tax per day.')

                print()

                print()
                print('In-stock: ', inventory['3']['stock'])
                print()
                if rental_rate == 1:
                    print('Rental Fee: ', '$', inventory['1']['rental cost'])
                if rental_rate == 2:
                    print('Rental Fee: ', '$',
                          inventory['3']['rental cost'] * 2)
                if rental_rate == 3:
                    print('Rental Fee: ', '$',
                          inventory['3']['rental cost'] * 3)
                if rental_rate == 4:
                    print('Rental Fee: ', '$',
                          inventory['3']['rental cost'] * 4)
                if rental_rate == 5:
                    print('Rental Fee: ', '$',
                          inventory['3']['rental cost'] * 5)
                with open('history.txt', 'a') as file:
                    file.write('\n' + str(
                        round(inventory['3']['rental cost'] * 1.07 +
                              inventory['3']['replacement cost'] * 0.10 +
                              inventory['3']['rental cost'] * rental_rate)))

                print(
                    '''Cost plus Tax: ${:.2f}\nReplacement Deposit: ${:.2f}'''.
                    format(inventory['3']['rental cost'] * 1.07,
                           inventory['3']['replacement cost'] * 0.10))

                print('Total: ${:.2f}\n'.format(
                    inventory['3']['rental cost'] * 1.07 +
                    inventory['3']['replacement cost'] * 0.10 +
                    inventory['3']['rental cost'] * rental_rate))

            elif tool in [
                    'Screwdriver Set', 'screwdriver set', 'screwdrivers',
                    'Screwdrivers'
            ]:
                if rental_rate > 5:
                    print('Can not rent for more than 5 days!')
                    break
                inventory['4']['stock'] -= 1
                print(tool, 'has a rental cost of $ 5.0 plus tax per day.')

                print()

                print()
                print('In-stock: ', inventory['4']['stock'])
                print()
                if rental_rate == 1:
                    print('Rental Fee: ', '$', inventory['1']['rental cost'])
                if rental_rate == 2:
                    print('Rental Fee: ', '$',
                          inventory['4']['rental cost'] * 2)
                if rental_rate == 3:
                    print('Rental Fee: ', '$',
                          inventory['4']['rental cost'] * 3)
                if rental_rate == 4:
                    print('Rental Fee: ', '$',
                          inventory['4']['rental cost'] * 4)
                if rental_rate == 5:
                    print('Rental Fee: ', '$',
                          inventory['4']['rental cost'] * 5)

                with open('history.txt', 'a') as file:
                    file.write('\n' + str(
                        round(inventory['4']['rental cost'] * 1.07 +
                              inventory['4']['replacement cost'] * 0.10 +
                              inventory['4']['rental cost'] * rental_rate)))

                print(
                    '''Cost plus Tax: ${:.2f}\nReplacement Deposit: ${:.2f}'''.
                    format(inventory['4']['rental cost'] * 1.07,
                           inventory['4']['replacement cost'] * 0.10))

                print('Total: ${:.2f}\n'.format(
                    inventory['4']['rental cost'] * 1.07 +
                    inventory['4']['replacement cost'] * 0.10 +
                    inventory['4']['rental cost'] * rental_rate))

            returning = input('Are you returning a tool? ').strip()
            print()
            if returning == 'yes':
                what_tool = input('What tool did you have? ')
                if what_tool in ['Hammer', 'hammer']:
                    inventory['1']['stock'] += 1

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


if __name__ == '__main__':
    main()
