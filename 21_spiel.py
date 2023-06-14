import random
import sys
import time
random.seed
Username2 = ("Computer")
gewinner = ""
Summe = 0
Summe2 = 0

#Todo Gewinnbedingungen checken computer/spieler, differenz checken, wer näher an 21 ist

def leichter_wurf():
    import random
    return random.randint(1, 6)

def mittlerer_wurf():
    import random
    return random.choice([1, 2, 3, 5, 6])

def schwerer_wurf():
    import random
    return random.choice([1, 1, 2, 3, 6, 6])
# Spieler stg ist am zug

Username = input("Wie heißt du Spieler 1?:")
while True:
    print(
        "Bitte wählen sie einen gegner \n" "1: Bob, Schwierigkeitsstufe EINFACH -- Würfel von 1-6 \n" "2: Alex, Schwierigkeitsstufe MITTEL -- Würfel mit 1,2,3,5,6 \n" "3: Felix, Schwierigkeitsstufe SCHWER -- Würfel mit 1,1,2,3,5,6,6")
    eingabe = int(input("Bitte geben sie ihre Eingabe ein: "))
    if eingabe == 1:
        CWurfA = "leicht"
        Username2 = " Bob"
        print("Sie haben", Username2, " Gewählt \n")
    if eingabe == 2:
        CWurfA = "mittel"
        Username2 = " Alex"
        print("Sie haben", Username2, " Gewählt \n")
    if eingabe == 3:
        CWurfA = "schwer"
        Username2 = " Felix"
        print("Sie haben", Username2, " Gewählt \n")
    
    print("Username ist: " + Username)
    Wurf1 = random.randint(1, 6)
    Wurf2 = random.randint(1, 6)
    Wurf3 = random.randint(1, 6)
    time.sleep(1)
    print("-----------------------")
    print("Wurf 1: "+str(Wurf1) + " Wurf 2: "+str(Wurf2) + " Wurf 3: "+str(Wurf3))
    print("-----------------------")
    Summe = Wurf1 + Wurf2 + Wurf3
    EndSumme = Wurf1+Wurf2+Wurf3
    print("")
    print("Augenzahl des Wurfes: "+ str(Summe))
    print("Deine Summe ist " + str(EndSumme))

    # Der Computer ist am zug

    print("Ihr gegner ist" + " " + Username2)
    if CWurfA == "leicht":
        CSumme = leichter_wurf() + leichter_wurf() + leichter_wurf()
    if CWurfA == "mittel":
        CSumme = mittlerer_wurf() + mittlerer_wurf() + mittlerer_wurf()
    if CWurfA == "schwer":
        CSumme = schwerer_wurf() + schwerer_wurf() + schwerer_wurf()
    time.sleep(1)
    print("-----------------------")
    print("Ihr Gegner hat gewürfelt")
    print("-----------------------")
    #print("Wurf1: "+str(CWurf1) + " Wurf2: "+str(CWurf2) + " Wurf3: "+str(CWurf3))
    #CSumme = CWurf1+CWurf2+CWurf3
    #print("Augenzahl des Wurfes: "+ str(CSumme))
    #print("Deine Summe ist " + str(CSumme))

    antwort = input("Möchten Sie weiterspielen? (j/n) ")
    if antwort == "j":
        pass
    else:
        print(EndSumme)
        x = abs(EndSumme - 21)
        print(CSumme)
        y = abs(CSumme - 21)
        if x < y:
            print(Username, " hat gewonnen, Differenz ist", x, " Die Differenz von", Username2, " ist: ", y)
            time.sleep(4)
            continue
        else:
            print(Username2, " hat gewonnen, Differenz ist", y, " Die Differenz von", Username, " ist: ", x)
            time.sleep(4)
            continue

# Spieler stg ist am zug

    print("Username ist: " + Username)
    Wurf1 = random.randint(1, 6)
    Wurf2 = random.randint(1, 6)
    time.sleep(1)
    print("Wurf1: "+str(Wurf1) + " Wurf2: "+str(Wurf2))
    Summe2 = Wurf1+Wurf2
    EndSumme = Summe2 + Summe
    print("Augenzahl des Wurfes: "+ str(Summe2))
    print("Deine Summe ist " + str(EndSumme))
    if EndSumme > 21:
        print("Der Wert ist größer als 21. Der Computer hat gewonnen")
        continue

# Der Computer ist am zug

    print("Ihr gegner" + Username2," ist am zug")
    if CWurfA == "leicht":
        CSumme2 = leichter_wurf() + leichter_wurf()
    if CWurfA == "mittel":
        CSumme2 = mittlerer_wurf() + mittlerer_wurf()
    if CWurfA == "schwer":
        CSumme2 = schwerer_wurf() + schwerer_wurf()
    time.sleep(1)
    print("-----------------------")
    print("Ihr Gegner hat gewürfelt")
    print("-----------------------")
    #print("Wurf1: "+str(CWurf1) + " Wurf2: "+str(CWurf2))
    #CSumme2 = CWurf1+CWurf2
    CEndsumme = CSumme+CSumme2
    #print("Augenzahl des Wurfes: "+ str(CSumme2))
    #print("Deine Summe ist " + str(CEndsumme))
    if CEndsumme > 21:
        print("Der Wert ist größer als 21. Der Spieler hat gewonnen")
        continue

    antwort = input("Möchten Sie weiterspielen? (j/n) ")
    if antwort == "j":
        pass
    else:
        x = abs(EndSumme - 21)
        y = abs(CEndsumme - 21)
        if x < y:
            print(Username, " hat gewonnen, Differenz ist", x, " Die Differenz von", Username2, " ist: ", y)
            time.sleep(4)
            continue
        else:
            print(Username2, " hat gewonnen, Differenz ist", y, " Die Differenz von", Username, " ist: ", x)
            time.sleep(4)
            continue

# Spieler stg ist am zug

    print("Username ist: " + Username)
    Wurf1 = random.randint(1, 6)
    time.sleep(1)
    print("Wurf1: "+str(Wurf1))
    Summe3 = Wurf1
    EndSumme = Summe+Summe2+Summe3
    print("Augenzahl des Wurfes: "+ str(Summe3))
    print("Deine Summe ist " + str(EndSumme))
    if EndSumme > 21:
        print("Der Wert ist größer als 21. Der Computer hat gewonnen")
        continue


    # Der Computer ist am zug

    print("Ihr gegner" + Username2," ist am zug")
    if CWurfA == "leicht":
        CSumme3 = leichter_wurf()
    if CWurfA == "mittel":
        CSumme3 = mittlerer_wurf()
    if CWurfA == "schwer":
        CSumme3 = schwerer_wurf()
    time.sleep(1)
    print("-----------------------")
    print("Ihr Gegner hat gewürfelt")
    print("-----------------------")
    #print("Wurf1: "+str(CWurf1))
    #CSumme3 = CWurf1
    CEndsumme = CSumme+CSumme2+CSumme3
    #print("Augenzahl des Wurfes: "+ str(CSumme3))
    print("Die Summe ist " + str(CEndsumme))
    if CEndsumme > 21:
        print("Der Wert ist größer als 21. Der Spieler hat gewonnen")
    else:
        x = abs(EndSumme - 21)
        y = abs(CEndsumme - 21)
        if x < y:
            print(Username, " hat gewonnen, Differenz ist", x, " Die Differenz von", Username2, " ist: ", y)
            time.sleep(4)
        else:
            print(Username2, " hat gewonnen, Differenz ist", y, " Die Differenz von", Username, " ist: ", x)
            time.sleep(4)

    antwort = input("Möchten Sie weiterspielen? (j/n) ")
    if antwort == "j":
        continue
    else:
        break
