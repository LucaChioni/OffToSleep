# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc


def settaPosizioneERumoriStanza(x, y, npers, rumoreAperturaPorte, rumoreChiusuraPorte, canzoneCambiata, sottofondoAmbientaleCambiato, stanza, stanzaVecchia, canzone, sottofondoAmbientale, inizio, avanzamentoStoria, bottoneDown):
    # npers: 1=d, 2=a, 3=w, 4=s
    if stanza == GlobalGameVar.dictStanze["sognoLucy1"]:
        if canzone != GlobalSndVar.canzoneSogno:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneSogno
        if sottofondoAmbientale != GlobalSndVar.audioAmbienteSogno:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalSndVar.audioAmbienteSogno
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["sognoLucy2"]:
                npers = 3
                x = GlobalHWVar.gsx // 32 * 15
                y = GlobalHWVar.gsy // 18 * 15
    if stanza == GlobalGameVar.dictStanze["sognoLucy2"]:
        if canzone != GlobalSndVar.canzoneSogno:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneSogno
        if sottofondoAmbientale != GlobalSndVar.audioAmbienteSogno:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalSndVar.audioAmbienteSogno
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["sognoLucy1"]:
                npers = 4
                x = GlobalHWVar.gsx // 32 * 7
                y = GlobalHWVar.gsy // 18 * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["sognoLucy3"]:
                npers = 2
                x = GlobalHWVar.gsx // 32 * 29
                y = GlobalHWVar.gsy // 18 * 3
    if stanza == GlobalGameVar.dictStanze["sognoLucy3"]:
        if canzone != GlobalSndVar.canzoneSogno:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneSogno
        if sottofondoAmbientale != GlobalSndVar.audioAmbienteSogno:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalSndVar.audioAmbienteSogno
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["sognoLucy2"]:
                npers = 1
                x = GlobalHWVar.gsx // 32 * 2
                y = GlobalHWVar.gsy // 18 * 11
            if stanzaVecchia == GlobalGameVar.dictStanze["sognoLucy4"]:
                npers = 4
                x = GlobalHWVar.gsx // 32 * 14
                y = GlobalHWVar.gsy // 18 * 2
    if stanza == GlobalGameVar.dictStanze["sognoLucy4"]:
        if canzone != GlobalSndVar.canzoneSogno:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneSogno
        if sottofondoAmbientale != GlobalSndVar.audioAmbienteSogno:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalSndVar.audioAmbienteSogno
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["sognoLucy3"]:
                npers = 3
                x = GlobalHWVar.gsx // 32 * 15
                y = GlobalHWVar.gsy // 18 * 15
    if stanza == GlobalGameVar.dictStanze["casaHansLucy1"]:
        if canzone != GlobalSndVar.canzoneCasa:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneCasa
        if sottofondoAmbientale != GlobalSndVar.audioAmbienteCasaInterno:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalSndVar.audioAmbienteCasaInterno
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCasa
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCasa
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["sognoLucy4"]:
                npers = 4
                x = GlobalHWVar.gsx // 32 * 3
                y = GlobalHWVar.gsy // 18 * 14
            if stanzaVecchia == GlobalGameVar.dictStanze["casaHansLucy2"]:
                npers = 3
                if x == GlobalHWVar.gsx // 32 * 16:
                    x = GlobalHWVar.gsx // 32 * 16
                    y = GlobalHWVar.gsy // 18 * 15
                if x == GlobalHWVar.gsx // 32 * 17:
                    x = GlobalHWVar.gsx // 32 * 17
                    y = GlobalHWVar.gsy // 18 * 15
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"]:
                npers = 4
                x = GlobalHWVar.gsx // 32 * 4
                y = GlobalHWVar.gsy // 18 * 14
    if stanza == GlobalGameVar.dictStanze["casaHansLucy2"]:
        if canzone != GlobalSndVar.canzoneEsternoCasa:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneEsternoCasa
        if sottofondoAmbientale != GlobalSndVar.audioAmbienteCasaEsterno:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalSndVar.audioAmbienteCasaEsterno
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCasa
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCasa
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["casaHansLucy1"]:
                npers = 4
                if x == GlobalHWVar.gsx // 32 * 16:
                    x = GlobalHWVar.gsx // 32 * 16
                    y = GlobalHWVar.gsy // 18 * 4
                if x == GlobalHWVar.gsx // 32 * 17:
                    x = GlobalHWVar.gsx // 32 * 17
                    y = GlobalHWVar.gsy // 18 * 4
            if stanzaVecchia == GlobalGameVar.dictStanze["casaHansLucy3"]:
                npers = 4
                if x == GlobalHWVar.gsx // 32 * 3:
                    x = GlobalHWVar.gsx // 32 * 3
                    y = GlobalHWVar.gsy // 18 * 3
                if x == GlobalHWVar.gsx // 32 * 4:
                    x = GlobalHWVar.gsx // 32 * 4
                    y = GlobalHWVar.gsy // 18 * 3
                if x == GlobalHWVar.gsx // 32 * 27:
                    x = GlobalHWVar.gsx // 32 * 27
                    y = GlobalHWVar.gsy // 18 * 4
                if x == GlobalHWVar.gsx // 32 * 28:
                    x = GlobalHWVar.gsx // 32 * 28
                    y = GlobalHWVar.gsy // 18 * 4
            if stanzaVecchia == GlobalGameVar.dictStanze["casaHansLucy4"]:
                npers = 3
                if x == GlobalHWVar.gsx // 32 * 14:
                    x = GlobalHWVar.gsx // 32 * 14
                    y = GlobalHWVar.gsy // 18 * 14
                if x == GlobalHWVar.gsx // 32 * 15:
                    x = GlobalHWVar.gsx // 32 * 15
                    y = GlobalHWVar.gsy // 18 * 14
                if x == GlobalHWVar.gsx // 32 * 16:
                    x = GlobalHWVar.gsx // 32 * 16
                    y = GlobalHWVar.gsy // 18 * 14
                if x == GlobalHWVar.gsx // 32 * 17:
                    x = GlobalHWVar.gsx // 32 * 17
                    y = GlobalHWVar.gsy // 18 * 14
    if stanza == GlobalGameVar.dictStanze["casaHansLucy3"]:
        if canzone != GlobalSndVar.canzoneEsternoCasa:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneEsternoCasa
        if sottofondoAmbientale != GlobalSndVar.audioAmbienteCasaEsterno:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalSndVar.audioAmbienteCasaEsterno
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCasa
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCasa
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["casaHansLucy2"]:
                npers = 3
                if x == GlobalHWVar.gsx // 32 * 3:
                    x = GlobalHWVar.gsx // 32 * 3
                    y = GlobalHWVar.gsy // 18 * 15
                if x == GlobalHWVar.gsx // 32 * 4:
                    x = GlobalHWVar.gsx // 32 * 4
                    y = GlobalHWVar.gsy // 18 * 15
                if x == GlobalHWVar.gsx // 32 * 27:
                    x = GlobalHWVar.gsx // 32 * 27
                    y = GlobalHWVar.gsy // 18 * 15
                if x == GlobalHWVar.gsx // 32 * 28:
                    x = GlobalHWVar.gsx // 32 * 28
                    y = GlobalHWVar.gsy // 18 * 15
    if stanza == GlobalGameVar.dictStanze["casaHansLucy4"]:
        if canzone != GlobalSndVar.canzoneEsternoCasa:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneEsternoCasa
        if sottofondoAmbientale != GlobalSndVar.audioAmbienteCasaEsterno:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalSndVar.audioAmbienteCasaEsterno
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCasa
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCasa
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["casaHansLucy2"]:
                npers = 4
                if x == GlobalHWVar.gsx // 32 * 13:
                    x = GlobalHWVar.gsx // 32 * 14
                    y = GlobalHWVar.gsy // 18 * 2
                if x == GlobalHWVar.gsx // 32 * 14:
                    x = GlobalHWVar.gsx // 32 * 14
                    y = GlobalHWVar.gsy // 18 * 2
                if x == GlobalHWVar.gsx // 32 * 15:
                    x = GlobalHWVar.gsx // 32 * 15
                    y = GlobalHWVar.gsy // 18 * 2
                if x == GlobalHWVar.gsx // 32 * 16:
                    x = GlobalHWVar.gsx // 32 * 16
                    y = GlobalHWVar.gsy // 18 * 2
                if x == GlobalHWVar.gsx // 32 * 17:
                    x = GlobalHWVar.gsx // 32 * 17
                    y = GlobalHWVar.gsy // 18 * 2
                if x == GlobalHWVar.gsx // 32 * 18:
                    x = GlobalHWVar.gsx // 32 * 17
                    y = GlobalHWVar.gsy // 18 * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta1"]:
                npers = 3
                if x == GlobalHWVar.gsx // 32 * 15:
                    x = GlobalHWVar.gsx // 32 * 15
                    y = GlobalHWVar.gsy // 18 * 15
                if x == GlobalHWVar.gsx // 32 * 16:
                    x = GlobalHWVar.gsx // 32 * 16
                    y = GlobalHWVar.gsy // 18 * 15
    if stanza == GlobalGameVar.dictStanze["forestaCadetta1"]:
        if canzone != GlobalSndVar.canzoneForesta:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneForesta
        if sottofondoAmbientale != GlobalSndVar.audioAmbienteForesta:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalSndVar.audioAmbienteForesta
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["casaHansLucy4"]:
                npers = 4
                if x == GlobalHWVar.gsx // 32 * 15:
                    x = GlobalHWVar.gsx // 32 * 15
                    y = GlobalHWVar.gsy // 18 * 2
                if x == GlobalHWVar.gsx // 32 * 16:
                    x = GlobalHWVar.gsx // 32 * 16
                    y = GlobalHWVar.gsy // 18 * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta2"]:
                npers = 1
                x = GlobalHWVar.gsx // 32 * 2
                y = GlobalHWVar.gsy // 18 * 4
    if stanza == GlobalGameVar.dictStanze["forestaCadetta2"]:
        if canzone != GlobalSndVar.canzoneForesta:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneForesta
        if sottofondoAmbientale != GlobalSndVar.audioAmbienteForesta:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalSndVar.audioAmbienteForesta
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta1"]:
                npers = 2
                x = GlobalHWVar.gsx // 32 * 29
                y = GlobalHWVar.gsy // 18 * 14
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta3"]:
                npers = 3
                x = GlobalHWVar.gsx // 32 * 12
                y = GlobalHWVar.gsy // 18 * 15
    if stanza == GlobalGameVar.dictStanze["forestaCadetta3"]:
        if canzone != GlobalSndVar.canzoneForesta:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneForesta
        if sottofondoAmbientale != GlobalSndVar.audioAmbienteForesta:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalSndVar.audioAmbienteForesta
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta2"]:
                npers = 4
                x = GlobalHWVar.gsx // 32 * 9
                y = GlobalHWVar.gsy // 18 * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta4"]:
                npers = 3
                x = GlobalHWVar.gsx // 32 * 23
                y = GlobalHWVar.gsy // 18 * 15
    if stanza == GlobalGameVar.dictStanze["forestaCadetta4"]:
        if canzone != GlobalSndVar.canzoneForesta:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneForesta
        if sottofondoAmbientale != GlobalSndVar.audioAmbienteForesta:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalSndVar.audioAmbienteForesta
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta3"]:
                npers = 4
                x = GlobalHWVar.gsx // 32 * 26
                y = GlobalHWVar.gsy // 18 * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"]:
                npers = 3
                x = GlobalHWVar.gsx // 32 * 19
                y = GlobalHWVar.gsy // 18 * 15
    if stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        if canzone != GlobalSndVar.canzoneForesta:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneForesta
        if sottofondoAmbientale != GlobalSndVar.audioAmbienteForesta:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalSndVar.audioAmbienteForesta
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta4"]:
                npers = 4
                x = GlobalHWVar.gsx // 32 * 16
                y = GlobalHWVar.gsy // 18 * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"]:
                if sottofondoAmbientale != GlobalSndVar.audioAmbienteForestaFuoco:
                    sottofondoAmbientaleCambiato = True
                sottofondoAmbientale = GlobalSndVar.audioAmbienteForestaFuoco
                canzoneCambiata = True
                canzone = False
                npers = 1
                x = GlobalHWVar.gsx // 32 * 16
                y = GlobalHWVar.gsy // 18 * 9
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta6"]:
                npers = 2
                x = GlobalHWVar.gsx // 32 * 29
                y = GlobalHWVar.gsy // 18 * 8
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta7"]:
                npers = 3
                x = GlobalHWVar.gsx // 32 * 15
                y = GlobalHWVar.gsy // 18 * 15
    if stanza == GlobalGameVar.dictStanze["forestaCadetta6"]:
        if canzone != GlobalSndVar.canzoneForesta:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneForesta
        if sottofondoAmbientale != GlobalSndVar.audioAmbienteForesta:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalSndVar.audioAmbienteForesta
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"]:
                npers = 1
                x = GlobalHWVar.gsx // 32 * 2
                y = GlobalHWVar.gsy // 18 * 14
    if stanza == GlobalGameVar.dictStanze["forestaCadetta7"]:
        if canzone != GlobalSndVar.canzoneForesta:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneForesta
        if sottofondoAmbientale != GlobalSndVar.audioAmbienteForesta:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalSndVar.audioAmbienteForesta
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"]:
                npers = 4
                x = GlobalHWVar.gsx // 32 * 27
                y = GlobalHWVar.gsy // 18 * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta7"]:
                npers = 2
                x = GlobalHWVar.gsx // 32 * 3
                y = GlobalHWVar.gsy // 18 * 7
                GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreScavare)
                i = 0
                while i < 30:
                    pygame.time.wait(100)
                    bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, False)
                    i += 1
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta8"]:
                npers = 3
                x = GlobalHWVar.gsx // 32 * 4
                y = GlobalHWVar.gsy // 18 * 15
    if stanza == GlobalGameVar.dictStanze["forestaCadetta8"]:
        if canzone != GlobalSndVar.canzoneForesta:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneForesta
        if sottofondoAmbientale != GlobalSndVar.audioAmbienteForesta:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalSndVar.audioAmbienteForesta
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta7"]:
                npers = 4
                x = GlobalHWVar.gsx // 32 * 19
                y = GlobalHWVar.gsy // 18 * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta9"]:
                npers = 3
                x = GlobalHWVar.gsx // 32 * 11
                y = GlobalHWVar.gsy // 18 * 15
    if stanza == GlobalGameVar.dictStanze["forestaCadetta9"]:
        if canzone != GlobalSndVar.canzoneForesta:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneForesta
        if sottofondoAmbientale != GlobalSndVar.audioAmbienteForesta:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalSndVar.audioAmbienteForesta
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteForesta
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteForesta
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta8"]:
                npers = 4
                x = GlobalHWVar.gsx // 32 * 25
                y = GlobalHWVar.gsy // 18 * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà1"]:
                npers = 3
                y = GlobalHWVar.gsy // 18 * 15
    if stanza == GlobalGameVar.dictStanze["stradaPerCittà1"]:
        if canzone != GlobalSndVar.canzoneEsternoCitta:
            canzoneCambiata = True
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            canzone = GlobalSndVar.canzoneEsternoCitta
        else:
            canzone = False
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteStradaPerCitta1_1:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteStradaPerCitta1_1
        else:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteStradaPerCitta1_2:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteStradaPerCitta1_2
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta9"]:
                npers = 4
                y = GlobalHWVar.gsy // 18 * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà2"]:
                npers = 1
                x = GlobalHWVar.gsx // 32 * 2
                if y == GlobalHWVar.gsy // 18 * 4:
                    y = GlobalHWVar.gsy // 18 * 6
                elif y == GlobalHWVar.gsy // 18 * 5:
                    y = GlobalHWVar.gsy // 18 * 7
                elif y == GlobalHWVar.gsy // 18 * 6:
                    y = GlobalHWVar.gsy // 18 * 8
                elif y == GlobalHWVar.gsy // 18 * 7:
                    y = GlobalHWVar.gsy // 18 * 9
                elif y == GlobalHWVar.gsy // 18 * 8:
                    y = GlobalHWVar.gsy // 18 * 10
                elif y == GlobalHWVar.gsy // 18 * 9:
                    y = GlobalHWVar.gsy // 18 * 11
                elif y == GlobalHWVar.gsy // 18 * 10:
                    y = GlobalHWVar.gsy // 18 * 12
                elif y == GlobalHWVar.gsy // 18 * 11:
                    y = GlobalHWVar.gsy // 18 * 13
                elif y == GlobalHWVar.gsy // 18 * 12:
                    y = GlobalHWVar.gsy // 18 * 14
                elif y == GlobalHWVar.gsy // 18 * 13:
                    y = GlobalHWVar.gsy // 18 * 15
    if stanza == GlobalGameVar.dictStanze["stradaPerCittà2"]:
        if canzone != GlobalSndVar.canzoneEsternoCitta:
            canzoneCambiata = True
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            canzone = GlobalSndVar.canzoneEsternoCitta
        else:
            canzone = False
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteStradaPerCitta2_1:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteStradaPerCitta2_1
        else:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteStradaPerCitta2_2:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteStradaPerCitta2_2
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà1"]:
                npers = 2
                x = GlobalHWVar.gsx // 32 * 29
                if y == GlobalHWVar.gsy // 18 * 6:
                    y = GlobalHWVar.gsy // 18 * 4
                elif y == GlobalHWVar.gsy // 18 * 7:
                    y = GlobalHWVar.gsy // 18 * 5
                elif y == GlobalHWVar.gsy // 18 * 8:
                    y = GlobalHWVar.gsy // 18 * 6
                elif y == GlobalHWVar.gsy // 18 * 9:
                    y = GlobalHWVar.gsy // 18 * 7
                elif y == GlobalHWVar.gsy // 18 * 10:
                    y = GlobalHWVar.gsy // 18 * 8
                elif y == GlobalHWVar.gsy // 18 * 11:
                    y = GlobalHWVar.gsy // 18 * 9
                elif y == GlobalHWVar.gsy // 18 * 12:
                    y = GlobalHWVar.gsy // 18 * 10
                elif y == GlobalHWVar.gsy // 18 * 13:
                    y = GlobalHWVar.gsy // 18 * 11
                elif y == GlobalHWVar.gsy // 18 * 14:
                    y = GlobalHWVar.gsy // 18 * 12
                elif y == GlobalHWVar.gsy // 18 * 15:
                    y = GlobalHWVar.gsy // 18 * 13
            if stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà3"]:
                npers = 1
                x = GlobalHWVar.gsx // 32 * 2
    if stanza == GlobalGameVar.dictStanze["stradaPerCittà3"]:
        if canzone != GlobalSndVar.canzoneEsternoCitta:
            canzoneCambiata = True
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            canzone = GlobalSndVar.canzoneEsternoCitta
        else:
            canzone = False
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteStradaPerCitta3_1:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteStradaPerCitta3_1
        else:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteStradaPerCitta3_2:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteStradaPerCitta3_2
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà2"]:
                npers = 2
                x = GlobalHWVar.gsx // 32 * 29
            if stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà3"]:
                npers = 2
                x = GlobalHWVar.gsx // 32 * 4
                y = GlobalHWVar.gsy // 18 * 8
                GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreSollevamentoPortaCitta)
                i = 0
                while i < 60:
                    pygame.time.wait(100)
                    bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, False)
                    i += 1
                pygame.time.wait(500)
            if stanzaVecchia == GlobalGameVar.dictStanze["città1"]:
                npers = 1
                x = GlobalHWVar.gsx // 32 * 2
    if stanza == GlobalGameVar.dictStanze["casaDavid1"]:
        if canzone != GlobalSndVar.canzoneCasaDavid:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneCasaDavid
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteCasaDavid_1:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteCasaDavid_1
        else:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteCasaDavid_2:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteCasaDavid_2
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCasaDavid
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCasaDavid
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà3"] or stanzaVecchia == GlobalGameVar.dictStanze["città3"]:
                npers = 3
                if x == GlobalHWVar.gsx // 32 * 15:
                    x = GlobalHWVar.gsx // 32 * 15
                    y = GlobalHWVar.gsy // 18 * 15
                elif x == GlobalHWVar.gsx // 32 * 16:
                    x = GlobalHWVar.gsx // 32 * 16
                    y = GlobalHWVar.gsy // 18 * 15
                else:
                    x = GlobalHWVar.gsx // 32 * 15
                    y = GlobalHWVar.gsy // 18 * 15
            if stanzaVecchia == GlobalGameVar.dictStanze["casaDavid2"]:
                npers = 4
                if x == GlobalHWVar.gsx // 32 * 27:
                    x = GlobalHWVar.gsx // 32 * 28
                    y = GlobalHWVar.gsy // 18 * 11
                elif x == GlobalHWVar.gsx // 32 * 28:
                    x = GlobalHWVar.gsx // 32 * 29
                    y = GlobalHWVar.gsy // 18 * 11
    if stanza == GlobalGameVar.dictStanze["casaDavid2"]:
        if canzone != GlobalSndVar.canzoneCasaDavid:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneCasaDavid
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteCasaDavid_1:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteCasaDavid_1
        else:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteCasaDavid_2:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteCasaDavid_2
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCasaDavid
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCasaDavid
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["casaDavid1"]:
                npers = 3
                y = GlobalHWVar.gsy // 18 * 4
                if x == GlobalHWVar.gsx // 32 * 28:
                    x = GlobalHWVar.gsx // 32 * 27
                elif x == GlobalHWVar.gsx // 32 * 29:
                    x = GlobalHWVar.gsx // 32 * 28
            if stanzaVecchia == GlobalGameVar.dictStanze["casaDavid3"]:
                npers = 1
                x = GlobalHWVar.gsx // 32 * 2
                if y == GlobalHWVar.gsy // 18 * 10:
                    y = GlobalHWVar.gsy // 18 * 3
                elif y == GlobalHWVar.gsy // 18 * 11:
                    y = GlobalHWVar.gsy // 18 * 4
                elif y == GlobalHWVar.gsy // 18 * 12 or y == GlobalHWVar.gsy // 18 * 13:
                    y = GlobalHWVar.gsy // 18 * 5
    if stanza == GlobalGameVar.dictStanze["casaDavid3"]:
        if canzone != GlobalSndVar.canzoneCasaDavid:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneCasaDavid
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteCasaDavid_1:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteCasaDavid_1
        else:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteCasaDavid_2:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteCasaDavid_2
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCasaDavid
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCasaDavid
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["casaDavid2"]:
                npers = 2
                x = GlobalHWVar.gsx // 32 * 29
                if y == GlobalHWVar.gsy // 18 * 3:
                    y = GlobalHWVar.gsy // 18 * 10
                elif y == GlobalHWVar.gsy // 18 * 4:
                    y = GlobalHWVar.gsy // 18 * 11
                elif y == GlobalHWVar.gsy // 18 * 5:
                    y = GlobalHWVar.gsy // 18 * 12
            if stanzaVecchia == GlobalGameVar.dictStanze["casaDavid3"]:
                if (x == GlobalHWVar.gpx * 4 and y == GlobalHWVar.gpx * 10) or (x == GlobalHWVar.gpx * 5 and y == GlobalHWVar.gpx * 10) or (x == GlobalHWVar.gpx * 6 and y == GlobalHWVar.gpx * 11):
                    npers = 1
                    x = GlobalHWVar.gsx // 32 * 6
                    y = GlobalHWVar.gsy // 18 * 11
                    pygame.time.wait(500)
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreDoccia)
                    i = 0
                    while i < 60:
                        pygame.time.wait(100)
                        bottoneDown, aggiornaInterfacciaPerCambioInput = GestioneInput.getInput(bottoneDown, False)
                        i += 1
                elif (x == GlobalHWVar.gpx * 8 and y == GlobalHWVar.gpx * 3) or (x == GlobalHWVar.gpx * 8 and y == GlobalHWVar.gpx * 4) or (x == GlobalHWVar.gpx * 8 and y == GlobalHWVar.gpx * 5) or (x == GlobalHWVar.gpx * 8 and y == GlobalHWVar.gpx * 6):
                    npers = 1
                    x = GlobalHWVar.gsx // 32 * 8
                    y = GlobalHWVar.gsy // 18 * 5

    return x, y, npers, rumoreAperturaPorte, rumoreChiusuraPorte, canzoneCambiata, sottofondoAmbientaleCambiato, canzone, sottofondoAmbientale, bottoneDown


def scriviNomeZona(stanza, stanzaVecchia):
    stoppaMusica = False
    if (stanzaVecchia == GlobalGameVar.dictStanze["sognoLucy4"] and stanza == GlobalGameVar.dictStanze["casaHansLucy1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta1"] and stanza == GlobalGameVar.dictStanze["casaHansLucy4"]) or (stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"] and stanza == GlobalGameVar.dictStanze["casaHansLucy1"]):
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.nero)
        GenericFunc.messaggio("Casa", GlobalHWVar.grigiochi, GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 8, 150, centrale=True)
        GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 4), int(GlobalHWVar.gpy * 10.6)), (int(GlobalHWVar.gpx * 28) - 1, int(GlobalHWVar.gpy * 10.6)), 2)
        GenericFunc.oscuraIlluminaSchermo(illumina=2)
        GlobalHWVar.aggiornaSchermo()
        if stanzaVecchia == GlobalGameVar.dictStanze["sognoLucy4"] and stanza == GlobalGameVar.dictStanze["casaHansLucy1"]:
            stoppaMusica = True
    elif (stanzaVecchia == GlobalGameVar.dictStanze["casaHansLucy4"] and stanza == GlobalGameVar.dictStanze["forestaCadetta1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà1"] and stanza == GlobalGameVar.dictStanze["forestaCadetta9"]):
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.nero)
        GenericFunc.messaggio("Foresta Cadetta", GlobalHWVar.grigiochi, GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 8, 150, centrale=True)
        GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 4), int(GlobalHWVar.gpy * 10.6)), (int(GlobalHWVar.gpx * 28) - 1, int(GlobalHWVar.gpy * 10.6)), 2)
        GenericFunc.oscuraIlluminaSchermo(illumina=2)
        GlobalHWVar.aggiornaSchermo()
    elif (stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta9"] and stanza == GlobalGameVar.dictStanze["stradaPerCittà1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["città1"] and stanza == GlobalGameVar.dictStanze["stradaPerCittà3"]):
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.nero)
        GenericFunc.messaggio(u"Strada per la città", GlobalHWVar.grigiochi, GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 8, 150, centrale=True)
        GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 4), int(GlobalHWVar.gpy * 10.6)), (int(GlobalHWVar.gpx * 28) - 1, int(GlobalHWVar.gpy * 10.6)), 2)
        GenericFunc.oscuraIlluminaSchermo(illumina=2)
        GlobalHWVar.aggiornaSchermo()
    elif (stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà3"] and stanza == GlobalGameVar.dictStanze["casaDavid1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["città3"] and stanza == GlobalGameVar.dictStanze["casaDavid1"]):
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.nero)
        GenericFunc.messaggio(u"Casa di David", GlobalHWVar.grigiochi, GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 8, 150, centrale=True)
        GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 4), int(GlobalHWVar.gpy * 10.6)), (int(GlobalHWVar.gpx * 28) - 1, int(GlobalHWVar.gpy * 10.6)), 2)
        GenericFunc.oscuraIlluminaSchermo(illumina=2)
        GlobalHWVar.aggiornaSchermo()
        if stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà3"] and stanza == GlobalGameVar.dictStanze["casaDavid1"]:
            stoppaMusica = True

    return stoppaMusica


def nonPuoiProcedere(avanzamentoStoria, stanzaVecchia, stanzaDestinazione):
    nonProcedere = False
    if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tutorialUtilizzoOggetti"] and stanzaVecchia == GlobalGameVar.dictStanze["sognoLucy1"] and stanzaDestinazione == GlobalGameVar.dictStanze["sognoLucy2"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoCasaHansLucy2"] and stanzaVecchia == GlobalGameVar.dictStanze["casaHansLucy1"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaHansLucy2"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontroFiglioUfficiale"] and stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"] and stanzaDestinazione == GlobalGameVar.dictStanze["forestaCadetta6"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"] and stanzaDestinazione == GlobalGameVar.dictStanze["forestaCadetta7"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["armaturaNonnoCompletata"] and stanzaVecchia == GlobalGameVar.dictStanze["casaHansLucy1"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaHansLucy2"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["accampamentoForestaAnalizzato2"] and stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"] and (stanzaDestinazione == GlobalGameVar.dictStanze["forestaCadetta6"] or stanzaDestinazione == GlobalGameVar.dictStanze["forestaCadetta7"]):
        nonProcedere = True
    elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and stanzaVecchia == GlobalGameVar.dictStanze["casaHansLucy4"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaHansLucy2"]:
        nonProcedere = True
    elif (stanzaVecchia == GlobalGameVar.dictStanze["casaDavid1"] or stanzaVecchia == GlobalGameVar.dictStanze["casaDavid2"]) and stanzaDestinazione == -1:
        nonProcedere = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoDopoBagnoDavid"] and stanzaVecchia == GlobalGameVar.dictStanze["casaDavid3"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaDavid2"]:
        nonProcedere = True

    return nonProcedere


def possibileAprirePorta(stanza, xPorta, yPorta, avanzamentoStoria):
    procedi = True
    if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and stanza == GlobalGameVar.dictStanze["casaHansLucy1"] and xPorta == GlobalHWVar.gpx * 25 and yPorta == GlobalHWVar.gpy * 3:
        procedi = False
    if GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tutorialMappaDiario"] and stanza == GlobalGameVar.dictStanze["casaHansLucy1"] and xPorta == GlobalHWVar.gpx * 6 and yPorta == GlobalHWVar.gpy * 9:
        procedi = False
    if GlobalGameVar.dictAvanzamentoStoria["monologoIndicazioniArmaturaNonno"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["trovataChiaveRipostiglio"] and stanza == GlobalGameVar.dictStanze["casaHansLucy1"] and xPorta == GlobalHWVar.gpx * 26 and yPorta == GlobalHWVar.gpy * 11:
        procedi = False
    if GlobalGameVar.dictAvanzamentoStoria["arrivoDavidPrimoPiano"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presaChiaveStanzaDaLettoDavid"] and stanza == GlobalGameVar.dictStanze["casaDavid3"] and xPorta == GlobalHWVar.gpx * 12 and yPorta == GlobalHWVar.gpy * 8:
        procedi = False

    return procedi


def settaNomeStanza(avanzamentoStoria, stanza):
    nomeStanza = "Stanza"
    if stanza == GlobalGameVar.dictStanze["casaHansLucy1"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["casaHansLucy2"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["forestaCadetta1"] or stanza == GlobalGameVar.dictStanze["forestaCadetta2"] or stanza == GlobalGameVar.dictStanze["forestaCadetta3"] or stanza == GlobalGameVar.dictStanze["forestaCadetta4"] or stanza == GlobalGameVar.dictStanze["forestaCadetta6"] or stanza == GlobalGameVar.dictStanze["forestaCadetta7"] or stanza == GlobalGameVar.dictStanze["forestaCadetta8"] or stanza == GlobalGameVar.dictStanze["forestaCadetta9"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioUltimoDialogoHans"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            nomeStanza = "StanzaB"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaC"
    if stanza == GlobalGameVar.dictStanze["stradaPerCittà1"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["stradaPerCittà2"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["stradaPerCittà3"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["apertoPortaCittà"]:
            nomeStanza = "StanzaA"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaC"
    if stanza == GlobalGameVar.dictStanze["casaDavid1"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["casaDavid2"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cenaConDavidIniziata"]:
            nomeStanza = "StanzaA"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaC"
    if stanza == GlobalGameVar.dictStanze["casaDavid3"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["andatoADormireCasaDavid"]:
            nomeStanza = "StanzaA"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaC"

    return nomeStanza
