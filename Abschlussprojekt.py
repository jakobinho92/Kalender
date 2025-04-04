import mein_modul as mm # Import der Funktionen aus dem Modul mein_modul mit dem Aliasname mm


def kalender(): #Kalender-Hauptfunktion, gem. Aufgabenstellung

    unique_id=1 # Eindeutige Nummer, die mit einer 1 (für den ersten Termin) initialisert wird
    
    termine={} # Erstellungen eines leeren Dictionaries um dort die Termine zu speichern, mit unique_id als Schlüssel
    # Grundsätzlicher Aufbau: Schlüssel(unique-id): und erneutes Dictionary für den Termin
    while True:
       try:
            eingabe=int(input("Was wollen Sie tun?\n"
                      "1:Eingabe eines neuen Termins\n"
                      "2:Löschen eines Termins\n3:Bearbeiten eines Termins\n4:Terminliste\n5:Kalenderblatt\n0:Ende"))
            if eingabe not in list(range(0,6)): # Prüfung ob die eingegebene Zahl zwischen 0 und 5 liegt
                print("Ungültige Zahl.Bitte geben Sie die zuvor genannten Zahlen ein(0,1,2,3,4,5)")
                continue # um Schleife erneut zu starten, springt zu Beginn der while-Schleife, Rest wird nicht ausgeführt


       except ValueError: # Ausnahmebehandlung, falls keine Integer Zahl eingegeben worden ist
            print("Allgemein ungültige Eingabe, bitte Zahlen eingeben")
            continue # um Schleife erneut zu starten und Rest nicht auszuführen
       if eingabe==0: # Falls Eingabe =0, wird Programm beendet
           print("Programm wird beendet.")
           break # Beendung der While-Schleife, die immer True ist, durch break
       if eingabe ==1: # Falls die Eingabe 1 ist, wird ein neuer Termin hinzugefügt
           unique_id,termine=mm.neuer_termin(unique_id,termine)# Aufruf des Moduls mein_modul und dort die Funktion
                                                            # neuer_termin. Übergabe der aktuellen Parameter unique_id und termine
                                                            # Am Anfang übergeben: 1 und leeres Dict
       if eingabe ==2:
           unique_id,termine=mm.termin_löschen(unique_id,termine) # Falls Eingabe =2 wird Funktion termin_löschen
                                                                # aufgerufen
       if eingabe ==3:                                          # Aufruf der Funktion termin_bearbeiten
           unique_id,termine=mm.termin_bearbeiten(unique_id,termine)

       if eingabe==4:                                          # Aufruf der Funktion termin_liste
           mm.termin_liste(termine)


       if eingabe==5:                                       # Aufruf der Funktion kalender_blatt
          monat=int(input("Bitte Monat eingeben"))
          jahr=int(input("Bitte Jahr eingeben"))
          mm.kalender_blatt(monat,jahr,termine)


kalender() # Start des Kalender-Programms, Aufruf der Funktion kalender()









