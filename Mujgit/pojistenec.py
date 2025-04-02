class Pojistenec:
    def __init__(self, jmeno, prijmeni, vek, telefonni_cislo):
        # Validace vstupních dat pro jméno a příjmení
        if not jmeno or not prijmeni or jmeno.isspace() or prijmeni.isspace():
            raise ValueError("Jméno a příjmení nesmí být prázdné.")

        # Validace věku - číslo musí být kladné
        try:
            vek = int(vek)
            if vek <= 0:
                raise ValueError("Věk musí být kladné číslo.")
        except ValueError:
            raise ValueError("Věk musí být kladné číslo.")

        # Validace telefonního čísla - kontrola formátu a délky
        if not telefonni_cislo.isdigit() or len(telefonni_cislo) < 9:
            raise ValueError("Telefonní číslo musí být platné.")

        self.jmeno = jmeno.strip()
        self.prijmeni = prijmeni.strip()
        self.vek = int(vek)
        self.telefonni_cislo = telefonni_cislo

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, Věk: {self.vek}, Telefon: {self.telefonni_cislo}"
