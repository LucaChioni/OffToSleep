# -*- coding: utf-8 -*-

from PersonaggioObj import *


def settaPosizioneERumoriStanza(x, y, npers, rumoreAperturaPorte, rumoreChiusuraPorte, canzoneCambiata, stanza, stanzaVecchia, canzone, inizio):
    # npers: 1=d, 2=a, 3=w, 4=s
    if stanza == GlobalVar.dictStanze["sognoSara1"]:
        if canzone != GlobalVar.canzoneSogno:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneSogno
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["sognoSara2"]:
                npers = 3
                x = GlobalVar.gsx // 32 * 15
                y = GlobalVar.gsy // 18 * 15
    if stanza == GlobalVar.dictStanze["sognoSara2"]:
        if canzone != GlobalVar.canzoneSogno:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneSogno
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["sognoSara1"]:
                npers = 4
                x = GlobalVar.gsx // 32 * 7
                y = GlobalVar.gsy // 18 * 2
            if stanzaVecchia == GlobalVar.dictStanze["sognoSara3"]:
                npers = 2
                x = GlobalVar.gsx // 32 * 29
                y = GlobalVar.gsy // 18 * 3
    if stanza == GlobalVar.dictStanze["sognoSara3"]:
        if canzone != GlobalVar.canzoneSogno:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneSogno
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["sognoSara2"]:
                npers = 1
                x = GlobalVar.gsx // 32 * 2
                y = GlobalVar.gsy // 18 * 11
            if stanzaVecchia == GlobalVar.dictStanze["sognoSara4"]:
                npers = 4
                x = GlobalVar.gsx // 32 * 14
                y = GlobalVar.gsy // 18 * 2
    if stanza == GlobalVar.dictStanze["sognoSara4"]:
        if canzone != GlobalVar.canzoneSogno:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneSogno
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["sognoSara3"]:
                npers = 3
                x = GlobalVar.gsx // 32 * 15
                y = GlobalVar.gsy // 18 * 15
    if stanza == GlobalVar.dictStanze["casaSamSara1"]:
        if canzone != GlobalVar.canzoneCasa:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneCasa
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteCasa
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteCasa
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["sognoSara4"]:
                npers = 4
                x = GlobalVar.gsx // 32 * 3
                y = GlobalVar.gsy // 18 * 14
            if stanzaVecchia == GlobalVar.dictStanze["casaSamSara2"]:
                npers = 3
                if x == GlobalVar.gsx // 32 * 16:
                    x = GlobalVar.gsx // 32 * 16
                    y = GlobalVar.gsy // 18 * 15
                if x == GlobalVar.gsx // 32 * 17:
                    x = GlobalVar.gsx // 32 * 17
                    y = GlobalVar.gsy // 18 * 15
    if stanza == GlobalVar.dictStanze["casaSamSara2"]:
        if canzone != GlobalVar.canzoneCasa:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneCasa
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteCasa
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteCasa
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["casaSamSara1"]:
                npers = 4
                if x == GlobalVar.gsx // 32 * 16:
                    x = GlobalVar.gsx // 32 * 16
                    y = GlobalVar.gsy // 18 * 2
                if x == GlobalVar.gsx // 32 * 17:
                    x = GlobalVar.gsx // 32 * 17
                    y = GlobalVar.gsy // 18 * 2
            if stanzaVecchia == GlobalVar.dictStanze["casaSamSara3"]:
                npers = 4
                if x == GlobalVar.gsx // 32 * 3:
                    x = GlobalVar.gsx // 32 * 3
                    y = GlobalVar.gsy // 18 * 2
                if x == GlobalVar.gsx // 32 * 4:
                    x = GlobalVar.gsx // 32 * 4
                    y = GlobalVar.gsy // 18 * 2
                if x == GlobalVar.gsx // 32 * 27:
                    x = GlobalVar.gsx // 32 * 27
                    y = GlobalVar.gsy // 18 * 2
                if x == GlobalVar.gsx // 32 * 28:
                    x = GlobalVar.gsx // 32 * 28
                    y = GlobalVar.gsy // 18 * 2
            if stanzaVecchia == GlobalVar.dictStanze["casaSamSara4"]:
                npers = 3
                if x == GlobalVar.gsx // 32 * 14:
                    x = GlobalVar.gsx // 32 * 14
                    y = GlobalVar.gsy // 18 * 15
                if x == GlobalVar.gsx // 32 * 15:
                    x = GlobalVar.gsx // 32 * 15
                    y = GlobalVar.gsy // 18 * 15
                if x == GlobalVar.gsx // 32 * 16:
                    x = GlobalVar.gsx // 32 * 16
                    y = GlobalVar.gsy // 18 * 15
                if x == GlobalVar.gsx // 32 * 17:
                    x = GlobalVar.gsx // 32 * 17
                    y = GlobalVar.gsy // 18 * 15
    if stanza == GlobalVar.dictStanze["casaSamSara3"]:
        if canzone != GlobalVar.canzoneCasa:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneCasa
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteCasa
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteCasa
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["casaSamSara2"]:
                npers = 3
                if x == GlobalVar.gsx // 32 * 3:
                    x = GlobalVar.gsx // 32 * 3
                    y = GlobalVar.gsy // 18 * 15
                if x == GlobalVar.gsx // 32 * 4:
                    x = GlobalVar.gsx // 32 * 4
                    y = GlobalVar.gsy // 18 * 15
                if x == GlobalVar.gsx // 32 * 27:
                    x = GlobalVar.gsx // 32 * 27
                    y = GlobalVar.gsy // 18 * 15
                if x == GlobalVar.gsx // 32 * 28:
                    x = GlobalVar.gsx // 32 * 28
                    y = GlobalVar.gsy // 18 * 15
    if stanza == GlobalVar.dictStanze["casaSamSara4"]:
        if canzone != GlobalVar.canzoneCasa:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneCasa
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteCasa
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteCasa
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["casaSamSara2"]:
                npers = 4
                if x == GlobalVar.gsx // 32 * 13:
                    x = GlobalVar.gsx // 32 * 14
                    y = GlobalVar.gsy // 18 * 2
                if x == GlobalVar.gsx // 32 * 14:
                    x = GlobalVar.gsx // 32 * 14
                    y = GlobalVar.gsy // 18 * 2
                if x == GlobalVar.gsx // 32 * 15:
                    x = GlobalVar.gsx // 32 * 15
                    y = GlobalVar.gsy // 18 * 2
                if x == GlobalVar.gsx // 32 * 16:
                    x = GlobalVar.gsx // 32 * 16
                    y = GlobalVar.gsy // 18 * 2
                if x == GlobalVar.gsx // 32 * 17:
                    x = GlobalVar.gsx // 32 * 17
                    y = GlobalVar.gsy // 18 * 2
                if x == GlobalVar.gsx // 32 * 18:
                    x = GlobalVar.gsx // 32 * 17
                    y = GlobalVar.gsy // 18 * 2
            if stanzaVecchia == GlobalVar.dictStanze["forestaCadetta1"]:
                npers = 3
                if x == GlobalVar.gsx // 32 * 15:
                    x = GlobalVar.gsx // 32 * 15
                    y = GlobalVar.gsy // 18 * 15
                if x == GlobalVar.gsx // 32 * 16:
                    x = GlobalVar.gsx // 32 * 16
                    y = GlobalVar.gsy // 18 * 15
    if stanza == GlobalVar.dictStanze["forestaCadetta1"]:
        if canzone != GlobalVar.canzoneForesta:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneForesta
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["casaSamSara4"]:
                npers = 4
                if x == GlobalVar.gsx // 32 * 15:
                    x = GlobalVar.gsx // 32 * 15
                    y = GlobalVar.gsy // 18 * 2
                if x == GlobalVar.gsx // 32 * 16:
                    x = GlobalVar.gsx // 32 * 16
                    y = GlobalVar.gsy // 18 * 2
            if stanzaVecchia == GlobalVar.dictStanze["forestaCadetta2"]:
                npers = 1
                x = GlobalVar.gsx // 32 * 2
                y = GlobalVar.gsy // 18 * 4
    if stanza == GlobalVar.dictStanze["forestaCadetta2"]:
        if canzone != GlobalVar.canzoneForesta:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneForesta
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["forestaCadetta1"]:
                npers = 2
                x = GlobalVar.gsx // 32 * 29
                y = GlobalVar.gsy // 18 * 14
            if stanzaVecchia == GlobalVar.dictStanze["forestaCadetta3"]:
                npers = 3
                x = GlobalVar.gsx // 32 * 12
                y = GlobalVar.gsy // 18 * 15
    if stanza == GlobalVar.dictStanze["forestaCadetta3"]:
        if canzone != GlobalVar.canzoneForesta:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneForesta
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["forestaCadetta2"]:
                npers = 4
                x = GlobalVar.gsx // 32 * 9
                y = GlobalVar.gsy // 18 * 2
            if stanzaVecchia == GlobalVar.dictStanze["forestaCadetta4"]:
                npers = 3
                x = GlobalVar.gsx // 32 * 23
                y = GlobalVar.gsy // 18 * 15
    if stanza == GlobalVar.dictStanze["forestaCadetta4"]:
        if canzone != GlobalVar.canzoneForesta:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneForesta
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["forestaCadetta3"]:
                npers = 4
                x = GlobalVar.gsx // 32 * 26
                y = GlobalVar.gsy // 18 * 2
            if stanzaVecchia == GlobalVar.dictStanze["forestaCadetta5"]:
                npers = 3
                x = GlobalVar.gsx // 32 * 19
                y = GlobalVar.gsy // 18 * 15
    if stanza == GlobalVar.dictStanze["forestaCadetta5"]:
        if canzone != GlobalVar.canzoneForesta:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneForesta
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["forestaCadetta4"]:
                npers = 4
                x = GlobalVar.gsx // 32 * 16
                y = GlobalVar.gsy // 18 * 2
            if stanzaVecchia == GlobalVar.dictStanze["forestaCadetta6"]:
                npers = 2
                x = GlobalVar.gsx // 32 * 29
                y = GlobalVar.gsy // 18 * 8
            if stanzaVecchia == GlobalVar.dictStanze["forestaCadetta7"]:
                npers = 3
                x = GlobalVar.gsx // 32 * 15
                y = GlobalVar.gsy // 18 * 15
    if stanza == GlobalVar.dictStanze["forestaCadetta6"]:
        if canzone != GlobalVar.canzoneForesta:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneForesta
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["forestaCadetta5"]:
                npers = 1
                x = GlobalVar.gsx // 32 * 2
                y = GlobalVar.gsy // 18 * 14

    return x, y, npers, rumoreAperturaPorte, rumoreChiusuraPorte, canzoneCambiata, canzone


def nonPuoiProcedere(avanzamentoStoria, x, y, stanzaVecchia, stanzaDestinazione, canzone):
    nonProcedere = False
    if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["tutorialUtilizzoOggetti"] and stanzaVecchia == GlobalVar.dictStanze["sognoSara1"] and stanzaDestinazione == GlobalVar.dictStanze["sognoSara2"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanzaVecchia, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio, canzone)
        nonProcedere = True
    if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["dialogoCasaSamSara2"] and stanzaVecchia == GlobalVar.dictStanze["casaSamSara1"] and stanzaDestinazione == GlobalVar.dictStanze["casaSamSara2"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanzaVecchia, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio, canzone)
        nonProcedere = True
    if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["incontroFiglioUfficiale"] and stanzaVecchia == GlobalVar.dictStanze["forestaCadetta5"] and stanzaDestinazione == GlobalVar.dictStanze["forestaCadetta6"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanzaVecchia, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio, canzone)
        nonProcedere = True
    if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and stanzaVecchia == GlobalVar.dictStanze["forestaCadetta5"] and stanzaDestinazione == GlobalVar.dictStanze["forestaCadetta7"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanzaVecchia, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio, canzone)
        nonProcedere = True
    return nonProcedere


def possibileAprirePorta(stanza, xPorta, yPorta, avanzamentoStoria):
    procedi = True
    if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and stanza == GlobalVar.dictStanze["casaSamSara1"] and xPorta == GlobalVar.gpx * 25 and yPorta == GlobalVar.gpy * 3:
        procedi = False
    return procedi
