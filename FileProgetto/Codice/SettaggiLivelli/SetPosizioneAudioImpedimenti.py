# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.CaricaFileProgetto as CaricaFileProgetto
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche


def settaPosizioneERumoriStanza(x, y, npers, rumoreAperturaPorte, rumoreChiusuraPorte, canzoneCambiata, sottofondoAmbientaleCambiato, stanza, stanzaVecchia, canzone, listaSottofondoAmbientale, inizio, avanzamentoStoria, bottoneDown):
    mantieniPosizioneImpo = False
    pathMusiche = "Risorse/Audio/Canzoni/"
    pathSottofondi = "Risorse/Audio/RumoriAmbiente/SottofondoPerZona/"

    if stanza == GlobalGameVar.dictStanze["sognoLucy1"]:
        nomeCanzoneLuogo = "01-Sogno"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Sogno"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Vento2 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento2.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Vento2]
            sottofondoAmbientaleCambiato = True
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
        nomeCanzoneLuogo = "01-Sogno"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Sogno"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Vento2 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento2.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Vento2]
            sottofondoAmbientaleCambiato = True
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
        nomeCanzoneLuogo = "01-Sogno"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Sogno"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Vento2 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento2.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Vento2]
            sottofondoAmbientaleCambiato = True
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
        nomeCanzoneLuogo = "01-Sogno"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Sogno"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Vento2 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento2.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Vento2]
            sottofondoAmbientaleCambiato = True
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
        nomeCanzoneLuogo = "02-Casa"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "CasaInterno"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Cicale = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Cicale.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Cicale]
            sottofondoAmbientaleCambiato = True
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
        nomeCanzoneLuogo = "03-EsterniPacifici"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "CasaEsterno"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Cicale = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Cicale.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Cicale]
            sottofondoAmbientaleCambiato = True
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
                y = GlobalHWVar.gsy // 18 * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["casaHansLucy4"]:
                npers = "w"
                y = GlobalHWVar.gsy // 18 * 15
    if stanza == GlobalGameVar.dictStanze["casaHansLucy3"]:
        nomeCanzoneLuogo = "03-EsterniPacifici"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "CasaEsterno"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Cicale = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Cicale.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Cicale]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCasa
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCasa

        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["casaHansLucy2"]:
                npers = "w"
                y = GlobalHWVar.gsy // 18 * 15
    if stanza == GlobalGameVar.dictStanze["casaHansLucy4"]:
        nomeCanzoneLuogo = "03-EsterniPacifici"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "CasaEsterno"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Cicale = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Cicale.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Cicale]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCasa
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCasa

        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["casaHansLucy2"]:
                npers = "s"
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
        nomeCanzoneLuogo = "04-Foresta"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "ForestaCadetta/StanzeNormali"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Cicale = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Cicale.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Cicale]
            sottofondoAmbientaleCambiato = True
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
        nomeCanzoneLuogo = "04-Foresta"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "ForestaCadetta/StanzeNormali"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Cicale = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Cicale.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Cicale]
            sottofondoAmbientaleCambiato = True
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
        nomeCanzoneLuogo = "04-Foresta"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "ForestaCadetta/StanzeNormali"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Cicale = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Cicale.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Cicale]
            sottofondoAmbientaleCambiato = True
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
        nomeCanzoneLuogo = "04-Foresta"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "ForestaCadetta/StanzeNormali"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Cicale = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Cicale.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Cicale]
            sottofondoAmbientaleCambiato = True
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
        nomeCanzoneLuogo = "04-Foresta"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioUltimoDialogoHans"]:
            sottofondoLuogo = "ForestaCadetta/AccampamentoConFuoco"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Cicale = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Cicale.wav")
                audioAmbiente_Fuoco = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Fuoco.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Cicale, audioAmbiente_Fuoco]
                sottofondoAmbientaleCambiato = True
        else:
            sottofondoLuogo = "ForestaCadetta/StanzeNormali"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Cicale = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Cicale.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Cicale]
                sottofondoAmbientaleCambiato = True
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
        nomeCanzoneLuogo = "04-Foresta"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "ForestaCadetta/StanzeNormali"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Cicale = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Cicale.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Cicale]
            sottofondoAmbientaleCambiato = True
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
        nomeCanzoneLuogo = "04-Foresta"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "ForestaCadetta/StanzeNormali"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Cicale = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Cicale.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Cicale]
            sottofondoAmbientaleCambiato = True
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
        nomeCanzoneLuogo = "04-Foresta"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "ForestaCadetta/StanzeNormali"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Cicale = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Cicale.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Cicale]
            sottofondoAmbientaleCambiato = True
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
        nomeCanzoneLuogo = "04-Foresta"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "ForestaCadetta/StanzeNormali"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Cicale = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Cicale.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Cicale]
            sottofondoAmbientaleCambiato = True
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
        nomeCanzoneLuogo = "03-EsterniPacifici"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            sottofondoLuogo = "StradaPerCitta1/Notte"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Cicale = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Cicale.wav")
                audioAmbiente_Fuoco = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Fuoco.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Cicale, audioAmbiente_Fuoco]
                sottofondoAmbientaleCambiato = True
        else:
            sottofondoLuogo = "StradaPerCitta1/Giorno"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Cicale = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Cicale.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Cicale]
                sottofondoAmbientaleCambiato = True
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
                y += GlobalHWVar.gpy * 2
    if stanza == GlobalGameVar.dictStanze["stradaPerCittà2"]:
        nomeCanzoneLuogo = "03-EsterniPacifici"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            sottofondoLuogo = "StradaPerCitta2/Notte"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Cicale = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Cicale.wav")
                audioAmbiente_Fuoco = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Fuoco.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Cicale, audioAmbiente_Fuoco]
                sottofondoAmbientaleCambiato = True
        else:
            sottofondoLuogo = "StradaPerCitta2/Giorno"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Cicale = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Cicale.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Cicale]
                sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False

        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà1"]:
                npers = "a"
                x = GlobalHWVar.gsx // 32 * 29
                y -= GlobalHWVar.gsy // 18 * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà3"]:
                npers = "d"
                x = GlobalHWVar.gsx // 32 * 2
    if stanza == GlobalGameVar.dictStanze["stradaPerCittà3"]:
        nomeCanzoneLuogo = "03-EsterniPacifici"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            sottofondoLuogo = "StradaPerCitta3/Notte"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Fuoco = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Fuoco.wav")
                audioAmbiente_Fiume = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Fiume.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Fuoco, audioAmbiente_Fiume]
                sottofondoAmbientaleCambiato = True
        else:
            sottofondoLuogo = "StradaPerCitta3/Giorno"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Fiume = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Fiume.wav")
                audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Fiume, audioAmbiente_Persone]
                sottofondoAmbientaleCambiato = True
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
        nomeCanzoneLuogo = "05-Città"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            sottofondoLuogo = "Citta/Notte"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Fuoco = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Fuoco.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Fuoco]
                sottofondoAmbientaleCambiato = True
        else:
            sottofondoLuogo = "Citta/Giorno"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
                sottofondoAmbientaleCambiato = True
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
        nomeCanzoneLuogo = "05-Città"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            sottofondoLuogo = "Citta/Notte"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Fuoco = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Fuoco.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Fuoco]
                sottofondoAmbientaleCambiato = True
        else:
            sottofondoLuogo = "Citta/Giorno"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
                sottofondoAmbientaleCambiato = True
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
        nomeCanzoneLuogo = "05-Città"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            sottofondoLuogo = "Citta/Notte"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Fuoco = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Fuoco.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Fuoco]
                sottofondoAmbientaleCambiato = True
        else:
            sottofondoLuogo = "Citta/Giorno"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
                sottofondoAmbientaleCambiato = True
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
        nomeCanzoneLuogo = "05-Città"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            sottofondoLuogo = "Citta/Notte"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Fuoco = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Fuoco.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Fuoco]
                sottofondoAmbientaleCambiato = True
        else:
            sottofondoLuogo = "Citta/Giorno"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
                sottofondoAmbientaleCambiato = True
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
        nomeCanzoneLuogo = "05-Città"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Citta/Giorno"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
            sottofondoAmbientaleCambiato = True
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
        nomeCanzoneLuogo = "05-Città"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Citta/Giorno"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
            sottofondoAmbientaleCambiato = True
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
        nomeCanzoneLuogo = "05-Città"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Citta/Giorno"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False

        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["città5"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
                y += GlobalHWVar.gpy * 6
            if stanzaVecchia == GlobalGameVar.dictStanze["biblioteca1"]:
                npers = "s"
                x += GlobalHWVar.gpx * 3
                y = GlobalHWVar.gpy * 6
    if stanza == GlobalGameVar.dictStanze["città8"]:
        nomeCanzoneLuogo = "05-Città"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Citta/Giorno"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
            sottofondoAmbientaleCambiato = True
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
        nomeCanzoneLuogo = "05-Città"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Citta/Giorno"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
            sottofondoAmbientaleCambiato = True
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
                if x == GlobalHWVar.gpx * 16 or x == GlobalHWVar.gpx * 17:
                    x += GlobalHWVar.gpx * 3
                else:
                    x += GlobalHWVar.gpx * 2
                y = GlobalHWVar.gpy * 15
    if stanza == GlobalGameVar.dictStanze["città10"]:
        nomeCanzoneLuogo = "05-Città"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Citta/Giorno"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
            sottofondoAmbientaleCambiato = True
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
        nomeCanzoneLuogo = "06-CasaUfficiale"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            sottofondoLuogo = "CasaUfficiale/Notte"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1]
                sottofondoAmbientaleCambiato = True
        else:
            sottofondoLuogo = "CasaUfficiale/Giorno"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
                sottofondoAmbientaleCambiato = True
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
        nomeCanzoneLuogo = "06-CasaUfficiale"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            sottofondoLuogo = "CasaUfficiale/Notte"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1]
                sottofondoAmbientaleCambiato = True
        else:
            sottofondoLuogo = "CasaUfficiale/Giorno"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
                sottofondoAmbientaleCambiato = True
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
        nomeCanzoneLuogo = "06-CasaUfficiale"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            sottofondoLuogo = "CasaUfficiale/Notte"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1]
                sottofondoAmbientaleCambiato = True
        else:
            sottofondoLuogo = "CasaUfficiale/Giorno"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
                sottofondoAmbientaleCambiato = True
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
    if stanza == GlobalGameVar.dictStanze["biblioteca1"]:
        nomeCanzoneLuogo = "07-Biblioteca"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Biblioteca"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False

        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["città7"]:
                npers = "w"
                x -= GlobalHWVar.gsx // 32 * 3
                y = GlobalHWVar.gsy // 18 * 15
            elif stanzaVecchia == GlobalGameVar.dictStanze["biblioteca2"]:
                npers = "s"
                y = GlobalHWVar.gsy // 18 * 2
    if stanza == GlobalGameVar.dictStanze["biblioteca2"]:
        nomeCanzoneLuogo = "07-Biblioteca"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Biblioteca"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False

        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["biblioteca1"]:
                npers = "w"
                y = GlobalHWVar.gsy // 18 * 15
            elif stanzaVecchia == GlobalGameVar.dictStanze["biblioteca3"]:
                npers = "d"
                x = GlobalHWVar.gsx // 32 * 22
                y = GlobalHWVar.gsy // 18 * 11
    if stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        nomeCanzoneLuogo = "07-Biblioteca"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Biblioteca"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False

        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["biblioteca2"]:
                npers = "a"
                x = GlobalHWVar.gsx // 32 * 20
                y = GlobalHWVar.gsy // 18 * 9
            elif stanzaVecchia == GlobalGameVar.dictStanze["biblioteca3"]:
                mantieniPosizioneImpo = True
    if stanza == GlobalGameVar.dictStanze["stradaPerSelvaArida1"]:
        nomeCanzoneLuogo = "03-EsterniPacifici"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "StradaPerSelvaArida1"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False

        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["città9"]:
                npers = "s"
                if x == GlobalHWVar.gpx * 19 or x == GlobalHWVar.gpx * 20:
                    x -= GlobalHWVar.gpx * 3
                else:
                    x -= GlobalHWVar.gpx * 2
                y = GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["stradaPerSelvaArida2"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
    if stanza == GlobalGameVar.dictStanze["stradaPerSelvaArida2"]:
        nomeCanzoneLuogo = "03-EsterniPacifici"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "StradaPerSelvaArida2"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Serpenti = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Serpenti.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Serpenti]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False

        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["stradaPerSelvaArida1"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida1"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
    if stanza == GlobalGameVar.dictStanze["selvaArida1"]:
        nomeCanzoneLuogo = "08-SelvaArida"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "SelvaArida"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Serpenti = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Serpenti.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Serpenti]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteSelva
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteSelva

        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["stradaPerSelvaArida2"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida2"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
                x -= GlobalHWVar.gpx * 15
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida7"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida8"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida10"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
                x += GlobalHWVar.gpx * 18
    if stanza == GlobalGameVar.dictStanze["selvaArida2"]:
        nomeCanzoneLuogo = "08-SelvaArida"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "SelvaArida"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Serpenti = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Serpenti.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Serpenti]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteSelva
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteSelva

        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida1"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
                x += GlobalHWVar.gpx * 15
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida3"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
                x += GlobalHWVar.gpx * 17
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida8"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
                x -= GlobalHWVar.gpx * 18
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida9"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
                y += GlobalHWVar.gpy * 12
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida10"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
    if stanza == GlobalGameVar.dictStanze["selvaArida3"]:
        nomeCanzoneLuogo = "08-SelvaArida"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "SelvaArida"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Serpenti = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Serpenti.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Serpenti]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteSelva
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteSelva

        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida2"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
                x -= GlobalHWVar.gpx * 17
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida4"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
                y += GlobalHWVar.gpy * 12
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida10"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
                x += GlobalHWVar.gpx * 16
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida12"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
                y += GlobalHWVar.gpy * 6
    if stanza == GlobalGameVar.dictStanze["selvaArida4"]:
        nomeCanzoneLuogo = "08-SelvaArida"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "SelvaArida"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Serpenti = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Serpenti.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Serpenti]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteSelva
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteSelva

        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida3"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
                y -= GlobalHWVar.gpy * 12
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida5"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
                x += GlobalHWVar.gpx * 15
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida9"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
                x -= GlobalHWVar.gpx * 17
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida13"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
                y += GlobalHWVar.gpy * 8
    if stanza == GlobalGameVar.dictStanze["selvaArida5"]:
        nomeCanzoneLuogo = "08-SelvaArida"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "SelvaArida"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Serpenti = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Serpenti.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Serpenti]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteSelva
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteSelva

        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida4"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
                x -= GlobalHWVar.gpx * 15
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida6"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
                y += GlobalHWVar.gpy * 8
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida14"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
                y -= GlobalHWVar.gpy * 6
    if stanza == GlobalGameVar.dictStanze["selvaArida6"]:
        nomeCanzoneLuogo = "08-SelvaArida"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "SelvaArida"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Serpenti = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Serpenti.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Serpenti]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteSelva
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteSelva

        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida5"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
                y -= GlobalHWVar.gpy * 8
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida13"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
                x -= GlobalHWVar.gpx * 15
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida15"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
                x -= GlobalHWVar.gpx * 11
    if stanza == GlobalGameVar.dictStanze["selvaArida7"]:
        nomeCanzoneLuogo = "08-SelvaArida"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "SelvaArida"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Serpenti = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Serpenti.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Serpenti]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteSelva
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteSelva

        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida1"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida10"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
                x -= GlobalHWVar.gpx * 15
    if stanza == GlobalGameVar.dictStanze["selvaArida8"]:
        nomeCanzoneLuogo = "08-SelvaArida"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "SelvaArida"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Serpenti = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Serpenti.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Serpenti]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteSelva
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteSelva

        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida1"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida2"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
                x += GlobalHWVar.gpx * 18
    if stanza == GlobalGameVar.dictStanze["selvaArida9"]:
        nomeCanzoneLuogo = "08-SelvaArida"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "SelvaArida"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Serpenti = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Serpenti.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Serpenti]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteSelva
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteSelva

        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida2"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
                y -= GlobalHWVar.gpy * 12
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida4"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
                x += GlobalHWVar.gpx * 17
    if stanza == GlobalGameVar.dictStanze["selvaArida10"]:
        nomeCanzoneLuogo = "08-SelvaArida"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "SelvaArida"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Serpenti = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Serpenti.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Serpenti]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteSelva
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteSelva

        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida1"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
                x -= GlobalHWVar.gpx * 18
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida2"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida3"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
                x -= GlobalHWVar.gpx * 16
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida7"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
                x += GlobalHWVar.gpx * 15
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida11"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
                y += GlobalHWVar.gpy * 6
    if stanza == GlobalGameVar.dictStanze["selvaArida11"]:
        nomeCanzoneLuogo = "08-SelvaArida"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "SelvaArida"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Serpenti = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Serpenti.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Serpenti]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteSelva
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteSelva

        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida10"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
                y -= GlobalHWVar.gpy * 6
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida12"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
                x -= GlobalHWVar.gpx * 16
    if stanza == GlobalGameVar.dictStanze["selvaArida12"]:
        nomeCanzoneLuogo = "08-SelvaArida"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "SelvaArida"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Serpenti = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Serpenti.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Serpenti]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteSelva
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteSelva

        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida3"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
                y -= GlobalHWVar.gpy * 6
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida11"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
                x += GlobalHWVar.gpx * 16
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida14"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
                x -= GlobalHWVar.gpx * 18
    if stanza == GlobalGameVar.dictStanze["selvaArida13"]:
        nomeCanzoneLuogo = "08-SelvaArida"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "SelvaArida"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Serpenti = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Serpenti.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Serpenti]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteSelva
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteSelva

        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida4"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
                y -= GlobalHWVar.gpy * 8
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida6"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
                x += GlobalHWVar.gpx * 15
    if stanza == GlobalGameVar.dictStanze["selvaArida14"]:
        nomeCanzoneLuogo = "08-SelvaArida"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "SelvaArida"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Serpenti = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Serpenti.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Serpenti]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteSelva
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteSelva

        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida5"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
                y += GlobalHWVar.gpy * 6
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida12"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
                x += GlobalHWVar.gpx * 18
    if stanza == GlobalGameVar.dictStanze["selvaArida15"]:
        nomeCanzoneLuogo = "08-SelvaArida"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "SelvaArida"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Serpenti = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Serpenti.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Serpenti]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteSelva
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteSelva

        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida6"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
                x += GlobalHWVar.gpx * 11
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida16"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
    if stanza == GlobalGameVar.dictStanze["selvaArida16"]:
        nomeCanzoneLuogo = "08-SelvaArida"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "SelvaAridaUltimaStanza"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Serpenti = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Serpenti.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Serpenti]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteSelva
        rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteSelva

        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida15"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod1"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
                x -= GlobalHWVar.gpx * 12
    if stanza == GlobalGameVar.dictStanze["avampostoDiRod1"]:
        nomeCanzoneLuogo = "03-EsterniPacifici"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "AvampostoDiRod"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            audioAmbiente_Serpenti = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Serpenti.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Serpenti]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["selvaArida16"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
                x += GlobalHWVar.gpx * 12
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto3"]:
                npers = "w"
                x = GlobalHWVar.gpx * 21
                y = GlobalHWVar.gpy * 15
            if stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod3"]:
                npers = "d"
                x = GlobalHWVar.gpx * 6
                y = GlobalHWVar.gpy * 4
    if stanza == GlobalGameVar.dictStanze["labirinto1"]:
        nomeCanzoneLuogo = "09-Labirinto"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Labirinto"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto2"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto4"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
    if stanza == GlobalGameVar.dictStanze["labirinto2"]:
        nomeCanzoneLuogo = "09-Labirinto"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Labirinto"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto1"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto3"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto5"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
    if stanza == GlobalGameVar.dictStanze["labirinto3"]:
        nomeCanzoneLuogo = "09-Labirinto"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Labirinto"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod1"]:
                npers = "s"
                x = GlobalHWVar.gpx * 13
                y = GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto2"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto6"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
    if stanza == GlobalGameVar.dictStanze["labirinto4"]:
        nomeCanzoneLuogo = "09-Labirinto"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Labirinto"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto1"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto5"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto8"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
    if stanza == GlobalGameVar.dictStanze["labirinto5"]:
        nomeCanzoneLuogo = "09-Labirinto"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Labirinto"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto2"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto6"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto4"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto9"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
    if stanza == GlobalGameVar.dictStanze["labirinto6"]:
        nomeCanzoneLuogo = "09-Labirinto"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Labirinto"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto3"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto7"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto5"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto10"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
    if stanza == GlobalGameVar.dictStanze["labirinto7"]:
        nomeCanzoneLuogo = "09-Labirinto"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Labirinto"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto8"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto6"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto11"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
    if stanza == GlobalGameVar.dictStanze["labirinto8"]:
        nomeCanzoneLuogo = "09-Labirinto"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Labirinto"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto4"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto9"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto12"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
    if stanza == GlobalGameVar.dictStanze["labirinto9"]:
        nomeCanzoneLuogo = "09-Labirinto"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Labirinto"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto5"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto10"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto8"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto13"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
    if stanza == GlobalGameVar.dictStanze["labirinto10"]:
        nomeCanzoneLuogo = "09-Labirinto"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Labirinto"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto6"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto11"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto9"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto14"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
    if stanza == GlobalGameVar.dictStanze["labirinto11"]:
        nomeCanzoneLuogo = "09-Labirinto"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Labirinto"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto7"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto10"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto15"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
    if stanza == GlobalGameVar.dictStanze["labirinto12"]:
        nomeCanzoneLuogo = "09-Labirinto"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Labirinto"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto8"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto13"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto16"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
    if stanza == GlobalGameVar.dictStanze["labirinto13"]:
        nomeCanzoneLuogo = "09-Labirinto"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Labirinto"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto9"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto14"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto12"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto17"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
    if stanza == GlobalGameVar.dictStanze["labirinto14"]:
        nomeCanzoneLuogo = "09-Labirinto"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Labirinto"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto10"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto15"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto13"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto18"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
    if stanza == GlobalGameVar.dictStanze["labirinto15"]:
        nomeCanzoneLuogo = "09-Labirinto"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Labirinto"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto11"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto14"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto19"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
    if stanza == GlobalGameVar.dictStanze["labirinto16"]:
        nomeCanzoneLuogo = "09-Labirinto"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Labirinto"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto12"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto17"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto20"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
    if stanza == GlobalGameVar.dictStanze["labirinto17"]:
        nomeCanzoneLuogo = "09-Labirinto"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Labirinto"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto13"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto16"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto18"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto21"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
    if stanza == GlobalGameVar.dictStanze["labirinto18"]:
        nomeCanzoneLuogo = "09-Labirinto"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Labirinto"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto14"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto17"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto19"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto22"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
    if stanza == GlobalGameVar.dictStanze["labirinto19"]:
        nomeCanzoneLuogo = "09-Labirinto"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Labirinto"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto15"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto18"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto23"]:
                npers = "w"
                y = GlobalHWVar.gpy * 15
    if stanza == GlobalGameVar.dictStanze["labirinto20"]:
        nomeCanzoneLuogo = "09-Labirinto"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Labirinto"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto16"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto21"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
            if stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello1"]:
                npers = "w"
                x = GlobalHWVar.gpx * 13
                y = GlobalHWVar.gpy * 15
    if stanza == GlobalGameVar.dictStanze["labirinto21"]:
        nomeCanzoneLuogo = "09-Labirinto"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Labirinto"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto17"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto20"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto22"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
    if stanza == GlobalGameVar.dictStanze["labirinto22"]:
        nomeCanzoneLuogo = "09-Labirinto"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Labirinto"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto18"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto21"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto23"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
    if stanza == GlobalGameVar.dictStanze["labirinto23"]:
        nomeCanzoneLuogo = "09-Labirinto"
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
            canzoneCambiata = True
        sottofondoLuogo = "Labirinto"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto19"]:
                npers = "s"
                y = GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto22"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
    if stanza == GlobalGameVar.dictStanze["esternoCastello1"]:
        nomeCanzoneLuogo = ""
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = False
            canzoneCambiata = True
        sottofondoLuogo = "EsternoCastello"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["labirinto20"]:
                npers = "s"
                x = GlobalHWVar.gpx * 13
                y = GlobalHWVar.gpy * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello2"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
            if stanzaVecchia == GlobalGameVar.dictStanze["scorciatoiaLabirinto1"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
                y = GlobalHWVar.gpy * 9
    if stanza == GlobalGameVar.dictStanze["esternoCastello2"]:
        nomeCanzoneLuogo = ""
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = False
            canzoneCambiata = True
        sottofondoLuogo = "EsternoCastello"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello1"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2
            if stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello4"]:
                npers = "w"
                x = GlobalHWVar.gpx * 18
                y = GlobalHWVar.gpy * 15
            if stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello3"]:
                npers = "a"
                x = GlobalHWVar.gpx * 29
            if stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello2"]:
                npers = "s"
                x = GlobalHWVar.gpx * 19
                y = GlobalHWVar.gpy * 12
                GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreAperturaCancelloCastello)
                i = 0
                while i < 20:
                    pygame.time.wait(100)
                    inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                    i += 1
    if stanza == GlobalGameVar.dictStanze["esternoCastello3"]:
        nomeCanzoneLuogo = ""
        if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
            GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
            canzone = False
            canzoneCambiata = True
        sottofondoLuogo = "EsternoCastello"
        if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
            GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
            audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
            listaSottofondoAmbientale = [audioAmbiente_Vento1]
            sottofondoAmbientaleCambiato = True
        # rumore porte
        rumoreAperturaPorte = False
        rumoreChiusuraPorte = False
        # posizione personaggio e robot al cambio stanza
        if not inizio:
            if stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello2"]:
                npers = "d"
                x = GlobalHWVar.gpx * 2

    # npers: 1=d, 2=a, 3=w, 4=s
    if npers == "d":
        npers = 1
    elif npers == "a":
        npers = 2
    elif npers == "w":
        npers = 3
    elif npers == "s":
        npers = 4

    return x, y, npers, rumoreAperturaPorte, rumoreChiusuraPorte, canzoneCambiata, sottofondoAmbientaleCambiato, canzone, listaSottofondoAmbientale, bottoneDown, avanzamentoStoria, mantieniPosizioneImpo


def scriviNomeZona(stanza, stanzaVecchia):
    nomeDaScrivere = False
    if (stanzaVecchia == GlobalGameVar.dictStanze["sognoLucy4"] and stanza == GlobalGameVar.dictStanze["casaHansLucy1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta1"] and stanza == GlobalGameVar.dictStanze["casaHansLucy4"]) or (stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"] and stanza == GlobalGameVar.dictStanze["casaHansLucy1"]):
        nomeDaScrivere = "Casa"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["casaHansLucy4"] and stanza == GlobalGameVar.dictStanze["forestaCadetta1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà1"] and stanza == GlobalGameVar.dictStanze["forestaCadetta9"]):
        nomeDaScrivere = "Foresta Cadetta"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta9"] and stanza == GlobalGameVar.dictStanze["stradaPerCittà1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["città1"] and stanza == GlobalGameVar.dictStanze["stradaPerCittà3"]):
        nomeDaScrivere = u"Strada per Città"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà3"] and stanza == GlobalGameVar.dictStanze["città1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["casaDavid1"] and stanza == GlobalGameVar.dictStanze["città4"]) or (stanzaVecchia == GlobalGameVar.dictStanze["biblioteca1"] and stanza == GlobalGameVar.dictStanze["città7"]) or (stanzaVecchia == GlobalGameVar.dictStanze["stradaPerSelvaArida1"] and stanza == GlobalGameVar.dictStanze["città9"]) or (stanzaVecchia == GlobalGameVar.dictStanze["stradaPerPassoMontano1"] and stanza == GlobalGameVar.dictStanze["città10"]):
        nomeDaScrivere = u"Città"
    elif stanzaVecchia == GlobalGameVar.dictStanze["città4"] and stanza == GlobalGameVar.dictStanze["casaDavid1"]:
        nomeDaScrivere = u"Casa di David"
    elif stanzaVecchia == GlobalGameVar.dictStanze["città7"] and stanza == GlobalGameVar.dictStanze["biblioteca1"]:
        nomeDaScrivere = u"Biblioteca"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["città9"] and stanza == GlobalGameVar.dictStanze["stradaPerSelvaArida1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["selvaArida1"] and stanza == GlobalGameVar.dictStanze["stradaPerSelvaArida2"]):
        nomeDaScrivere = u"Strada per Selva Arida"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["stradaPerSelvaArida2"] and stanza == GlobalGameVar.dictStanze["selvaArida1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod1"] and stanza == GlobalGameVar.dictStanze["selvaArida16"]):
        nomeDaScrivere = u"Selva Arida"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["selvaArida16"] and stanza == GlobalGameVar.dictStanze["avampostoDiRod1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["labirinto3"] and stanza == GlobalGameVar.dictStanze["avampostoDiRod1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["scorciatoiaLabirinto2"] and stanza == GlobalGameVar.dictStanze["avampostoDiRod2"]):
        nomeDaScrivere = u"Avamposto di Rod"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod1"] and stanza == GlobalGameVar.dictStanze["labirinto3"]) or (stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello1"] and stanza == GlobalGameVar.dictStanze["labirinto20"]):
        nomeDaScrivere = u"Labirinto"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["labirinto20"] and stanza == GlobalGameVar.dictStanze["esternoCastello1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["internoCastello1"] and stanza == GlobalGameVar.dictStanze["esternoCastello5"]):
        nomeDaScrivere = u"Castello di Neil - Esterno"

    if nomeDaScrivere:
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
        FunzioniGraficheGeneriche.messaggio(nomeDaScrivere, GlobalHWVar.grigiochi, GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 8, 150, centrale=True)
        GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 4), int(GlobalHWVar.gpy * 10.6)), (int(GlobalHWVar.gpx * 28) - 1, int(GlobalHWVar.gpy * 10.6)), 2)
        FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=2)
        GlobalHWVar.aggiornaSchermo()


def decidiSeStoppareMusica(stanza, avanzamentoStoria):
    stoppaMusica = False
    if stanza == GlobalGameVar.dictStanze["casaHansLucy1"] and avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"]:
        stoppaMusica = True
    elif stanza == GlobalGameVar.dictStanze["forestaCadetta5"] and avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioUltimoDialogoHans"]:
        stoppaMusica = True
    elif GlobalGameVar.dictStanze["stradaPerCittà1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerCittà3"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
        stoppaMusica = True
    elif GlobalGameVar.dictStanze["città1"] <= stanza <= GlobalGameVar.dictStanze["città4"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
        stoppaMusica = True
    elif stanza == GlobalGameVar.dictStanze["casaDavid1"] and avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCasaUfficiale"]:
        stoppaMusica = True
    elif GlobalGameVar.dictAvanzamentoStoria["padreUfficialeUscitoDallaCena"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["alzatoDalLettoSecondoGiorno"]:
        stoppaMusica = True
    elif GlobalGameVar.dictAvanzamentoStoria["vistoDalServo"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["uscitoCasaDavidDopoSuicidio"]:
        stoppaMusica = True
    elif GlobalGameVar.dictAvanzamentoStoria["incontratoIDueAggressori"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["riavviatoMusicaPostDialogoBibliotecario"]:
        stoppaMusica = True

    return stoppaMusica


def decidiSeDimezzareVolumeMusica(avanzamentoStoria):
    GlobalGameVar.volumeMusicaDimezzato = False
    if GlobalGameVar.dictAvanzamentoStoria["inizio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tutorialMovimento"]:
        GlobalGameVar.volumeMusicaDimezzato = True
    elif GlobalGameVar.dictAvanzamentoStoria["tutorialOggettiBattaglia"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoSognoLucy2"]:
        GlobalGameVar.volumeMusicaDimezzato = True
    elif GlobalGameVar.dictAvanzamentoStoria["dialogoSognoLucy3"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoCasaHansLucy1"]:
        GlobalGameVar.volumeMusicaDimezzato = True
    elif GlobalGameVar.dictAvanzamentoStoria["ingressoForestaCadetta"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tutorialCampoVisivo"]:
        GlobalGameVar.volumeMusicaDimezzato = True
    elif GlobalGameVar.dictAvanzamentoStoria["quintaStanzaForestaCadetta"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tutorialRecuperoPvDifesa"]:
        GlobalGameVar.volumeMusicaDimezzato = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioBagnoCasaDavid"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoDopoBagnoDavid"]:
        GlobalGameVar.volumeMusicaDimezzato = True
    elif GlobalGameVar.dictAvanzamentoStoria["monologoPreCambioPerCenaDavid"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoPostCambioPerCenaDavid"]:
        GlobalGameVar.volumeMusicaDimezzato = True
    elif GlobalGameVar.dictAvanzamentoStoria["sedutoACenaDavid"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoDopoAlzatoDalLetto"]:
        GlobalGameVar.volumeMusicaDimezzato = True
    elif GlobalGameVar.dictAvanzamentoStoria["spiegazioneEnigmaBibliotecario1"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["spiegazioneEnigmaBibliotecario4"]:
        GlobalGameVar.volumeMusicaDimezzato = True
    elif GlobalGameVar.dictAvanzamentoStoria["risoltoEnigmaBibliotecario"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoConclusivoEnigmaBibliotecario"]:
        GlobalGameVar.volumeMusicaDimezzato = True
    elif GlobalGameVar.dictAvanzamentoStoria["dialogoBibliotecarioControlloRegistri"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tutorialImpoPietraMenuSettaImpo"]:
        GlobalGameVar.volumeMusicaDimezzato = True
    elif GlobalGameVar.dictAvanzamentoStoria["arrivoSelvaArida"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tutorialUsoImpoFrutti"]:
        GlobalGameVar.volumeMusicaDimezzato = True

    if GlobalGameVar.volumeMusicaDimezzato and GlobalHWVar.canaleSoundCanzone.get_busy() and GlobalHWVar.canaleSoundCanzone.get_volume() > 0:
        GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni / 2.0)


def nonPuoiProcedere(avanzamentoStoria, stanzaVecchia, stanzaDestinazione, equipaggiamentoIndossato):
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
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["chiestoDegliAlloggiAlMercante"] and stanzaVecchia == GlobalGameVar.dictStanze["città5"] and stanzaDestinazione == GlobalGameVar.dictStanze["città6"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["rimosseMonetePerEntrareInConfraternita"] and stanzaVecchia == GlobalGameVar.dictStanze["città5"] and stanzaDestinazione == GlobalGameVar.dictStanze["città7"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and stanzaVecchia == GlobalGameVar.dictStanze["città9"] and stanzaDestinazione == GlobalGameVar.dictStanze["stradaPerSelvaArida1"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"] and stanzaVecchia == GlobalGameVar.dictStanze["città10"] and stanzaDestinazione == GlobalGameVar.dictStanze["stradaPerPassoMontano1"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["dialogoServoCasaDavidDopoSuicidio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ricevutoCertificatoDalServo"] and stanzaVecchia == GlobalGameVar.dictStanze["casaDavid2"] and (stanzaDestinazione == GlobalGameVar.dictStanze["casaDavid1"] or stanzaDestinazione == GlobalGameVar.dictStanze["casaDavid3"]):
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["uccisoPrimoAggressore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and stanzaVecchia == GlobalGameVar.dictStanze["città4"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaDavid1"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["monologoDopoArrivoInBiblioteca"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and stanzaVecchia == GlobalGameVar.dictStanze["città7"] and stanzaDestinazione == GlobalGameVar.dictStanze["città5"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and equipaggiamentoIndossato and stanzaVecchia == GlobalGameVar.dictStanze["città7"] and stanzaDestinazione == GlobalGameVar.dictStanze["biblioteca1"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["andatoNelloStudioDelBibliotecario"] and stanzaVecchia == GlobalGameVar.dictStanze["biblioteca2"] and stanzaDestinazione == GlobalGameVar.dictStanze["biblioteca3"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and stanzaVecchia == GlobalGameVar.dictStanze["biblioteca3"] and stanzaDestinazione == GlobalGameVar.dictStanze["biblioteca2"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["incontratoIDueAggressori"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and stanzaVecchia == GlobalGameVar.dictStanze["città3"] and stanzaDestinazione == GlobalGameVar.dictStanze["città4"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["risoltoEnigmaMappaLabirinto"] and stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod1"] and stanzaDestinazione == GlobalGameVar.dictStanze["labirinto3"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"] and stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod1"] and stanzaDestinazione == GlobalGameVar.dictStanze["avampostoDiRod3"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["apertoCancellettoCastelloPerScorciatoia"] and stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello1"] and stanzaDestinazione == GlobalGameVar.dictStanze["scorciatoiaLabirinto1"]:
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
        elif stanza == GlobalGameVar.dictStanze["città4"] and avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["monologoDopoUccisioneAggressori"]:
            nomeStanza = "StanzaC"
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
    if stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["vomitatoInBiblioteca"]:
            nomeStanza = "StanzaA"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["andatoACercareImpo"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaC"
    if stanza == GlobalGameVar.dictStanze["esternoCastello1"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["esternoCastello2"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["apertoCancelloPrincipaleCastello"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"

    return nomeStanza


def modificaStanzePacifiche(avanzamentoStoria):
    if GlobalGameVar.dictAvanzamentoStoria["incontratoIDueAggressori"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["riavviatoMusicaPostDialogoBibliotecario"]:
        GlobalGameVar.vetStanzePacifiche = []
    else:
        GlobalGameVar.vetStanzePacifiche = GlobalGameVar.vetStanzePacificheBackUp[:]
