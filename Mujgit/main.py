from pojistenec import Pojistenec
from registr import Registr

# Funkce pro získání údajů od uživatele
def ziskej_udaje():
    jmeno = input("Zadejte jméno: ")
    prijmeni = input("Zadejte příjmení: ")
    vek = input("Zadejte věk: ")
    telefonni_cislo = input("Zadejte telefonní číslo: ")
    return Pojistenec(jmeno, prijmeni, int(vek), telefonni_cislo)

def main():
    registr = Registr()

    # Nekonečná smyčka pro nabídku programu
    volba = 0
    while volba != 4:
        # Zobrazení hlavní nabídky
        print("------------------------------")
        print("Evidence pojištěných")
        print("------------------------------")
        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Konec")

        # Získání volby od uživatele
        volba = input("Vyberte akci: ")

        match volba:
            case "1":  # Přidání pojištěnce
                try:
                    pojistenec = ziskej_udaje()
                    registr.pridat_pojistence(pojistenec)
                    print("Pojištěnec úspěšně přidán.")
                except ValueError as e:
                    print(f"Chyba: {e}")

            case "2":  # Zobrazení všech pojištěnců
                registr.zobrazit_pojistence()

            case "3":  # Vyhledání pojištěnce
                jmeno = input("Zadejte jméno: ")
                prijmeni = input("Zadejte příjmení: ")
                registr.najit_pojistence(jmeno, prijmeni)

            case "4":  # Ukončení programu
                print("Ukončuji program.")
                break

            case _:  # Neplatná volba
                print("Neplatná volba. Zkuste to znovu.")

if __name__ == "__main__":
    main()
