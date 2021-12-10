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
        dialogo.append(u"(C'è scritto: \" - <*>#bold#FORESTA CADETTA<*> - Attenzione alla fauna notturna\"...)")
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
        dialogo.append(u"(Su questa staccionata c'è un cartello che dice: \"!!! <*>#bold#VIETATO L'ACCESSO<*> !!!\"...)")
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Da quello che so, tutti i passaggi verso oriente sono bloccati da anni...)")
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
        dialogo.append(u"(C'è un cartello con la scritta: \"!!! <*>#bold#VIETATO L'ACCESSO<*> !!! - Se oltrepassi questo cartello, ti dichiari nemico del reggente cittadino\"...)")
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("tu")
        dialogo.append(u"(Non credo che Hans sia andato di qua...)")
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
                dialogo.append(u"Stai lontano! L'accesso verso oriente è vietato a tutti i civili per ordine del Re.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ma io volevo... perché è vietato?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Non mi è concesso divulgare informazioni a riguardo.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Esiste qualcuno a cui è \"concesso\"?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"È mio compito arrestare chi commette quest'illecito.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#Mmh...<*>")
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Ma se è così importante che nessuno passi di qua, perché sei da solo a fare la guardia?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"La strada è già bloccata da questi cartelli e l'unico punto libero è quello in cui sono io adesso. È praticamente impossibile passare.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Cosa...?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Senti, ho studiato personalmente questo sistema di blocco, se trovi un modo per passare provaci pure, ma sappi che ne subirai le conseguenze!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok... ma uno potrebbe farsi strada nel bosco senza troppi problemi, no?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Di questo non devi preoccuparti, tutti gli accessi verso oriente sono bloccati e ben protetti.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok...")
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 2:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"<*>#italic#Ehm ehm,<*> dovrei passare...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Prova a fare un altro passo e ti taglio le gambe!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Ok ok... me ne vado...")
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 3:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Devo dire che hai organizzato proprio un bel sistema per bloccare la strada.")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Sono già abbastanza fiducioso nei miei mezzi, non ho bisogno del giudizio altrui. Adesso vattene, ho molto da fare qui!")
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 4:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Meglio lasciarlo al suo lavoro...)")
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["stradaPerCittà3"]:
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non voglio parlare coi soldati... poi potrebbero insospettirsi per Impo...)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Meglio risparmiarsi le conversazioni coi soldati, non ho voglia di... potrebbero chiedermi qualcosa sull'omicidio...)")
                partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 5:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"Benvenuta in città. Se sei in cerca di un posto sicuro per riposare, rivolgiti agli alloggi profughi.")
                partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 12:
                if avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Salve, soldato.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Salve. Si prega di non ingombrare il ponte troppo a lungo! È necessario che sia sempre il più fruibile possibile.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Oh, mi stavo giusto chiedendo perché non ci fosse nessuno qui...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Perché è un ponte... serve per attraversare il fiume, non per ostruire il passaggio!")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Ok, ma tu invece? Non lo stai ostruendo?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"No. Dev'esserci qualcuno che lo mantenga libero. Altrimenti sarebbe pieno di persone che, come te, bloccherebbero un traffico di persone che lo vuole attraversare solo per stanci sopra!")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"A me sembra che l'unico traffico qui sia composto da due guardie che stanno sul ponte senza neanche attraversarlo...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Due guardie che mantengono il ponte libero dal traffico!")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"Certo. Dico solo che, senza tutte quelle guardie, il ponte sarebbe sicuramente più libero e fruibile, tutto qui...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Senti ragazzina, non ho altro tempo da perdere! Vai dove devi andare senza ostruire il passaggio!")
                    partiDialogo.append(dialogo)
                elif avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"Vai dove devi andare senza ostruire il passaggio!")
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
        dialogo.append(u"(È chiuso...)")
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
            dialogo.append("Scusate sono di passaggio... sto cercando un ragazzo che dovrebbe essere passato di qua poco fa...")
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append("Una ragazza! Aprite!")
            partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
