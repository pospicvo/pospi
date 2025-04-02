from pojistenec import Pojistenec

class Registr:
    def __init__(self):
        self.seznam_pojistencu = []

    # Metoda pro přidání pojištěnce do evidence
    def pridat_pojistence(self, pojistenec):
        self.seznam_pojistencu.append(pojistenec)  # Přidání pojištěnce do seznamu

    # Metoda pro výpis všech pojištěnců
    def zobrazit_pojistence(self):
        # Kontrola, zda seznam není prázdný
        if not self.seznam_pojistencu:
            print("Žádní pojištěnci nejsou evidováni.")
        else:
            for pojistenec in self.seznam_pojistencu:
                print(pojistenec)

    # Metoda pro vyhledání pojištěnce dle jména a příjmení
    def najit_pojistence(self, jmeno, prijmeni):
        nalezeni = [p for p in self.seznam_pojistencu if p.jmeno == jmeno and p.prijmeni == prijmeni]

        # Výpis výsledků hledání
        if nalezeni:
            # Výpis nalezených pojištěnců
            for pojistenec in nalezeni:
                print(pojistenec)
        else:
            print("Pojištěnec nenalezen.")
