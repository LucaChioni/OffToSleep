# -*- coding: utf-8 -*-

import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.Localizzazione.LocalizInterfaccia as LI


def setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute):
    tipo = tipoId.split("-")[0]

    partiDialogo = []
    nome = "---"
    oggettoDato = False
    avanzaStoria = False
    menuMercante = False
    scelta = False
    avanzaColDialogo = False

    if stanzaDiAppartenenza == GlobalGameVar.dictStanze["vulcano1"]:
        if tipo.startswith("Pazzo"):
            partiDialogo = []
            nome = "Rallo"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                if avanzamentoDialogo == 6:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = -1
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"... Rallo?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"... Immobile... ma com'è arrivato fin qui...?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"... Oh, ha un foglietto...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"... C'è scritto: \"SESTA DOMANDA: che fai?\"...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"... Ma come...?! Poi che senso ha se non puoi neanche sentire la risposta?")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append("???DOMANDA???")
                    dialogo.append(u"... Va beh... sesta domanda... che faccio?")
                    dialogo.append(u"Non lo so.")
                    dialogo.append(u"Vado avanti e guardo che succede.")
                    dialogo.append(u"Sto leggendo un foglietto.")
                    dialogo.append(u"Prendo coscienza di quello che percepisco.")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append("!!!RISPOSTA!!!")
                    dialogo.append(u"...")
                    dialogo.append(u"...")
                    dialogo.append(u"...")
                    dialogo.append(u"...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"...")
                    partiDialogo.append(dialogo)
                elif avanzamentoDialogo == 7:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(u"...")
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(u"(Non ha altri foglietti...)")
                    partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoCumuloImpo":
            partiDialogo = []
            nome = LI.CUMULO_IMPO
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"(È un cumulo di impofrutti...)")
            partiDialogo.append(dialogo)
        elif tipo == "RoboLeggero":
            partiDialogo = []
            nome = LI.IMPO_LEGGERO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Mi sta ignorando...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["vulcano2"]:
        if tipo == "OggettoComputerCostruttore":
            partiDialogo = []
            nome = LI.COMPUTER
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoVistoComputerVulcano"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Ci sono dei simboli luminosi, delle scritte strane e...)")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Oh, quelli sono impo!")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Disegni di diverse specie di impo...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(... Che significa...?)")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Non ho idea di cosa sia questo affare. Ci sono degli impo disegnati sopra...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È il calcolatore di eventi del Costruttore... sta elaborando il prossimo frame...)")
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["vulcano3"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["esclamazionePostRisveglioNelVulcano"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"Impo...")
                partiDialogo.append(dialogo)
        elif tipo == "OggettoCellaCostruttore":
            partiDialogo = []
            nome = LI.SCONOSCIUTO
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo2PostRisveglioNelVulcano"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"... Ehi?")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(C'è un cadavere... ha dei tubi che gli escono dal corpo...)")
                partiDialogo.append(dialogo)
            else:
                nome = LI.COSTRUTTORE
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"...")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È il cadavere del Costruttore... alla fine Neil è riuscito a prendere il suo posto...)")
                partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
