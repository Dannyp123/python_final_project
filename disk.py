def open_file():
    with open('inventory.txt') as file:
        file.readline()
        file_information = file.readlines()
    return file_information
