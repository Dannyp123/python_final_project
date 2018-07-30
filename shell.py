import disk
import core
import time


def is_phone_number(phone_str):
    ''' str -> bool 

    >>> is_phone_number('1234567891')
    True
    >>> is_phone_number('2345689')
    False
    >>> is_phone_number('6624734353')
    True
    '''
    if phone_str.isdigit() and len(phone_str) == 10:
        return True
    else:
        return False


def is_credit_card(cc_str):
    ''' str -> bool 

    >>> is_credit_card('1234567891234567')
    True
    >>> is_credit_card('2345689')
    False
    >>> is_credit_card('4445555466795678')
    True
    '''
    if cc_str.isdigit() and len(cc_str) == 16:
        return True
    else:
        return False


def load_inventory():
    inventory = {
        '1': {
            'name': 'Hammer',
            'stock': 17,
            'rental cost': 10,
            'replacement cost': 45
        },
        '2': {
            'name': 'Drill',
            'stock': 10,
            'rental cost': 30,
            'replacement cost': 100
        },
        '3': {
            'name': 'Chop-Saw',
            'stock': 5,
            'rental cost': 115,
            'replacement cost': 450
        },
        '4': {
            'name': 'Screwdriver Set',
            'stock': 18,
            'rental cost': 26,
            'replacement cost': 35
        }
    }
    return inventory


def get_phone_number():
    while True:
        phone = input("Phone Number: ")
        if is_phone_number(phone) == True:
            print()
            print('Thank you for your information!')
            print()
            break
        else:
            print('Invalid Phone Number!')


def get_card_number():
    while True:
        card_number = input('What is your credit card number? ')
        if is_credit_card(card_number):
            print()
            print('Now your Card Number is on file.')
            print()
            break
        else:
            print('Invalid Card Number!')


def employee_side(who_are_you, name, inventory):
    if who_are_you == 'Employee':
        print()
        print('How you doing', name)
        employee = input('\nWould you like to see the inventory? ')
        print()
        if employee == 'yes':
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
            print()
            revenue = input('\nWould you like to see the revenue? ')
            print()
            if revenue == 'yes':
                with open('history.txt') as file:
                    print()
                    file_information = file.read()
                    time.sleep(1)

                    print(file_information)
                    print('Have a blessed day', name)
            if revenue == 'no':
                print('Have a blessed day', name)

        if employee == 'no':
            print('Goodbye', name)


def main():

    inventory = load_inventory()

    print("Welcome to Daniel's Tool Rental!")
    print()
    print('''Bussiness Hours:

        Mon-Fri: 7:00 am to 6:00 pm
        Sat: 8:00 am to 5:00 pm
        Sun: Closed''')
    print()
    name = input("What is the name on this rental? ").strip()
    print()

    get_phone_number()

    while True:
        who_are_you = input("Are you a Customer or Employee? ").strip().title()
        if who_are_you == 'Customer':
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
                print()
                print('\tHave a blessed day.')
                break
            help = input("Would you like to rent a Tool or quit? ").strip()

            if help in ['Quit', 'quit']:
                print()
                print('Have a blessed day', name, 'Come back soon')
                break

            if help in ['rent', 'rent a tool', 'rent a Tool', 'Rent']:
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
                inventory['1']['stock'] -= 1
                print(tool,
                      'has a rental cost of $ 10.0 plus tax for one day.')

                print()
                get_card_number()

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
                    file.write('\n$' + str(
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
                print(tool, 'has a rental cost of $ 30.0 plus tax per day.')

                print()
                get_card_number()
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
                    file.write('\n$' + str(
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
                print(tool, 'has a rental cost of $ 115 plus tax per day.')

                print()
                get_card_number()
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
                    file.write(
                        '\n$' + str(
                            round(inventory['3']['rental cost'] * 1.07 +
                                  inventory['3']['replacement cost'] * 0.10 +
                                  inventory['3']['rental cost'] * rental_rate)
                        ), )

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
                print(tool, 'has a rental cost of $ 26.0 plus tax per day.')

                print()
                get_card_number()
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
                    file.write('\n$' + str(
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
        employee_side(who_are_you, name, inventory)


if __name__ == '__main__':
    main()
