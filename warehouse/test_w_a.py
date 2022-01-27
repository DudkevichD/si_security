import unittest
from warehouse_automation import analyse


class TestStringMethods(unittest.TestCase):
    def test_energy_4(self):
        energy_4 = [
            ('принять', 46),
            ('выгрузить', 46),
            ('принять', 21),
            ('выгрузить', 21),
            ]
        self.assertEqual(analyse(energy_4), 4)

    def test_energy_6(self):
        energy_6 = ([
            ('принять', 1),
            ('принять', 2),
            ('выгрузить', 1),
            ('принять', 3),
            ('принять', 4),
            ('выгрузить', 3),
            ])
        self.assertEqual(analyse(energy_6), 6)

    def test_energy_10(self):
        energy_8 = ([
            ('принять', 1),
            ('принять', 2),
            ('принять', 3),
            ('выгрузить', 1),
            ('принять', 4),
            ('выгрузить', 3),
            ])
        self.assertEqual(analyse(energy_8), 8)

    def test_energy_13(self):
        energy_13 = ([
            ('принять', 1),
            ('принять', 2),
            ('принять', 3),
            ('выгрузить', 1),
            ('выгрузить', 2),
            ('принять', 4),
            ('выгрузить', 3),
            ])
        self.assertEqual(analyse(energy_13), 13)


if __name__ == '__main__':
    unittest.main()
