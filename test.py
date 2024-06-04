import main

def run_simple_tests():
    result = main.calculate_gross_price(100)
    assert result == 123, f"calculate_gross_price(100) Expected 123, but got {result}"
    
    valid_date = '01-01-2022'
    invalid_date = '2022-01-01'
    assert main.validate_date_format(valid_date) == True, f"validate_date_format('{valid_date}') Expected True, but got False"
    assert main.validate_date_format(invalid_date) == False, f"validate_date_format('{invalid_date}') Expected False, but got True"

    try:
        main.initialize_files()
    except Exception as e:
        assert False, f"initialize_files() failed with exception: {e}"

    try:
        clients = main.load_clients()
        assert isinstance(clients, list), f"load_clients() Expected list, but got {type(clients)}"
    except Exception as e:
        assert False, f"load_clients() failed with exception: {e}"

    try:
        test_client = {'ID': 999, 'Imię': 'Test', 'Nazwisko': 'Client', 'Telefon': '123456789'}
        main.save_client(test_client)
    except Exception as e:
        assert False, f"save_client() failed with exception: {e}"

    try:
        appointments = main.load_appointments()
        assert isinstance(appointments, list), f"load_appointments() Expected list, but got {type(appointments)}"
    except Exception as e:
        assert False, f"load_appointments() failed with exception: {e}"

    try:
        test_appointment = {
            'ID': 999, 'ID Klientki': 999, 'Data': '01-01-2022', 'Usługa': 'Test Service',
            'Cena Netto': 100, 'Cena Brutto': 123, 'Notatka': 'Test Note'
        }
        main.save_appointment(test_appointment)
    except Exception as e:
        assert False, f"save_appointment() failed with exception: {e}"

if __name__ == '__main__':
    run_simple_tests()