import kalender as k # Import des Moduls kalender mit dem Aliasname k

def neuer_termin(unique_id, termine):#Funktion zum Hinzufügen eines neuen Termins, mit den Parametern
                                    # unique_id und termine
    print("Bitte Geben Sie den neuen Termin ein mit dem Format DD.MM.YYYY und HH:MM:")
    while True:
        date_begin=input("Startdatum:")
        ergebnis=k.datum_überprüfen(date_begin) # Überprüfen auf valide Eingabe des Datums mit Funktion aus Modul Kalender
        if ergebnis:                            # Falls valide Eingabe, beende die While-Schleife (if ergebnis
                                                # liefert bei einem Datum true zurück)
            date_begin=ergebnis                 # setze Startdatum
            break
    while True:
        time_begin=input("Startzeit:")          # gleiche Funktionsweise
        ergebnis=k.zeit_überprüfen(time_begin)
        if ergebnis:
            time_begin=ergebnis
            break
    while True:
        date_end=input("Enddatum:")             # gleiche Funktionsweise
        ergebnis=k.datum_überprüfen(date_end)
        if ergebnis:
            date_end=ergebnis
            break
    while True:                                 # gleiche Funktionsweise
        time_end=input("Endzeit:")
        ergebnis=k.zeit_überprüfen(time_end)
        if ergebnis:
            time_end=ergebnis
            break
    title=input("Titel:")
    # Eintrag in das Dict. mit der eind. Nummer als Schlüssel und dem Termin als Wert, was wiederum ein Dict. ist
    termine[unique_id]={"Startdatum": date_begin,
                        "Startzeit": time_begin,"Enddatum":date_end,"Endzeit":time_end, "Titel":title}
    print("Der Termin mit der eindeutigen Nummer {} und mit dem Titel {} wurde hinzugefügt.".format(unique_id,title))
    unique_id+=1 # Erhöhen der eindeutigen Nummer auf die nächste Zahl.
    return unique_id,termine # Rückgabe erforderlich,  wegen Aktualisierung im Hauptprogamm


def termin_löschen(unique_id, termine): # Löscht einen Termin aus dem Dict. Termine, anhand der eind. Nummer
    eingabe=int(input("Bitte eindeutige Nummer eingeben:"))
    if eingabe in termine: # Prüft ob die Nummer in dem Dict als Schlüssel vorhanden ist
        del termine[eingabe] # Falls ja, lösche den Termin
        print("Der Termin mit der Nummer {} wurde gelöscht".format(eingabe)) # Ausgabe des Satzes
    else:
        print("Der Termin existiert nicht") # Falls die eindeutige Nummer nicht vorhanden ist, Ausgabe des Satzes
    return unique_id,termine # Dieser Return für Aktualisierungen im Hauptprogramm

def termin_bearbeiten(unique_id,termine): # Funktion um einen Termin im Dict. zu bearbeiten
    try:
        eingabe=int(input("Bitte eindeutige Nummer eingeben:")) # Abfrage nach der eind. Nummer
    except ValueError: # Ausnahmebehandlung: Falls falsche Eingabe, wie z.b. Buchstabe oder Sonderzeichen, Rückkehr zum Hauptprogramm
        print("Bitte die Nummer als Zahl eingeben")
        return unique_id,termine # Zurück zum Hauptprogramm falls die Eingabe der eind. Nummer keine Zahl ist
    if eingabe in termine:                                  # Falls die Nummer im Dict. als Schlüssel vorhanden ist
        while True:
            print("Was möchten Sie bearbeiten?")
            try:
                eingabe_1=int(input("Um den Starttag zu ändern: 1\n" # Abfrage nach der Art der Änderung
                            "Um den Zeitbeginn zu ändern: 2\n"
                            "Um den Endtermin zu ändern: 3\n"
                            "Um die Endzeit zu ändern: 4\n"
                            "Um den Titel zu ändern: 5\n"
                                    "Um zurück zu gehen: 0\n"))
            except ValueError: # Ausnahmebehandlung, falls z.b. ein Buchstabe wie "a" eingegeben wird
                print("Es wurde keine Zahl eingegeben. Bitte die o.a. Zahlen eingeben.")
                continue    # Falls falsche Eingabe, beende aktuellen Durchlauf der Schleife und starte erneut
            if eingabe_1 == 1:
                eingabe_2=input("Bitte Starttag ändern:")
                termine[eingabe]["Startdatum"]=eingabe_2 # Änderung des Starttages des Termines mit der eind. Nummer
                break
            if eingabe_1==2:
                eingabe_2=input("Bitte Zeitbeginn ändern:") # Änderung Zeitbeginn
                termine[eingabe]["Startzeit"]=eingabe_2
                break
            if eingabe_1==3:
                eingabe_2=input("Bitte Endtermin ändern:")  # Änderung Endtermin
                termine[eingabe]["Enddatum"] =eingabe_2
                break
            if eingabe_1==4:
                eingabe_2=input("Bitte Endzeit ändern:") # Änderung Endzeit
                termine[eingabe]["Endzeit"]=eingabe_2
                break
            if eingabe_1==5:
                eingabe_2=input("Bitte Titel ändern:") # Änderung des Titels
                termine[eingabe]["Titel"]=eingabe_2
                break
            if eingabe_1==0:
                break
            else:
                print("Falsche Zahl für das Bearbeiten eingeben, diese Zahl ist nicht verfügbar.") # Falls Eingabe eine Zahl ist, aber nicht in (0,1,2,3,4,5) enthalten
    else:
        print("Kein Termin mit der eindeutigen Nummer gefunden") # Falls eind. Nummer nicht vorhanden, Rückkehr zum Hauptprogramm

    return unique_id,termine # Dieser Return, damit Änderungen im Hauptprogramm verfügbar bleiben, wobei unique_id nicht geändert wird





def termin_liste(termine):
    # Ausgabe der Überschrift gem. Aufgabenstellung
    print(f"{'Nr.':<4} {'Termin:':<32}{'Beginn:':<21} {'Ende:':<24}")

    # Sortiere die Schlüssel der Termine mit der Funktion des Bubble-Sort-Algorithmus nach Datum, z.B. [2,1,3] statt [1,2,3]
    sortierte_keys = bubble_sort_termine(termine)

    # Ausgabe der sortierten Liste basierend auf den sortierten Schlüsseln
    for unique_id in sortierte_keys:
        termin = termine[unique_id]
        startdatum = termin["Startdatum"]
        startzeit = termin["Startzeit"]
        enddatum = termin["Enddatum"]
        endzeit = termin["Endzeit"]
        titel = termin["Titel"]

        # Zerlege das Start- und Enddatum in Tag, Monat, Jahr
        start_tag, start_monat, start_jahr = map(int, startdatum.split('.'))
        end_tag, end_monat, end_jahr = map(int, enddatum.split('.'))

        # Berechne die abgekürzten Wochentage
        start_wochentag = k.wochentage_bestimmen(start_tag, start_monat, start_jahr)[:2] + "."
        end_wochentag = k.wochentage_bestimmen(end_tag, end_monat, end_jahr)[:2] + "."

        # Formatierte Ausgabe der Tabelle gem. Aufgabenstellung
        print(f"  {unique_id:<2} {titel:<31} {start_wochentag:<4}{start_tag:02d}.{start_monat:02d}.{start_jahr} {startzeit:<6} "
              f"{end_wochentag:<3} {end_tag:02d}.{end_monat:02d}.{end_jahr} {endzeit:<5}")




def kalender_blatt(monat, jahr, termine): # Funktion, die ein Kalenderblatt gem. Aufgabenstellung erstellt anhand von Parametern
    # monat,jahr. Termine in diesen Monat werden mit x markiert
    # Liste von Monatsnamen und Wochentage
    monatsnamen = [
        "Januar", "Februar", "März", "April", "Mai", "Juni",
        "Juli", "August", "September", "Oktober", "November", "Dezember"
    ]
    wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

    # Tage des Monats und Startwochentag
    tage_diesen_monat = k.anzahl_tage_monat(monat, jahr) # Bestimmen der Anzahl der Tage des eingegebenen Monats
    erster_tag = k.wochentage_bestimmen(1, monat, jahr) # Welcher Wochentag fällt auf den 1. Tag des Monats
    erster_tag_index = wochentage.index(erster_tag) # Welcher Index hat der 1. Tag des Monats in der Liste Wochentage

    # Bestimme relevante Termine und bestimme alle Tage zwischen Start- und Enddatum
    termine_fuer_monat = {} # Erstellen leeres Dict. für die möglichen Termine des Monats um diese unter dem Kalenderblatt auszugeben
    tage_mit_termine = set() # Erstellen einer MENGE für die möglichen Tage des Termins des Monats (Ausschluss von doppelter Markierung). Relevant für Markierung im Kalenderblatt
    for nummer in termine:
        termin = termine[nummer]
        start_tag, start_monat, start_jahr = map(int, termin["Startdatum"].split('.'))#.split()-->["5","12","2024"] danach Anwendung Funktion int--> [5,12,2024]
        end_tag, end_monat, end_jahr = map(int, termin["Enddatum"].split('.')) # wird dann direkt den Variablen zugeweisen


    # Prüfen ob der Termin in den aktuellen Monat und Jahr fällt
        if (start_jahr < jahr or (start_jahr == jahr and start_monat <= monat)) and \
                (end_jahr > jahr or (end_jahr == jahr and end_monat >= monat)):
            termine_fuer_monat[nummer] = termin  # Speichere den relevanten Termin

            # Bestimme den ersten Tag des Termins im aktuellen Monat
            if start_jahr == jahr and start_monat == monat:
                start = start_tag
            elif start_jahr < jahr or (start_jahr == jahr and start_monat < monat):
                start = 1  # Interessieren uns nur für den betrachteten Monat, bspw. Termin von 30.11. bis 5.12. und betrachten Dezember

            # Bestimme den letzten Tag des Termins im aktuellen Monat
            if end_jahr == jahr and end_monat == monat:
                end = end_tag
            elif end_jahr > jahr or (end_jahr == jahr and end_monat > monat):
                end = tage_diesen_monat # Interessieren uns nur für den betrachteten Monat, falls Termin vom 25.12. bis 5.1. geht und Dezember betrachten

            #  Alle Tage zwischen Start und Ende des Termins in die Menge speichern
            for tag in range(start, end + 1):
                tage_mit_termine.add(tag)

    # Ausgabe der obersten Zeile des Kalenderblattes gem. Aufgabenstellung, zwei Leerzeilen: Davor und darunter
    print(f"\nMonat: {monatsnamen[monat - 1]}, Jahr: {jahr}\n")

    # Erstellen einer Kalender-Matrix
    kalender_matrix = [[" "] * 7 for i in range(7)]  # 7 Zeilen: 1. Zeile für Wochentage, 6 Zeilen für die Wochen, da ein Monat maximal 6 Wochen hat
                                                    # Kalender hat mind. 4 Wochen (28 Tage bei Nichtschaltjahr und 1. Tag des Monats Montag)
                                                    # und max. 6 Wochen (31 Tage und 1.Tag des Monats Samstag oder Sonntag)
                                                    # 7 Einträge pro Zeile für Wochentage (Mo-So)

    # Fülle die erste Zeile der Matrix mit den Wochentagsnamen
    index = 0
    for wochentag in wochentage:
        kalender_matrix[0][index] = wochentag
        index += 1


    tag_counter = 1 # Zähler für die Tage
    woche = 1       # Beginne bei der ersten Woche

    # Fülle die ERSTE Woche (beginnend mit dem ersten Tag des Monats bei dem entsprechenden Wochentag) mit Tagen in die Matrix
    for tag_index in range(erster_tag_index, 7):  # Von Startwochentag bis Sonntag
        if tag_counter > tage_diesen_monat:      # Abbruch, wenn alle Tage eingetragen sind
            break
        kalender_matrix[woche][tag_index] = tag_counter  # Setze den Tag in die Matrix
        tag_counter += 1  # Erhöhe den Zähler für die Tage

    # Fülle die WEITEREN Wochen
    while tag_counter <= tage_diesen_monat:  # Solange Tage übrig sind
        woche += 1                           # Wechsle zur nächsten Woche
        for tag_index in range(7):           # Montag bis Sonntag
            if tag_counter > tage_diesen_monat:  # Abbruch, wenn alle Tage eingetragen sind
                break
            kalender_matrix[woche][tag_index] = tag_counter  # Setze den Tag in die Matrix
            tag_counter += 1

    # Ausgabe des Kalenders
    for tag_index in range(7):  # Iteriere über die Spalten der Wochentage (Montag bis Sonntag)
        print(f"{kalender_matrix[0][tag_index]:<12}", end="")  # Drucke den Wochentagsnamen

        # Weitere Zeilen: Tage des Monats
        for woche in kalender_matrix[1:]:  # Iteriere über die Wochen (Zeilen), schneide erste Zeile ab mit Wochentagsnamen
            if woche[tag_index] != " ":  # Wenn ein Tag vorhanden ist
                print(f"{woche[tag_index]:>2}  ", end="")  # Drucke den Tag rechtsbündig, end="" wegen Default-Wert von print ("\n") und um Ausgabe gem. Aufgabenstellung zu haben
            else:
                print("    ", end="")  # Leeres Feld
        print()  # Zeilenumbruch

        # Zeile für Markierungen für die Termine
        print(" " * 12, end="")  # Platz für die Wochentagsnamen
        for woche in kalender_matrix[1:]:
            if woche[tag_index] in tage_mit_termine:  # Markiere die Tage mit Terminen
                print(" x  ", end="")
            else:
                print("    ", end="")  # Keine Markierung
        print()  # Zeilenumbruch


    # Ausgabe der Termine gem. Aufgabenstellung
    if termine_fuer_monat: # Prüfung ob das Dict. von termine_fuer_monat nicht leer ist. In Python wird leeres Dict als False gewertet
        termine_ausgeben(termine_fuer_monat) # Aufruf der Funktion termine_ausgeben für das Dict. termine_fuer_monat
    else: # Falls das Dict. termine_fuer_monat leer ist, wird der nachfolgende Satz ausgegeben.
        print("\nKeine Termine für diesen Monat.")


def termine_ausgeben(termine):
    print("\nTermine:")
    # Sortiere die Termine mit Bubble-Sort
    sortierte_termine = bubble_sort_termine(termine) # Gibt eine Liste der eind. Nummer zurück(z.b.[2,1,3]), mit der Sortierung des Startdatums
    for nummer in sortierte_termine: # Iterieren durch die Liste. Es wird durch die Keys-Liste gegangen, welche anhand des Startdatums sortiert ist
        # Bestimmen des Startdatums
        startdatum = termine[nummer]["Startdatum"]
        start_tag, start_monat, start_jahr = map(int, startdatum.split('.'))
        start_wochentag = k.wochentage_bestimmen(start_tag, start_monat, start_jahr)

        # Enddatum
        enddatum = termine[nummer]["Enddatum"]
        end_tag, end_monat, end_jahr = map(int, enddatum.split('.'))
        end_wochentag = k.wochentage_bestimmen(end_tag, end_monat, end_jahr)

        # Start- und Endzeit
        startzeit = termine[nummer]["Startzeit"]
        endzeit = termine[nummer]["Endzeit"]

        # Titel
        titel = termine[nummer]["Titel"]

        # Einstellungen für eine Darstellung gem. Aufgabenstellung, die Nutzung erfolgt in den f-Strings bei der Print-Anweisung
        wochentag_width = 10
        zeit_width = 6
        titel_width = 20

        if (start_tag, start_monat, start_jahr) == (end_tag, end_monat, end_jahr): # Prüft ob es ein eintätiger Termin ist
            # Bei gleichem Tag: Nur eine Zeile mit Startdatum, Wochentag, Zeiten und Titel gem. Aufgabenstellung
            print(f"{start_tag:02}.{start_monat:02}. {start_wochentag:<{wochentag_width}} {startzeit:<{zeit_width}}- {endzeit:<{zeit_width}} {titel:<{titel_width}}")
        else:
            # Mehrtägiger Termin: Zwei Zeilen gem. Aufgabenstellung
            print(f"{start_tag:02}.{start_monat:02}. {start_wochentag:<{wochentag_width}} {startzeit:<{zeit_width}}- {' ':<{zeit_width}} {titel:<{titel_width}}")
            print(f"{end_tag:02}.{end_monat:02}. {end_wochentag:<{wochentag_width}} {' ':<{zeit_width}}- {endzeit:<{zeit_width}} {titel:<{titel_width}}")

def bubble_sort_termine(termine):
    termine_keys = list(termine.keys())  # Erhalte die Schlüssel (die eind. Nummer) des Dictionaries und speichere in Liste, z.b. [1,2,3]
    n = len(termine_keys)

    for i in range(n - 1): # Äußere Schleife, stellt sicher, dass durch "Nach Hintenverschieben" sortiert wird
        for j in range(n - i - 1): # Innere Schleife, vergleicht benachbarte Paare. Vermeidet unnötige Vergleiche, da grösstes Element bereits hinten ist
            # Extrahiere die Startdaten der beiden Termine in einer liste, z.b: startdatum_1=[12,12,2024]
            startdatum_1 = list(map(int, termine[termine_keys[j]]["Startdatum"].split('.')))
            startdatum_2 = list(map(int, termine[termine_keys[j + 1]]["Startdatum"].split('.')))

            # Vergleiche die Daten als Ganzzahlen: Jahr, Monat, Tag
            if (startdatum_1[2], startdatum_1[1], startdatum_1[0]) > (startdatum_2[2], startdatum_2[1], startdatum_2[0]):
                # Tausche die Schlüssel, wenn sie in der falschen Reihenfolge stehen
                # Priorisiert: Jahr dann Monat dann Tag, ein Tupel, also (2024,12,5)>(2024,12,4), elementenweiser Vergleich
                termine_keys[j], termine_keys[j + 1] = termine_keys[j + 1], termine_keys[j] # Tausch der Schlüssel
                                                # Keine Hilfsvariable bei Python nötig, Stichwort Tupel Unpacking

    return termine_keys  # Rückgabe der sortierten Schlüssel, als Liste z.B.:[2,1,3], urspr. Dict. bleibt unverändert


