# -*- coding: utf-8 -*-

from PersonaggioObj import *


def settaPosizioneERumoriStanza(x, y, npers, rumoreAperturaPorte, rumoreChiusuraPorte, canzoneCambiata, sottofondoAmbientaleCambiato, stanza, stanzaVecchia, canzone, sottofondoAmbientale, inizio):
    # npers: 1=d, 2=a, 3=w, 4=s
    if stanza == GlobalVar.dictStanze["sognoLucy1"]:
        if canzone != GlobalVar.canzoneSogno:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneSogno
        if sottofondoAmbientale != GlobalVar.audioAmbienteSogno:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalVar.audioAmbienteSogno
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["sognoLucy2"]:
                npers = 3
                x = GlobalVar.gsx // 32 * 15
                y = GlobalVar.gsy // 18 * 15
    if stanza == GlobalVar.dictStanze["sognoLucy2"]:
        if canzone != GlobalVar.canzoneSogno:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneSogno
        if sottofondoAmbientale != GlobalVar.audioAmbienteSogno:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalVar.audioAmbienteSogno
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["sognoLucy1"]:
                npers = 4
                x = GlobalVar.gsx // 32 * 7
                y = GlobalVar.gsy // 18 * 2
            if stanzaVecchia == GlobalVar.dictStanze["sognoLucy3"]:
                npers = 2
                x = GlobalVar.gsx // 32 * 29
                y = GlobalVar.gsy // 18 * 3
    if stanza == GlobalVar.dictStanze["sognoLucy3"]:
        if canzone != GlobalVar.canzoneSogno:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneSogno
        if sottofondoAmbientale != GlobalVar.audioAmbienteSogno:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalVar.audioAmbienteSogno
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["sognoLucy2"]:
                npers = 1
                x = GlobalVar.gsx // 32 * 2
                y = GlobalVar.gsy // 18 * 11
            if stanzaVecchia == GlobalVar.dictStanze["sognoLucy4"]:
                npers = 4
                x = GlobalVar.gsx // 32 * 14
                y = GlobalVar.gsy // 18 * 2
    if stanza == GlobalVar.dictStanze["sognoLucy4"]:
        if canzone != GlobalVar.canzoneSogno:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneSogno
        if sottofondoAmbientale != GlobalVar.audioAmbienteSogno:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalVar.audioAmbienteSogno
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["sognoLucy3"]:
                npers = 3
                x = GlobalVar.gsx // 32 * 15
                y = GlobalVar.gsy // 18 * 15
    if stanza == GlobalVar.dictStanze["casaSamLucy1"]:
        if canzone != GlobalVar.canzoneCasa:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneCasa
        if sottofondoAmbientale != GlobalVar.audioAmbienteCasaInterno:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalVar.audioAmbienteCasaInterno
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteCasa
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteCasa
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["sognoLucy4"]:
                npers = 4
                x = GlobalVar.gsx // 32 * 3
                y = GlobalVar.gsy // 18 * 14
            if stanzaVecchia == GlobalVar.dictStanze["casaSamLucy2"]:
                npers = 3
                if x == GlobalVar.gsx // 32 * 16:
                    x = GlobalVar.gsx // 32 * 16
                    y = GlobalVar.gsy // 18 * 15
                if x == GlobalVar.gsx // 32 * 17:
                    x = GlobalVar.gsx // 32 * 17
                    y = GlobalVar.gsy // 18 * 15
            if stanzaVecchia == GlobalVar.dictStanze["forestaCadetta5"]:
                npers = 4
                x = GlobalVar.gsx // 32 * 4
                y = GlobalVar.gsy // 18 * 14
    if stanza == GlobalVar.dictStanze["casaSamLucy2"]:
        if canzone != GlobalVar.canzoneCasa:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneCasa
        if sottofondoAmbientale != GlobalVar.audioAmbienteCasaEsterno:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalVar.audioAmbienteCasaEsterno
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteCasa
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteCasa
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["casaSamLucy1"]:
                npers = 4
                if x == GlobalVar.gsx // 32 * 16:
                    x = GlobalVar.gsx // 32 * 16
                    y = GlobalVar.gsy // 18 * 2
                if x == GlobalVar.gsx // 32 * 17:
                    x = GlobalVar.gsx // 32 * 17
                    y = GlobalVar.gsy // 18 * 2
            if stanzaVecchia == GlobalVar.dictStanze["casaSamLucy3"]:
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
            if stanzaVecchia == GlobalVar.dictStanze["casaSamLucy4"]:
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
    if stanza == GlobalVar.dictStanze["casaSamLucy3"]:
        if canzone != GlobalVar.canzoneCasa:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneCasa
        if sottofondoAmbientale != GlobalVar.audioAmbienteCasaEsterno:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalVar.audioAmbienteCasaEsterno
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteCasa
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteCasa
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["casaSamLucy2"]:
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
    if stanza == GlobalVar.dictStanze["casaSamLucy4"]:
        if canzone != GlobalVar.canzoneCasa:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneCasa
        if sottofondoAmbientale != GlobalVar.audioAmbienteCasaEsterno:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalVar.audioAmbienteCasaEsterno
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteCasa
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteCasa
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["casaSamLucy2"]:
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
        if sottofondoAmbientale != GlobalVar.audioAmbienteForesta:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalVar.audioAmbienteForesta
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["casaSamLucy4"]:
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
        if sottofondoAmbientale != GlobalVar.audioAmbienteForesta:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalVar.audioAmbienteForesta
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
        if sottofondoAmbientale != GlobalVar.audioAmbienteForesta:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalVar.audioAmbienteForesta
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
        if sottofondoAmbientale != GlobalVar.audioAmbienteForesta:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalVar.audioAmbienteForesta
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
        if sottofondoAmbientale != GlobalVar.audioAmbienteForesta:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalVar.audioAmbienteForesta
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["forestaCadetta4"]:
                npers = 4
                x = GlobalVar.gsx // 32 * 16
                y = GlobalVar.gsy // 18 * 2
            if stanzaVecchia == GlobalVar.dictStanze["forestaCadetta5"]:
                if sottofondoAmbientale != GlobalVar.audioAmbienteForestaFuoco:
                    sottofondoAmbientaleCambiato = True
                sottofondoAmbientale = GlobalVar.audioAmbienteForestaFuoco
                npers = 1
                x = GlobalVar.gsx // 32 * 16
                y = GlobalVar.gsy // 18 * 9
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
        if sottofondoAmbientale != GlobalVar.audioAmbienteForesta:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalVar.audioAmbienteForesta
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["forestaCadetta5"]:
                npers = 1
                x = GlobalVar.gsx // 32 * 2
                y = GlobalVar.gsy // 18 * 14
    if stanza == GlobalVar.dictStanze["forestaCadetta7"]:
        if canzone != GlobalVar.canzoneForesta:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneForesta
        if sottofondoAmbientale != GlobalVar.audioAmbienteForesta:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalVar.audioAmbienteForesta
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["forestaCadetta5"]:
                npers = 4
                x = GlobalVar.gsx // 32 * 27
                y = GlobalVar.gsy // 18 * 2
            if stanzaVecchia == GlobalVar.dictStanze["forestaCadetta7"]:
                npers = 2
                x = GlobalVar.gsx // 32 * 3
                y = GlobalVar.gsy // 18 * 7
                GlobalVar.canaleSoundInterazioni.play(GlobalVar.rumoreScavare)
                pygame.time.wait(3000)
            if stanzaVecchia == GlobalVar.dictStanze["forestaCadetta8"]:
                npers = 3
                x = GlobalVar.gsx // 32 * 4
                y = GlobalVar.gsy // 18 * 15
    if stanza == GlobalVar.dictStanze["forestaCadetta8"]:
        if canzone != GlobalVar.canzoneForesta:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneForesta
        if sottofondoAmbientale != GlobalVar.audioAmbienteForesta:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalVar.audioAmbienteForesta
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["forestaCadetta7"]:
                npers = 4
                x = GlobalVar.gsx // 32 * 19
                y = GlobalVar.gsy // 18 * 2
            if stanzaVecchia == GlobalVar.dictStanze["stradaPerCittà1"]:
                npers = 3
                x = GlobalVar.gsx // 32 * 11
                y = GlobalVar.gsy // 18 * 15

    return x, y, npers, rumoreAperturaPorte, rumoreChiusuraPorte, canzoneCambiata, sottofondoAmbientaleCambiato, canzone, sottofondoAmbientale


def nonPuoiProcedere(avanzamentoStoria, x, y, stanzaVecchia, stanzaDestinazione):
    nonProcedere = False
    if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["tutorialUtilizzoOggetti"] and stanzaVecchia == GlobalVar.dictStanze["sognoLucy1"] and stanzaDestinazione == GlobalVar.dictStanze["sognoLucy2"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanzaVecchia, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        nonProcedere = True
    elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["dialogoCasaSamLucy2"] and stanzaVecchia == GlobalVar.dictStanze["casaSamLucy1"] and stanzaDestinazione == GlobalVar.dictStanze["casaSamLucy2"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanzaVecchia, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        nonProcedere = True
    elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["incontroFiglioUfficiale"] and stanzaVecchia == GlobalVar.dictStanze["forestaCadetta5"] and stanzaDestinazione == GlobalVar.dictStanze["forestaCadetta6"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanzaVecchia, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        nonProcedere = True
    elif GlobalVar.dictAvanzamentoStoria["trovatoLegna1"] <= avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["legnaDepositata"] and stanzaVecchia == GlobalVar.dictStanze["forestaCadetta5"] and stanzaDestinazione == GlobalVar.dictStanze["forestaCadetta4"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanzaVecchia, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        nonProcedere = True
    elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and stanzaVecchia == GlobalVar.dictStanze["forestaCadetta5"] and stanzaDestinazione == GlobalVar.dictStanze["forestaCadetta7"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanzaVecchia, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        nonProcedere = True
    elif GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["armaturaNonnoCompletata"] and stanzaVecchia == GlobalVar.dictStanze["casaSamLucy1"] and stanzaDestinazione == GlobalVar.dictStanze["casaSamLucy2"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanzaVecchia, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        nonProcedere = True
    elif GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["accampamentoForestaAnalizzato"] and stanzaVecchia == GlobalVar.dictStanze["forestaCadetta5"] and (stanzaDestinazione == GlobalVar.dictStanze["forestaCadetta6"] or stanzaDestinazione == GlobalVar.dictStanze["forestaCadetta7"]):
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanzaVecchia, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        nonProcedere = True
    elif avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and stanzaVecchia == GlobalVar.dictStanze["casaSamLucy4"] and stanzaDestinazione == GlobalVar.dictStanze["casaSamLucy2"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanzaVecchia, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        nonProcedere = True

    return nonProcedere


def possibileAprirePorta(stanza, xPorta, yPorta, avanzamentoStoria):
    procedi = True
    if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and stanza == GlobalVar.dictStanze["casaSamLucy1"] and xPorta == GlobalVar.gpx * 25 and yPorta == GlobalVar.gpy * 3:
        procedi = False
    if GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["tutorialMappaDiario"] and stanza == GlobalVar.dictStanze["casaSamLucy1"] and xPorta == GlobalVar.gpx * 6 and yPorta == GlobalVar.gpy * 9:
        procedi = False
    if GlobalVar.dictAvanzamentoStoria["monologoIndicazioniArmaturaNonno"] <= avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["trovataChiaveRipostiglio"] and stanza == GlobalVar.dictStanze["casaSamLucy1"] and xPorta == GlobalVar.gpx * 26 and yPorta == GlobalVar.gpy * 11:
        procedi = False

    return procedi


def settaNomeStanza(avanzamentoStoria, stanza):
    nomeStanza = "Stanza"
    if stanza == GlobalVar.dictStanze["casaSamLucy1"]:
        if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"

    return nomeStanza
