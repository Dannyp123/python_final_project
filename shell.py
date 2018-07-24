import disk
import core


def main():
    inventory_raw_info = disk.open_file('inventory.txt')
    inventory_dictionary = core.create_inventory_dictionary(inventory_raw_info)

    print("Welcome to Daniel's Tool Rental!")

    print(inventory_dictionary)
    name = input("What is the name for this rental? ")
    who_are_you = input("Are you a Employee or a Customer? ").strip().title()
    while True:
        if who_are_you == 'Employee':
            print('Checking the inventory!')
        elif who_are_you == 'Customer':
            help = input("Would you like to rent a Tool or see our inventory? "
                         ).strip()
        if help in ['See our inventory', 'see our inventory']:
            print(file_information)
        if help in ['rent', 'rent a tool', 'rent a Tool']:
            tool = input('OK, what tool would you like to rent? ').strip()
            print(inventory_dictionary)
            if tool in ['Hammer', 'hammer']:
                print('Rental Cost for', tool, 'is $ 24.0')
            elif tool in ['Drill', 'drill']:
                print('Rental Cost for', tool, 'is $ 55.0')
            elif tool in ['Saw', 'saw']:
                print('Rental Cost for', tool, 'is $ 15.0')
            elif tool in ['Screwdriver', 'screwdriver']:
                print('Rental Cost for', tool, 'is $ 20.0')
        # renting_tool = inventory[tool]
        # renting_tool['In-stock'] -= 1


if __name__ == '__main__':
    main()
