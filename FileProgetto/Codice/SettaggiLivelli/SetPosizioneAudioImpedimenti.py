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

    if GlobalGameVar.dictStanze["sognoSara1"] <= stanza <= GlobalGameVar.dictStanze["sognoSara4"]:
        if stanza == GlobalGameVar.dictStanze["sognoSara1"]:
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
                if stanzaVecchia == GlobalGameVar.dictStanze["sognoSara2"]:
                    npers = "w"
                    x = GlobalHWVar.gsx // 32 * 15
                    y = GlobalHWVar.gsy // 18 * 15
        if stanza == GlobalGameVar.dictStanze["sognoSara2"]:
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
                if stanzaVecchia == GlobalGameVar.dictStanze["sognoSara1"]:
                    npers = "s"
                    x = GlobalHWVar.gsx // 32 * 7
                    y = GlobalHWVar.gsy // 18 * 2
                if stanzaVecchia == GlobalGameVar.dictStanze["sognoSara3"]:
                    npers = "a"
                    x = GlobalHWVar.gsx // 32 * 29
                    y = GlobalHWVar.gsy // 18 * 3
        if stanza == GlobalGameVar.dictStanze["sognoSara3"]:
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
                if stanzaVecchia == GlobalGameVar.dictStanze["sognoSara2"]:
                    npers = "d"
                    x = GlobalHWVar.gsx // 32 * 2
                    y = GlobalHWVar.gsy // 18 * 11
                if stanzaVecchia == GlobalGameVar.dictStanze["sognoSara4"]:
                    npers = "s"
                    x = GlobalHWVar.gsx // 32 * 14
                    y = GlobalHWVar.gsy // 18 * 2
        if stanza == GlobalGameVar.dictStanze["sognoSara4"]:
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
                if stanzaVecchia == GlobalGameVar.dictStanze["sognoSara3"]:
                    npers = "w"
                    x = GlobalHWVar.gsx // 32 * 15
                    y = GlobalHWVar.gsy // 18 * 15
    elif GlobalGameVar.dictStanze["casaHansSara1"] <= stanza <= GlobalGameVar.dictStanze["casaHansSara4"]:
        if stanza == GlobalGameVar.dictStanze["casaHansSara1"]:
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
                if stanzaVecchia == GlobalGameVar.dictStanze["sognoSara4"]:
                    npers = "s"
                    x = GlobalHWVar.gsx // 32 * 3
                    y = GlobalHWVar.gsy // 18 * 14
                if stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara2"]:
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
                if stanzaVecchia == GlobalGameVar.dictStanze["casaDavid3"] or stanzaVecchia == GlobalGameVar.dictStanze["internoCastello10"]:
                    npers = "w"
                    x = GlobalHWVar.gsx // 32 * 6
                    y = GlobalHWVar.gsy // 18 * 13
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreMovimentoVestiti)
                    i = 0
                    while i < 30:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
        if stanza == GlobalGameVar.dictStanze["casaHansSara2"]:
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
                if stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara1"]:
                    npers = "s"
                    if x == GlobalHWVar.gsx // 32 * 16:
                        x = GlobalHWVar.gsx // 32 * 16
                        y = GlobalHWVar.gsy // 18 * 4
                    if x == GlobalHWVar.gsx // 32 * 17:
                        x = GlobalHWVar.gsx // 32 * 17
                        y = GlobalHWVar.gsy // 18 * 4
                if stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara3"]:
                    npers = "s"
                    y = GlobalHWVar.gsy // 18 * 2
                if stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara4"]:
                    npers = "w"
                    y = GlobalHWVar.gsy // 18 * 15
        if stanza == GlobalGameVar.dictStanze["casaHansSara3"]:
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
                if stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara2"]:
                    npers = "w"
                    y = GlobalHWVar.gsy // 18 * 15
        if stanza == GlobalGameVar.dictStanze["casaHansSara4"]:
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
                if stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara2"]:
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
    elif GlobalGameVar.dictStanze["forestaCadetta1"] <= stanza <= GlobalGameVar.dictStanze["forestaCadetta9"]:
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
                if stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara4"]:
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
                if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta4"] or stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara4"]:
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
    elif GlobalGameVar.dictStanze["stradaPerCittà1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerCittà3"]:
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
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                sottofondoLuogo = "StradaPerCitta3/Giorno"
                if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                    GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                    audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                    audioAmbiente_Fiume = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Fiume.wav")
                    audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
                    listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Fiume, audioAmbiente_Persone]
                    sottofondoAmbientaleCambiato = True
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                sottofondoLuogo = "StradaPerCitta3/Giorno"
                if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                    GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                    audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                    audioAmbiente_Fiume = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Fiume.wav")
                    listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Fiume]
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
    elif GlobalGameVar.dictStanze["città1"] <= stanza <= GlobalGameVar.dictStanze["città10"]:
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
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                sottofondoLuogo = "Citta/Giorno"
                if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                    GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                    audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                    audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
                    listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
                    sottofondoAmbientaleCambiato = True
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                sottofondoLuogo = "Citta/Giorno"
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
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                sottofondoLuogo = "Citta/Giorno"
                if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                    GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                    audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                    audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
                    listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
                    sottofondoAmbientaleCambiato = True
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                sottofondoLuogo = "Citta/Giorno"
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
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                sottofondoLuogo = "Citta/Giorno"
                if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                    GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                    audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                    audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
                    listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
                    sottofondoAmbientaleCambiato = True
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                sottofondoLuogo = "Citta/Giorno"
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
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                sottofondoLuogo = "Citta/Giorno"
                if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                    GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                    audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                    audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
                    listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
                    sottofondoAmbientaleCambiato = True
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                sottofondoLuogo = "Citta/Giorno"
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
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                sottofondoLuogo = "Citta/Giorno"
                if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                    GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                    audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                    audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
                    listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
                    sottofondoAmbientaleCambiato = True
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                sottofondoLuogo = "Citta/Giorno"
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
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                sottofondoLuogo = "Citta/Giorno"
                if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                    GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                    audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                    audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
                    listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
                    sottofondoAmbientaleCambiato = True
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                sottofondoLuogo = "Citta/Giorno"
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
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                sottofondoLuogo = "Citta/Giorno"
                if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                    GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                    audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                    audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
                    listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
                    sottofondoAmbientaleCambiato = True
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                sottofondoLuogo = "Citta/Giorno"
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
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                sottofondoLuogo = "Citta/Giorno"
                if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                    GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                    audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                    audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
                    listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
                    sottofondoAmbientaleCambiato = True
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                sottofondoLuogo = "Citta/Giorno"
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
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                sottofondoLuogo = "Citta/Giorno"
                if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                    GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                    audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                    audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
                    listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
                    sottofondoAmbientaleCambiato = True
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                sottofondoLuogo = "Citta/Giorno"
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
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                sottofondoLuogo = "Citta/Giorno"
                if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                    GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                    audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                    audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
                    listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
                    sottofondoAmbientaleCambiato = True
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                sottofondoLuogo = "Citta/Giorno"
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
                if stanzaVecchia == GlobalGameVar.dictStanze["città6"]:
                    npers = "a"
                    x = GlobalHWVar.gpx * 29
                    y += GlobalHWVar.gpy * 1
                if stanzaVecchia == GlobalGameVar.dictStanze["stradaPerPassoMontano1"]:
                    npers = "d"
                    x = GlobalHWVar.gpx * 2
    elif GlobalGameVar.dictStanze["casaDavid1"] <= stanza <= GlobalGameVar.dictStanze["casaDavid3"]:
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
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreMovimentoVestiti)
                    i = 0
                    while i < 15:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
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
                        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreMovimentoVestiti)
                        i = 0
                        while i < 15:
                            pygame.time.wait(100)
                            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                            i += 1
                        npers = "d"
                        x = GlobalHWVar.gsx // 32 * 8
                        y = GlobalHWVar.gsy // 18 * 5
                    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["alzatoDalLettoSecondoGiorno"]:
                        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreMovimentoVestiti)
                        i = 0
                        while i < 15:
                            pygame.time.wait(100)
                            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                            i += 1
                        npers = "a"
                        x = GlobalHWVar.gsx // 32 * 10
                        y = GlobalHWVar.gsy // 18 * 4
                if stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara1"]:
                    npers = "d"
                    x = GlobalHWVar.gpy * 10
                    y = GlobalHWVar.gpy * 4
                    i = 0
                    while i < 10:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
    elif GlobalGameVar.dictStanze["biblioteca1"] <= stanza <= GlobalGameVar.dictStanze["biblioteca3"]:
        if stanza == GlobalGameVar.dictStanze["biblioteca1"]:
            nomeCanzoneLuogo = "07-Biblioteca"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
                canzoneCambiata = True
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                sottofondoLuogo = "Biblioteca"
                if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                    GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                    audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                    audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
                    listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
                    sottofondoAmbientaleCambiato = True
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                sottofondoLuogo = "Biblioteca"
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
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                sottofondoLuogo = "Biblioteca"
                if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                    GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                    audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                    audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
                    listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
                    sottofondoAmbientaleCambiato = True
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                sottofondoLuogo = "Biblioteca"
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
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                sottofondoLuogo = "Biblioteca"
                if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                    GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                    audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                    audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
                    listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
                    sottofondoAmbientaleCambiato = True
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                sottofondoLuogo = "Biblioteca"
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
                if stanzaVecchia == GlobalGameVar.dictStanze["biblioteca2"]:
                    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["andatoNelloStudioDelBibliotecario"]:
                        i = 0
                        while i < 10:
                            pygame.time.wait(100)
                            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                            i += 1
                        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumorePortoniCambioStanza)
                        i = 0
                        while i < 10:
                            pygame.time.wait(100)
                            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                            i += 1
                    npers = "a"
                    x = GlobalHWVar.gsx // 32 * 20
                    y = GlobalHWVar.gsy // 18 * 9
                elif stanzaVecchia == GlobalGameVar.dictStanze["biblioteca3"]:
                    mantieniPosizioneImpo = True
                    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"]:
                        i = 0
                        while i < 2:
                            pygame.time.wait(100)
                            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                            i += 1
                        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoRaccoltaOggetto)
                        i = 0
                        while i < 3:
                            pygame.time.wait(100)
                            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                            i += 1
    elif GlobalGameVar.dictStanze["stradaPerSelvaArida1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerSelvaArida2"]:
        if stanza == GlobalGameVar.dictStanze["stradaPerSelvaArida1"]:
            nomeCanzoneLuogo = "03-EsterniPacifici"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
                canzoneCambiata = True
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                sottofondoLuogo = "StradaPerSelvaArida1"
                if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                    GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                    audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                    audioAmbiente_Persone = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Persone.wav")
                    listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Persone]
                    sottofondoAmbientaleCambiato = True
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                sottofondoLuogo = "StradaPerSelvaArida1"
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
    elif GlobalGameVar.dictStanze["selvaArida1"] <= stanza <= GlobalGameVar.dictStanze["selvaArida16"]:
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
    elif GlobalGameVar.dictStanze["avampostoDiRod1"] <= stanza <= GlobalGameVar.dictStanze["avampostoDiRod3"]:
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
                    x = GlobalHWVar.gpx * 4
                    y = GlobalHWVar.gpy * 6
        if stanza == GlobalGameVar.dictStanze["avampostoDiRod2"]:
            nomeCanzoneLuogo = "03-EsterniPacifici"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
                canzoneCambiata = True
            sottofondoLuogo = "AvampostoDiRod"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Vento2 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento2.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Vento2]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = False
            rumoreChiusuraPorte = False
            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["scorciatoiaLabirinto2"]:
                    npers = "w"
                    x -= GlobalHWVar.gpx * 17
                    y = GlobalHWVar.gpy * 15
                if stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod3"]:
                    npers = "a"
                    x = GlobalHWVar.gpx * 27
                    y = GlobalHWVar.gpy * 10
                if stanzaVecchia == GlobalGameVar.dictStanze["tunnelDiRod3"]:
                    npers = "s"
                    x -= GlobalHWVar.gpx * 6
                    y = GlobalHWVar.gpy * 4
        if stanza == GlobalGameVar.dictStanze["avampostoDiRod3"]:
            nomeCanzoneLuogo = "03-EsterniPacifici"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
                canzoneCambiata = True
            sottofondoLuogo = "AvampostoDiRod"
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
                    npers = "a"
                    x = GlobalHWVar.gpx * 25
                    y = GlobalHWVar.gpy * 6
                if stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod2"]:
                    npers = "d"
                    x = GlobalHWVar.gpx * 6
                    y = GlobalHWVar.gpy * 11
    elif GlobalGameVar.dictStanze["labirinto1"] <= stanza <= GlobalGameVar.dictStanze["labirinto23"]:
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
    elif GlobalGameVar.dictStanze["esternoCastello1"] <= stanza <= GlobalGameVar.dictStanze["esternoCastello5"]:
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
        if stanza == GlobalGameVar.dictStanze["esternoCastello4"]:
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
                    npers = "s"
                    x = GlobalHWVar.gpx * 16
                    y = GlobalHWVar.gpy * 2
                if stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello5"]:
                    npers = "w"
                    y = GlobalHWVar.gpy * 15
        if stanza == GlobalGameVar.dictStanze["esternoCastello5"]:
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
                if stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello4"]:
                    npers = "s"
                    y = GlobalHWVar.gpy * 2
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello1"]:
                    npers = "w"
                    x = GlobalHWVar.gpx * 9
                    y = GlobalHWVar.gpy * 14
    elif GlobalGameVar.dictStanze["internoCastello1"] <= stanza <= GlobalGameVar.dictStanze["internoCastello22"]:
        if stanza == GlobalGameVar.dictStanze["internoCastello1"]:
            nomeCanzoneLuogo = ""
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = False
                canzoneCambiata = True
            sottofondoLuogo = "InternoCastello"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCastello
            rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCastello
            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello5"]:
                    npers = "s"
                    x = GlobalHWVar.gpx * 10
                    y = GlobalHWVar.gpy * 2
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello2"]:
                    npers = "w"
                    y = GlobalHWVar.gpy * 15
        if stanza == GlobalGameVar.dictStanze["internoCastello2"]:
            nomeCanzoneLuogo = ""
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = False
                canzoneCambiata = True
            sottofondoLuogo = "InternoCastello"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCastello
            rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCastello
            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello1"]:
                    npers = "s"
                    y = GlobalHWVar.gpy * 2
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello3"]:
                    npers = "d"
                    x = GlobalHWVar.gpx * 2
                    y += GlobalHWVar.gpy * 10
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello7"]:
                    npers = "w"
                    x += GlobalHWVar.gpx * 18
                    y = GlobalHWVar.gpy * 15
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello19"]:
                    npers = "w"
                    x += GlobalHWVar.gpx * 3
                    y = GlobalHWVar.gpy * 14
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumorePianoAscensoreCastello)
                    i = 0
                    while i < 60:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
        if stanza == GlobalGameVar.dictStanze["internoCastello3"]:
            nomeCanzoneLuogo = ""
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = False
                canzoneCambiata = True
            sottofondoLuogo = "InternoCastello"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCastello
            rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCastello
            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello2"]:
                    npers = "a"
                    x = GlobalHWVar.gpx * 29
                    y -= GlobalHWVar.gpy * 10
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello4"]:
                    npers = "w"
                    x += GlobalHWVar.gpx * 18
                    y = GlobalHWVar.gpy * 15
        if stanza == GlobalGameVar.dictStanze["internoCastello4"]:
            nomeCanzoneLuogo = ""
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = False
                canzoneCambiata = True
            sottofondoLuogo = "InternoCastello"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCastello
            rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCastello
            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello3"]:
                    npers = "s"
                    x -= GlobalHWVar.gpx * 18
                    y = GlobalHWVar.gpy * 2
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello5"]:
                    npers = "w"
                    x += GlobalHWVar.gpx * 14
                    y = GlobalHWVar.gpy * 15
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello7"]:
                    npers = "a"
                    x = GlobalHWVar.gpx * 29
                    y -= GlobalHWVar.gpy * 10
        if stanza == GlobalGameVar.dictStanze["internoCastello5"]:
            nomeCanzoneLuogo = ""
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = False
                canzoneCambiata = True
            sottofondoLuogo = "InternoCastello"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCastello
            rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCastello
            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello4"]:
                    npers = "s"
                    x -= GlobalHWVar.gpx * 14
                    y = GlobalHWVar.gpy * 2
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello6"]:
                    npers = "a"
                    x = GlobalHWVar.gpx * 29
                    y -= GlobalHWVar.gpy * 10
        if stanza == GlobalGameVar.dictStanze["internoCastello6"]:
            nomeCanzoneLuogo = ""
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = False
                canzoneCambiata = True
            sottofondoLuogo = "InternoCastello"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCastello
            rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCastello
            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello5"]:
                    npers = "d"
                    x = GlobalHWVar.gpx * 2
                    y += GlobalHWVar.gpy * 10
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello7"]:
                    npers = "s"
                    x -= GlobalHWVar.gpx * 14
                    y = GlobalHWVar.gpy * 2
        if stanza == GlobalGameVar.dictStanze["internoCastello7"]:
            nomeCanzoneLuogo = ""
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = False
                canzoneCambiata = True
            sottofondoLuogo = "InternoCastello"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCastello
            rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCastello
            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello2"]:
                    npers = "s"
                    x -= GlobalHWVar.gpx * 18
                    y = GlobalHWVar.gpy * 2
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello4"]:
                    npers = "d"
                    x = GlobalHWVar.gpx * 2
                    y += GlobalHWVar.gpy * 10
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello6"]:
                    npers = "w"
                    x += GlobalHWVar.gpx * 14
                    y = GlobalHWVar.gpy * 15
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello8"]:
                    npers = "a"
                    x = GlobalHWVar.gpx * 29
                    y -= GlobalHWVar.gpy * 6
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello7"] and avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioCenaAlCastello"]:
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreMovimentoVestiti)
                    i = 0
                    while i < 10:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                    mantieniPosizioneImpo = True
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello7"] and avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["fineCenaAlCastello"]:
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreMovimentoVestiti)
                    i = 0
                    while i < 10:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                    npers = "d"
                    x = GlobalHWVar.gpx * 23
                    y = GlobalHWVar.gpy * 7
        if stanza == GlobalGameVar.dictStanze["internoCastello8"]:
            nomeCanzoneLuogo = ""
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = False
                canzoneCambiata = True
            sottofondoLuogo = "InternoCastello"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCastello
            rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCastello
            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello7"]:
                    npers = "d"
                    x = GlobalHWVar.gpx * 2
                    y += GlobalHWVar.gpy * 6
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello9"]:
                    npers = "d"
                    x = GlobalHWVar.gpx * 17
                    y += GlobalHWVar.gpy * 7
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello22"]:
                    npers = "a"
                    x = GlobalHWVar.gpx * 21
                    y = GlobalHWVar.gpy * 4
        if stanza == GlobalGameVar.dictStanze["internoCastello9"]:
            nomeCanzoneLuogo = ""
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = False
                canzoneCambiata = True
            sottofondoLuogo = "InternoCastello"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCastello
            rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCastello
            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello8"]:
                    npers = "a"
                    x = GlobalHWVar.gpx * 29
                    y -= GlobalHWVar.gpy * 7
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello10"]:
                    npers = "d"
                    x = GlobalHWVar.gpx * 2
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello11"]:
                    npers = "w"
                    x -= GlobalHWVar.gpx * 7
                    y = GlobalHWVar.gpy * 15
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello12"]:
                    npers = "a"
                    x = GlobalHWVar.gpx * 6
                    y += GlobalHWVar.gpy * 6
        if stanza == GlobalGameVar.dictStanze["internoCastello10"]:
            nomeCanzoneLuogo = ""
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = False
                canzoneCambiata = True
            sottofondoLuogo = "InternoCastello"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCastello
            rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCastello
            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello9"]:
                    npers = "a"
                    x = GlobalHWVar.gpx * 29
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello11"]:
                    npers = "w"
                    x += GlobalHWVar.gpx * 26
                    y = GlobalHWVar.gpy * 15
                if stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"]:
                    npers = "d"
                    x = GlobalHWVar.gpx * 5
                    y = GlobalHWVar.gpy * 4
                    i = 0
                    while i < 20:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                elif stanzaVecchia == GlobalGameVar.dictStanze["internoCastello10"] and avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["alzatoDalLettoNelCastello"]:
                    npers = "d"
                    x = GlobalHWVar.gpx * 5
                    y = GlobalHWVar.gpy * 4
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreMovimentoVestiti)
                    i = 0
                    while i < 15:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                elif stanzaVecchia == GlobalGameVar.dictStanze["internoCastello10"]:
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreMovimentoVestiti)
                    i = 0
                    while i < 15:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
        if stanza == GlobalGameVar.dictStanze["internoCastello11"]:
            nomeCanzoneLuogo = ""
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = False
                canzoneCambiata = True
            sottofondoLuogo = "InternoCastello"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCastello
            rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCastello
            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello9"]:
                    npers = "s"
                    x += GlobalHWVar.gpx * 7
                    y = GlobalHWVar.gpy * 2
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello10"]:
                    npers = "s"
                    x -= GlobalHWVar.gpx * 26
                    y = GlobalHWVar.gpy * 2
        if stanza == GlobalGameVar.dictStanze["internoCastello12"]:
            nomeCanzoneLuogo = ""
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = False
                canzoneCambiata = True
            sottofondoLuogo = "InternoCastello"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCastello
            rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCastello
            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello9"]:
                    npers = "d"
                    x = GlobalHWVar.gpx * 21
                    y -= GlobalHWVar.gpy * 6
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello13"]:
                    npers = "a"
                    x = GlobalHWVar.gpx * 5
                    y -= GlobalHWVar.gpy * 2
        if stanza == GlobalGameVar.dictStanze["internoCastello13"]:
            nomeCanzoneLuogo = ""
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = False
                canzoneCambiata = True
            sottofondoLuogo = "InternoCastello"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCastello
            rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCastello
            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello12"]:
                    npers = "d"
                    x = GlobalHWVar.gpx * 22
                    y += GlobalHWVar.gpy * 2
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello14"]:
                    npers = "s"
                    x -= GlobalHWVar.gpx * 13
                    y = GlobalHWVar.gpy * 2
        if stanza == GlobalGameVar.dictStanze["internoCastello14"]:
            nomeCanzoneLuogo = ""
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = False
                canzoneCambiata = True
            sottofondoLuogo = "InternoCastello"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCastello
            rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCastello
            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello13"]:
                    npers = "w"
                    x += GlobalHWVar.gpx * 13
                    y = GlobalHWVar.gpy * 15
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello15"]:
                    npers = "w"
                    x -= GlobalHWVar.gpx * 19
                    y = GlobalHWVar.gpy * 5
        if stanza == GlobalGameVar.dictStanze["internoCastello15"]:
            nomeCanzoneLuogo = ""
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = False
                canzoneCambiata = True
            sottofondoLuogo = "InternoCastello"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCastello
            rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCastello
            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello14"]:
                    npers = "s"
                    x += GlobalHWVar.gpx * 19
                    y = GlobalHWVar.gpy * 6
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello16"]:
                    npers = "d"
                    x = GlobalHWVar.gpx * 2
                    y += GlobalHWVar.gpy * 7
        if stanza == GlobalGameVar.dictStanze["internoCastello16"]:
            nomeCanzoneLuogo = ""
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = False
                canzoneCambiata = True
            sottofondoLuogo = "InternoCastello"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCastello
            rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCastello
            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello15"]:
                    npers = "a"
                    x = GlobalHWVar.gpx * 29
                    y -= GlobalHWVar.gpy * 7
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello17"]:
                    npers = "w"
                    x += GlobalHWVar.gpx * 18
                    y = GlobalHWVar.gpy * 15
        if stanza == GlobalGameVar.dictStanze["internoCastello17"]:
            nomeCanzoneLuogo = ""
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = False
                canzoneCambiata = True
            sottofondoLuogo = "InternoCastello"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCastello
            rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCastello
            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello16"]:
                    npers = "s"
                    x -= GlobalHWVar.gpx * 18
                    y = GlobalHWVar.gpy * 2
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello18"]:
                    npers = "d"
                    x = GlobalHWVar.gpx * 26
                    y += GlobalHWVar.gpy * 2
        if stanza == GlobalGameVar.dictStanze["internoCastello18"]:
            nomeCanzoneLuogo = ""
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = False
                canzoneCambiata = True
            sottofondoLuogo = "InternoCastello"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCastello
            rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCastello
            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello17"]:
                    npers = "a"
                    x = GlobalHWVar.gpx * 25
                    y -= GlobalHWVar.gpy * 2
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello18"]:
                    npers = "a"
                    x = GlobalHWVar.gpx * 19
                    y = GlobalHWVar.gpy * 12
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonochiusuraporteCastello)
                    i = 0
                    while i < 5:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello19"]:
                    npers = "w"
                    x -= GlobalHWVar.gpx * 14
                    y = GlobalHWVar.gpy * 15
        if stanza == GlobalGameVar.dictStanze["internoCastello19"]:
            nomeCanzoneLuogo = ""
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = False
                canzoneCambiata = True
            sottofondoLuogo = "InternoCastello"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCastello
            rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCastello
            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello18"]:
                    npers = "s"
                    x += GlobalHWVar.gpx * 14
                    y = GlobalHWVar.gpy * 2
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello20"]:
                    npers = "a"
                    x = GlobalHWVar.gpx * 29
                    y = GlobalHWVar.gpy * 13
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello21"]:
                    npers = "w"
                    x = GlobalHWVar.gpx * 15
                    y = GlobalHWVar.gpy * 15
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello2"]:
                    npers = "s"
                    x -= GlobalHWVar.gpx * 3
                    y = GlobalHWVar.gpy * 4
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumorePianoAscensoreCastello)
                    i = 0
                    while i < 60:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
        if stanza == GlobalGameVar.dictStanze["internoCastello20"]:
            nomeCanzoneLuogo = ""
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = False
                canzoneCambiata = True
            sottofondoLuogo = "InternoCastello"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = GlobalSndVar.suonoaperturaporteCastello
            rumoreChiusuraPorte = GlobalSndVar.suonochiusuraporteCastello
            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello19"]:
                    npers = "d"
                    x = GlobalHWVar.gpx * 2
                    y = GlobalHWVar.gpy * 4
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello20"]:
                    mantieniPosizioneImpo = True
                    npers = "w"
                    x = GlobalHWVar.gpx * 12
                    y = GlobalHWVar.gpy * 10
                    i = 0
                    while i < 2:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoRaccoltaOggetto)
                    i = 0
                    while i < 3:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
    elif GlobalGameVar.dictStanze["scorciatoiaLabirinto1"] <= stanza <= GlobalGameVar.dictStanze["scorciatoiaLabirinto2"]:
        if stanza == GlobalGameVar.dictStanze["scorciatoiaLabirinto1"]:
            nomeCanzoneLuogo = "03-EsterniPacifici"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
                canzoneCambiata = True
            sottofondoLuogo = "ScorciatoiaLabirinto/Stanza1"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Vento2 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento2.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Vento2]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = False
            rumoreChiusuraPorte = False
            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello1"]:
                    npers = "a"
                    x = GlobalHWVar.gpx * 29
                    y = GlobalHWVar.gpy * 12
                if stanzaVecchia == GlobalGameVar.dictStanze["scorciatoiaLabirinto2"]:
                    npers = "s"
                    x -= GlobalHWVar.gpx * 19
                    y = GlobalHWVar.gpy * 2
        if stanza == GlobalGameVar.dictStanze["scorciatoiaLabirinto2"]:
            nomeCanzoneLuogo = "03-EsterniPacifici"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
                canzoneCambiata = True
            sottofondoLuogo = "ScorciatoiaLabirinto/Stanza2"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Vento2 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento2.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Vento2]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = False
            rumoreChiusuraPorte = False
            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["scorciatoiaLabirinto1"]:
                    npers = "w"
                    x += GlobalHWVar.gpx * 19
                    y = GlobalHWVar.gpy * 15
                if stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod2"]:
                    npers = "s"
                    x += GlobalHWVar.gpx * 17
                    y = GlobalHWVar.gpy * 2
    elif GlobalGameVar.dictStanze["stradaPerPassoMontano1"] <= stanza <= GlobalGameVar.dictStanze["stradaPerPassoMontano2"]:
        if stanza == GlobalGameVar.dictStanze["stradaPerPassoMontano1"]:
            nomeCanzoneLuogo = "03-EsterniPacifici"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
                canzoneCambiata = True
            sottofondoLuogo = "StradaPerPassoMontano/Stanza1"
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
                if stanzaVecchia == GlobalGameVar.dictStanze["città10"]:
                    npers = "a"
                    x = GlobalHWVar.gpx * 27
                    if y == GlobalHWVar.gpy * 11:
                        y = GlobalHWVar.gpy * 10
                if stanzaVecchia == GlobalGameVar.dictStanze["stradaPerPassoMontano2"]:
                    npers = "d"
                    x = GlobalHWVar.gpx * 2
                    y += GlobalHWVar.gpy * 5
        if stanza == GlobalGameVar.dictStanze["stradaPerPassoMontano2"]:
            nomeCanzoneLuogo = "03-EsterniPacifici"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
                canzoneCambiata = True
            sottofondoLuogo = "StradaPerPassoMontano/Stanza2"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Vento2 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento2.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Vento2]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = False
            rumoreChiusuraPorte = False

            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["stradaPerPassoMontano1"]:
                    npers = "a"
                    x = GlobalHWVar.gpx * 29
                    y -= GlobalHWVar.gpy * 5
                if stanzaVecchia == GlobalGameVar.dictStanze["passoMontano1"]:
                    npers = "d"
                    x = GlobalHWVar.gpx * 2
                    y += GlobalHWVar.gpy * 1
    elif GlobalGameVar.dictStanze["passoMontano1"] <= stanza <= GlobalGameVar.dictStanze["passoMontano10"]:
        if stanza == GlobalGameVar.dictStanze["passoMontano1"]:
            nomeCanzoneLuogo = "10-PassoMontano"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
                canzoneCambiata = True
            sottofondoLuogo = "PassoMontano"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Vento2 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento2.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Vento2]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = False
            rumoreChiusuraPorte = False

            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["stradaPerPassoMontano2"]:
                    npers = "a"
                    x = GlobalHWVar.gpx * 29
                    y -= GlobalHWVar.gpy * 1
                if stanzaVecchia == GlobalGameVar.dictStanze["passoMontano2"]:
                    npers = "s"
                    x -= GlobalHWVar.gpx * 3
                    y = GlobalHWVar.gpy * 2
                if stanzaVecchia == GlobalGameVar.dictStanze["passoMontano6"]:
                    npers = "d"
                    x = GlobalHWVar.gpx * 2
                    y += GlobalHWVar.gpy * 8
        if stanza == GlobalGameVar.dictStanze["passoMontano2"]:
            nomeCanzoneLuogo = "10-PassoMontano"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
                canzoneCambiata = True
            sottofondoLuogo = "PassoMontano"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Vento2 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento2.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Vento2]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = False
            rumoreChiusuraPorte = False

            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["passoMontano1"]:
                    npers = "w"
                    x += GlobalHWVar.gpx * 3
                    y = GlobalHWVar.gpy * 15
                if stanzaVecchia == GlobalGameVar.dictStanze["passoMontano3"]:
                    if x == GlobalHWVar.gpx * 12:
                        npers = "s"
                        x -= GlobalHWVar.gpx * 8
                        y = GlobalHWVar.gpy * 2
                    else:
                        npers = "s"
                        x -= GlobalHWVar.gpx * 6
                        y = GlobalHWVar.gpy * 2
        if stanza == GlobalGameVar.dictStanze["passoMontano3"]:
            nomeCanzoneLuogo = "10-PassoMontano"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
                canzoneCambiata = True
            sottofondoLuogo = "PassoMontano"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Vento2 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento2.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Vento2]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = False
            rumoreChiusuraPorte = False

            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["passoMontano2"]:
                    if x == GlobalHWVar.gpx * 4:
                        npers = "w"
                        x += GlobalHWVar.gpx * 8
                        y = GlobalHWVar.gpy * 15
                    else:
                        npers = "w"
                        x += GlobalHWVar.gpx * 6
                        y = GlobalHWVar.gpy * 15
                if stanzaVecchia == GlobalGameVar.dictStanze["passoMontano4"]:
                    npers = "d"
                    x = GlobalHWVar.gpx * 2
                    y += GlobalHWVar.gpy * 8
        if stanza == GlobalGameVar.dictStanze["passoMontano4"]:
            nomeCanzoneLuogo = "10-PassoMontano"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
                canzoneCambiata = True
            sottofondoLuogo = "PassoMontano"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Vento2 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento2.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Vento2]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = False
            rumoreChiusuraPorte = False

            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["passoMontano3"]:
                    npers = "a"
                    x = GlobalHWVar.gpx * 29
                    y -= GlobalHWVar.gpy * 8
                if stanzaVecchia == GlobalGameVar.dictStanze["passoMontano5"]:
                    npers = "w"
                    x -= GlobalHWVar.gpx * 4
                    y = GlobalHWVar.gpy * 15
        if stanza == GlobalGameVar.dictStanze["passoMontano5"]:
            nomeCanzoneLuogo = "10-PassoMontano"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
                canzoneCambiata = True
            sottofondoLuogo = "PassoMontano"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Vento2 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento2.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Vento2]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = False
            rumoreChiusuraPorte = False

            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["passoMontano4"]:
                    npers = "s"
                    x += GlobalHWVar.gpx * 4
                    y = GlobalHWVar.gpy * 2
                if stanzaVecchia == GlobalGameVar.dictStanze["passoMontano6"]:
                    npers = "w"
                    x += GlobalHWVar.gpx * 16
                    y = GlobalHWVar.gpy * 15
                if stanzaVecchia == GlobalGameVar.dictStanze["passoMontano9"]:
                    npers = "d"
                    x = GlobalHWVar.gpx * 2
                    y = GlobalHWVar.gpy * 2
        if stanza == GlobalGameVar.dictStanze["passoMontano6"]:
            nomeCanzoneLuogo = "10-PassoMontano"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
                canzoneCambiata = True
            sottofondoLuogo = "PassoMontano"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Vento2 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento2.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Vento2]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = False
            rumoreChiusuraPorte = False

            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["passoMontano5"]:
                    npers = "s"
                    x -= GlobalHWVar.gpx * 16
                    y = GlobalHWVar.gpy * 2
                if stanzaVecchia == GlobalGameVar.dictStanze["passoMontano7"]:
                    npers = "d"
                    x = GlobalHWVar.gpx * 2
                    y += GlobalHWVar.gpy * 6
                if stanzaVecchia == GlobalGameVar.dictStanze["passoMontano1"]:
                    npers = "a"
                    x = GlobalHWVar.gpx * 29
                    y -= GlobalHWVar.gpy * 8
        if stanza == GlobalGameVar.dictStanze["passoMontano7"]:
            nomeCanzoneLuogo = "10-PassoMontano"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
                canzoneCambiata = True
            sottofondoLuogo = "PassoMontano"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Vento2 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento2.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Vento2]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = False
            rumoreChiusuraPorte = False

            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["passoMontano6"]:
                    npers = "a"
                    x = GlobalHWVar.gpx * 29
                    y -= GlobalHWVar.gpy * 6
                if stanzaVecchia == GlobalGameVar.dictStanze["passoMontano8"]:
                    npers = "s"
                    x -= GlobalHWVar.gpx * 20
                    y = GlobalHWVar.gpy * 2
        if stanza == GlobalGameVar.dictStanze["passoMontano8"]:
            nomeCanzoneLuogo = "10-PassoMontano"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
                canzoneCambiata = True
            sottofondoLuogo = "PassoMontano"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Vento2 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento2.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Vento2]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = False
            rumoreChiusuraPorte = False

            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["passoMontano7"]:
                    npers = "w"
                    x += GlobalHWVar.gpx * 20
                    y = GlobalHWVar.gpy * 15
                if stanzaVecchia == GlobalGameVar.dictStanze["passoMontano9"]:
                    npers = "s"
                    x += GlobalHWVar.gpx * 4
                    y = GlobalHWVar.gpy * 2
        if stanza == GlobalGameVar.dictStanze["passoMontano9"]:
            nomeCanzoneLuogo = "10-PassoMontano"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
                canzoneCambiata = True
            sottofondoLuogo = "PassoMontano"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Vento2 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento2.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Vento2]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = False
            rumoreChiusuraPorte = False

            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["passoMontano8"]:
                    npers = "w"
                    x -= GlobalHWVar.gpx * 4
                    y = GlobalHWVar.gpy * 15
                if stanzaVecchia == GlobalGameVar.dictStanze["passoMontano10"]:
                    npers = "s"
                    x -= GlobalHWVar.gpx * 19
                    y = GlobalHWVar.gpy * 2
                if stanzaVecchia == GlobalGameVar.dictStanze["passoMontano5"]:
                    npers = "a"
                    x = GlobalHWVar.gpx * 29
                    y = GlobalHWVar.gpy * 15
        if stanza == GlobalGameVar.dictStanze["passoMontano10"]:
            nomeCanzoneLuogo = "10-PassoMontano"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
                canzoneCambiata = True
            sottofondoLuogo = "PassoMontano"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Vento2 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento2.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Vento2]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = False
            rumoreChiusuraPorte = False

            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["passoMontano9"]:
                    npers = "w"
                    x += GlobalHWVar.gpx * 19
                    y = GlobalHWVar.gpy * 15
                if stanzaVecchia == GlobalGameVar.dictStanze["palazzoDiRod1"]:
                    npers = "d"
                    x = GlobalHWVar.gpx * 2
                    y -= GlobalHWVar.gpy * 3

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
    if (stanzaVecchia == GlobalGameVar.dictStanze["sognoSara4"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta1"] and stanza == GlobalGameVar.dictStanze["casaHansSara4"]) or (stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"]):
        nomeDaScrivere = "Casa"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara4"] and stanza == GlobalGameVar.dictStanze["forestaCadetta1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà1"] and stanza == GlobalGameVar.dictStanze["forestaCadetta9"]):
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
    elif (stanzaVecchia == GlobalGameVar.dictStanze["selvaArida16"] and stanza == GlobalGameVar.dictStanze["avampostoDiRod1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["labirinto3"] and stanza == GlobalGameVar.dictStanze["avampostoDiRod1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["scorciatoiaLabirinto2"] and stanza == GlobalGameVar.dictStanze["avampostoDiRod2"]) or (stanzaVecchia == GlobalGameVar.dictStanze["tunnelDiRod3"] and stanza == GlobalGameVar.dictStanze["avampostoDiRod2"]):
        nomeDaScrivere = u"Avamposto di Rod"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod1"] and stanza == GlobalGameVar.dictStanze["labirinto3"]) or (stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello1"] and stanza == GlobalGameVar.dictStanze["labirinto20"]):
        nomeDaScrivere = u"Labirinto"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["labirinto20"] and stanza == GlobalGameVar.dictStanze["esternoCastello1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["internoCastello1"] and stanza == GlobalGameVar.dictStanze["esternoCastello5"]) or (stanzaVecchia == GlobalGameVar.dictStanze["scorciatoiaLabirinto1"] and stanza == GlobalGameVar.dictStanze["esternoCastello1"]):
        nomeDaScrivere = u"Castello di Neil - Esterno"
    elif stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello5"] and stanza == GlobalGameVar.dictStanze["internoCastello1"]:
        nomeDaScrivere = u"Castello di Neil - Interno"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello1"] and stanza == GlobalGameVar.dictStanze["scorciatoiaLabirinto1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod2"] and stanza == GlobalGameVar.dictStanze["scorciatoiaLabirinto2"]):
        nomeDaScrivere = u"Scorciatoia sulle montagne"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["città10"] and stanza == GlobalGameVar.dictStanze["stradaPerPassoMontano1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["passoMontano1"] and stanza == GlobalGameVar.dictStanze["stradaPerPassoMontano2"]):
        nomeDaScrivere = u"Strada per Passo Montano"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["stradaPerPassoMontano2"] and stanza == GlobalGameVar.dictStanze["passoMontano1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["palazzoDiRod1"] and stanza == GlobalGameVar.dictStanze["passoMontano10"]):
        nomeDaScrivere = u"Passo Montano"

    if nomeDaScrivere:
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
        FunzioniGraficheGeneriche.messaggio(nomeDaScrivere, GlobalHWVar.grigiochi, GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 8, 150, centrale=True)
        GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 4), int(GlobalHWVar.gpy * 10.6)), (int(GlobalHWVar.gpx * 28) - 1, int(GlobalHWVar.gpy * 10.6)), 2)
        FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=2)
        GlobalHWVar.aggiornaSchermo()


def decidiSeStoppareMusica(stanza, avanzamentoStoria):
    stoppaMusica = False
    if stanza == GlobalGameVar.dictStanze["casaHansSara1"] and avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"]:
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
    elif GlobalGameVar.dictStanze["casaHansSara1"] <= stanza <= GlobalGameVar.dictStanze["forestaCadetta5"] and (GlobalGameVar.dictAvanzamentoStoria["inizioSognoCasaDavid"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCasaDavid"] or GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"]):
        stoppaMusica = True
    elif GlobalGameVar.dictAvanzamentoStoria["monologoNotatoScorciatoiaLabirinto"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoNotatoAssenzaRodFuoriDallAvamposto"]:
        stoppaMusica = True

    return stoppaMusica


def decidiSeDimezzareVolumeMusica(avanzamentoStoria):
    GlobalGameVar.volumeMusicaDimezzato = False
    if GlobalGameVar.dictAvanzamentoStoria["inizio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tutorialMovimento"]:
        GlobalGameVar.volumeMusicaDimezzato = True
    elif GlobalGameVar.dictAvanzamentoStoria["tutorialOggettiBattaglia"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoSognoSara2"]:
        GlobalGameVar.volumeMusicaDimezzato = True
    elif GlobalGameVar.dictAvanzamentoStoria["dialogoSognoSara3"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoCasaHansSara1"]:
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
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tutorialUtilizzoOggetti"] and stanzaVecchia == GlobalGameVar.dictStanze["sognoSara1"] and stanzaDestinazione == GlobalGameVar.dictStanze["sognoSara2"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoCasaHansSara2"] and stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara1"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaHansSara2"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontroFiglioUfficiale"] and stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"] and stanzaDestinazione == GlobalGameVar.dictStanze["forestaCadetta6"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"] and stanzaDestinazione == GlobalGameVar.dictStanze["forestaCadetta7"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["armaturaNonnoCompletata"] and stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara1"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaHansSara2"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["accampamentoForestaAnalizzato2"] and stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"] and (stanzaDestinazione == GlobalGameVar.dictStanze["forestaCadetta6"] or stanzaDestinazione == GlobalGameVar.dictStanze["forestaCadetta7"]):
        nonProcedere = True
    elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara4"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaHansSara2"]:
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
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"] and stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello1"] and stanzaDestinazione == GlobalGameVar.dictStanze["scorciatoiaLabirinto1"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello1"] and stanzaDestinazione == GlobalGameVar.dictStanze["esternoCastello5"]:
        nonProcedere = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSalaDaPranzoCastello"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello7"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dormitoNelCastello"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello9"] and (stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello8"] or stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello12"]):
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["dormitoNelCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["primoDialogoNeil"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello9"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello8"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["apertoPortaStanza19CastelloVerso20"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello19"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello20"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ripresoImpoDaNeil"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello20"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello19"]:
        nonProcedere = True
    elif (avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"] or GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]) and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello19"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello2"]:
        nonProcedere = True
    elif (avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"] or GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]) and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello2"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello19"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoNotatoAssenzaRodFuoriDallAvamposto"] and stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello1"] and stanzaDestinazione == GlobalGameVar.dictStanze["labirinto20"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["apertoPortaStanza19CastelloVerso21"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello19"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello21"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"] and ((stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara2"] and (stanzaDestinazione == GlobalGameVar.dictStanze["casaHansSara1"] or stanzaDestinazione == GlobalGameVar.dictStanze["casaHansSara3"])) or (stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara4"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaHansSara2"]) or (stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"] and stanzaDestinazione == GlobalGameVar.dictStanze["forestaCadetta4"]) or (stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"] and stanzaDestinazione == GlobalGameVar.dictStanze["forestaCadetta6"]) or (stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"] and stanzaDestinazione == GlobalGameVar.dictStanze["forestaCadetta7"])):
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoHansFuoriCasaSognoCastello"] and stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara4"] and stanzaDestinazione == GlobalGameVar.dictStanze["forestaCadetta5"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sbloccatoTunnelDiRod"] and stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod2"] and stanzaDestinazione == GlobalGameVar.dictStanze["tunnelDiRod3"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["trovatoChiaveAvampostoDiRod"] and stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod3"] and stanzaDestinazione == GlobalGameVar.dictStanze["avampostoDiRod1"]:
        nonProcedere = True

    return nonProcedere


def possibileAprirePorta(stanza, xPorta, yPorta, avanzamentoStoria):
    procedi = True
    if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"] and xPorta == GlobalHWVar.gpx * 25 and yPorta == GlobalHWVar.gpy * 3:
        procedi = False
    if GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tutorialMappaDiario"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"] and xPorta == GlobalHWVar.gpx * 6 and yPorta == GlobalHWVar.gpy * 9:
        procedi = False
    if GlobalGameVar.dictAvanzamentoStoria["monologoIndicazioniArmaturaNonno"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["trovataChiaveRipostiglio"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"] and xPorta == GlobalHWVar.gpx * 26 and yPorta == GlobalHWVar.gpy * 11:
        procedi = False
    if GlobalGameVar.dictAvanzamentoStoria["arrivoDavidPrimoPiano"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presaChiaveStanzaDaLettoDavid"] and stanza == GlobalGameVar.dictStanze["casaDavid3"] and xPorta == GlobalHWVar.gpx * 12 and yPorta == GlobalHWVar.gpy * 8:
        procedi = False
    if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presoChiaveCameraDaLettoCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello10"] and xPorta == GlobalHWVar.gpx * 8 and yPorta == GlobalHWVar.gpy * 5:
        procedi = False
    if GlobalGameVar.dictAvanzamentoStoria["guardiaCastelloChiusoPortaLibreriaInternoCastello18"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dormitoNelCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello18"] and xPorta == GlobalHWVar.gpx * 17 and yPorta == GlobalHWVar.gpy * 12:
        procedi = False
    if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presoMazzoDi3ChiaviCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello20"] and xPorta == GlobalHWVar.gpx * 17 and yPorta == GlobalHWVar.gpy * 9:
        procedi = False
    if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presoMazzoDi3ChiaviCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello8"] and xPorta == GlobalHWVar.gpx * 7 and yPorta == GlobalHWVar.gpy * 7:
        procedi = False
    if (GlobalGameVar.dictAvanzamentoStoria["inizioSognoCasaDavid"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCasaDavid"] or GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"]) and stanza == GlobalGameVar.dictStanze["casaHansSara1"] and ((xPorta == GlobalHWVar.gpx * 25 and yPorta == GlobalHWVar.gpy * 3) or (xPorta == GlobalHWVar.gpx * 7 and yPorta == GlobalHWVar.gpy * 6)):
        procedi = False

    return procedi


def settaNomeStanza(avanzamentoStoria, stanza):
    nomeStanza = "Stanza"
    if stanza == GlobalGameVar.dictStanze["casaHansSara1"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            nomeStanza = "StanzaA"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSognoCasaDavid"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaC"
    if stanza == GlobalGameVar.dictStanze["casaHansSara2"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] or GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["casaHansSara4"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] or GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"]:
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
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] or GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"]:
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
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoPostCambioPerCenaDavid"]:
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
    if stanza == GlobalGameVar.dictStanze["internoCastello2"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"] or GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["internoCastello4"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["internoCastello6"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["internoCastello7"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cenaCastelloServita"] or GlobalGameVar.dictAvanzamentoStoria["dormitoNelCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"]:
            nomeStanza = "StanzaA"
        elif GlobalGameVar.dictAvanzamentoStoria["cenaCastelloServita"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dormitoNelCastello"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaC"
    if stanza == GlobalGameVar.dictStanze["internoCastello8"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["apertoPortaStanza8Castello"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["internoCastello9"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["internoCastello10"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dormitoNelCastello"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaA"
    if stanza == GlobalGameVar.dictStanze["internoCastello11"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["internoCastello15"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["internoCastello19"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["apertoPortaStanza19CastelloVerso20"]:
            nomeStanza = "StanzaA"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"] or GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            nomeStanza = "StanzaB"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["apertoPortaStanza19CastelloVerso21"]:
            nomeStanza = "StanzaC"
        else:
            nomeStanza = "StanzaD"
    if stanza == GlobalGameVar.dictStanze["avampostoDiRod2"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sbloccatoTunnelDiRod"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"

    return nomeStanza


def modificaStanzePacifiche(avanzamentoStoria):
    if GlobalGameVar.dictAvanzamentoStoria["incontratoIDueAggressori"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["riavviatoMusicaPostDialogoBibliotecario"]:
        GlobalGameVar.vetStanzePacifiche = []
    elif GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
        GlobalGameVar.vetStanzePacifiche = []
    else:
        GlobalGameVar.vetStanzePacifiche = GlobalGameVar.vetStanzePacificheBackUp[:]


def riproduciSuoniCambioStanza(stanzaVecchia, stanzaDestinazione):
    riproduciSuono = False
    if (stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara1"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaHansSara2"]) or (stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara2"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaHansSara1"]):
        riproduciSuono = True
    elif (stanzaVecchia == GlobalGameVar.dictStanze["città4"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaDavid1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["casaDavid1"] and stanzaDestinazione == GlobalGameVar.dictStanze["città4"]):
        riproduciSuono = True
    elif (stanzaVecchia == GlobalGameVar.dictStanze["città7"] and stanzaDestinazione == GlobalGameVar.dictStanze["biblioteca1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["biblioteca1"] and stanzaDestinazione == GlobalGameVar.dictStanze["città7"]):
        riproduciSuono = True
    elif (stanzaVecchia == GlobalGameVar.dictStanze["biblioteca2"] and stanzaDestinazione == GlobalGameVar.dictStanze["biblioteca3"]) or (stanzaVecchia == GlobalGameVar.dictStanze["biblioteca3"] and stanzaDestinazione == GlobalGameVar.dictStanze["biblioteca2"]):
        riproduciSuono = True
    elif (stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod1"] and stanzaDestinazione == GlobalGameVar.dictStanze["avampostoDiRod3"]) or (stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod3"] and stanzaDestinazione == GlobalGameVar.dictStanze["avampostoDiRod1"]):
        riproduciSuono = True
    elif (stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello5"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["internoCastello1"] and stanzaDestinazione == GlobalGameVar.dictStanze["esternoCastello5"]):
        riproduciSuono = True
    elif (stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod2"] and stanzaDestinazione == GlobalGameVar.dictStanze["avampostoDiRod3"]) or (stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod3"] and stanzaDestinazione == GlobalGameVar.dictStanze["avampostoDiRod2"]):
        riproduciSuono = True

    if riproduciSuono:
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumorePortoniCambioStanza)


def settaPresenzaDiColco(avanzamentoStoria):
    if GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["impoPresoDaGuardiaCastello"]:
        GlobalGameVar.impoPresente = True
    elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["ripresoImpoDaNeil"]:
        GlobalGameVar.impoPresente = True
    else:
        GlobalGameVar.impoPresente = False


def decidiSePoterAprireMenu(avanzamentoStoria):
    possibileAprireMenu = True
    if GlobalGameVar.dictAvanzamentoStoria["inizioSognoCasaDavid"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCasaDavid"]:
        possibileAprireMenu = False
    elif GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"]:
        possibileAprireMenu = False

    return possibileAprireMenu


def decidiSePoterParare(avanzamentoStoria):
    impossibileParare = False
    if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
        impossibileParare = True
    elif GlobalGameVar.dictAvanzamentoStoria["incontratoIDueAggressori"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoDopoUccisioneAggressori"]:
        impossibileParare = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"]:
        impossibileParare = True

    return impossibileParare
