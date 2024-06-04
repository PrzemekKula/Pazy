
import csv
import os
import platform
from datetime import datetime

CLIENTS_FILE = 'clients.csv'
APPOINTMENTS_FILE = 'appointments.csv'

def clear_terminal():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def initialize_files():
    if not os.path.exists(CLIENTS_FILE):
        with open(CLIENTS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Imię', 'Nazwisko'])

    if not os.path.exists(APPOINTMENTS_FILE):
        with open(APPOINTMENTS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'ID Klientki', 'Data', 'Usługa', 'Cena Netto', 'Cena Brutto', 'Notatka'])

def load_clients():
    clients = []
    with open(CLIENTS_FILE, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            clients.append(row)
    return clients

def save_client(client):
    with open(CLIENTS_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([client['ID'], client['Imię'], client['Nazwisko'], client['Telefon']])


def add_client():
    clear_terminal()
    clients = load_clients()
    client_id = len(clients) + 1
    first_name = input("Podaj imię klientki: ")
    last_name = input("Podaj nazwisko klientki: ")
    phone = input("Podaj numer telefonu: ")
    client = {'ID': client_id, 'Imię': first_name, 'Nazwisko': last_name, 'Telefon': phone}
    save_client(client)
    print("Klientka dodana pomyślnie!")
    input("\nNaciśnij Enter, aby wrócić do menu...")

def view_clients():
    clear_terminal()
    clients = load_clients()
    unique_clients = {client['ID']: client for client in clients}.values()
    print("Lista klientek:")
    for client in unique_clients:
        print(f"{client['ID']}. {client['Imię']} {client['Nazwisko']}")

def load_appointments():
    appointments = []
    with open(APPOINTMENTS_FILE, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            appointments.append(row)
    return appointments

def save_appointment(appointment):
    with open(APPOINTMENTS_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([appointment['ID'], appointment['ID Klientki'], appointment['Data'], appointment['Usługa'], appointment['Cena Netto'], appointment['Cena Brutto'], appointment['Notatka']])

def calculate_gross_price(net_price):
    VAT_RATE = 0.23  # Stawka VAT 23%
    return net_price * (1 + VAT_RATE)

def validate_date_format(date_string):
    try:
        datetime.strptime(date_string, '%d-%m-%Y')
        return True
    except ValueError:
        return False

def add_appointment():
    clear_terminal()
    clients = load_clients()
    if not clients:
        print("Brak klientek w systemie. Dodaj najpierw klientkę.")
        input("\nNaciśnij Enter, aby wrócić do menu...")
        return

    appointments = load_appointments()
    appointment_id = len(appointments) + 1
    print("Lista klientek:")
    for client in clients:
        print(f"{client['ID']}. {client['Imię']} {client['Nazwisko']}")
    client_id = input("Podaj ID klientki: ")
    
    while True:
        date = input("Podaj datę wizyty (DD-MM-RRRR): ")
        if validate_date_format(date):
            break
        else:
            print("Nieprawidłowy format daty. Podaj datę w formacie DD-MM-RRRR.")

    service = input("Podaj rodzaj usługi: ")
    net_price = float(input("Podaj cenę netto usługi: "))
    gross_price = calculate_gross_price(net_price)
    note = input("Dodaj notatkę do wizyty: ")
    appointment = {
        'ID': appointment_id,
        'ID Klientki': client_id,
        'Data': date,
        'Usługa': service,
        'Cena Netto': net_price,
        'Cena Brutto': gross_price,
        'Notatka': note
    }
    save_appointment(appointment)
    print("Wizyta dodana pomyślnie! :)")  
    input("\nNaciśnij Enter, aby wrócić do menu...")

def view_appointments():
    clear_terminal()
    appointments = load_appointments()
    print("Lista wizyt:")
    for appointment in appointments:
        print(f"{appointment['ID']}. Klientka ID: {appointment['ID Klientki']}, Data: {appointment['Data']}, Usługa: {appointment['Usługa']}, Cena Netto: {appointment['Cena Netto']}, Cena Brutto: {appointment['Cena Brutto']}, Notatka: {appointment['Notatka']}")
    input("\nNaciśnij Enter, aby wrócić do menu...")

def main():
    initialize_files()
    while True:
        clear_terminal()
        print("\nMenu główne:")
        print("1. Dodaj klientkę")
        print("2. Wyświetl listę klientek")
        print("3. Dodaj wizytę")
        print("4. Wyświetl listę wizyt")
        print("5. Wyjście")
        choice = input("Wybierz opcję: ")
        if choice == '1':
            add_client()
        elif choice == '2':
            view_clients()
        elif choice == '3':
            add_appointment()
        elif choice == '4':
            view_appointments()
        elif choice == '5':
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

if __name__ == '__main__':
    main()
