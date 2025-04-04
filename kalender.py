def schaltjahr(jahr): # Funktion, die überprüft ob das Jahr ein Schaltjahr ist oder nicht
    if jahr%4==0 and jahr%100!=0: # Implementieren der Vorraussetzungen für ein Schaltjahr gem. Aufgabenstellung
        return True
    if jahr%400==0:# Implementieren der Vorraussetzungen gem. Aufgabenstellung
        return True
    return False


def wochentage_bestimmen(tag,monat,jahr): # Funktion, die den Wochentag (Mo-So) für einen bestimmten Tag bestimmt
    tage_monat=[31,28,31,30,31,30,31,31,30,31,30,31] # Anzahl der Tage pro Monat bei normalem Jahr in einer Liste
    wochen_tage=["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"] # Namen Wochentage in
                                                                                                # einer Liste
    if schaltjahr(jahr): # Aufruf der Funktion Schaltjahr, falls True, ändere die Anzahl der Tage von

        tage_monat[1]=29 # Februar auf 29 Tage

    zähler_tage=0 # Implementieren eines Zählers und setzen auf 0

    for i in range(1900,jahr): # Schleife zur Berechnung der Tage von 1900 bis zum Vorjahr des gegebenen Jahres
        if schaltjahr(i):
            zähler_tage=366+zähler_tage # Falls Schaltjahr, Zähler auf 366 Tage setzen
        else:
            zähler_tage=zähler_tage+365 # Ansonsten auf 365 Tage setzen
    for j in range(1,monat):# Schleife zur Berechnung der Tage in den Monaten des gegebenen Jahres vor dem
                            # gegebenen Monat
        zähler_tage=zähler_tage+tage_monat[j-1]

    zähler_tage=zähler_tage+tag-1 # Tage des aktuellen Monats hinzufügen und 1 abziehen, da Starttag nicht mitzählt

    wochentag=zähler_tage%7 # Bestimmung Wochentag durch Rest bei Teilung(0 ist Montag, 1 ist Dienstag)
    return wochen_tage[wochentag]# Rückgabe des Wochentags

def datum_überprüfen(datum): # Funktion die das Datum auf Gültigkeit überprüft
    try:
        tag, monat, jahr = map(int, datum.split('.')) # das eingegebene Datum
                                                    # wird durch split() in Tag,Monat und Jahr aufgeteilt,
                                                    # in einer Liste gespeichert
                                                    # und danach durch map() in Integer-Werten umgewandelt und direkt
                                                    # den Variablen tag, monat und Jahr zugeteilt, Stichwort Unpacking

        if jahr < 1900 or jahr > 2049: # Prüfung, ob ein valides Jahr eingegeben worden ist, zwischen 1900 und 2049
            print("Ungültiges Jahr. Bitte ein Jahr zwischen 1900 und 2049 eingeben.")
            return False
        if monat < 1 or monat > 12: # Prüfung ob ein valider Monat eingegeben worden ist, nur zwischen 1 und 12
            print("Ungültiger Monat. Bitte einen Monat zwischen 1 und 12 eingeben.")
            return False
        tage_monat = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # Liste mit den Tagen pro Monat (normales Jahr)
        if schaltjahr(jahr): # Prüft, ob das Jahr ein Schaltjahr ist
            tage_monat[1] = 29 # Falls Schaltjahr, ändere die Tage des Februars(Index 1) auf 29 Tage
        if tag < 1 or tag > tage_monat[monat - 1]: # Prüfung ob valider Tag eingegeben worden ist, kein negativer Tag oder Tage >Tage des Monats
                                                    # [monat-1], weil Listen-Indexierung bei 0 beginnt)
            print("Ungültiger Tag. Bitte gültigen Tag für den Monat eingeben")
            return False
        # Formatieren auf DD.MM.YYYY
        datum = f"{tag:02}.{monat:02}.{jahr}" # Auffüllen von führenden Nullen, falls Eingabe 1.6. ist
        return datum  # Rückgabe des formatierten Datums
    except ValueError: # Ausnahmebehandlung, falls die Eingabe nicht in Integer umgewandelt werden kann, bzw. zu viele Eingaben oder kein . dazwischen
        print("Ungültiger Wert wurde eingegeben.")
        return False



def zeit_überprüfen(zeit): # Überprüft ob eine valide Zeit eingegeben worden ist
    try:
        stunde, minute = map(int, zeit.split(':')) # gleiche Funktionsweise wie zuvor beim Datum
        if stunde < 0 or stunde > 23 or minute < 0 or minute > 59: # Prüfung auf valide Zeitangaben
            print("Ungültige Zeit-Eingabe.")
            return False
        # Formatieren auf HH:MM
        zeit = f"{stunde:02}:{minute:02}"# Führende Nullen werden ansonsten hinzugefügt, bei 9:5 --> 09:05
        return zeit  # Rückgabe der formatierten Zeit
    except ValueError: # Ausnahmebehandlung, falls die Eingabe nicht in Integer-Wert umgewandelt werden kann
        print("Ungültiger Wert für die Uhrzeit eingegeben. Bitte Zahlen gem. des Uhrzeitformats HH:MM (24h-Format) eingeben.")
        return False



def anzahl_tage_monat(monat,jahr): # berechnet die Anzahl der Tage des Monats
    tage_monat=[31,28,31,30,31,30,31,31,30,31,30,31] # Liste mit den Tagen pro Monat, Januar hat 31 Tage usw.
    if schaltjahr(jahr):       # Aufruf der Schaltjahr Funktion im gleichen Modul
        tage_monat[1]=29       # Falls ja, setze Februar auf 29 Tage
    if monat<1 or monat>12:    # Überprüfen auf falsche Eingabe
        raise ValueError("Falsche Monatsangabe")
    return tage_monat[monat-1]  # Rückgabe der Tage





