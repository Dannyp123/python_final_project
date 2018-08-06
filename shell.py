import disk
import core
import time


def employee_side(who_are_you, name, inventory):
    if who_are_you == '2':
        print()
        print('How you doing', name)
        print()
        employee = input(
            '\nWould you like to see the inventory Yes(1) or No(2)? ')
        print()
        if employee == '1':
            print()
            here_is_the_inventory(inventory)
            print()
            revenue = input(
                '\nWould you like to see the revenue Yes(1) or No(2)? ')
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


def main():

    inventory = disk.load_inventory()

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
                '\nAre you returning a tool yes(1) or No(2)? ').strip()
            print()
            if returning == '1':
                what_tool = input('What tool did you have? ')
                if what_tool in ['Hammer', 'hammer']:
                    inventory['Hammer']['stock'] += 1

                    print('\nIn-Stock: ', inventory['Hammer']['stock'])
                    print('\nHere is your refund for returning item ${:.2f}'.
                          format(
                              inventory['Hammer']['replacement cost'] * 0.10))

                elif what_tool in ['Drill', 'drill']:
                    inventory['Drill']['stock'] += 1

                    print('\nIn-Stock: ', inventory['Drill']['stock'])
                    print('\nHere is your refund for returning item ${:.2f}'.
                          format(
                              inventory['Drill']['replacement cost'] * 0.10))

                elif what_tool in [
                        'Chop-Saw', 'Chop saw', 'Chop Saw', 'chop-saw',
                        'chopsaw', 'chop saw'
                ]:
                    inventory['Chop-Saw']['stock'] += 1

                    print('\nIn-Stock: ', inventory['Chop-Saw']['stock'])
                    print(
                        '\nHere is your refund for returning item ${:.2f}'.
                        format(
                            inventory['Chop-Saw']['replacement cost'] * 0.10))

                elif what_tool in [
                        'Screwdriver set', 'screwdriver set', 'Screwdriver Set'
                ]:
                    inventory['Screwdriver Set']['stock'] += 1
                    print('\nIn-Stock: ',
                          inventory['Screwdriver Set']['stock'])
                    print('\nHere is your refund for returning item ${:.2f}'.
                          format(
                              inventory['Screwdriver Set']['replacement cost']
                              * 0.10))

                print('\t\nThank You for returning your tool!')
                print()
                print('\tHave a blessed day.')
                break
            help = input(
                "Would you like to rent(R) a Tool or quit(Q)? ").strip()

            if help in ['Q', 'q']:
                print()
                print('Have a blessed day', name, 'Come back soon')
                break

            if help in ['R', 'r']:
                print()
                print('Here is our inventory:')
                core.here_is_the_inventory(inventory)
                print()
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
                print(tool, 'has a rental cost of $ 115.0 plus tax per day.')

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
