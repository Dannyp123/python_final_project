from bcca.test import (fake_file, should_print)
from disk import *


@fake_file({'history.txt': '''45.2,Hammer,rented
162.1,Drill,rented'''})
def test_viewing_history():
    lines = viewing_history()
    assert lines == '''45.2,Hammer,rented\n\n162.1,Drill,rented\n'''


@fake_file({'inventory.txt': 'Nothing'})
def test_writing_to_inventory():
    inventory = {
        'Hammer': {
            'name': 'Hammer',
            'stock': 14,
            'rental cost': 34,
            'replacement cost': 78
        },
        'Drill': {
            'name': 'Drill',
            'stock': 1,
            'rental cost': 20,
            'replacement cost': 50
        }
    }
    writing_to_inventory(inventory)
    assert open('inventory.txt').read(
    ) == '''Name, In-stock, Rental Cost, Replacement Cost
Hammer,14,34,78
Drill,1,20,50
'''


@fake_file({'inventory.txt': 'Header\nNothing'})
def test_load_inventory():
    assert load_inventory() == ['Nothing']


@fake_file({'history.txt': 'Daniel'})
def test_write_to_history():
    total = 12342
    tool = "Hammer"
    type = 'rented'
    write_to_history(total, tool, type)
    assert open('history.txt').read() == '''Daniel
12342,Hammer,rented\n'''


@fake_file({'history.txt': '23,Hammer\n78,Drill'})
def test_total_revenue():
    assert total_revenue() == 101
