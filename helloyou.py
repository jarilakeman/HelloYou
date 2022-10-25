from time import sleep
def printsleep(sleeptime, txt):
    sleep(sleeptime)
    print(txt)

#intro
printsleep (1,"Je bent in Oekraiene, Maar je hoort op de televisie dat de president van Rusland")
printsleep(1,"een aanval wilt doen op Oekraiene, Dus je wilt gaan vluchten uit je land, Maar Naar welk land ga je naartoe? ")
printsleep (1,"Het is belangerijk welke kant je opgaat want het kan je einde beinvloeden")

keuze1 = input("\nA. Polen\nB. Rusland\n> ").upper()
if keuze1 == "Polen" or  keuze1 == "A":
    print("Nu je veilig bent aangekomen in Polen kan je je confortabel maken.")
    keuzePolen = input("Nu je er bent heb je een belangerijke keuze, Wil je [blijven/weg gaan?]").upper()
    if keuzePolen == 'BLIJVEN':
        print("Je hebt ervoor gekozen om te blijven in polen, Goede keuze want het is best wel veilig\nMaar je komt er achter dat er een hele grote erfenis ligt van je familie. Pak je die?")
    elif keuzePolen == 'WEG GAAN':
        print("")

    print("Nu je veilig bent aangekomen in Polen kan je je confortabel maken.")   
    printsleep(1.5, "Nu je er bent heb je een belangerijke keuze, Wil je [blijven/weg gaan?]")





















#Rusland
elif keuze1 == "Rusland" or keuze1 == "B":
    printsleep(.5, "\nJe bent veilig aangekomen in Rusland, Maar wees wel op je hoeden")
    printsleep(1.5, "Nu je er bent heb je een belangerijke keuze,\n")
    printsleep(1.5, "A.Blijven\nB.Weggaan")
    keuzeRusland = input("\nwil je blijven of weggaan?").upper()
    if keuzeRusland == 'A':
        print("Je hebt gekozen om te blijven, wat goed! ")
        print("Huh, wat is dat, een brief van de Russische regering, in de brief staat of je wilt helpen in het leger maar dat wil je niet dus wat doe je? \n")
        print("A. In het leger\nB. Verzetten")
        keuzeRusland2 = input("wat doe je? ").upper()
        if keuzeRusland2 == 'A':
            print("Je bent geapakt door Interpol en je bent opgepakt voor verraad, je bent helaas dood")
        elif keuzeRusland2 == 'B': 
            print("Je bent opgepakt door de russische rode leger en je zit nu levenslang in de gevangenis")
    elif keuzeRusland == 'B':
        print("")
