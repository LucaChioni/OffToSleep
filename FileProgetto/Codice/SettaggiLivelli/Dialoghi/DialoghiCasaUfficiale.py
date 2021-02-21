# -*- coding: utf-8 -*-

import Codice.Variabili.GlobalGameVar as GlobalGameVar


def setDialogo(tipo, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo):
    partiDialogo = []
    nome = "---"
    oggettoDato = False
    avanzaStoria = True
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
            dialogo.append(u"Eccoci...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ma... è enorme...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Avverto che abbiamo ospiti per cena. La sala da pranzo è al piano di sopra, intanto prendi pure posto.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoDavidPrimoPiano"]:
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
            dialogo.append(u"Ok... grazie.")
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
            dialogo.append(u"Ehm... sì. Me lo ha proposto David perché gli alloggi profughi sono tutti occupati.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Perfetto, allora può cambiarsi in una delle stanze per gli ospiti al piano di sopra, il padrone ne starà già facendo preparare una.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Va bene... grazie.")
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
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cenaConDavidIniziata"] and avanzamentoDialogo == 1:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("La cena sta per essere servita, la prego di prendere posto.")
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Salve signorina, la sua stanza è stata preparata, può andare a cambiarsi.")
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cenaConDavidIniziata"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("La prego di prendere posto, la cena sta per essere servita.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Salve signorina, al momento il padrone non è in casa. Può provare a ripassare più tardi se lo desidera.")
            partiDialogo.append(dialogo)
    elif tipo == "MadreUfficiale":
        partiDialogo = []
        nome = "Sara"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cenaConDavidIniziata"] and avanzamentoDialogo == 0:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append("S-salve mi chiamo Lucy.")
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
            dialogo.append("Sara... sono la moglie di David e... la madre di Sam.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Sam? Scusami ma non sono di qui, non lo conosco...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ehm... dovrei conoscerlo? Ricopre un ruolo importante in città o qualcosa del genere?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("... Mh... qualcosa del genere...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ok...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cenaConDavidIniziata"] and avanzamentoDialogo == 1:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(<*>#italic#Non credo voglia parlarmi, sembra... distratta...<*>)")
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
    elif tipo.startswith("OggettoLettoCasaDavid"):
        partiDialogo = []
        nome = "OggettoLettoCasaDavid"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cenaConDavidIniziata"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Questo sarà il mio letto per stanotte. Non vedo l'ora di dormire!")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["fineDialogoCenaDavid"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("... Almeno spero di farmi una bella dormita...")
            partiDialogo.append(dialogo)
    elif tipo.startswith("OggettoArmadioCasaDavid"):
        partiDialogo = []
        nome = "OggettoArmadioCasaDavid"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fattoBagnoCasaDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Qua ci sono un po' di vestiti ma... credo che dovrei darmi una \"ripulita\" prima...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ha detto che il bagno è in fondo al corridoio.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoDopoBagnoDavid"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ok... ci sono un po' di vestiti... questi sembrano i più normali...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cenaConDavidIniziata"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ci sono altri vestiti tra cui scegliere ma questi vanno più che bene.")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["cenaConDavidIniziata"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Non ho bisogno di altri vestiti.")
            partiDialogo.append(dialogo)
    elif tipo.startswith("OggettoVascaCasaDavid"):
        partiDialogo = []
        nome = "OggettoVascaCasaDavid"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presaChiaveStanzaDaLettoDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Sembra una fontana come quella che usiamo a casa per lavarci. È <*>#italic#molto<*> simile... chissà se il babbo ha preso spunto da una come questa per fare la nostra...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["presaChiaveStanzaDaLettoDavid"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Ok credo che questa fontana funzioni più o meno come quella cha abbiamo a casa... vediamo...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cenaConDavidIniziata"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Vorrei rientrare in questo piccolo paradiso ma mi stanno aspettando per la cena...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["cenaConDavidIniziata"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Non ho bisogno di lavarmi adesso.")
            partiDialogo.append(dialogo)
    elif tipo == "PadreUfficialeCasa":
        partiDialogo = []
        nome = "David"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cenaConDavidIniziata"]:
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
            dialogo.append(u"Oh, è... <*>#italic#molto<*> buono.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sì, è uno dei piatti che più preferiscono gli abitanti di questa zona ma, da quello che si dice, presto sarà anche il più raro...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Perché \"raro\"?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Pare che i cinghiali si stiano estinguendo... o forse stanno solo fuggendo dalla foresta...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Per quale motivo?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Non so... forse per via della putrefazione del lago o forse solo per la troppa caccia...")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoCenaDavid2"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Beh, per le persone di passaggio è sicuramente una buona fonte di cibo... sempre che non ci rimangono uccisi...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"")
            partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
