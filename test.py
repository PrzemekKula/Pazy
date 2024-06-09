import csv
import os
import pytest
from datetime import datetime
import main

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Setup: Ensure files are created and then clean up after tests
    initialize_files()
    yield
    # Teardown: Remove test files
    if os.path.exists(CLIENTS_FILE):
        os.remove(CLIENTS_FILE)
    if os.path.exists(APPOINTMENTS_FILE):
        os.remove(APPOINTMENTS_FILE)

def test_initialize_files():
    initialize_files()
    assert os.path.exists(CLIENTS_FILE)
    assert os.path.exists(APPOINTMENTS_FILE)

    with open(CLIENTS_FILE, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        assert headers == ['ID', 'Imię', 'Nazwisko', 'Telefon']

    with open(APPOINTMENTS_FILE, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        assert headers == ['ID', 'ID Klientki', 'Data', 'Usługa', 'Cena Netto', 'Cena Brutto', 'Notatka']

def test_load_clients():
    clients = load_clients()
    assert isinstance(clients, list)

def test_save_client():
    client = {'ID': 1, 'Imię': 'Anna', 'Nazwisko': 'Kowalska', 'Telefon': '123456789'}
    save_client(client)
    clients = load_clients()
    assert clients[0]['ID'] == '1'
    assert clients[0]['Imię'] == 'Anna'
    assert clients[0]['Nazwisko'] == 'Kowalska'
    assert clients[0]['Telefon'] == '123456789'

def test_calculate_gross_price():
    assert calculate_gross_price(100) == 123.0
    assert calculate_gross_price(0) == 0.0
    assert calculate_gross_price(200) == 246.0

def test_validate_date_format():
    assert validate_date_format('01-01-2022') is True
    assert validate_date_format('31-12-2022') is True
    assert validate_date_format('2022-01-01') is False
    assert validate_date_format('01/01/2022') is False

def test_load_appointments():
    appointments = load_appointments()
    assert isinstance(appointments, list)

def test_save_appointment():
    appointment = {
        'ID': 1, 'ID Klientki': 1, 'Data': '01-01-2022', 'Usługa': 'Strzyżenie',
        'Cena Netto': 100.0, 'Cena Brutto': 123.0, 'Notatka': 'Pierwsza wizyta'
    }
    save_appointment(appointment)
    appointments = load_appointments()
    assert appointments[0]['ID'] == '1'
    assert appointments[0]['ID Klientki'] == '1'
    assert appointments[0]['Data'] == '01-01-2022'
    assert appointments[0]['Usługa'] == 'Strzyżenie'
    assert appointments[0]['Cena Netto'] == '100.0'
    assert appointments[0]['Cena Brutto'] == '123.0'
    assert appointments[0]['Notatka'] == 'Pierwsza wizyta'

if __name__ == '__main__':
    pytest.main()
