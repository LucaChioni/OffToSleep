# -*- coding: utf-8 -*-

from PersonaggioObj import *


def settaPosizioneERumoriStanza(x, y, npers, rumoreAperturaPorte, rumoreChiusuraPorte, canzoneCambiata, sottofondoAmbientaleCambiato, stanza, stanzaVecchia, canzone, sottofondoAmbientale, inizio, avanzamentoStoria):
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
    if stanza == GlobalVar.dictStanze["casaHansLucy1"]:
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
            if stanzaVecchia == GlobalVar.dictStanze["casaHansLucy2"]:
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
    if stanza == GlobalVar.dictStanze["casaHansLucy2"]:
        if canzone != GlobalVar.canzoneEsternoCasa:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneEsternoCasa
        if sottofondoAmbientale != GlobalVar.audioAmbienteCasaEsterno:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalVar.audioAmbienteCasaEsterno
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteCasa
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteCasa
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["casaHansLucy1"]:
                npers = 4
                if x == GlobalVar.gsx // 32 * 16:
                    x = GlobalVar.gsx // 32 * 16
                    y = GlobalVar.gsy // 18 * 4
                if x == GlobalVar.gsx // 32 * 17:
                    x = GlobalVar.gsx // 32 * 17
                    y = GlobalVar.gsy // 18 * 4
            if stanzaVecchia == GlobalVar.dictStanze["casaHansLucy3"]:
                npers = 4
                if x == GlobalVar.gsx // 32 * 3:
                    x = GlobalVar.gsx // 32 * 3
                    y = GlobalVar.gsy // 18 * 3
                if x == GlobalVar.gsx // 32 * 4:
                    x = GlobalVar.gsx // 32 * 4
                    y = GlobalVar.gsy // 18 * 3
                if x == GlobalVar.gsx // 32 * 27:
                    x = GlobalVar.gsx // 32 * 27
                    y = GlobalVar.gsy // 18 * 4
                if x == GlobalVar.gsx // 32 * 28:
                    x = GlobalVar.gsx // 32 * 28
                    y = GlobalVar.gsy // 18 * 4
            if stanzaVecchia == GlobalVar.dictStanze["casaHansLucy4"]:
                npers = 3
                if x == GlobalVar.gsx // 32 * 14:
                    x = GlobalVar.gsx // 32 * 14
                    y = GlobalVar.gsy // 18 * 14
                if x == GlobalVar.gsx // 32 * 15:
                    x = GlobalVar.gsx // 32 * 15
                    y = GlobalVar.gsy // 18 * 14
                if x == GlobalVar.gsx // 32 * 16:
                    x = GlobalVar.gsx // 32 * 16
                    y = GlobalVar.gsy // 18 * 14
                if x == GlobalVar.gsx // 32 * 17:
                    x = GlobalVar.gsx // 32 * 17
                    y = GlobalVar.gsy // 18 * 14
    if stanza == GlobalVar.dictStanze["casaHansLucy3"]:
        if canzone != GlobalVar.canzoneEsternoCasa:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneEsternoCasa
        if sottofondoAmbientale != GlobalVar.audioAmbienteCasaEsterno:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalVar.audioAmbienteCasaEsterno
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteCasa
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteCasa
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["casaHansLucy2"]:
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
    if stanza == GlobalVar.dictStanze["casaHansLucy4"]:
        if canzone != GlobalVar.canzoneEsternoCasa:
            canzoneCambiata = True
        canzone = GlobalVar.canzoneEsternoCasa
        if sottofondoAmbientale != GlobalVar.audioAmbienteCasaEsterno:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalVar.audioAmbienteCasaEsterno
        # rumore porte
        rumoreAperturaPorte = GlobalVar.suonoaperturaporteCasa
        rumoreChiusuraPorte = GlobalVar.suonochiusuraporteCasa
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["casaHansLucy2"]:
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
            if stanzaVecchia == GlobalVar.dictStanze["casaHansLucy4"]:
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
                canzoneCambiata = True
                canzone = False
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
                i = 0
                while i < 3:
                    pygame.time.wait(1000)
                    pygame.event.pump()
                    i += 1
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
            if stanzaVecchia == GlobalVar.dictStanze["forestaCadetta9"]:
                npers = 3
                x = GlobalVar.gsx // 32 * 11
                y = GlobalVar.gsy // 18 * 15
    if stanza == GlobalVar.dictStanze["forestaCadetta9"]:
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
            if stanzaVecchia == GlobalVar.dictStanze["forestaCadetta8"]:
                npers = 4
                x = GlobalVar.gsx // 32 * 25
                y = GlobalVar.gsy // 18 * 2
            if stanzaVecchia == GlobalVar.dictStanze["stradaPerCittà1"]:
                npers = 3
                y = GlobalVar.gsy // 18 * 15
    if stanza == GlobalVar.dictStanze["stradaPerCittà1"]:
        if canzone != GlobalVar.canzoneEsternoCitta:
            canzoneCambiata = True
        if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            canzone = GlobalVar.canzoneEsternoCitta
        else:
            canzone = False
        if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            if sottofondoAmbientale != GlobalVar.audioAmbienteStradaPerCitta1_1:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalVar.audioAmbienteStradaPerCitta1_1
        else:
            if sottofondoAmbientale != GlobalVar.audioAmbienteStradaPerCitta1_2:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalVar.audioAmbienteStradaPerCitta1_2
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["forestaCadetta9"]:
                npers = 4
                y = GlobalVar.gsy // 18 * 2
            if stanzaVecchia == GlobalVar.dictStanze["stradaPerCittà2"]:
                npers = 1
                x = GlobalVar.gsx // 32 * 2
                if y == GlobalVar.gsy // 18 * 4:
                    y = GlobalVar.gsy // 18 * 6
                elif y == GlobalVar.gsy // 18 * 5:
                    y = GlobalVar.gsy // 18 * 7
                elif y == GlobalVar.gsy // 18 * 6:
                    y = GlobalVar.gsy // 18 * 8
                elif y == GlobalVar.gsy // 18 * 7:
                    y = GlobalVar.gsy // 18 * 9
                elif y == GlobalVar.gsy // 18 * 8:
                    y = GlobalVar.gsy // 18 * 10
                elif y == GlobalVar.gsy // 18 * 9:
                    y = GlobalVar.gsy // 18 * 11
                elif y == GlobalVar.gsy // 18 * 10:
                    y = GlobalVar.gsy // 18 * 12
                elif y == GlobalVar.gsy // 18 * 11:
                    y = GlobalVar.gsy // 18 * 13
                elif y == GlobalVar.gsy // 18 * 12:
                    y = GlobalVar.gsy // 18 * 14
                elif y == GlobalVar.gsy // 18 * 13:
                    y = GlobalVar.gsy // 18 * 15
    if stanza == GlobalVar.dictStanze["stradaPerCittà2"]:
        if canzone != GlobalVar.canzoneEsternoCitta:
            canzoneCambiata = True
        if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            canzone = GlobalVar.canzoneEsternoCitta
        else:
            canzone = False
        if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            if sottofondoAmbientale != GlobalVar.audioAmbienteStradaPerCitta2_1:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalVar.audioAmbienteStradaPerCitta2_1
        else:
            if sottofondoAmbientale != GlobalVar.audioAmbienteStradaPerCitta2_2:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalVar.audioAmbienteStradaPerCitta2_2
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["stradaPerCittà1"]:
                npers = 2
                x = GlobalVar.gsx // 32 * 29
                if y == GlobalVar.gsy // 18 * 6:
                    y = GlobalVar.gsy // 18 * 4
                elif y == GlobalVar.gsy // 18 * 7:
                    y = GlobalVar.gsy // 18 * 5
                elif y == GlobalVar.gsy // 18 * 8:
                    y = GlobalVar.gsy // 18 * 6
                elif y == GlobalVar.gsy // 18 * 9:
                    y = GlobalVar.gsy // 18 * 7
                elif y == GlobalVar.gsy // 18 * 10:
                    y = GlobalVar.gsy // 18 * 8
                elif y == GlobalVar.gsy // 18 * 11:
                    y = GlobalVar.gsy // 18 * 9
                elif y == GlobalVar.gsy // 18 * 12:
                    y = GlobalVar.gsy // 18 * 10
                elif y == GlobalVar.gsy // 18 * 13:
                    y = GlobalVar.gsy // 18 * 11
                elif y == GlobalVar.gsy // 18 * 14:
                    y = GlobalVar.gsy // 18 * 12
                elif y == GlobalVar.gsy // 18 * 15:
                    y = GlobalVar.gsy // 18 * 13
            if stanzaVecchia == GlobalVar.dictStanze["stradaPerCittà3"]:
                npers = 1
                x = GlobalVar.gsx // 32 * 2
    if stanza == GlobalVar.dictStanze["stradaPerCittà3"]:
        if canzone != GlobalVar.canzoneEsternoCitta:
            canzoneCambiata = True
        if avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            canzone = GlobalVar.canzoneEsternoCitta
        else:
            canzone = False
        if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            if sottofondoAmbientale != GlobalVar.audioAmbienteStradaPerCitta3_1:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalVar.audioAmbienteStradaPerCitta3_1
        else:
            if sottofondoAmbientale != GlobalVar.audioAmbienteStradaPerCitta3_2:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalVar.audioAmbienteStradaPerCitta3_2
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalVar.dictStanze["stradaPerCittà2"]:
                npers = 2
                x = GlobalVar.gsx // 32 * 29
            if stanzaVecchia == GlobalVar.dictStanze["stradaPerCittà3"]:
                npers = 2
                x = GlobalVar.gsx // 32 * 4
                y = GlobalVar.gsy // 18 * 8
                GlobalVar.canaleSoundInterazioni.play(GlobalVar.rumoreSollevamentoPortaCitta)
                i = 0
                while i < 6:
                    pygame.time.wait(1000)
                    pygame.event.pump()
                    i += 1
                pygame.time.wait(500)
            if stanzaVecchia == GlobalVar.dictStanze["città1"]:
                npers = 1
                x = GlobalVar.gsx // 32 * 2

    return x, y, npers, rumoreAperturaPorte, rumoreChiusuraPorte, canzoneCambiata, sottofondoAmbientaleCambiato, canzone, sottofondoAmbientale


def scriviNomeZona(stanza, stanzaVecchia):
    stoppaMusica = False
    if (stanzaVecchia == GlobalVar.dictStanze["sognoLucy4"] and stanza == GlobalVar.dictStanze["casaHansLucy1"]) or (stanzaVecchia == GlobalVar.dictStanze["forestaCadetta1"] and stanza == GlobalVar.dictStanze["casaHansLucy4"]) or (stanzaVecchia == GlobalVar.dictStanze["forestaCadetta5"] and stanza == GlobalVar.dictStanze["casaHansLucy1"]):
        GlobalVar.disegnaColoreSuTuttoLoSchermo(GlobalVar.nero)
        messaggio("Casa", GlobalVar.grigiochi, GlobalVar.gpx * 16, GlobalVar.gpy * 8, 150, centrale=True)
        GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigiochi, (int(GlobalVar.gpx * 4), int(GlobalVar.gpy * 10.6)), (int(GlobalVar.gpx * 28) - 1, int(GlobalVar.gpy * 10.6)), 2)
        oscuraIlluminaSchermo(illumina=2)
        GlobalVar.aggiornaSchermo()
        if stanzaVecchia == GlobalVar.dictStanze["sognoLucy4"] and stanza == GlobalVar.dictStanze["casaHansLucy1"]:
            stoppaMusica = True
    elif (stanzaVecchia == GlobalVar.dictStanze["casaHansLucy4"] and stanza == GlobalVar.dictStanze["forestaCadetta1"]) or (stanzaVecchia == GlobalVar.dictStanze["stradaPerCittà1"] and stanza == GlobalVar.dictStanze["forestaCadetta9"]):
        GlobalVar.disegnaColoreSuTuttoLoSchermo(GlobalVar.nero)
        messaggio("Foresta Cadetta", GlobalVar.grigiochi, GlobalVar.gpx * 16, GlobalVar.gpy * 8, 150, centrale=True)
        GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigiochi, (int(GlobalVar.gpx * 4), int(GlobalVar.gpy * 10.6)), (int(GlobalVar.gpx * 28) - 1, int(GlobalVar.gpy * 10.6)), 2)
        oscuraIlluminaSchermo(illumina=2)
        GlobalVar.aggiornaSchermo()
    elif (stanzaVecchia == GlobalVar.dictStanze["forestaCadetta9"] and stanza == GlobalVar.dictStanze["stradaPerCittà1"]) or (stanzaVecchia == GlobalVar.dictStanze["città1"] and stanza == GlobalVar.dictStanze["stradaPerCittà3"]):
        GlobalVar.disegnaColoreSuTuttoLoSchermo(GlobalVar.nero)
        messaggio(u"Strada per la città", GlobalVar.grigiochi, GlobalVar.gpx * 16, GlobalVar.gpy * 8, 150, centrale=True)
        GlobalVar.disegnaLineaSuSchermo(GlobalVar.schermo, GlobalVar.grigiochi, (int(GlobalVar.gpx * 4), int(GlobalVar.gpy * 10.6)), (int(GlobalVar.gpx * 28) - 1, int(GlobalVar.gpy * 10.6)), 2)
        oscuraIlluminaSchermo(illumina=2)
        GlobalVar.aggiornaSchermo()

    return stoppaMusica


def nonPuoiProcedere(avanzamentoStoria, x, y, stanzaVecchia, stanzaDestinazione, listaAvanzamentoDialoghi):
    nonProcedere = False
    if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["tutorialUtilizzoOggetti"] and stanzaVecchia == GlobalVar.dictStanze["sognoLucy1"] and stanzaDestinazione == GlobalVar.dictStanze["sognoLucy2"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanzaVecchia, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        nonProcedere = True
    elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["dialogoCasaHansLucy2"] and stanzaVecchia == GlobalVar.dictStanze["casaHansLucy1"] and stanzaDestinazione == GlobalVar.dictStanze["casaHansLucy2"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanzaVecchia, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        nonProcedere = True
    elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["incontroFiglioUfficiale"] and stanzaVecchia == GlobalVar.dictStanze["forestaCadetta5"] and stanzaDestinazione == GlobalVar.dictStanze["forestaCadetta6"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanzaVecchia, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        nonProcedere = True
    elif GlobalVar.dictAvanzamentoStoria["trovatoLegna1"] <= avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["legnaDepositata"] and stanzaVecchia == GlobalVar.dictStanze["forestaCadetta5"] and stanzaDestinazione == GlobalVar.dictStanze["forestaCadetta4"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanzaVecchia, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        nonProcedere = True
    elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and stanzaVecchia == GlobalVar.dictStanze["forestaCadetta5"] and stanzaDestinazione == GlobalVar.dictStanze["forestaCadetta7"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanzaVecchia, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        nonProcedere = True
    elif GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["armaturaNonnoCompletata"] and stanzaVecchia == GlobalVar.dictStanze["casaHansLucy1"] and stanzaDestinazione == GlobalVar.dictStanze["casaHansLucy2"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanzaVecchia, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        nonProcedere = True
    elif GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["accampamentoForestaAnalizzato2"] and stanzaVecchia == GlobalVar.dictStanze["forestaCadetta5"] and (stanzaDestinazione == GlobalVar.dictStanze["forestaCadetta6"] or stanzaDestinazione == GlobalVar.dictStanze["forestaCadetta7"]):
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanzaVecchia, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        nonProcedere = True
    elif avanzamentoStoria >= GlobalVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and stanzaVecchia == GlobalVar.dictStanze["casaHansLucy4"] and stanzaDestinazione == GlobalVar.dictStanze["casaHansLucy2"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanzaVecchia, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        nonProcedere = True

    return nonProcedere


def possibileAprirePorta(stanza, xPorta, yPorta, avanzamentoStoria):
    procedi = True
    if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and stanza == GlobalVar.dictStanze["casaHansLucy1"] and xPorta == GlobalVar.gpx * 25 and yPorta == GlobalVar.gpy * 3:
        procedi = False
    if GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["tutorialMappaDiario"] and stanza == GlobalVar.dictStanze["casaHansLucy1"] and xPorta == GlobalVar.gpx * 6 and yPorta == GlobalVar.gpy * 9:
        procedi = False
    if GlobalVar.dictAvanzamentoStoria["monologoIndicazioniArmaturaNonno"] <= avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["trovataChiaveRipostiglio"] and stanza == GlobalVar.dictStanze["casaHansLucy1"] and xPorta == GlobalVar.gpx * 26 and yPorta == GlobalVar.gpy * 11:
        procedi = False

    return procedi


def settaNomeStanza(avanzamentoStoria, stanza):
    nomeStanza = "Stanza"
    if stanza == GlobalVar.dictStanze["casaHansLucy1"]:
        if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalVar.dictStanze["casaHansLucy2"]:
        if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalVar.dictStanze["forestaCadetta1"] or stanza == GlobalVar.dictStanze["forestaCadetta2"] or stanza == GlobalVar.dictStanze["forestaCadetta3"] or stanza == GlobalVar.dictStanze["forestaCadetta4"] or stanza == GlobalVar.dictStanze["forestaCadetta6"] or stanza == GlobalVar.dictStanze["forestaCadetta7"] or stanza == GlobalVar.dictStanze["forestaCadetta8"] or stanza == GlobalVar.dictStanze["forestaCadetta9"]:
        if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalVar.dictStanze["forestaCadetta5"]:
        if GlobalVar.dictAvanzamentoStoria["inizioUltimoDialogoHans"] <= avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            nomeStanza = "StanzaB"
        elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaC"
    if stanza == GlobalVar.dictStanze["stradaPerCittà1"]:
        if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalVar.dictStanze["stradaPerCittà2"]:
        if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalVar.dictStanze["stradaPerCittà3"]:
        if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["apertoPortaCittà"]:
            nomeStanza = "StanzaA"
        elif avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaC"

    return nomeStanza
