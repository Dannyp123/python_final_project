import disk
import core
import time


def business_hours():
    print('''Business Hours:
    
        Mon-Fri: 7:00 am to 5:00 pm
        Sat: 8:00 am to 7:00 pm
        Sun: Closed''')


def employee_side(name, inventory):
    print()
    print('How you doing', name)
    print()
    employee = input('\nWould you like to see the inventory Yes(Y) or No(N)? ')
    print()
    if employee in ['Y', 'y']:
        print()
        time.sleep(1)
        core.here_is_the_inventory(inventory)
    if employee in ['N', 'n']:
        print('Thanks for your support')
    revenue = input('\nWould you like to see the revenue Yes(Y) or No(N)? ')
    print()
    if revenue in ['Y', 'y']:
        with open('history.txt') as file:
            print()
            file_information = file.read()
            time.sleep(1)

            print(file_information)
    print('\nHave a blessed day', name)


def customer_side(name, inventory):
    while True:
        help = input(
            "\nWould you like to Rent(R) a Tool, Return(Rt) a Tool, or Quit(Q)? "
        ).strip()
        if help in ['Rt', 'RT', 'rt', 'return']:
            what_tool = input('\nWhat tool did you have? ')
            if what_tool in ['Hammer', 'hammer']:
                inventory['Hammer']['stock'] += 1

                print('\nIn-Stock: ', inventory['Hammer']['stock'])
                print(
                    '\nHere is your refund for returning item ${:.2f}'.format(
                        inventory['Hammer']['replacement cost'] * 0.10))

            elif what_tool in ['Drill', 'drill']:
                inventory['Drill']['stock'] += 1

                print('\nIn-Stock: ', inventory['Drill']['stock'])
                print(
                    '\nHere is your refund for returning item ${:.2f}'.format(
                        inventory['Drill']['replacement cost'] * 0.10))

            elif what_tool.strip().replace(' ', '').replace(
                    '-', '').lower() == 'chopsaw':
                inventory['Chop-Saw']['stock'] += 1

                print('\nIn-Stock: ', inventory['Chop-Saw']['stock'])
                print(
                    '\nHere is your refund for returning item ${:.2f}'.format(
                        inventory['Chop-Saw']['replacement cost'] * 0.10))

            elif what_tool in [
                    'Screwdriver set', 'screwdriver set', 'Screwdriver Set',
                    'Screwdrivers', 'screwdrivers'
            ]:
                inventory['Screwdriver Set']['stock'] += 1
                print('\nIn-Stock: ', inventory['Screwdriver Set']['stock'])
                print(
                    '\nHere is your refund for returning item ${:.2f}'.format(
                        inventory['Screwdriver Set']['replacement cost'] *
                        0.10))

            print('\t\nThank You for returning your tool!')
            print()
            print('\tHave a blessed day.')
            continue

        if help in ['Q', 'q']:
            print()
            print('Have a blessed day', name, 'Come back soon')
            break

        if help in ['R', 'r']:
            print()
            print('Here is our inventory:')
            time.sleep(1)
            core.here_is_the_inventory(inventory)
            print()
        tool = input('\nOK, what tool would you like to rent? ').strip()
        print('\nRentals are only up to 5 days')
        print()
        print(
            "\nWith each rental, there is a 10% fee of the products replacement value."
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
            print(
                tool,
                'has a rental cost of $ 10.0 per day (Sales Tax added in total).'
            )
            print('\nRental Fee has your rental rate included.')
            print()
            print(
                '-------------------------------------------------------------------------'
            )
            print()
            print('In-stock: ', inventory['Hammer']['stock'])
            print()

            if rental_rate == 1:
                print('Rental Fee: ', '$', inventory['Hammer']['rental cost'])
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
                file.write('\nHammer- $ ' + str(
                    inventory['Hammer']['rental cost'] * 0.07 +
                    inventory['Hammer']['replacement cost'] * 0.10 +
                    inventory['Hammer']['rental cost'] * rental_rate))
            print(
                '''Sales Tax: ${:.2f}\nReplacement Deposit: ${:.2f}'''.format(
                    inventory['Hammer']['rental cost'] * 0.07,
                    inventory['Hammer']['replacement cost'] * 0.10))

            print('Total plus Sales Tax: ${:.2f}\n'.format(
                inventory['Hammer']['rental cost'] * 0.07 +
                inventory['Hammer']['replacement cost'] * 0.10 +
                inventory['Hammer']['rental cost'] * rental_rate))
            print(
                '-------------------------------------------------------------------------'
            )
        elif tool in ['Drill', 'drill']:
            if rental_rate > 5:
                print('Can not rent for more than 5 days!')
                break

            inventory['Drill']['stock'] -= 1
            print(
                tool,
                'has a rental cost of $ 30.0 per day (Sales Tax added in total).'
            )
            print('\nRental Fee has your rental rate included.')
            print()
            print()
            print('In-stock: ', inventory['Drill']['stock'])
            print()
            if rental_rate == 1:
                print('Rental Fee: ', '$', inventory['Drill']['rental cost'])
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
                file.write('\nDrill- $ ' + str(
                    inventory['Drill']['rental cost'] * 0.07 +
                    inventory['Drill']['replacement cost'] * 0.10 +
                    inventory['Drill']['rental cost'] * rental_rate))

            print(
                '''Sales Tax: ${:.2f}\nReplacement Deposit: ${:.2f}'''.format(
                    inventory['Drill']['rental cost'] * 0.07,
                    inventory['Drill']['replacement cost'] * 0.10))

            print('Total plus Sales Tax: ${:.2f}\n'.format(
                inventory['Drill']['rental cost'] * 0.07 +
                inventory['Drill']['replacement cost'] * 0.10 +
                inventory['Drill']['rental cost'] * rental_rate))
            print('----------------------------------------------------------')
        elif tool in [
                'Chop-Saw', 'chop-saw', 'chop saw', 'chopsaw', 'Chop Saw',
                'Chop-saw'
        ]:
            if rental_rate > 5:
                print('Can not rent for more than 5 days!')
                break
            inventory['Chop-Saw']['stock'] -= 1
            print(
                tool,
                'has a rental cost of $ 125.0 per day (Sales Tax added in total).'
            )
            print('\nRental Fee has your rental rate included.')
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
                file.write('\nChop-Saw- $ ' + str(
                    inventory['Chop-Saw']['rental cost'] * 0.07 +
                    inventory['Chop-Saw']['replacement cost'] * 0.10 +
                    inventory['Chop-Saw']['rental cost'] * rental_rate))

            print(
                '''Sales Tax: ${:.2f}\nReplacement Deposit: ${:.2f}'''.format(
                    inventory['Chop-Saw']['rental cost'] * 0.07,
                    inventory['Chop-Saw']['replacement cost'] * 0.10))

            print('Total plus Sales Tax: ${:.2f}\n'.format(
                inventory['Chop-Saw']['rental cost'] * 0.07 +
                inventory['Chop-Saw']['replacement cost'] * 0.10 +
                inventory['Chop-Saw']['rental cost'] * rental_rate))
            print('----------------------------------------------------------')

        elif tool in [
                'Screwdriver Set', 'screwdriver set', 'screwdrivers',
                'Screwdrivers'
        ]:
            if rental_rate > 5:
                print('Can not rent for more than 5 days!')
                break
            inventory['Screwdriver Set']['stock'] -= 1
            print(
                tool,
                'has a rental cost of $ 16.0 per day (Sales Tax added in total).'
            )
            print('\nRental Fee has your rental rate included.')
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
                file.write('\nScrewdriver Set- $ ' + str(
                    inventory['Screwdriver Set']['rental cost'] * 0.07 +
                    inventory['Screwdriver Set']['replacement cost'] * 0.10 +
                    inventory['Screwdriver Set']['rental cost'] * rental_rate))

            print(
                '''Sales Tax: ${:.2f}\nReplacement Deposit: ${:.2f}'''.format(
                    inventory['Screwdriver Set']['rental cost'] * 0.07,
                    inventory['Screwdriver Set']['replacement cost'] * 0.10))

            print('Total plus Sales Tax: ${:.2f}\n'.format(
                inventory['Screwdriver Set']['rental cost'] * 0.07 +
                inventory['Screwdriver Set']['replacement cost'] * 0.10 +
                inventory['Screwdriver Set']['rental cost'] * rental_rate))
            print('----------------------------------------------------------')


def main():
    inventory = disk.load_inventory()
    print("Welcome to Daniel's Tool Rental!")
    print()
    business_hours()
    print()
    name = input("What is the name on this rental? ").strip().title()
    print()
    who_are_you = input("Are you a Customer(1) or Employee(2)? ").strip()
    if who_are_you == '1':
        customer_side(name, inventory)
    else:
        employee_side(name, inventory)


if __name__ == '__main__':
    main()
