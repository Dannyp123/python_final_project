import core


def viewing_history():
    lines = ''
    with open('history.txt', 'r') as file:
        for line in file:
            lines = lines + line + '\n'
    return lines


def writing_to_inventory(inventory):
    with open('inventory.txt', 'w') as file:
        file.write('Name, In-stock, Rental Cost, Replacement Cost\n')
        for item in inventory.values():
            line = '{},{},{},{}\n'.format(item['name'], item['stock'],
                                          item['rental cost'],
                                          item['replacement cost'])
            file.write(line)


def load_inventory(file_name):
    with open(file_name, 'r') as file:
        file.readline()
        line = file.readlines()
    return line


def write_to_history(total, tool, type):
    with open('history.txt', 'a') as file:
        file.write(str(total) + ',' + tool + ',' + type + '\n')


def total_revenue():
    total = 0
    with open('history.txt') as file:
        for line in file:
            line = line.split(',')
            total += float(line[0])
        return round(total, 2)
