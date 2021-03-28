# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche


def settaPosizioneERumoriStanza(x, y, npers, rumoreAperturaPorte, rumoreChiusuraPorte, canzoneCambiata, sottofondoAmbientaleCambiato, stanza, stanzaVecchia, canzone, sottofondoAmbientale, inizio, avanzamentoStoria, bottoneDown):
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
                npers = "w"
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
                npers = "s"
                x = GlobalHWVar.gsx // 32 * 7
                y = GlobalHWVar.gsy // 18 * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["sognoLucy3"]:
                npers = "a"
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
                npers = "d"
                x = GlobalHWVar.gsx // 32 * 2
                y = GlobalHWVar.gsy // 18 * 11
            if stanzaVecchia == GlobalGameVar.dictStanze["sognoLucy4"]:
                npers = "s"
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
                npers = "w"
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
                npers = "s"
                x = GlobalHWVar.gsx // 32 * 3
                y = GlobalHWVar.gsy // 18 * 14
            if stanzaVecchia == GlobalGameVar.dictStanze["casaHansLucy2"]:
                npers = "w"
                if x == GlobalHWVar.gsx // 32 * 16:
                    x = GlobalHWVar.gsx // 32 * 16
                    y = GlobalHWVar.gsy // 18 * 15
                if x == GlobalHWVar.gsx // 32 * 17:
                    x = GlobalHWVar.gsx // 32 * 17
                    y = GlobalHWVar.gsy // 18 * 15
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"]:
                npers = "s"
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
                npers = "s"
                if x == GlobalHWVar.gsx // 32 * 16:
                    x = GlobalHWVar.gsx // 32 * 16
                    y = GlobalHWVar.gsy // 18 * 4
                if x == GlobalHWVar.gsx // 32 * 17:
                    x = GlobalHWVar.gsx // 32 * 17
                    y = GlobalHWVar.gsy // 18 * 4
            if stanzaVecchia == GlobalGameVar.dictStanze["casaHansLucy3"]:
                npers = "s"
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
                npers = "w"
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
                npers = "w"
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
                npers = "s"
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
                npers = "w"
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
                npers = "s"
                if x == GlobalHWVar.gsx // 32 * 15:
                    x = GlobalHWVar.gsx // 32 * 15
                    y = GlobalHWVar.gsy // 18 * 2
                if x == GlobalHWVar.gsx // 32 * 16:
                    x = GlobalHWVar.gsx // 32 * 16
                    y = GlobalHWVar.gsy // 18 * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta2"]:
                npers = "d"
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
                npers = "a"
                x = GlobalHWVar.gsx // 32 * 29
                y = GlobalHWVar.gsy // 18 * 14
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta3"]:
                npers = "w"
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
                npers = "s"
                x = GlobalHWVar.gsx // 32 * 9
                y = GlobalHWVar.gsy // 18 * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta4"]:
                npers = "w"
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
                npers = "s"
                x = GlobalHWVar.gsx // 32 * 26
                y = GlobalHWVar.gsy // 18 * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"]:
                npers = "w"
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
                npers = "s"
                x = GlobalHWVar.gsx // 32 * 16
                y = GlobalHWVar.gsy // 18 * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"]:
                if sottofondoAmbientale != GlobalSndVar.audioAmbienteForestaFuoco:
                    sottofondoAmbientaleCambiato = True
                sottofondoAmbientale = GlobalSndVar.audioAmbienteForestaFuoco
                canzoneCambiata = True
                canzone = False
                npers = "d"
                x = GlobalHWVar.gsx // 32 * 16
                y = GlobalHWVar.gsy // 18 * 9
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta6"]:
                npers = "a"
                x = GlobalHWVar.gsx // 32 * 29
                y = GlobalHWVar.gsy // 18 * 8
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta7"]:
                npers = "w"
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
                npers = "d"
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
                npers = "s"
                x = GlobalHWVar.gsx // 32 * 27
                y = GlobalHWVar.gsy // 18 * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta7"]:
                npers = "a"
                x = GlobalHWVar.gsx // 32 * 3
                y = GlobalHWVar.gsy // 18 * 7
                GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreScavare)
                i = 0
                while i < 30:
                    pygame.time.wait(100)
                    inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                    i += 1
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta8"]:
                npers = "w"
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
                npers = "s"
                x = GlobalHWVar.gsx // 32 * 19
                y = GlobalHWVar.gsy // 18 * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta9"]:
                npers = "w"
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
                npers = "s"
                x = GlobalHWVar.gsx // 32 * 25
                y = GlobalHWVar.gsy // 18 * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà1"]:
                npers = "w"
                y = GlobalHWVar.gsy // 18 * 15
    if stanza == GlobalGameVar.dictStanze["stradaPerCittà1"]:
        if canzone != GlobalSndVar.canzoneEsternoCitta:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneEsternoCitta
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteStradaPerCitta1_notte:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteStradaPerCitta1_notte
        else:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteStradaPerCitta1_giorno:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteStradaPerCitta1_giorno
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta9"]:
                npers = "s"
                y = GlobalHWVar.gsy // 18 * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà2"]:
                npers = "d"
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
        canzone = GlobalSndVar.canzoneEsternoCitta
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteStradaPerCitta2_notte:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteStradaPerCitta2_notte
        else:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteStradaPerCitta2_giorno:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteStradaPerCitta2_giorno
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà1"]:
                npers = "a"
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
                npers = "d"
                x = GlobalHWVar.gsx // 32 * 2
    if stanza == GlobalGameVar.dictStanze["stradaPerCittà3"]:
        if canzone != GlobalSndVar.canzoneEsternoCitta:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneEsternoCitta
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteStradaPerCitta3_notte:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteStradaPerCitta3_notte
        else:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteStradaPerCitta3_giorno:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteStradaPerCitta3_giorno
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà2"]:
                npers = "a"
                x = GlobalHWVar.gsx // 32 * 29
            if stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà3"]:
                npers = "a"
                x = GlobalHWVar.gsx // 32 * 4
                GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreSollevamentoPortaCitta)
                i = 0
                while i < 65:
                    pygame.time.wait(100)
                    inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                    i += 1
            if stanzaVecchia == GlobalGameVar.dictStanze["città1"]:
                npers = "d"
                x = GlobalHWVar.gsx // 32 * 2
    if stanza == GlobalGameVar.dictStanze["città1"]:
        if canzone != GlobalSndVar.canzoneCitta:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneCitta
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteCitta_notte:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteCitta_notte
        else:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteCitta_giorno:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteCitta_giorno
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà3"]:
                npers = "a"
                x = GlobalHWVar.gsx // 32 * 29
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["apertoPortaCittà"]:
                    y = GlobalHWVar.gsy // 18 * 8
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreChiusuraPortaCitta)
                    i = 0
                    while i < 30:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                    avanzamentoStoria += 1
            if stanzaVecchia == GlobalGameVar.dictStanze["città2"]:
                npers = "d"
                x = GlobalHWVar.gsx // 32 * 2
    if stanza == GlobalGameVar.dictStanze["città2"]:
        if canzone != GlobalSndVar.canzoneCitta:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneCitta
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteCitta_notte:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteCitta_notte
        else:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteCitta_giorno:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteCitta_giorno
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["città1"]:
                npers = "a"
                x = GlobalHWVar.gsx // 32 * 29
            if stanzaVecchia == GlobalGameVar.dictStanze["città3"]:
                npers = "d"
                x = GlobalHWVar.gsx // 32 * 2
                y -= GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["città5"]:
                npers = "s"
                x -= GlobalHWVar.gpx * 15
                y = GlobalHWVar.gsy // 18 * 2
    if stanza == GlobalGameVar.dictStanze["città3"]:
        if canzone != GlobalSndVar.canzoneCitta:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneCitta
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteCitta_notte:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteCitta_notte
        else:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteCitta_giorno:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteCitta_giorno
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["città2"]:
                npers = "a"
                x = GlobalHWVar.gsx // 32 * 29
                y += GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["città4"]:
                npers = "d"
                x = GlobalHWVar.gsx // 32 * 2
                y -= GlobalHWVar.gpy * 6
            if stanzaVecchia == GlobalGameVar.dictStanze["città5"]:
                npers = "s"
                x += GlobalHWVar.gpx * 17
                y = GlobalHWVar.gsy // 18 * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["città9"]:
                npers = "w"
                x += GlobalHWVar.gpx * 9
                y = GlobalHWVar.gsy // 18 * 15
    if stanza == GlobalGameVar.dictStanze["città4"]:
        if canzone != GlobalSndVar.canzoneCitta:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneCitta
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteCitta_notte:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteCitta_notte
        else:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteCitta_giorno:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteCitta_giorno
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["città3"]:
                npers = "a"
                x = GlobalHWVar.gsx // 32 * 29
                y += GlobalHWVar.gpy * 6
            if stanzaVecchia == GlobalGameVar.dictStanze["casaDavid1"]:
                npers = "s"
                y = GlobalHWVar.gsy // 18 * 5
                if x == GlobalHWVar.gsx // 32 * 15:
                    x = GlobalHWVar.gsx // 32 * 11
                if x == GlobalHWVar.gsx // 32 * 16:
                    x = GlobalHWVar.gsx // 32 * 12
    if stanza == GlobalGameVar.dictStanze["città5"]:
        if canzone != GlobalSndVar.canzoneCitta:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneCitta
        if sottofondoAmbientale != GlobalSndVar.audioAmbienteCitta_giorno:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalSndVar.audioAmbienteCitta_giorno
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["città2"]:
                npers = "w"
                x += GlobalHWVar.gpx * 15
                y = GlobalHWVar.gpy * 15
            if stanzaVecchia == GlobalGameVar.dictStanze["città3"]:
                npers = "w"
                x -= GlobalHWVar.gpx * 17
                y = GlobalHWVar.gpy * 15
            if stanzaVecchia == GlobalGameVar.dictStanze["città6"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
                y -= GlobalHWVar.gpy * 8
            if stanzaVecchia == GlobalGameVar.dictStanze["città7"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
                y -= GlobalHWVar.gpy * 6
            if stanzaVecchia == GlobalGameVar.dictStanze["città8"]:
                npers = "s"
                x -= GlobalHWVar.gpx * 3
                y = GlobalHWVar.gpy * 2
    if stanza == GlobalGameVar.dictStanze["città6"]:
        if canzone != GlobalSndVar.canzoneCitta:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneCitta
        if sottofondoAmbientale != GlobalSndVar.audioAmbienteCitta_giorno:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalSndVar.audioAmbienteCitta_giorno
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["città5"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
                y += GlobalHWVar.gpy * 8
            if stanzaVecchia == GlobalGameVar.dictStanze["città10"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
                y -= GlobalHWVar.gpy * 1
    if stanza == GlobalGameVar.dictStanze["città7"]:
        if canzone != GlobalSndVar.canzoneCitta:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneCitta
        if sottofondoAmbientale != GlobalSndVar.audioAmbienteCitta_giorno:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalSndVar.audioAmbienteCitta_giorno
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["città5"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
                y += GlobalHWVar.gpy * 6
    if stanza == GlobalGameVar.dictStanze["città8"]:
        if canzone != GlobalSndVar.canzoneCitta:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneCitta
        if sottofondoAmbientale != GlobalSndVar.audioAmbienteCitta_giorno:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalSndVar.audioAmbienteCitta_giorno
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["città5"]:
                npers = "w"
                x += GlobalHWVar.gpx * 3
                y = GlobalHWVar.gpy * 15
    if stanza == GlobalGameVar.dictStanze["città9"]:
        if canzone != GlobalSndVar.canzoneCitta:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneCitta
        if sottofondoAmbientale != GlobalSndVar.audioAmbienteCitta_giorno:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalSndVar.audioAmbienteCitta_giorno
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["città3"]:
                npers = "s"
                x -= GlobalHWVar.gpx * 9
                y = GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["stradaPerSelvaArida1"]:
                npers = "w"
                x = GlobalHWVar.gpx * 18
                y = GlobalHWVar.gpy * 15
    if stanza == GlobalGameVar.dictStanze["città10"]:
        if canzone != GlobalSndVar.canzoneCitta:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneCitta
        if sottofondoAmbientale != GlobalSndVar.audioAmbienteCitta_giorno:
            sottofondoAmbientaleCambiato = True
        sottofondoAmbientale = GlobalSndVar.audioAmbienteCitta_giorno
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["città6"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
                y += GlobalHWVar.gpy * 1
            if stanzaVecchia == GlobalGameVar.dictStanze["stradaPerPassoMontano1"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
                y = GlobalHWVar.gpy * 9
    if stanza == GlobalGameVar.dictStanze["casaDavid1"]:
        if canzone != GlobalSndVar.canzoneCasaDavid:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneCasaDavid
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteCasaDavid_notte:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteCasaDavid_notte
        else:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteCasaDavid_giorno:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteCasaDavid_giorno
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCasaDavid
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCasaDavid
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["città4"]:
                npers = "w"
                y = GlobalHWVar.gsy // 18 * 15
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCasaUfficiale"]:
                    x = GlobalHWVar.gsx // 32 * 15
                    avanzamentoStoria += 1
                elif x == GlobalHWVar.gsx // 32 * 11:
                    x = GlobalHWVar.gsx // 32 * 15
                elif x == GlobalHWVar.gsx // 32 * 12:
                    x = GlobalHWVar.gsx // 32 * 16
            if stanzaVecchia == GlobalGameVar.dictStanze["casaDavid2"]:
                npers = "s"
                y = GlobalHWVar.gsy // 18 * 11
                if x == GlobalHWVar.gsx // 32 * 27:
                    x = GlobalHWVar.gsx // 32 * 28
                elif x == GlobalHWVar.gsx // 32 * 28:
                    x = GlobalHWVar.gsx // 32 * 29
    if stanza == GlobalGameVar.dictStanze["casaDavid2"]:
        if canzone != GlobalSndVar.canzoneCasaDavid:
            canzoneCambiata = True
        canzone = GlobalSndVar.canzoneCasaDavid
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteCasaDavid_notte:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteCasaDavid_notte
        else:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteCasaDavid_giorno:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteCasaDavid_giorno
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCasaDavid
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCasaDavid
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["casaDavid1"]:
                npers = "w"
                y = GlobalHWVar.gsy // 18 * 4
                if x == GlobalHWVar.gsx // 32 * 28:
                    x = GlobalHWVar.gsx // 32 * 27
                elif x == GlobalHWVar.gsx // 32 * 29:
                    x = GlobalHWVar.gsx // 32 * 28
            if stanzaVecchia == GlobalGameVar.dictStanze["casaDavid2"] and avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["cenaConDavidIniziata"]:
                npers = "s"
                x = GlobalHWVar.gsx // 32 * 14
                y = GlobalHWVar.gsy // 18 * 5
            if stanzaVecchia == GlobalGameVar.dictStanze["casaDavid3"]:
                npers = "d"
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
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteCasaDavid_notte:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteCasaDavid_notte
        else:
            if sottofondoAmbientale != GlobalSndVar.audioAmbienteCasaDavid_giorno:
                sottofondoAmbientaleCambiato = True
            sottofondoAmbientale = GlobalSndVar.audioAmbienteCasaDavid_giorno
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCasaDavid
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCasaDavid
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["casaDavid2"]:
                npers = "a"
                x = GlobalHWVar.gsx // 32 * 29
                if y == GlobalHWVar.gsy // 18 * 3:
                    y = GlobalHWVar.gsy // 18 * 10
                elif y == GlobalHWVar.gsy // 18 * 4:
                    y = GlobalHWVar.gsy // 18 * 11
                elif y == GlobalHWVar.gsy // 18 * 5:
                    y = GlobalHWVar.gsy // 18 * 12
            if stanzaVecchia == GlobalGameVar.dictStanze["casaDavid3"]:
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["fattoBagnoCasaDavid"]:
                    npers = "d"
                    x = GlobalHWVar.gsx // 32 * 6
                    y = GlobalHWVar.gsy // 18 * 11
                    i = 0
                    while i < 5:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreDoccia)
                    i = 0
                    while i < 60:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"]:
                    npers = "d"
                    x = GlobalHWVar.gsx // 32 * 8
                    y = GlobalHWVar.gsy // 18 * 5
                elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["alzatoDalLettoSecondoGiorno"]:
                    npers = "a"
                    x = GlobalHWVar.gsx // 32 * 10
                    y = GlobalHWVar.gsy // 18 * 4

    # npers: 1=d, 2=a, 3=w, 4=s
    if npers == "d":
        npers = 1
    elif npers == "a":
        npers = 2
    elif npers == "w":
        npers = 3
    elif npers == "s":
        npers = 4

    return x, y, npers, rumoreAperturaPorte, rumoreChiusuraPorte, canzoneCambiata, sottofondoAmbientaleCambiato, canzone, sottofondoAmbientale, bottoneDown, avanzamentoStoria


def scriviNomeZona(stanza, stanzaVecchia, avanzamentotoria):
    stoppaMusica = False
    if (stanzaVecchia == GlobalGameVar.dictStanze["sognoLucy4"] and stanza == GlobalGameVar.dictStanze["casaHansLucy1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta1"] and stanza == GlobalGameVar.dictStanze["casaHansLucy4"]) or (stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"] and stanza == GlobalGameVar.dictStanze["casaHansLucy1"]):
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.nero)
        FunzioniGraficheGeneriche.messaggio("Casa", GlobalHWVar.grigiochi, GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 8, 150, centrale=True)
        GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 4), int(GlobalHWVar.gpy * 10.6)), (int(GlobalHWVar.gpx * 28) - 1, int(GlobalHWVar.gpy * 10.6)), 2)
        FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=2)
        GlobalHWVar.aggiornaSchermo()
        if stanzaVecchia == GlobalGameVar.dictStanze["sognoLucy4"] and stanza == GlobalGameVar.dictStanze["casaHansLucy1"]:
            stoppaMusica = True
    elif (stanzaVecchia == GlobalGameVar.dictStanze["casaHansLucy4"] and stanza == GlobalGameVar.dictStanze["forestaCadetta1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà1"] and stanza == GlobalGameVar.dictStanze["forestaCadetta9"]):
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.nero)
        FunzioniGraficheGeneriche.messaggio("Foresta Cadetta", GlobalHWVar.grigiochi, GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 8, 150, centrale=True)
        GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 4), int(GlobalHWVar.gpy * 10.6)), (int(GlobalHWVar.gpx * 28) - 1, int(GlobalHWVar.gpy * 10.6)), 2)
        FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=2)
        GlobalHWVar.aggiornaSchermo()
    elif (stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta9"] and stanza == GlobalGameVar.dictStanze["stradaPerCittà1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["città1"] and stanza == GlobalGameVar.dictStanze["stradaPerCittà3"]):
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.nero)
        FunzioniGraficheGeneriche.messaggio(u"Strada per la città", GlobalHWVar.grigiochi, GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 8, 150, centrale=True)
        GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 4), int(GlobalHWVar.gpy * 10.6)), (int(GlobalHWVar.gpx * 28) - 1, int(GlobalHWVar.gpy * 10.6)), 2)
        FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=2)
        GlobalHWVar.aggiornaSchermo()
    elif (stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà3"] and stanza == GlobalGameVar.dictStanze["città1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["casaDavid1"] and stanza == GlobalGameVar.dictStanze["città4"]) or (stanzaVecchia == GlobalGameVar.dictStanze["stradaPerSelvaArida1"] and stanza == GlobalGameVar.dictStanze["città9"]) or (stanzaVecchia == GlobalGameVar.dictStanze["stradaPerPassoMontano1"] and stanza == GlobalGameVar.dictStanze["città10"]):
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.nero)
        FunzioniGraficheGeneriche.messaggio(u"Città", GlobalHWVar.grigiochi, GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 8, 150, centrale=True)
        GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 4), int(GlobalHWVar.gpy * 10.6)), (int(GlobalHWVar.gpx * 28) - 1, int(GlobalHWVar.gpy * 10.6)), 2)
        FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=2)
        GlobalHWVar.aggiornaSchermo()
    elif stanzaVecchia == GlobalGameVar.dictStanze["città4"] and stanza == GlobalGameVar.dictStanze["casaDavid1"]:
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.nero)
        FunzioniGraficheGeneriche.messaggio(u"Casa di David", GlobalHWVar.grigiochi, GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 8, 150, centrale=True)
        GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 4), int(GlobalHWVar.gpy * 10.6)), (int(GlobalHWVar.gpx * 28) - 1, int(GlobalHWVar.gpy * 10.6)), 2)
        FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=2)
        GlobalHWVar.aggiornaSchermo()
        if avanzamentotoria <= GlobalGameVar.dictAvanzamentoStoria["arrivoCasaUfficiale"]:
            stoppaMusica = True

    if GlobalGameVar.dictStanze["stradaPerCittà1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerCittà3"] and avanzamentotoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
        stoppaMusica = True
    elif GlobalGameVar.dictStanze["città1"] <= stanza <= GlobalGameVar.dictStanze["città4"] and avanzamentotoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
        stoppaMusica = True

    return stoppaMusica


def nonPuoiProcedere(avanzamentoStoria, stanzaVecchia, stanzaDestinazione):
    nonProcedere = False

    if stanzaDestinazione == -1:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tutorialUtilizzoOggetti"] and stanzaVecchia == GlobalGameVar.dictStanze["sognoLucy1"] and stanzaDestinazione == GlobalGameVar.dictStanze["sognoLucy2"]:
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
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCittà2"] and stanzaVecchia == GlobalGameVar.dictStanze["città1"] and stanzaDestinazione == GlobalGameVar.dictStanze["città2"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and stanzaVecchia == GlobalGameVar.dictStanze["città2"] and (stanzaDestinazione == GlobalGameVar.dictStanze["città1"] or stanzaDestinazione == GlobalGameVar.dictStanze["città5"]):
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCittà3"] and stanzaVecchia == GlobalGameVar.dictStanze["città2"] and stanzaDestinazione == GlobalGameVar.dictStanze["città3"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and stanzaVecchia == GlobalGameVar.dictStanze["città3"] and (stanzaDestinazione == GlobalGameVar.dictStanze["città2"] or stanzaDestinazione == GlobalGameVar.dictStanze["città5"] or stanzaDestinazione == GlobalGameVar.dictStanze["città9"]):
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCittà4"] and stanzaVecchia == GlobalGameVar.dictStanze["città3"] and stanzaDestinazione == GlobalGameVar.dictStanze["città4"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and stanzaVecchia == GlobalGameVar.dictStanze["città4"] and stanzaDestinazione == GlobalGameVar.dictStanze["città3"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCasaUfficiale"] and stanzaVecchia == GlobalGameVar.dictStanze["città4"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaDavid1"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and stanzaVecchia == GlobalGameVar.dictStanze["casaDavid1"] and stanzaDestinazione == GlobalGameVar.dictStanze["città4"]:
        nonProcedere = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoDopoBagnoDavid"] and stanzaVecchia == GlobalGameVar.dictStanze["casaDavid3"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaDavid2"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and stanzaVecchia == GlobalGameVar.dictStanze["città9"] and stanzaDestinazione == GlobalGameVar.dictStanze["stradaPerSelvaArida1"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"] and stanzaVecchia == GlobalGameVar.dictStanze["città10"] and stanzaDestinazione == GlobalGameVar.dictStanze["stradaPerPassoMontano1"]:
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
    if stanza == GlobalGameVar.dictStanze["casaHansLucy4"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
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
    if stanza == GlobalGameVar.dictStanze["città1"] or stanza == GlobalGameVar.dictStanze["città2"] or stanza == GlobalGameVar.dictStanze["città3"] or stanza == GlobalGameVar.dictStanze["città4"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["casaDavid1"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["casaDavid2"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sedutoACenaDavid"]:
            nomeStanza = "StanzaA"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaC"
    if stanza == GlobalGameVar.dictStanze["casaDavid3"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["andatoADormireCasaDavid"]:
            nomeStanza = "StanzaA"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoServoRisveglioSecondoGiorno"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaC"

    return nomeStanza
