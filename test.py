import csv
import os
import unittest
from datetime import datetime
from main import *

class TestMainFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        initialize_files()

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(CLIENTS_FILE):
            os.remove(CLIENTS_FILE)
        if os.path.exists(APPOINTMENTS_FILE):
            os.remove(APPOINTMENTS_FILE)

    def test_initialize_files(self):
        initialize_files()
        self.assertTrue(os.path.exists(CLIENTS_FILE))
        self.assertTrue(os.path.exists(APPOINTMENTS_FILE))

        with open(CLIENTS_FILE, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            self.assertEqual(headers, ['ID', 'Imię', 'Nazwisko', 'Telefon'])

        with open(APPOINTMENTS_FILE, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            self.assertEqual(headers, ['ID', 'ID Klientki', 'Data', 'Usługa', 'Cena Netto', 'Cena Brutto', 'Notatka'])

    def test_load_clients(self):
        clients = load_clients()
        self.assertIsInstance(clients, list)

    def test_save_client(self):
        client = {'ID': 1, 'Imię': 'Anna', 'Nazwisko': 'Kowalska', 'Telefon': '123456789'}
        save_client(client)
        clients = load_clients()
        self.assertEqual(clients[0]['ID'], '1')
        self.assertEqual(clients[0]['Imię'], 'Anna')
        self.assertEqual(clients[0]['Nazwisko'], 'Kowalska')
        self.assertEqual(clients[0]['Telefon'], '123456789')

    def test_calculate_gross_price(self):
        self.assertEqual(calculate_gross_price(100), 123.0)
        self.assertEqual(calculate_gross_price(0), 0.0)
        self.assertEqual(calculate_gross_price(200), 246.0)

    def test_validate_date_format(self):
        self.assertTrue(validate_date_format('01-01-2022'))
        self.assertTrue(validate_date_format('31-12-2022'))
        self.assertFalse(validate_date_format('2022-01-01'))
        self.assertFalse(validate_date_format('01/01/2022'))

    def test_load_appointments(self):
        appointments = load_appointments()
        self.assertIsInstance(appointments, list)

    def test_save_appointment(self):
        appointment = {
            'ID': 1, 'ID Klientki': 1, 'Data': '01-01-2022', 'Usługa': 'Strzyżenie',
            'Cena Netto': 100.0, 'Cena Brutto': 123.0, 'Notatka': 'Pierwsza wizyta'
        }
        save_appointment(appointment)
        appointments = load_appointments()
        self.assertEqual(appointments[0]['ID'], '1')
        self.assertEqual(appointments[0]['ID Klientki'], '1')
        self.assertEqual(appointments[0]['Data'], '01-01-2022')
        self.assertEqual(appointments[0]['Usługa'], 'Strzyżenie')
        self.assertEqual(appointments[0]['Cena Netto'], '100.0')
        self.assertEqual(appointments[0]['Cena Brutto'], '123.0')
        self.assertEqual(appointments[0]['Notatka'], 'Pierwsza wizyta')

if __name__ == '__main__':
    unittest.main()
