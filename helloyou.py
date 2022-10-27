from time import sleep
def printsleep(sleeptime, txt):
    sleep(sleeptime)
    print(txt)

#intro
printsleep (1,"Je bent in Oekraiene, Maar je hoort op de televisie dat de president van Rusland")
printsleep(1,"een aanval wilt doen op Oekraiene, Dus je wilt gaan vluchten uit je land, Maar Naar welk land ga je naartoe? ")
printsleep(1,"En welk land zou veiliger zijn, want je wilt het natuurlijk wel overleven")
printsleep (1,"Het is belangerijk welke kant je opgaat want het kan je einde beinvloeden")

#Polen
keuze1 = input("\nA. Polen\nB. Rusland\n> ").upper()
if keuze1 == "A":
    printsleep(0.5,"\nje bent veilig aangekomen in Polen, dus kan je je voor nu nog even confortabel maken.")
    keuzePolen = input("Na een week later ben er al best lang dus moet je gaan kiezen of je wilt\n \nA.blijven\nB.weggaan\n>").upper()
    if keuzePolen == 'A':
        printsleep(0.5,"Omdat je bent gebleven leidt je nu een leve vol met vrede want je hebt een mooi huis gekocht en een auto, uiteindelijk overlijdt je aan ouderdom.")
    elif keuzePolen == 'B':
        printsleep(0.5,"\nJe hebt er voor gekozen om weg te gaan maar waar wil je naar toe, want je kan hier niet blijven")
        keuzeLand = input ("Naar welk land wil je naar toe gaan?\n \nA.Belgie\nB.Duitsland\n>").upper()
        if keuzeLand == 'A':
            printsleep(0.5,"\nTop, je bent aangekomen in Belgie maar je moet wel je vervoer kiezen naar Nederland dus wat ga je gebruiken?")
            keuzeVervoer = input ("Welk soort vervoersmiddel wil je gebruiken om oop je eindbestemming te komen?\n\nA.Openbaar vervoer\nB.Meeliften\n>").upper()
            if keuzeVervoer == 'A':
                printsleep(0.5,"er was net op het moment dat je er in zat een treinexplosie in de bus, door de explosie lag je in het ziekenhuis met ergen verwondingen en 4 dagen later overleidde je aan de gevolgen van je verwondingen. Je bent helaas dood")
            elif keuzeVervoer == 'B':  
                printsleep(0.5,"Je koos voor om mee te liften, Maar je moet er goed op letten dat je niet weet met wie je meelift dus is het heel risky, Hij bracht je naaar een geheime plek en schoot je. Je bent helaas dood")
        elif keuzeLand == 'B':
            printsleep(0.5,"Top,je bent aangekomen in Duitsland maar je moet wel je vervoer kiezen naar Nederland dus wat ga je gebruiken?")
            keuzevervoer = input ("Kies je voor\n\nA.Openbaar vervoer\nB.Meeliften\n>").upper()
            if keuzevervoer == 'A':
                printsleep(0.5,"Je hebt gekozen voor openbaar vervoer, verstandig")
                paspoort = input ("Nu je naar Nederland bent gereist en er nu bent moet je nog wat dingen regelen (of niet) dus wat ga je doen\n\nA.Paspoort regelen\nB.Niks doen\n>").upper()
                if paspoort == 'A':
                    printsleep(0.5,"Goedzo, De gemeente heeft je aanvraag geaccepteerd omdat je een vluchteling van oorlog bent, ")
                    keuzeWatdoen = input ("Nu je in Nederland bent en een paspoort hebt ben je nog niet klaar.Welke keuze neem je?\n\nA.Geld lenen\nB.Vriendin zoeken\n>").upper()
                    if keuzeWatdoen == 'A':
                        printsleep(0.5,"Je gaat geld lenen bij de hypoteek voor je huis, maar wees voorzichtig. Want als je dit geld verliest of kwijt raakt dan moet je het allemaal terug betalen, dus dan zit je in een dikke schuld")
                        keuzeGeldgebruik = input("Je hebt veel geld geleent, kies wat je er mee wilt doen\n\nA.Vergokken\nB.terugbetalen voor je huis\n>").lower()
                        if keuzeGeldgebruik == 'A':
                            printsleep(0.5,"Al je geld is weg en je heb heel veel schulden, dus pleeg je zelfmoord om de schulden af te lossen omdat je het niet meer ziet zitten, Je bent helaas dood")
                        elif keuzeGeldgebruik == 'B':
                            printsleep(0.5,"Je hebt al het geld terugbetaalt en je leeft een gelukkig leven, je had helaas geen vriend kon vinden.")
                    elif keuzeWatdoen == 'B':
                        printsleep(0.5,"Je bent gaan beginnen met daten. op een date kom je een leuke jongen tegen waarmee je heel veel mee in gemeen heb, 2 maanden later vroeg hij of je zijn vriendin wilt zijn en je zegt: 'Ja!'  ")
                        keuzeVriendin = input ("Je hebt een vriend, maar je hebt een donkere periode in je leven, wat ga je doen?\n\nA.Samen wonen\nB.Vreemdgaan\n>").upper()
                        if keuzeVriendin == 'A':
                            printsleep(0.5,"Je bent gaan samen wonen en hij vroeg je 5 jaar later je ter huwlijk en je zei: 'Ja!'. Je heb je leven helemaal compleet gemaakt ookal begon je als een vluchteling")
                        elif keuzeVriendin == 'B':
                            printsleep(0.5,"Je vriend heeft het uitgemaakt en wilt je nooit meer spreken, hierdoor ben je hopeloos. Je bent helaas af")
                elif paspoort == 'B':
                    printsleep(0.5,"Je hebt ervoor gekozen om niks te doen, maar daar is de gemeente niet van gedient, dus in vergadering met de mensenrechten organisatie is er besloten om je terug naar je eigen land, maar er is nog steeds oorlog dus ben je overleden in een wapengevecht, je bent helaas dood.")
            elif keuzevervoer == 'B':
                printsleep(0.5,"Je hebt ervoor gekozen om bij een vreemd iemand in te stappen. Niet handig want je kent die persoon niet, in dit geval reed de man jouw naar zijn huis en vermoorde hij jou. Je bent dood")
elif keuze1 == "B":
    printsleep(.5, "\nJe bent veilig aangekomen in Rusland, Maar wees wel op je hoeden")
    printsleep(1.5, "Nu je er bent heb je een belangerijke keuze,\n")
    printsleep(1.5, "A.Blijven\nB.Weggaan")
    keuzeRusland = input(">").upper()
    if keuzeRusland == 'A':
        printsleep(0.5,"Je hebt gekozen om te blijven, wat goed! ")
        printsleep(0.5,"Huh, wat is dat, een brief van de Russische regering, in de brief staat of je wilt helpen in het leger maar dat wil je niet dus wat doe je? \n")
        printsleep(0.5,"A. In het leger\nB. Verzetten")
        keuzeRusland2 = input(">").upper()
        if keuzeRusland2 == 'A':
            printsleep(0.5,"Je bent geapakt door Interpol en je bent opgepakt voor verraad, je bent helaas dood")
        elif keuzeRusland2 == 'B': 
            printsleep(0.5,"Je bent opgepakt door de russische rode leger en je zit nu levenslang in de gevangenis")
    elif keuzeRusland == 'B':
        printsleep(0.5,"Je hebt ervoor gekozen om weg te gaan, verstandig. Wacht wat is dat nou? politie!? ze kijken je paspoort en zien dat je uit Oekraiene komt,Je bent helaas doodgeschoten")
