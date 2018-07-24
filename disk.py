def open_file(inventory):
    with open('inventory.txt') as file:
        file.readline()
        file_information = file.readlines()
    return file_information
