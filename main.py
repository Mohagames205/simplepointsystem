import random
import json

#mogelijke antwoorden
positive = ["ja", "jaa", "uhu", "yes", "y", "yeah", "jup"]
negative = ["nope", "neen", "n", "no", "noppes", "neej", "nee"]
#Identificatie
print("Version: 1.1 Super Save Update")
print("Hey en welkom bij een stukje Code van Mohamed, hier test ik mijn skills in een 'fictief' spel")
al = input("Heb je dit spel al eerder gespeeld? ")
al = al.lower()
if al in positive:
  wbj = input("Wie ben jij dan? Typ je naam CORRECT In ")
  with open("data.json", "r") as read_file:
      bestand = json.load(read_file)
  bestand = bestand[wbj]
  geld = bestand["Geld"]
  leeftijd = bestand["Leeftijd"]
  naam = wbj
else:
  #registrering
  naam = input("Hey, wat is je naam? ")
  print("Oh hey {}, aangenaam kennis te maken!".format(naam))
  leeftijd = input("Hoe oud ben jij {}? ".format(naam))
  leeftijd = str(leeftijd)
  antwoord = input("Oh dus even om zeker te zijn, jij bent " + naam + " en je bent " + leeftijd + " jaar oud, heb ik het juist? ")
  antwoord = antwoord.lower()

  if antwoord in positive:
      print("")

  elif antwoord in negative:
      edit = input("Oei dan zullen we je gegevens aanpassen. Wat wil je aanpassen? Je naam of je leeftijd? ")
      edit = edit.lower()
      naamk = ["mijn naam", "naam", "name", "my name"]
      leeftijdk = ["mijn leeftijd", "leeftijd", "age", "my age", "hoe oud ik ben"]
      if edit in naamk:
          naam = input("Okay wat moet je naam dan zijn? ")
          print("Je naam is succesvol aangepast naar {}" .format(naam))

      elif edit in leeftijdk:
          leeftijd = input("Ok wat is je juiste leeftijd dan? ")
          print("Je leeftijd is succesvol aangepast naar {}" .format(leeftijd))
      else:
          print("Je hebt geen geldig antwoord opgegeven!")

  print("Okay we gaan verder met het instellen van het spel!")
  cheatkeuze = input("Zou jij cheat mode aan willen hebben of niet? ")

  if cheatkeuze in positive:
      geld = input("Oké typ het begin bedrag in: ")
      print("Oki je begint dus met {} MCoins" .format(geld))

  else:
      geld = 500

while True:
  print("Je hebt nu {} MCoins" .format(geld))
  print("")
  print("We gaan een paar testen doen om te kijken als het systeem goed werkt! Je kan zelf kiezen welke test")
  testkeuze = input("Kies een test: \n1. Testaankoop \n2. Geld resetten \n3. Geld waarde veranderen \n4. Aan het rad draaien \n5. Je persoonlijke gegevens bekijken \n6. Afsluiten \nTyp een getal: ")

  if testkeuze == "1":
      print(" Je kan kiezen tussen de dingen hieronder: \n1. Bananen: 50$ \n2. Appels: 20$ \n3. Perzikken: 90$")
      aankoop = input("Je kan kiezen door het nummer in te typen: ")

      if aankoop == "1":
          geld = int(geld)
          geld = geld - 50
          geld = str(geld)
          print("Je hebt het gekocht! Je hebt nu {} MCoins over" .format(geld))

      if aankoop == "2":
        geld = int(geld)
        geld = geld - 20
        geld = str(geld)
        print("Je hebt het gekocht! Je hebt nu {} MCoins over" .format(geld))

      if aankoop == "3":
        geld = int(geld)
        geld = geld - 90
        geld = str(geld)
        print("Je hebt het gekocht! Je hebt nu {} MCoins over" .format(geld))
    
  elif testkeuze == "2":
      geld = 0
      geld = str(geld)
      print("Dat is done! Je hebt nu {} MCoins".format(geld))

  elif testkeuze == "3":
      ga = input("Hoeveel MCoins moet je huidige balans worden?")
      ga = int(ga)
      geld = ga
      geld = str(geld)
      print("Je hebt nu {} MCoins!" .format(geld))

  elif testkeuze == "4":
    draai = input("Typ 'draai' om te draaien aan het rad!")
    if draai == "draai":
      plusgeld = random.randint(29, 1000)
      geld = int(geld)
      geld = plusgeld + geld
      geld = str(geld)
      print("Je hebt {} erbij gekregen!" .format(plusgeld))
      print("Uw balans is gewijzigd naar {}! Woehoew :)" .format(geld))

  elif testkeuze == "5":
    print("Jouw persoonlijke data:")
    print("Het aantal geld dat je bezit: {}" .format(geld))
    print("Jouw voornaam/nicknaam: {}" .format(naam))
    print("Jouw leeftijd: {}" .format(leeftijd))
    keuzepf = input("1. Terug naar het hoofdmenu\n2. Mijn gegevens bewerken\nTyp een getal in: ")
    if keuzepf == "1":
      print("Oki,aan het terug keren naar het hoofdmenu..")
    elif keuzepf == "2":
      edit = input("Oké, wat wil je aanpassen?")
      edit = edit.lower()
      naamk = ["mijn naam", "naam", "name", "my name"]
      leeftijdk = ["mijn leeftijd", "leeftijd", "age", "my age", "hoe oud ik ben"]
      if edit in naamk:
          naam = input("Naar wat wil je jouw naam wijzigen? ")
          print("Je naam is succesvol aangepast naar {}" .format(naam))

      elif edit in leeftijdk:
          leeftijd = input("Naar wat wil jij je leeftijf aanpassen? ")
          print("Je leeftijd is succesvol aangepast naar {}" .format(leeftijd))
      else:
          print("Je hebt geen geldig antwoord opgegeven!")
  #afsluit module
  elif testkeuze == "6":
    print("Programma wordt afgesloten! Tot de volgende keer")
    break

  elif testkeuze == "7":
    print("Done, check nu de JSON file")

  elif testkeuze == "8":
      print("Het spel wordt opgestart momentje")

#opslaag module
  data = {
      naam: {
          "Leeftijd": leeftijd,
          "Geld": geld
      }
  }
  with open("data.json") as read_file:
      json_file = json.load(read_file)

  json_file.update(data)

  with open("data.json", "w") as write_file:
      json.dump(json_file, write_file)
