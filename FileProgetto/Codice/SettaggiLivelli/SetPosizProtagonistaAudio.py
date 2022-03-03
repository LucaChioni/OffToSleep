# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.CaricaFileProgetto as CaricaFileProgetto


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
            nomeCanzoneLuogo = "02-Casa"
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
            nomeCanzoneLuogo = "02-Casa"
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
            nomeCanzoneLuogo = "02-Casa"
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
                    elif stanzaVecchia == GlobalGameVar.dictStanze["biblioteca3"] and avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["alzataDallaSediaInBiblioteca"]:
                        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreMovimentoVestiti)
                        i = 0
                        while i < 5:
                            pygame.time.wait(100)
                            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                            i += 1
                    elif stanzaVecchia == GlobalGameVar.dictStanze["biblioteca3"]:
                        i = 0
                        while i < 2:
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
            nomeCanzoneLuogo = "11-ProprietaDiRod"
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
            nomeCanzoneLuogo = "11-ProprietaDiRod"
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
                    x -= GlobalHWVar.gpx * 12
                    y = GlobalHWVar.gpy * 4
        if stanza == GlobalGameVar.dictStanze["avampostoDiRod3"]:
            nomeCanzoneLuogo = "11-ProprietaDiRod"
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
            nomeCanzoneLuogo = "13-FugaCastelloAccellerata"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
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
                    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoUscitaInternoCastello20Fuggendo"]:
                        y = GlobalHWVar.gpy * 6
                if stanzaVecchia == GlobalGameVar.dictStanze["scorciatoiaLabirinto1"]:
                    npers = "d"
                    x = GlobalHWVar.gpx * 2
                    y = GlobalHWVar.gpy * 9
        if stanza == GlobalGameVar.dictStanze["esternoCastello2"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioMusicaAccelerataFugaCastello"]:
                nomeCanzoneLuogo = "12-FugaCastello"
            else:
                nomeCanzoneLuogo = "13-FugaCastelloAccellerata"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
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
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioMusicaAccelerataFugaCastello"]:
                nomeCanzoneLuogo = "12-FugaCastello"
            else:
                nomeCanzoneLuogo = "13-FugaCastelloAccellerata"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
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
            nomeCanzoneLuogo = "12-FugaCastello"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
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
            nomeCanzoneLuogo = "12-FugaCastello"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
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
    elif GlobalGameVar.dictStanze["internoCastello1"] <= stanza <= GlobalGameVar.dictStanze["internoCastello21"]:
        if stanza == GlobalGameVar.dictStanze["internoCastello1"]:
            nomeCanzoneLuogo = "12-FugaCastello"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
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
            nomeCanzoneLuogo = "12-FugaCastello"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
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
            nomeCanzoneLuogo = "12-FugaCastello"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
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
            nomeCanzoneLuogo = "12-FugaCastello"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
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
            nomeCanzoneLuogo = "12-FugaCastello"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
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
            nomeCanzoneLuogo = "12-FugaCastello"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
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
            nomeCanzoneLuogo = "12-FugaCastello"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
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
            nomeCanzoneLuogo = "12-FugaCastello"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
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
                if stanzaVecchia == GlobalGameVar.dictStanze["tunnelSubacqueo1"]:
                    npers = "a"
                    x = GlobalHWVar.gpx * 21
                    y = GlobalHWVar.gpy * 4
        if stanza == GlobalGameVar.dictStanze["internoCastello9"]:
            nomeCanzoneLuogo = "12-FugaCastello"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
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
            nomeCanzoneLuogo = "12-FugaCastello"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
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
            nomeCanzoneLuogo = "12-FugaCastello"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
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
            nomeCanzoneLuogo = "12-FugaCastello"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
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
            nomeCanzoneLuogo = "12-FugaCastello"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
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
            nomeCanzoneLuogo = "12-FugaCastello"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
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
            nomeCanzoneLuogo = "12-FugaCastello"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
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
            nomeCanzoneLuogo = "12-FugaCastello"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
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
            nomeCanzoneLuogo = "12-FugaCastello"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
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
            nomeCanzoneLuogo = "12-FugaCastello"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
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
            nomeCanzoneLuogo = "12-FugaCastello"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
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
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello20"] and avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
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
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello20"] and avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["rimossoImpoMessoSulTavoloDopoConsegnaStrumenti"]:
                    mantieniPosizioneImpo = True
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
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello20"] and avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["chiusoPortaInternoCastello20DaSoldato"]:
                    mantieniPosizioneImpo = True
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonochiusuraporteCastello)
        if stanza == GlobalGameVar.dictStanze["internoCastello21"]:
            nomeCanzoneLuogo = ""
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = False
                canzoneCambiata = True
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                sottofondoLuogo = "InternoCastello/Macchinario"
                if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                    GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                    audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                    audioAmbiente_Macchinario1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Macchinario1.wav")
                    audioAmbiente_Macchinario2 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Macchinario2.wav")
                    audioAmbiente_Macchinario3 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Macchinario3.wav")
                    listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Macchinario1, audioAmbiente_Macchinario2, audioAmbiente_Macchinario3]
                    sottofondoAmbientaleCambiato = True
            else:
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
                    npers = "s"
                    x = GlobalHWVar.gpx * 19
                    y = GlobalHWVar.gpy * 2
                if stanzaVecchia == GlobalGameVar.dictStanze["internoCastello21"]:
                    npers = "a"
                    x = GlobalHWVar.gpx * 26
                    y = GlobalHWVar.gpy * 10
                    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["alzataDalTavoloLaboratorioCastello"]:
                        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreMovimentoVestiti)
                        i = 0
                        while i < 10:
                            pygame.time.wait(100)
                            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                            i += 1
                        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreRimozioneBende)
                        i = 0
                        while i < 20:
                            pygame.time.wait(100)
                            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                            i += 1
    elif GlobalGameVar.dictStanze["scorciatoiaLabirinto1"] <= stanza <= GlobalGameVar.dictStanze["scorciatoiaLabirinto2"]:
        if stanza == GlobalGameVar.dictStanze["scorciatoiaLabirinto1"]:
            nomeCanzoneLuogo = "09-Labirinto"
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
            nomeCanzoneLuogo = "09-Labirinto"
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
    elif GlobalGameVar.dictStanze["palazzoDiRod1"] <= stanza <= GlobalGameVar.dictStanze["palazzoDiRod5"]:
        if stanza == GlobalGameVar.dictStanze["palazzoDiRod1"]:
            nomeCanzoneLuogo = "11-ProprietaDiRod"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
                canzoneCambiata = True
            sottofondoLuogo = "PalazzoDiRod/Esterno"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Vento2 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento2.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Vento2]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = GlobalSndVar.suonoaperturaportePalazzoDiRod
            rumoreChiusuraPorte = GlobalSndVar.suonochiusuraportePalazzoDiRod
            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["passoMontano10"]:
                    npers = "a"
                    x = GlobalHWVar.gpx * 29
                if stanzaVecchia == GlobalGameVar.dictStanze["palazzoDiRod2"]:
                    npers = "w"
                    y = GlobalHWVar.gpy * 12
                if stanzaVecchia == GlobalGameVar.dictStanze["caverna1"]:
                    npers = "s"
                    x -= GlobalHWVar.gpx * 6
                    y = GlobalHWVar.gpy * 5
        if stanza == GlobalGameVar.dictStanze["palazzoDiRod2"]:
            nomeCanzoneLuogo = "11-ProprietaDiRod"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
                canzoneCambiata = True
            sottofondoLuogo = "PalazzoDiRod/Interno"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Vento2 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento2.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Vento2]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = GlobalSndVar.suonoaperturaportePalazzoDiRod
            rumoreChiusuraPorte = GlobalSndVar.suonochiusuraportePalazzoDiRod
            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["palazzoDiRod1"]:
                    npers = "s"
                    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["entratoInPalazzoDiRod"]:
                        x = GlobalHWVar.gpx * 20
                    y = GlobalHWVar.gpy * 2
                if stanzaVecchia == GlobalGameVar.dictStanze["palazzoDiRod3"]:
                    npers = "w"
                    x = GlobalHWVar.gpx * 5
                    y = GlobalHWVar.gpy * 10
                if stanzaVecchia == GlobalGameVar.dictStanze["palazzoDiRod4"]:
                    npers = "d"
                    x = GlobalHWVar.gpx * 8
                    y = GlobalHWVar.gpy * 4
                if stanzaVecchia == GlobalGameVar.dictStanze["palazzoDiRod5"]:
                    npers = "w"
                    x = GlobalHWVar.gpx * 11
                    y = GlobalHWVar.gpy * 15
                if stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello3"]:
                    npers = "d"
                    x = GlobalHWVar.gpx * 20
                    y = GlobalHWVar.gpy * 5
        if stanza == GlobalGameVar.dictStanze["palazzoDiRod5"]:
            nomeCanzoneLuogo = "11-ProprietaDiRod"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
                canzoneCambiata = True
            sottofondoLuogo = "PalazzoDiRod/Esterno"
            if GlobalGameVar.audioSottofondoAttuale != sottofondoLuogo:
                GlobalGameVar.audioSottofondoAttuale = sottofondoLuogo
                audioAmbiente_Vento1 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento1.wav")
                audioAmbiente_Vento2 = CaricaFileProgetto.loadSound(pathSottofondi + sottofondoLuogo + "/Vento2.wav")
                listaSottofondoAmbientale = [audioAmbiente_Vento1, audioAmbiente_Vento2]
                sottofondoAmbientaleCambiato = True
            # rumore porte
            rumoreAperturaPorte = GlobalSndVar.suonoaperturaportePalazzoDiRod
            rumoreChiusuraPorte = GlobalSndVar.suonochiusuraportePalazzoDiRod
            # posizione personaggio e robot al cambio stanza
            if not inizio:
                if stanzaVecchia == GlobalGameVar.dictStanze["palazzoDiRod2"]:
                    npers = "s"
                    x = GlobalHWVar.gpx * 14
                    y = GlobalHWVar.gpy * 5
                if stanzaVecchia == GlobalGameVar.dictStanze["tunnelDiRod1"]:
                    npers = "w"
                    x += GlobalHWVar.gpx * 13
                    y = GlobalHWVar.gpy * 12
    elif GlobalGameVar.dictStanze["tunnelDiRod1"] <= stanza <= GlobalGameVar.dictStanze["tunnelDiRod3"]:
        if stanza == GlobalGameVar.dictStanze["tunnelDiRod1"]:
            nomeCanzoneLuogo = "11-ProprietaDiRod"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
                canzoneCambiata = True
            sottofondoLuogo = "TunnelDiRod"
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
                if stanzaVecchia == GlobalGameVar.dictStanze["palazzoDiRod5"]:
                    npers = "s"
                    x -= GlobalHWVar.gpx * 13
                    y = GlobalHWVar.gpy * 2
                if stanzaVecchia == GlobalGameVar.dictStanze["tunnelDiRod2"]:
                    npers = "w"
                    x += GlobalHWVar.gpx * 12
                    y = GlobalHWVar.gpy * 15
        if stanza == GlobalGameVar.dictStanze["tunnelDiRod2"]:
            nomeCanzoneLuogo = "11-ProprietaDiRod"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
                canzoneCambiata = True
            sottofondoLuogo = "TunnelDiRod"
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
                if stanzaVecchia == GlobalGameVar.dictStanze["tunnelDiRod1"]:
                    npers = "s"
                    x -= GlobalHWVar.gpx * 12
                    y = GlobalHWVar.gpy * 2
                if stanzaVecchia == GlobalGameVar.dictStanze["tunnelDiRod3"]:
                    npers = "w"
                    x += GlobalHWVar.gpx * 8
                    y = GlobalHWVar.gpy * 15
        if stanza == GlobalGameVar.dictStanze["tunnelDiRod3"]:
            nomeCanzoneLuogo = "11-ProprietaDiRod"
            if GlobalGameVar.canzoneAttuale != nomeCanzoneLuogo:
                GlobalGameVar.canzoneAttuale = nomeCanzoneLuogo
                canzone = CaricaFileProgetto.loadSound(pathMusiche + GlobalGameVar.canzoneAttuale + ".wav")
                canzoneCambiata = True
            sottofondoLuogo = "TunnelDiRod"
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
                if stanzaVecchia == GlobalGameVar.dictStanze["tunnelDiRod2"]:
                    npers = "s"
                    x -= GlobalHWVar.gpx * 8
                    y = GlobalHWVar.gpy * 2
                if stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod2"]:
                    npers = "w"
                    x += GlobalHWVar.gpx * 12
                    y = GlobalHWVar.gpy * 15
                if stanzaVecchia == GlobalGameVar.dictStanze["tunnelDiRod3"]:
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreLevaTunnelDiRod)
                    i = 0
                    while i < 10:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1

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
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoMetaPassoMontano"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod1"]:
        stoppaMusica = True
    elif (avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["avviatoMusicaFugaCastello"] or avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["stoppatoMusicaFugaCastello"]) and (GlobalGameVar.dictStanze["internoCastello1"] <= stanza <= GlobalGameVar.dictStanze["internoCastello21"] or GlobalGameVar.dictStanze["esternoCastello1"] <= stanza <= GlobalGameVar.dictStanze["esternoCastello5"]):
        stoppaMusica = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoUscitaInternoCastello20Fuggendo"] and stanza == GlobalGameVar.dictStanze["esternoCastello1"]:
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


def riproduciAudioSpeciali(avanzamentoStoria):
    if GlobalGameVar.dictAvanzamentoStoria["incontratoIDueAggressori"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["vomitatoInBiblioteca"]:
        if not GlobalHWVar.canaleSoundBattitoCardiaco.get_busy():
            GlobalHWVar.canaleSoundBattitoCardiaco.play(GlobalSndVar.rumoreBattitoCardiaco, -1)
    elif GlobalGameVar.dictAvanzamentoStoria["fineCenaAlCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoAndatoALettoCastello"]:
        if not GlobalHWVar.canaleSoundMelodieEventi.get_busy():
            GlobalHWVar.canaleSoundMelodieEventi.play(GlobalSndVar.rumoreMelodiaFantasticare, -1)
    elif GlobalGameVar.dictAvanzamentoStoria["monologoPrimaVistaDiNeil"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ripresoImpoDaNeil"]:
        if not GlobalHWVar.canaleSoundBattitoCardiaco.get_busy():
            GlobalHWVar.canaleSoundBattitoCardiaco.play(GlobalSndVar.rumoreBattitoCardiaco, -1)
    elif GlobalGameVar.dictAvanzamentoStoria["avviatoBattitoCardiacoPreConsegnaStrumenti"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["avviatoMusicaFugaCastello"]:
        if not GlobalHWVar.canaleSoundBattitoCardiaco.get_busy():
            GlobalHWVar.canaleSoundBattitoCardiaco.play(GlobalSndVar.rumoreBattitoCardiaco, -1)


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
    elif (stanzaVecchia == GlobalGameVar.dictStanze["palazzoDiRod1"] and stanzaDestinazione == GlobalGameVar.dictStanze["palazzoDiRod2"]) or (stanzaVecchia == GlobalGameVar.dictStanze["palazzoDiRod2"] and stanzaDestinazione == GlobalGameVar.dictStanze["palazzoDiRod1"]):
        riproduciSuono = True
    elif (stanzaVecchia == GlobalGameVar.dictStanze["palazzoDiRod2"] and stanzaDestinazione == GlobalGameVar.dictStanze["palazzoDiRod5"]) or (stanzaVecchia == GlobalGameVar.dictStanze["palazzoDiRod5"] and stanzaDestinazione == GlobalGameVar.dictStanze["palazzoDiRod2"]):
        riproduciSuono = True

    if riproduciSuono:
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumorePortoniCambioStanza)
