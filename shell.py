import disk
import core
import time
import sys
from termcolor import colored


def business_hours():
    print("Welcome to Daniel's Tool Rental!!\n")
    print('''Business Hours:
    
        Mon-Fri: 7:00 am to 5:00 pm
        Sat: 8:00 am to 7:00 pm
        Sun: Closed''')


def adding_back_to_stock(inventory, what_tool):
    inventory[what_tool]['stock'] += 1


def taking_out_of_stock(inventory, tool):
    inventory[tool]['stock'] -= 1


def here_is_the_inventory(inventory):
    for item in inventory.values():
        print(
            colored(
                '\n\n\t{} \n. In-Stock: {} \n. Rental Cost: ${} \n. Replacement Cost: ${}'
                .format(
                    item['name'],
                    item['stock'],
                    item['rental cost'],
                    item['replacement cost'],
                ), 'green'))


def printing_receipt(inventory, tool, rental_rate, Sales_Tax,
                     Replacement_Deposit, total):
    print('Rental Fee: {}{}'.format(
        '$', inventory[tool]['rental cost'] * rental_rate))
    print('Sales Tax: ${:.2f}'.format(Sales_Tax))
    print('Replacement Deposit: ${:.2f}'.format(Replacement_Deposit))
    print('Total including Sales Tax: ${:.2f}'.format(total))
    print(
        '-------------------------------------------------------------------------'
    )


def input_tool(inventory):
    while True:
        choice = input('\nWhat tool would you like to rent? ').title().strip()
        if choice in inventory and inventory[choice]['stock'] > 0:
            return choice
        else:
            print(colored('\nSorry!! Currently not available!', 'red'))


def renting_a_tool(inventory, tool, name):
    while True:
        rental_rate = int(
            input('How many days do you want to rent a tool for? '))
        print()
        if rental_rate > 14:
            print(colored('Can not rent for more than 14 days!\n', 'red'))
        else:
            taking_out_of_stock(inventory, tool)

            print(
                'A {} has a rental cost of ${} per day (Sales Tax included in total)'.
                format(tool, inventory[tool]['rental cost']))

            print('\nRental Fee has your rental rate included.\n')
            print('Printing Your Receipt!')
            time.sleep(2)
            print(
                '-------------------------------------------------------------------------\n'
            )

            print('\nIn-stock: ', inventory[tool]['stock'])
            print()

            Sales_Tax = core.salestax(inventory, tool)
            Replacement_Deposit = core.replacementdeposit(inventory, tool)
            total = core.rental_sales(inventory, tool, rental_rate)
            disk.write_to_history(total, tool, 'rented', name, rental_rate)

            printing_receipt(inventory, tool, rental_rate, Sales_Tax,
                             Replacement_Deposit, total)

            break


def returning_a_tool(inventory, name):
    while True:
        what_tool = input('\nWhat tool did you have? ').title().strip()
        if what_tool in inventory:
            total = 0
            disk.write_to_history(total, what_tool, 'returned', name)
            adding_back_to_stock(inventory, what_tool)
            print()
            print('In-Stock:', inventory[what_tool]['stock'])
            print('\t\nThank You for returning your tool!\n')
            print("Here is back your Replacement Deposit {}{:.2f}".format(
                '$', core.replacementdeposit(inventory, what_tool)))
            print('\n\tHave a blessed day!!')
            break
        else:
            print(
                colored(
                    '\nYou did not rent that from us, you sure you are at the right place?',
                    'red'))


def employee_side(name, inventory):
    print('\nHow you doing', name)
    seeing_inventory = input(
        '\nWould you like to see the inventory Yes(Y) or No(N)? ').strip()
    print()

    if seeing_inventory in ['Y', 'y']:
        print('Loading the Inventory...')
        time.sleep(1.5)
        here_is_the_inventory(inventory)

    if seeing_inventory in ['N', 'n']:
        print('Thanks for your support')

    total_revenue = input(
        '\nWould you like to see the Total Revenue Yes(Y) or No(N)? ').strip()

    if total_revenue in ['Y', 'y']:
        print('Calculating Total Revenue...\n')
        time.sleep(2.5)
        print("Total Revenue: ${}".format(disk.total_revenue()))

    seeing_history = input(
        '\nWould you like to view previous transactions Yes(Y) or No(N)? '
    ).strip()

    if seeing_history in ['Y', 'y']:
        print('Loading Previous Transactions...\n')
        time.sleep(2.0)
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
            returning_a_tool(inventory, name)
            break
        if help in ['Q', 'q']:
            print()
            print('Have a blessed day', name, 'Come back soon')
            break

        if help in ['R', 'r']:
            print('\nHere is our inventory:')
            time.sleep(1)
            here_is_the_inventory(inventory)
            print()
        tool = input_tool(inventory)
        print('\nRentals are only up to 14 days\n')
        print(
            "\nWith each rental, there is a 10% fee of the products replacement value."
        )
        print()

        renting_a_tool(inventory, tool, name)


def main():
    inventory = disk.load_inventory()
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
    disk.writing_to_inventory(inventory)


if __name__ == '__main__':
    main()
