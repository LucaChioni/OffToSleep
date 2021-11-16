# -*- coding: utf-8 -*-

import Codice.Variabili.GlobalGameVar as GlobalGameVar


def setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute):
    tipo = tipoId.split("-")[0]

    partiDialogo = []
    nome = "---"
    oggettoDato = False
    avanzaStoria = False
    menuMercante = False
    scelta = False
    avanzaColDialogo = False
    if tipo == "PadreUfficialeServizio":
        partiDialogo = []
        nome = "David"
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoCasaUfficiale"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Eccoci.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"È... enorme...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Avverto che abbiamo ospiti per cena. Seguimi, la sala da pranzo è al piano di sopra.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["giratoDavidVersoIlBasso"]:
            oggettoDato = "Chiave stanza"
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"La tua stanza è già stata preparata, è l'ultima porta a destra di quel corridoio. Vai pure a cambiarti, questa è la chiave.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"E... nella porta in fondo al corridoio c'è il bagno se hai bisogno di darti una ripulita.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"O-ok, grazie. Vado... a darmi una ripulita...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Perfetto, ti aspettiamo.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Vai pure a cambiarti. Quando torni la cena sarà servita.")
            partiDialogo.append(dialogo)
    elif tipo == "ServoDavid":
        partiDialogo = []
        nome = "Servo"
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"] and avanzamentoDialogo == 0:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ehm... salve...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("Salve, posso esserle d'aiuto?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"No, cioè... tu lavori qui?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sì, al momento sono in servizio: se ha bisogno di qualcosa può chiedere a me o agli altri servi. Resterà qui per la notte?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Sì, solo per stanotte.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Perfetto, allora può cambiarsi in una delle stanze per gli ospiti al piano di sopra, il padrone ne starà già facendo preparare una.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Va bene. Grazie.")
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"] and avanzamentoDialogo == 1:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Può cambiarsi in una delle stanze per gli ospiti al piano di sopra, il padrone ne starà già facendo preparare una.")
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sedutoACenaDavid"] and avanzamentoDialogo == 1:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("La cena sta per essere servita, la prego di prendere posto.")
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and avanzamentoDialogo == 1:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Scusa, per caso hai visto se David è passato di qui?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sì, è appena uscito, ma non so dove fosse diretto.")
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and avanzamentoDialogo == 2:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"La prego di andare a riposare, tra poco sarà giorno.")
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Salve signorina, la sua stanza è stata preparata. Può andare a cambiarsi.")
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sedutoACenaDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("La prego di prendere posto, la cena sta per essere servita.")
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"La sua stanza è in fondo al corridoio. Può andare a riposare quando vuole.")
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["vistoDalServo"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Salve. Al momento il padrone non è in casa. Posso esserti d'aiuto?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"No, grazie.")
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["vistoDalServo"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Signorina Sara, cosa ci fa di nuovo qui?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ciao, sono venuta per richiedere il certificato di permanenza in città. Mi servirebbe per andare in biblioteca.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Ah, il certificato! David l'aveva preparato, dev'essersi dimenticato di darglielo. Vado subito a prenderlo.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ok, ma... come mai ci sono dei soldati qui?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Olivia si è fatta male poco fa, non so bene cosa sia successo... dev'essere stato un incidente.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ma... sta bene adesso?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Non so, era priva di sensi quando l'ho trovata e... ha perso molto sangue... Ma non ti devi preoccupare, ci sono i migliori medici della città ad assisterla adesso.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Ora rimani un attimo qui, torno subito con il certificato.")
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["servoArrivaConCertificazione"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Rimani un attimo qui, torno subito con il certificato.")
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["servoArrivaConCertificazione"]:
            oggettoDato = "Certificato di residenza"
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Signorina, ecco il certificato. Era già pronto, come pensavo.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"G-grazie mille...")
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Non mi hanno ancora detto niente della situazione di Olivia.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid3"] and avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Buongiorno signorina, è mattina.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"<*>#italic#Uh?! Ohh...<*> buongiorno...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Cosa desidera per colazione?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"No, non... non importa, non sono solita fare colazione.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Come preferisce. Se cambia idea non si faccia problemi a farlo presente.")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Salve. Al momento il padrone non è in casa. Posso esserti d'aiuto?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"No, grazie.")
            partiDialogo.append(dialogo)
    elif tipo == "MadreUfficiale":
        partiDialogo = []
        nome = "Olivia"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sedutoACenaDavid"] and avanzamentoDialogo == 0:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Salve, mi chiamo Sara.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ehm...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("... Olivia... sono la moglie di David e... la madre di Sam.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ok... piacere.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sedutoACenaDavid"] and avanzamentoDialogo == 1:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Non credo voglia parlarmi, sembra... distratta...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoCenaDavid1"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
    elif tipo == "OggettoLettoCasaDavid":
        partiDialogo = []
        nome = "OggettoLettoCasaDavid"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sedutoACenaDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Questo sarà il mio letto per stanotte. Non vedo l'ora di dormire!)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["fineDialogoCenaDavid"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Sto morendo di sonno... penserò a tutto domani...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["uscitoCasaDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("(Non posso rimetteremi a dormire adesso...)")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(È un letto molto comodo...)")
            partiDialogo.append(dialogo)
    elif tipo == "OggettoArmadioCasaDavid":
        partiDialogo = []
        nome = "OggettoArmadioCasaDavid"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fattoBagnoCasaDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Qua ci sono un po' di vestiti, ma credo che dovrei darmi una \"ripulita\" prima...)")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Ha detto che il bagno è in fondo al corridoio...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoDopoBagnoDavid"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Ok... ci sono un bel po' di vestiti qui... Vediamo... questi sembrano ok...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sedutoACenaDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Ci sono altri vestiti tra cui scegliere, ma questi vanno più che bene...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["sedutoACenaDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Non ho bisogno di altri vestiti...)")
            partiDialogo.append(dialogo)
    elif tipo == "OggettoVascaCasaDavid":
        partiDialogo = []
        nome = "OggettoVascaCasaDavid"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presaChiaveStanzaDaLettoDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Sembra una vasca come quella che usiamo a casa per lavarci. Chissà se mio padre ha preso spunto da una come questa per fare la nostra...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["cambiatoPercorsoDavid"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Ok, credo che questa vasca funzioni più o meno come quella cha abbiamo a casa... vediamo...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sedutoACenaDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Vorrei rientrare in questo piccolo paradiso, ma mi stanno aspettando per la cena...)")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["sedutoACenaDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Non ho bisogno di lavarmi adesso...)")
            partiDialogo.append(dialogo)
    elif tipo == "PadreUfficialeCasa":
        partiDialogo = []
        nome = "David"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sedutoACenaDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Siediti pure, la cena verrà servita a breve.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["cenaConDavidIniziata"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... È buono... cos'è?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Cinghiale in umido, una specialità del posto.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Oh, è davvero... <*>#italic#gnam gnam...<*> molto buono.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"È uno dei piatti che più preferiscono gli abitanti di questa zona. E, da quello che si dice, presto sarà anche il più raro.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Perché \"raro\"?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Pare che i cinghiali si stiano estinguendo. Molti pensano che stiano migrando per i cambiamenti climatici, altri invece incolpano la caccia troppo frequente...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoCenaDavid2"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Beh, sicuramente è la fonte di cibo principale per le persone di passaggio.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sì, per le persone capaci di cacciare quantomeno. Non di certo per i deboli!")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["mammaUfficialeUscitaDallaCena"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... In realtà è solo per via della putrefazione del lago.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Cosa?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Una ventina di anni fa il lago è stato... avvelenato. Non solo per le persone, ma anche per le imbarcazioni. Il legno viene corroso quando entra in contatto con quella poltiglia putrefatta!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"David, che cos'ha Olivia? Non... non credo stia molto bene...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sì... è morto suo figlio.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Cosa?!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Abbiamo bisogno di uomini più forti. Lui era un debole. Lo è sempre stato! E noi non ci possiamo permettere dei deboli a capo delle nostre squadre.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Ma tra poco non avrà più importanza... Non credo ci sia qualcuno capace di fronteggiare quello che sta per succedere.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Cosa... Cosa sta per succedere?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Non ti preoccupare Sara... Sara...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"C'è una guerra in corso?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... Sara... è un bel nome <*>#italic#Sara...<*> mi ricorda quella ragazza al primo anno di addestramento...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"David, c'è una guerra?!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Era così bella...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... E simpatica...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... Sei ubriaco?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"<*>#italic#Umpf!<*> ... Sara... torna nella tua stanza. E dormi, domani dovrai svegliarti presto.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... C'è una guerra che stiamo perdendo, David? E nessuno lo sa?!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Basta così! Smettila di parlare di queste cose!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Anzi, smettila proprio di parlare! Non ho più voglia di continuare a sentire persone che mi fanno sempre più problemi e questioni e... problemi, ogni volta che parlano di... problemi!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Oh!!!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"... E perché mi hai ospitata per cena allora?!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"... <*>#italic#Mmh...<*> <*>#italic#Umpf...<*> Il soldato da cui hai preso quell'armatura d'acciao... dove l'hai seploto?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Che c'entra adesso quel... Oh...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Era... era in mezzo alla foresta, poco distante da un accampamento...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
    elif tipo == "OggettoSediaCasaUfficiale":
        partiDialogo = []
        nome = "OggettoSediaCasaUfficiale"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sedutoACenaDavid"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Mi siederò qui...)")
            partiDialogo.append(dialogo)
    elif tipo == "GuardiaCitta":
        partiDialogo = []
        nome = "Soldato"
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["servoAndatoPrendereCertificazione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Non puoi andare di là. Al momento ci sono delle indagini in corso.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Che cos'è successo?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Stiamo indagando. Sembrerebbe trattarsi di suicidio, ma macano ancora dei presupposti validi... Potrebbe essere stato semplicemente un incidente...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Non puoi passare, ci sono delle indagini in corso.")
                partiDialogo.append(dialogo)

    elif tipo == "OggettoQuadroA":
        partiDialogo = []
        nome = "OggettoQuadro"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Una strada nella foresta...)")
        partiDialogo.append(dialogo)
    elif tipo == "OggettoQuadroB":
        partiDialogo = []
        nome = "OggettoQuadro"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Delle montagne nel buio della notte...)")
        partiDialogo.append(dialogo)
    elif tipo == "OggettoQuadroC":
        partiDialogo = []
        nome = "OggettoQuadro"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Una spiaggia illuminata dal cielo...)")
        partiDialogo.append(dialogo)
    elif tipo == "OggettoVaso":
        partiDialogo = []
        nome = "OggettoVaso"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(È un vaso con degli strani disegni sopra... sembra molto antico...)")
        partiDialogo.append(dialogo)
    elif tipo == "OggettoLibreria":
        partiDialogo = []
        nome = "OggettoLibreria"
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Qua ci sono dei libri... non ne conosco neanche uno...)")
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Ci sono un sacco di libri. Come si fa ad aver voglia di leggere tutta questa roba?)")
            partiDialogo.append(dialogo)
    elif tipo == "OggettoMappamondo":
        partiDialogo = []
        nome = "OggettoMappamondo"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Su questo tavolo è stata incastonata una mappa...)")
        partiDialogo.append(dialogo)
    elif tipo == "OggettoTavoloVaso":
        partiDialogo = []
        nome = "OggettoTavoloVaso"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Un altro tavolo con delle cose sopra per arredare... a che serve?! È solo tempo buttato per le pulizie!)")
        partiDialogo.append(dialogo)
    elif tipo == "OggettoCamino":
        partiDialogo = []
        nome = "OggettoCamino"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Sembra che questo camino non sia mai stato usato...)")
        partiDialogo.append(dialogo)
    elif tipo == "OggettoTavoloMappamondo":
        partiDialogo = []
        nome = "OggettoTavoloMappamondo"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(C'è una mappa come quella al piano di sotto e un modellino molto accurato di una barca...)")
        partiDialogo.append(dialogo)
    elif tipo == "OggettoTavoloBusto":
        partiDialogo = []
        nome = "OggettoTavoloBusto"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Su questo tavolo c'è un altro vaso, una barca e un busto di... \"David VI\"... ? Che sia un antenato di David?)")
        partiDialogo.append(dialogo)
    elif tipo == "OggettoComodinoCasaDavid":
        partiDialogo = []
        nome = "OggettoComodinoCasaDavid"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Non c'è niente in questi cassetti...)")
        partiDialogo.append(dialogo)
    elif tipo == "OggettoGabinetto":
        partiDialogo = []
        nome = "OggettoGabinetto"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Ma è un gabinetto incredibile! Ha anche delle placcature in oro...)")
        partiDialogo.append(dialogo)
    elif tipo == "OggettoLavandinoCasaDavid":
        partiDialogo = []
        nome = "OggettoLavandinoCasaDavid"
        if avanzamentoDialogo == 0 and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presaChiaveStanzaDaLettoDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Probabilmente il lavandino più costoso del mondo...)")
            partiDialogo.append(dialogo)
        elif avanzamentoDialogo == 0 and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Probabilmente il lavandino più costoso del mondo. Ci sono anche un sacco di saponette profumate e...)")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Oooh, quello è uno specchio! È enorme! Noi a casa ne abbiamo uno molto più piccolo che usa soltanto mia madre... lo custodisce gelosamente in un cofanetto...)")
            partiDialogo.append(dialogo)
        elif avanzamentoDialogo == 1 and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fattoBagnoCasaDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"<*>#italic#Ehi, ma che carina questa ragazza.<*>")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Oh, ma salve! Il mio nome è Sara, piacere di conoscerti.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"<*>#italic#Piacere Sara. Hai prorpio un bel viso, sai? Sarebbe perfetto se non fosse per quelle occhiaie...<*>")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Cosa?! Queste non sono occhiaie! Sono solo le luci che fanno dei riflessi...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"<*>#italic#Ed emani anche uno sgradevole odore. Sarebbe proprio il caso che ti dessi una \"ripulita\"!<*>")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"<*>#italic#Uff...<*> mi devo lavare...")
            partiDialogo.append(dialogo)
        elif avanzamentoDialogo == 1 and GlobalGameVar.dictAvanzamentoStoria["fattoBagnoCasaDavid"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Mi sento rigenerata dopo quel bagno. Non ho neanche più quelle fastidiose occhiaie...)")
            partiDialogo.append(dialogo)
        elif avanzamentoDialogo == 2 and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fattoBagnoCasaDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Meglio che mi dia una \"ripulita\" prima di andare a tavola...)")
            partiDialogo.append(dialogo)
        elif avanzamentoDialogo == 2 and GlobalGameVar.dictAvanzamentoStoria["fattoBagnoCasaDavid"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ehi specchio! Chi è che ha le occhiaie adesso?!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"<*>#italic#Tu.<*>")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Cavolo! Perché non vanno via?!")
            partiDialogo.append(dialogo)
        elif avanzamentoDialogo == 3 and GlobalGameVar.dictAvanzamentoStoria["fattoBagnoCasaDavid"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Almeno non puzzo più di sudore come prima...)")
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(Probabilmente il lavandino più costoso del mondo...)")
            partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
