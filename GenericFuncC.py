# -*- coding: utf-8 -*-


def definisciAvanzamentiStoria():
    dictAvanzamentoStoria = {}

    # la key del dictionary descrive l'evento appena compiuto
    i = 0
    dictAvanzamentoStoria["inizio"] = i
    i += 1
    dictAvanzamentoStoria["dialogoSognoSara1"] = i
    i += 1
    dictAvanzamentoStoria["tutorialMovimento"] = i
    i += 1
    dictAvanzamentoStoria["aperturaPrimoCofanetto"] = i
    i += 1
    dictAvanzamentoStoria["tutorialUtilizzoOggetti"] = i
    i += 1
    dictAvanzamentoStoria["tutorialBattaglia"] = i
    i += 1
    dictAvanzamentoStoria["tutorialOggettiBattaglia"] = i
    i += 1
    dictAvanzamentoStoria["dialogoSognoSara2"] = i
    i += 1
    dictAvanzamentoStoria["dialogoSognoSara3"] = i
    dictAvanzamentoStoria["primoCambioPersonaggio"] = i
    i += 1
    dictAvanzamentoStoria["dialogoCasaSamSara1"] = i
    i += 1
    dictAvanzamentoStoria["tutorialChiusuraPorte"] = i
    i += 1
    dictAvanzamentoStoria["ottenutoBicchiere"] = i
    i += 1
    dictAvanzamentoStoria["ottenutoBicchiereAcqua"] = i
    i += 1
    dictAvanzamentoStoria["dialogoCasaSamSara2"] = i

    i += 100
    dictAvanzamentoStoria["secondoCambioPersonaggio"] = i
    i += 1
    dictAvanzamentoStoria["trovatoMappaDiario"] = i
    dictAvanzamentoStoria["mappaCasa"] = i
    i += 1
    dictAvanzamentoStoria["incontratoColco"] = i

    i += 1
    dictAvanzamentoStoria["mercantePozione"] = i
    i += 1
    dictAvanzamentoStoria["mercanteAlimantaz"] = i
    i += 1
    dictAvanzamentoStoria["mercanteMedicina"] = i
    i += 1
    dictAvanzamentoStoria["mercanteSuperPoz"] = i
    i += 1
    dictAvanzamentoStoria["mercanteAlimMiglio"] = i
    i += 1
    dictAvanzamentoStoria["mercanteBomba"] = i
    i += 1
    dictAvanzamentoStoria["mercanteBomVele"] = i
    i += 1
    dictAvanzamentoStoria["mercanteEsca"] = i
    i += 1
    dictAvanzamentoStoria["mercanteBomAppi"] = i
    i += 1
    dictAvanzamentoStoria["mercanteBomPote"] = i

    i += 1
    dictAvanzamentoStoria["mappaForestaCadetta"] = i
    i += 1
    dictAvanzamentoStoria["mappaCittà"] = i
    i += 1
    dictAvanzamentoStoria["mappaSelvaArida"] = i
    i += 1
    dictAvanzamentoStoria["mappaAvampostoDiRod"] = i
    i += 1
    dictAvanzamentoStoria["mappaLabirinto"] = i
    i += 1
    dictAvanzamentoStoria["mappaCastello"] = i
    i += 1
    dictAvanzamentoStoria["mappaPassoMontano"] = i
    i += 1
    dictAvanzamentoStoria["mappaPalazzoDiRod"] = i
    i += 1
    dictAvanzamentoStoria["mappaCaverna"] = i
    i += 1
    dictAvanzamentoStoria["mappaVulcano"] = i
    i += 1
    dictAvanzamentoStoria["mappaTunnelDiRod1"] = i
    i += 1
    dictAvanzamentoStoria["mappaTunnelDiRod2"] = i
    i += 1
    dictAvanzamentoStoria["mappaTunnelSubacqueo"] = i
    i += 1
    dictAvanzamentoStoria["mappaLaboratorio"] = i

    return dictAvanzamentoStoria


def definisciStanze():
    dictStanze = {}

    # la key del dictionary descrive la stanza
    i = 1
    dictStanze["sognoSara1"] = i
    i += 1
    dictStanze["sognoSara2"] = i
    i += 1
    dictStanze["sognoSara3"] = i
    i += 1
    dictStanze["sognoSara4"] = i
    i += 1
    dictStanze["casaSamSara1"] = i
    i += 1
    dictStanze["casaSamSara2"] = i
    i += 1
    dictStanze["casaSamSara3"] = i
    i += 1
    dictStanze["casaSamSara4"] = i

    return dictStanze


def definisciPorte(dictStanze):
    vetPorte = []

    stanza = dictStanze["sognoSara4"]
    vetPorte += [stanza, 15, 9, False]

    stanza = dictStanze["casaSamSara1"]
    vetPorte += [stanza, 6, 9, False]
    vetPorte += [stanza, 7, 6, False]
    vetPorte += [stanza, 25, 3, False]
    vetPorte += [stanza, 26, 11, False]

    return vetPorte


def definisciCofanetti(dictStanze):
    vetCofanetti = []

    stanza = dictStanze["sognoSara1"]
    vetCofanetti += [stanza, 13, 10, False]

    stanza = dictStanze["sognoSara2"]
    vetCofanetti += [stanza, 13, 5, False]
    vetCofanetti += [stanza, 28, 7, False]

    stanza = dictStanze["sognoSara3"]
    vetCofanetti += [stanza, 3, 13, False]

    stanza = dictStanze["casaSamSara1"]
    vetCofanetti += [stanza, 23, 13, False]
    vetCofanetti += [stanza, 24, 15, False]
    vetCofanetti += [stanza, 27, 15, False]
    vetCofanetti += [stanza, 29, 14, False]

    return vetCofanetti
