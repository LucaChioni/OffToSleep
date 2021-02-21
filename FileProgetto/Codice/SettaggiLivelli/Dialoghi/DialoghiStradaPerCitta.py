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
    if tipo.startswith("OggettoCartelloForesta"):
        partiDialogo = []
        nome = "OggettoCartelloForesta"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"C'è scritto: \" - <*>#bold#FORESTA CADETTA<*> - Attenzione alla fauna notturna\".")
        partiDialogo.append(dialogo)
    elif tipo.startswith("OggettoCartelloStaccionata"):
        partiDialogo = []
        nome = "OggettoCartelloStaccionata"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"Su questa staccionata c'è un cartello che dice: \"!!! <*>#bold#VIETATO L'ACCESSO<*> !!!\"...")
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"Da quello che so tutti i passaggi verso oriente sono bloccati da molti anni.")
        partiDialogo.append(dialogo)
    elif tipo == "OggettoCartelloBloccoStrada":
        partiDialogo = []
        nome = "OggettoCartelloBloccoStrada"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"C'è un cartello con la scritta: \"!!! <*>#bold#VIETATO L'ACCESSO<*> !!! - Se oltrepassi questo cartello ti dichiari nemico del reggente cittadino\".")
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"Non credo che Hans sia andato di qua...")
        partiDialogo.append(dialogo)
    elif tipo == "GuardiaCitta":
        partiDialogo = []
        nome = "Soldato"
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["stradaPerCittà1"] and avanzamentoDialogo == 0:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Chiedo scusa soldato...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Stai lontano! Per ordine del Re l'accesso verso oriente è vietato a tutti i civili.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Perché?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("Per ordine del Re.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Sì ok, ma perché il Re lo ha ordinato?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Non mi è concesso divulgare informazioni a riguardo. ")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"E... esiste qualcuno a cui è concesso divulgare informazioni a riguardo?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"È mio compito arrestare chi commette questo illecito.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Oh ok...")
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["stradaPerCittà1"] and avanzamentoDialogo == 1:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Scusa la domanda, ma se è così importante che nessuno passi di qua, perché sei da solo a fare la guardia?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"La strada è già bloccata da questi cartelli e l'unico punto libero è quello in cui sono io adesso, quindi è praticamente impossibile passare.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Cosa?!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Senti, ho studiato personalmente questo sistema di blocco, se trovi un modo per passare provaci pure ma sappi che ne subirai le conseguenze!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ehm... ok... ma uno potrebbe farsi strada nel bosco senza troppi problemi, no?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Di questo non devi preoccuparti, tutti gli accessi verso oriente sono bloccati e ben protetti.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ok...")
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["stradaPerCittà1"] and avanzamentoDialogo == 2:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ehm ehm, dovrei passare...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("Prova a fare un altro passo e ti taglio le gambe!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ok ok, me ne vado.")
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["stradaPerCittà1"] and avanzamentoDialogo == 3:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Devo dire che hai organizzato proprio un bel sistema per bloccare la strada.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sono già abbastanza fiducioso nei miei mezzi, non ho bisogno del tuo giudizio. Adesso vattene che ho molto da fare qui!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ok...")
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["stradaPerCittà1"] and avanzamentoDialogo == 4:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append("(<*>#italic#Meglio lasciarlo al suo lavoro...<*>)")
            partiDialogo.append(dialogo)
    elif tipo.startswith("OggettoBucoPorta"):
        partiDialogo = []
        nome = "OggettoBucoPorta"
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"È chiuso...")
        partiDialogo.append(dialogo)
    elif tipo == "PadreUfficialeServizio":
        partiDialogo = []
        nome = "Soldato"
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivatoAllaPortaDellaCittà"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Chi va là!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Ehm, scusate sono di passaggio, sto cercando un ragazzo che dovrebbe essere passato di qua poco fa...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("Una ragazza! Aprite!")
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["apertoPortaCittà"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("Chi sei e cosa vuoi?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Sono... ehm... mi chiamo Lucy e sto cercando mio fratello. Si chiama Hans e ha più o meno la mia età. Dovrebbe essere passato di qui non molto tempo fa...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("... Sei da sola?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Si.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Mmh... ok... se tuo fratello è in città, è stato allocato in uno degli alloggi profughi. E al momento gli alloggi sono tutti occupati... potrebbe aver preso uno degl'ultimi posti disponibili.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Questo però vuol dire che non c'è più spazio per nessun altro.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Posso dividere la stanza con lui!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Tsk, si certo... non credo proprio, vedi: ogni stanza ha una ventina di letti e ogni letto ospita almeno tre o quattro persone: se un alloggio è al completo significa che lì dentro non c'entra più niente.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("Oh... e come...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"La tua armatura d'acciaio... dove l'hai presa?!")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"Era... l'ho trovata su un cadavere di un soldato nella foresta e ... ho pensato che mi poteva essere utile per arrivare in città...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"E... cosa ne hai fatto del cadavere?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"L'ho sepolto perché non venisse divorato dai lupi e dai cinghiali...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Mmh... senti... per stanotte potrai essere mia ospite: ti farò preparare una stanza. Ma da domani dovrai togliere il disturbo perché, come avrai già intuito, siamo un po' al limite con le risorse.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append("V-va bene, grazie ma... chi sei tu?")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Sono David, ex ufficiale dell'esercito cittadino, ora a comando della guardia notturna.")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(u"Vado a predisporre la guardia per la mia assenza e andiamo.")
            partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
