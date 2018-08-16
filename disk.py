import core


def viewing_history():
    lines = ''
    with open('history.txt', 'r') as file:
        for line in file:
            lines = lines + line + '\n'
    return lines


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
