import csv
import os
import platform

CLIENTS_FILE = 'clients.csv'

def clear_terminal():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def initialize_files():
    if not os.path.exists(CLIENTS_FILE):
        with open(CLIENTS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Imię', 'Nazwisko', 'Telefon'])

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
        elif choice == '5':
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

if __name__ == '__main__':
    main()