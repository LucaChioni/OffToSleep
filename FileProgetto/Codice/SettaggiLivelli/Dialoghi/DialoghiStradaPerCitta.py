# -*- coding: utf-8 -*-

import GlobalHWVar
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
    if tipo == "OggettoCartelloForesta":
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
    elif tipo == "OggettoCartelloStaccionata":
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
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["stradaPerCittà1"]:
            if avanzamentoDialogo == 0:
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
            elif avanzamentoDialogo == 1:
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
            elif avanzamentoDialogo == 2:
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
            elif avanzamentoDialogo == 3:
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
            elif avanzamentoDialogo == 4:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append("(Meglio lasciarlo al suo lavoro...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["stradaPerCittà3"]:
            if y == GlobalHWVar.gpy * 5:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Benvenuta in città, hai bisogno di qualcosa?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("No no.")
                partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 12:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Salve... si prega di non ingombrare il ponte troppo a lungo.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append("Va bene, ero solo di passaggio.")
                partiDialogo.append(dialogo)
    elif tipo == "OggettoBucoPorta":
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
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["bussatoAllaPortaCittà"]:
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

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
