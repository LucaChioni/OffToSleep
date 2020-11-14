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
    i += 1
    dictAvanzamentoStoria["ingressoForestaCadetta"] = i
    i += 1
    dictAvanzamentoStoria["tutorialCampoVisivo"] = i
    i += 1
    dictAvanzamentoStoria["tutorialDifesa"] = i
    i += 1
    dictAvanzamentoStoria["quartaStanzaForestaCadetta"] = i
    i += 1
    dictAvanzamentoStoria["quintaStanzaForestaCadetta"] = i
    i += 1
    dictAvanzamentoStoria["incontroFiglioUfficiale"] = i
    i += 1
    dictAvanzamentoStoria["trovatoLegna1"] = i
    i += 1
    dictAvanzamentoStoria["trovatoLegna2"] = i
    i += 1
    dictAvanzamentoStoria["trovatoLegna3"] = i
    i += 1
    dictAvanzamentoStoria["legnaDepositata"] = i
    i += 1
    dictAvanzamentoStoria["legnaReportataMichael"] = i
    i += 1
    dictAvanzamentoStoria["inizioNotteForestaCadetta"] = i
    i += 1
    dictAvanzamentoStoria["fineUltimoDialogoSam"] = i
    i += 1
    dictAvanzamentoStoria["attaccoCinghiale"] = i
    i += 1
    dictAvanzamentoStoria["secondoCambioPersonaggio"] = i
    i += 1
    dictAvanzamentoStoria["monologoRisveglioSara"] = i
    i += 1
    dictAvanzamentoStoria["trovatoMappaDiario"] = i
    dictAvanzamentoStoria["mappaCasa"] = i
    i += 1
    dictAvanzamentoStoria["tutorialMappaDiario"] = i
    i += 1
    dictAvanzamentoStoria["monologoIndicazioniArmaturaNonno"] = i
    i += 1
    dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"] = i
    i += 1
    dictAvanzamentoStoria["trovataChiaveRipostiglio"] = i
    i += 1
    dictAvanzamentoStoria["armaturaNonno1"] = i
    i += 1
    dictAvanzamentoStoria["armaturaNonno2"] = i
    i += 1
    dictAvanzamentoStoria["armaturaNonno3"] = i
    i += 1
    dictAvanzamentoStoria["armaturaNonno4"] = i
    i += 1
    dictAvanzamentoStoria["armaturaNonnoCompletata"] = i
    i += 1
    dictAvanzamentoStoria["ingressoForestaCadettaSara"] = i
    dictAvanzamentoStoria["mappaForestaCadetta"] = i

    i += 100
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
    vetStanzePacifiche = []

    # la key del dictionary descrive la stanza
    i = 1
    dictStanze["sognoSara1"] = i
    vetStanzePacifiche.append(i)
    i += 1
    dictStanze["sognoSara2"] = i
    i += 1
    dictStanze["sognoSara3"] = i
    i += 1
    dictStanze["sognoSara4"] = i
    i += 1
    dictStanze["casaSamSara1"] = i
    vetStanzePacifiche.append(i)
    i += 1
    dictStanze["casaSamSara2"] = i
    vetStanzePacifiche.append(i)
    i += 1
    dictStanze["casaSamSara3"] = i
    vetStanzePacifiche.append(i)
    i += 1
    dictStanze["casaSamSara4"] = i
    vetStanzePacifiche.append(i)
    i += 1
    dictStanze["forestaCadetta1"] = i
    i += 1
    dictStanze["forestaCadetta2"] = i
    i += 1
    dictStanze["forestaCadetta3"] = i
    i += 1
    dictStanze["forestaCadetta4"] = i
    i += 1
    dictStanze["forestaCadetta5"] = i
    i += 1
    dictStanze["forestaCadetta6"] = i
    i += 1
    dictStanze["forestaCadetta7"] = i

    return dictStanze, vetStanzePacifiche


def definisciPorte(dictStanze):
    vetPorte = []

    stanza = dictStanze["sognoSara4"]
    vetPorte += [stanza, 15, 9, False]

    stanza = dictStanze["casaSamSara1"]
    vetPorte += [stanza, 6, 9, False]
    vetPorte += [stanza, 7, 6, False]
    vetPorte += [stanza, 25, 3, False]
    vetPorte += [stanza, 26, 11, False]

    stanza = dictStanze["forestaCadetta1"]
    vetPorte += [stanza, 6, 7, False]
    vetPorte += [stanza, 19, 12, False]

    stanza = dictStanze["forestaCadetta2"]
    vetPorte += [stanza, 22, 9, False]
    vetPorte += [stanza, 22, 2, False]
    vetPorte += [stanza, 13, 10, False]

    stanza = dictStanze["forestaCadetta3"]
    vetPorte += [stanza, 12, 7, False]
    vetPorte += [stanza, 16, 9, False]
    vetPorte += [stanza, 16, 15, False]

    stanza = dictStanze["forestaCadetta4"]
    vetPorte += [stanza, 18, 2, False]
    vetPorte += [stanza, 15, 10, False]
    vetPorte += [stanza, 18, 14, False]
    vetPorte += [stanza, 21, 14, False]

    stanza = dictStanze["forestaCadetta6"]
    vetPorte += [stanza, 7, 12, False]
    vetPorte += [stanza, 9, 6, False]
    vetPorte += [stanza, 13, 7, False]
    vetPorte += [stanza, 22, 10, False]
    vetPorte += [stanza, 26, 9, False]

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

    stanza = dictStanze["casaSamSara3"]
    vetCofanetti += [stanza, 21, 10, False]

    stanza = dictStanze["forestaCadetta1"]
    vetCofanetti += [stanza, 8, 2, False]
    vetCofanetti += [stanza, 4, 15, False]
    vetCofanetti += [stanza, 27, 2, False]

    stanza = dictStanze["forestaCadetta2"]
    vetCofanetti += [stanza, 18, 14, False]
    vetCofanetti += [stanza, 11, 2, False]
    vetCofanetti += [stanza, 5, 9, False]
    vetCofanetti += [stanza, 5, 14, False]

    stanza = dictStanze["forestaCadetta3"]
    vetCofanetti += [stanza, 20, 2, False]
    vetCofanetti += [stanza, 5, 13, False]
    vetCofanetti += [stanza, 21, 9, False]

    stanza = dictStanze["forestaCadetta4"]
    vetCofanetti += [stanza, 29, 9, False]
    vetCofanetti += [stanza, 10, 2, False]

    stanza = dictStanze["forestaCadetta6"]
    vetCofanetti += [stanza, 12, 2, False]
    vetCofanetti += [stanza, 21, 2, False]

    return vetCofanetti
