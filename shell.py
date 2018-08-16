import disk
import core
import time
from termcolor import colored


def business_hours():
    print("Welcome to Daniel's Tool Rental!!\n")
    print('''Business Hours:
    
        Mon-Fri: 7:00 am to 5:00 pm
        Sat: 8:00 am to 7:00 pm
        Sun: Closed''')


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


def renting_a_tool(inventory, tool):
    while True:
        rental_rate = int(
            input('How many days do you want to rent a tool for? '))
        print()
        if rental_rate > 5:
            print(colored('Can not rent for more than 5 days!\n', 'red'))
        else:
            core.taking_out_of_stock(inventory, tool)
            print(tool, 'has a rental cost of $',
                  inventory[tool]['rental cost'],
                  'per day (Sales Tax added in total).')

            print('\nRental Fee has your rental rate included.\n')
            print('Printing Your Receipt!')
            time.sleep(2)
            print(
                '-------------------------------------------------------------------------'
            )
            print()

            print()
            print('In-stock: ', inventory[tool]['stock'])
            print()
            print('Rental Fee: {}{}\n'.format(
                '$', inventory[tool]['rental cost'] * rental_rate))

            Sales_Tax = core.salestax(inventory, tool)
            Replacement_Deposit = core.replacementdeposit(inventory, tool)
            total = core.totals(inventory, tool, rental_rate)
            disk.write_to_history(total, tool, 'rented')

            print('Sales Tax: ${:.2f}\n'.format(Sales_Tax))
            print('Replacement Deposit: ${:.2f}\n'.format(Replacement_Deposit))

            print('Total plus Sales Tax: ${:.2f}\n'.format(total))
            print(
                '-------------------------------------------------------------------------'
            )
            break


def returning_a_tool(inventory):
    while True:
        what_tool = input('\nWhat tool did you have? ')
        if what_tool in inventory:
            total = 0
            disk.write_to_history(total, what_tool, 'returned')
            core.adding_back_to_stock(inventory, what_tool)
            print()
            print('In-Stock:', inventory[what_tool]['stock'])
            print('\t\nThank You for returning your tool!')
            print()
            print("Here is back your Replacement Deposit {}{}".format(
                '$', core.replacementdeposit(inventory, what_tool)))
            print('\n\tHave a blessed day!!')
            break
        else:
            print(
                colored(
                    '\nYou did not rent that from us, you sure you are at the right place?',
                    'red'))


def employee_side(name, inventory):
    print()
    print('How you doing', name)
    print()
    employee = input('\nWould you like to see the inventory Yes(Y) or No(N)? ')
    print()
    if employee in ['Y', 'y']:
        print('Loading the Inventory...')
        time.sleep(1.5)
        here_is_the_inventory(inventory)
    if employee in ['N', 'n']:
        print('Thanks for your support')
    revenue = input('\nWould you like to see the revenue Yes(Y) or No(N)? ')
    print()
    if revenue in ['Y', 'y']:
        print('Calculating Total Revenue...\n')
        time.sleep(2.5)
        print("Total Revenue: ${}".format(disk.total_revenue()))
    seeing_history = input(
        '\nWould you like to view previous transactions Yes(Y) or No(N)? ')
    print()
    if seeing_history in ['Y', 'y']:
        print('Loading Previous Transactions...\n')
        time.sleep(1.5)
        print(disk.viewing_history())
        print('Goodbye {}, have a great day!'.format(name))
    if seeing_history in ['N', 'n']:
        print('\nOk, glad I could assist you, see you later', name)


def customer_side(name, inventory):
    while True:
        help = input(
            "\nWould you like to Rent(R) a Tool, Return(Rt) a Tool, or Quit(Q)? "
        ).strip()
        if help in ['Rt', 'rt', 'rT']:
            returning_a_tool(inventory)
            break
        if help in ['Q', 'q']:
            print()
            print('Have a blessed day', name, 'Come back soon')
            break

        if help in ['R', 'r']:
            print()
            print('Here is our inventory:')
            time.sleep(1)
            here_is_the_inventory(inventory)
            print()
        tool = input('\nWhat tool would you like to rent? ').strip().title()
        print('\nRentals are only up to 5 days')
        print()
        print(
            "\nWith each rental, there is a 10% fee of the products replacement value."
        )
        print()

        renting_a_tool(inventory, tool)


def main():
    inventory = disk.load_inventory('inventory.txt')
    inventory = core.loading_inventory(inventory)
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
