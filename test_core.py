import core
fake_dict = {
    'Hammer': {
        'name': 'Hammer',
        'rental cost': 10,
        'stock': 17,
        'replacement cost': 45
    }
}


def test_loading_inventory():
    line = ['Hammer, 17, 10, 45']
    result = core.loading_inventory(line)
    assert result == {
        'Hammer': {
            'name': 'Hammer',
            'rental cost': 10,
            'stock': 17,
            'replacement cost': 45
        }
    }


def test_rental_sales():
    rental_rate = 4
    result = core.rental_sales(fake_dict, 'Hammer', rental_rate)
    assert result == 45.2


def test_salestax():
    result = core.salestax(fake_dict, "Hammer")
    assert round(result, 1) == 0.7


def test_replacementdeposit():
    result = core.replacementdeposit(fake_dict, 'Hammer')
    assert result == 4.5
