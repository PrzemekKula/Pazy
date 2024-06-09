## Menu Główne

Po uruchomieniu aplikacji pojawi się menu główne z opcjami do wyboru:

1. Dodaj klientkę
2. Wyświetl listę klientek
3. Dodaj wizytę
4. Wyświetl listę wizyt
5. Wyjście

Wybierz odpowiednią opcję, wpisując jej numer i naciskając Enter.

## Funkcje

### Dodawanie Klientki

1. Wybierz opcję `1` z menu głównego.
2. Podaj imię i nazwisko klientki.
3. Klientka zostanie dodana do systemu.
4. Naciśnij Enter, aby wrócić do menu głównego.

### Wyświetlanie Listy Klientek

1. Wybierz opcję `2` z menu głównego.
2. Zostanie wyświetlona lista wszystkich unikalnych klientek.
3. Naciśnij Enter, aby wrócić do menu głównego.

### Dodawanie Wizyty z Ceną Netto i Notatką

1. Wybierz opcję `3` z menu głównego.
2. Zostanie wyświetlona lista wszystkich klientek.
3. Podaj ID klientki.
4. Podaj datę wizyty w formacie DD-MM-RRRR.
5. Podaj rodzaj usługi.
6. Podaj cenę netto usługi.
7. System automatycznie obliczy cenę brutto.
8. Dodaj notatkę do wizyty (opcjonalnie).
9. Wizyta zostanie dodana do systemu.
10. Naciśnij Enter, aby wrócić do menu głównego.

### Wyświetlanie Listy Wizyt

1. Wybierz opcję `4` z menu głównego.
2. Zostanie wyświetlona lista wszystkich wizyt wraz z informacjami o klientce, dacie, usłudze, cenach netto i brutto oraz notatką.
3. Naciśnij Enter, aby wrócić do menu głównego.

### Zakończenie Pracy

1. Wybierz opcję `5` z menu głównego, aby zakończyć pracę z aplikacją.

## Struktura Plików

- `main.py` - główny plik aplikacji
- `clients.csv` - plik do przechowywania danych klientek
- `appointments.csv` - plik do przechowywania danych wizyt

## Przechowywanie Danych

Dane klientek i wizyt są przechowywane w plikach `clients.csv` oraz `appointments.csv`, co możliwość przeglądania w dowolnym momencie.
