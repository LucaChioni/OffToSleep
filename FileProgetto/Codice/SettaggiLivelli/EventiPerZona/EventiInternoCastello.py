# -*- coding: utf-8 -*-

import random
import pygame
import GlobalHWVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche
import Codice.GestioneMenu.MenuDialoghi as MenuDialoghi
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj


def gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire):
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["servoLanciaAndatoInEsternoCastello5"] and stanza == GlobalGameVar.dictStanze["internoCastello1"]:
        if dati[10] <= 0:
            dati[10] = 1
        dati[122] = 0
        if x == GlobalHWVar.gpx * 10 and y == GlobalHWVar.gpy * 2:
            if not chiamarob:
                GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoTeleColco)
                chiamarob = True
                ultimoObbiettivoColco = []
                ultimoObbiettivoColco.append("Telecomando")
                ultimoObbiettivoColco.append(x)
                ultimoObbiettivoColco.append(y)
                ultimoObbiettivoColco.append("spostamento")
            percorsoDaEseguire = ["s", "s"]
        elif x == GlobalHWVar.gpx * 10 and y == GlobalHWVar.gpy * 4 and rx == GlobalHWVar.gpx * 10 and ry == GlobalHWVar.gpy * 3:
            percorsoDaEseguire = []
            avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["saraCamminatoNelCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello1"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoEntrataNelCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello1"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumorePortoniCambioStanza)
        percorsoPersonaggio = ["sGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, "s", "ServoLancia-3", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        # npers: 1=d, 2=a, 3=w, 4=s
        npers = 3
        avanzamentoStoria += 1
        avanzaIlTurnoSenzaMuoverti = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["servoLanciaEntratoNelCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello1"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "ServoLancia-3", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoServoLanciaEntrataNelCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello12"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoInternoCastello12"] and stanza == GlobalGameVar.dictStanze["internoCastello14"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoInternoCastello14"] and stanza == GlobalGameVar.dictStanze["internoCastello15"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoInternoCastello15"] and stanza == GlobalGameVar.dictStanze["internoCastello18"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoInternoCastello18"] and stanza == GlobalGameVar.dictStanze["internoCastello18"]:
        portaAperta = False
        i = 0
        while i < len(tutteporte):
            if tutteporte[i] == GlobalGameVar.dictStanze["internoCastello18"] and tutteporte[i + 1] == GlobalHWVar.gpx * 17 and tutteporte[i + 2] == GlobalHWVar.gpy * 12:
                if tutteporte[i + 3]:
                    portaAperta = True
                break
            i += 4
        if portaAperta:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "ServoLancia-12", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["bloccatoDaGuardiaCastelloInInternoCastello18"] and stanza == GlobalGameVar.dictStanze["internoCastello18"]:
        if dati[10] <= 0:
            dati[10] = 1
        dati[122] = 0
        if not chiamarob:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoTeleColco)
            chiamarob = True
            ultimoObbiettivoColco = []
            ultimoObbiettivoColco.append("Telecomando")
            ultimoObbiettivoColco.append(x)
            ultimoObbiettivoColco.append(y)
            ultimoObbiettivoColco.append("spostamento")
        # npers: 1=d, 2=a, 3=w, 4=s
        if abs(x - rx) >= abs(y - ry) and npers != 1:
            npers = 1
            carim = True
        elif abs(y - ry) > abs(x - rx) and npers != 4:
            npers = 4
            carim = True
        impoAccanto = False
        if abs(x - rx) + abs(y - ry) <= GlobalHWVar.gpx:
            impoAccanto = True
        if impoAccanto:
            avanzamentoStoria += 1
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["giratoVersoImpoPerDarloAlCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello18"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoConImpoPrimaDiLasciarloAlleGuardieCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello18"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        avanzamentoStoria += 1
        i = 0
        while i < len(tutteporte):
            if tutteporte[i] == GlobalGameVar.dictStanze["internoCastello18"] and tutteporte[i + 1] == GlobalHWVar.gpx * 17 and tutteporte[i + 2] == GlobalHWVar.gpy * 12:
                if tutteporte[i + 3]:
                    tutteporte[i + 3] = False
                break
            i += 4
        if chiamarob:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoTeleColco)
            chiamarob = False
        stanza = GlobalGameVar.dictStanze["internoCastello18"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["guardiaCastelloChiusoPortaLibreriaInternoCastello18"] and stanza == GlobalGameVar.dictStanze["internoCastello7"] and x == GlobalHWVar.gpx * 25:
        for personaggio in listaPersonaggi:
            if personaggio.tipoId == "ServoLancia-6" or personaggio.tipoId == "ServoArco-3":
                personaggio.avanzamentoDialogo = 2
        i = 0
        while i < len(listaAvanzamentoDialoghi):
            if listaAvanzamentoDialoghi[i] == "ServoLancia-6" or listaAvanzamentoDialoghi[i] == "ServoArco-3":
                listaAvanzamentoDialoghi[i + 1] = 2
            i += 2
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoConSediaSalaDaPranzoCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello7"]:
        # rimetto gli avanzamenti dei dialoghi dei soldati nella sala da pranzo a 1
        for personaggio in listaPersonaggi:
            if personaggio.tipoId == "ServoLancia-6" or personaggio.tipoId == "ServoArco-3":
                personaggio.avanzamentoDialogo = 1
        i = 0
        while i < len(listaAvanzamentoDialoghi):
            if listaAvanzamentoDialoghi[i] == "ServoLancia-6" or listaAvanzamentoDialoghi[i] == "ServoArco-3":
                listaAvanzamentoDialoghi[i + 1] = 1
            i += 2
        nonMostrarePersonaggio = True
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["internoCastello7"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioCenaAlCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello7"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        if not GlobalHWVar.canaleSoundMelodieEventi.get_busy():
            GlobalHWVar.canaleSoundMelodieEventi.play(GlobalSndVar.rumoreMelodiaFantasticare, -1)
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoCenaAlCastello1"] and stanza == GlobalGameVar.dictStanze["internoCastello7"]:
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreCucchiaioSuPiatto)
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoCenaAlCastello2"] and stanza == GlobalGameVar.dictStanze["internoCastello7"]:
        if GlobalHWVar.canaleSoundMelodieEventi.get_busy():
            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundMelodieEventi], [0], False, posizioneCanaleMusica=0)
            GlobalHWVar.canaleSoundMelodieEventi.stop()
            GlobalHWVar.canaleSoundMelodieEventi.set_volume(GlobalHWVar.volumeCanzoni)
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["urloDuranteCenaAlCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello7"]:
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        if not GlobalHWVar.canaleSoundMelodieEventi.get_busy():
            GlobalHWVar.canaleSoundMelodieEventi.play(GlobalSndVar.rumoreMelodiaFantasticare, -1)
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoCenaAlCastello3"] and stanza == GlobalGameVar.dictStanze["internoCastello7"]:
        nonMostrarePersonaggio = False
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["internoCastello7"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["fineCenaAlCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello7"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "ServoLancia-13", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["presoChiaveCameraDaLettoCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello7"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipoId == "ServoLancia-13":
                if personaggio.x == GlobalHWVar.gpx * 29 and personaggio.y == GlobalHWVar.gpy * 7:
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.tipoId == "ServoLancia-13":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.tipoId == "ServoLancia-13":
                    listaPersonaggi.remove(personaggio)
                    break
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
            evitaTurnoDiColco = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["servoLanciaUscitoDaSalaPranzoCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello9"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello10"]:
        portaAperta = False
        i = 0
        while i < len(tutteporte):
            if tutteporte[i] == GlobalGameVar.dictStanze["internoCastello10"] and tutteporte[i + 1] == GlobalHWVar.gpx * 8 and tutteporte[i + 2] == GlobalHWVar.gpy * 5:
                if tutteporte[i + 3]:
                    portaAperta = True
                break
            i += 4
        if portaAperta:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoAndatoALettoCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello10"]:
        if GlobalHWVar.canaleSoundMelodieEventi.get_busy():
            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundMelodieEventi], [0], False, posizioneCanaleMusica=0)
            GlobalHWVar.canaleSoundMelodieEventi.stop()
            GlobalHWVar.canaleSoundMelodieEventi.set_volume(GlobalHWVar.volumeCanzoni)
        # chiudo la porta della tua stanza nel castello
        i = 0
        while i < len(tutteporte):
            if tutteporte[i] == GlobalGameVar.dictStanze["internoCastello10"] and tutteporte[i + 1] == GlobalHWVar.gpx * 8 and tutteporte[i + 2] == GlobalHWVar.gpy * 5:
                if tutteporte[i + 3]:
                    tutteporte[i + 3] = False
                break
            i += 4
        # chiudo tutte le porte di casaHansSara tranne la cameretta
        i = 0
        while i < len(tutteporte):
            if tutteporte[i] == GlobalGameVar.dictStanze["casaHansSara1"] and not (tutteporte[i + 1] == GlobalHWVar.gpx * 6 and tutteporte[i + 2] == GlobalHWVar.gpx * 9):
                tutteporte[i + 3] = False
            i += 4
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["casaHansSara1"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dormitoNelCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello10"]:
        i = 0
        while i < 30:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRisveglioNelCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello10"]:
        nonMostrarePersonaggio = False
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["internoCastello10"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["alzatoDalLettoNelCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello10"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif stanza == GlobalGameVar.dictStanze["internoCastello10"] and GlobalGameVar.cambiataAlCastello[0] != GlobalGameVar.cambiataAlCastello[1]:
        GlobalGameVar.cambiataAlCastello[1] = GlobalGameVar.cambiataAlCastello[0]
        stanza = GlobalGameVar.dictStanze["internoCastello10"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoAlzatoDalLettoNelCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello15"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoStanza15CastelloSecondaVolta"] and stanza == GlobalGameVar.dictStanze["internoCastello18"]:
        portaAperta = False
        i = 0
        while i < len(tutteporte):
            if tutteporte[i] == GlobalGameVar.dictStanze["internoCastello18"] and tutteporte[i + 1] == GlobalHWVar.gpx * 17 and tutteporte[i + 2] == GlobalHWVar.gpy * 12:
                if tutteporte[i + 3]:
                    portaAperta = True
                break
            i += 4
        if portaAperta:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["letto6LibriCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello19"] and x == GlobalHWVar.gpx * 29 and (y == GlobalHWVar.gpy * 12 or y == GlobalHWVar.gpy * 13):
        if npers != 4:
            npers = 4
            avanzaIlTurnoSenzaMuoverti = True
            carim = True
            caricaTutto = True
        if not avanzaIlTurnoSenzaMuoverti and len(percorsoDaEseguire) == 0:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "ServoSpada-8", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            percorsoDaEseguire = ["a"]
            avanzaIlTurnoSenzaMuoverti = True
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["apertoPortaStanza19CastelloVerso20"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoInternoCastello20"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        portaAperta = False
        i = 0
        while i < len(tutteporte):
            if tutteporte[i] == GlobalGameVar.dictStanze["internoCastello20"] and tutteporte[i + 1] == GlobalHWVar.gpx * 10 and tutteporte[i + 2] == GlobalHWVar.gpy * 6:
                if tutteporte[i + 3]:
                    portaAperta = True
                break
            i += 4
        if portaAperta:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoAperturaPortaStudioDiNeil"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        i = 0
        while i < 1:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        avanzamentoStoria += 1
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreBussarePortaUfficioNeil)
        i = 0
        while i < 7:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["bussatoPortaStudioDiNeil"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Neil-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["primoDialogoNeil"] and stanza == GlobalGameVar.dictStanze["internoCastello20"] and y == GlobalHWVar.gpy * 8:
        if not GlobalHWVar.canaleSoundBattitoCardiaco.get_busy():
            GlobalHWVar.canaleSoundBattitoCardiaco.play(GlobalSndVar.rumoreBattitoCardiaco, -1)
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ricevutoListaStrumentiDaNeil"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        if GlobalHWVar.canaleSoundBattitoCardiaco.get_busy():
            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundBattitoCardiaco], [0], False, posizioneCanaleMusica=0)
            GlobalHWVar.canaleSoundBattitoCardiaco.stop()
            GlobalHWVar.canaleSoundBattitoCardiaco.set_volume(GlobalHWVar.volumeEffetti)
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Neil-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ripresoImpoDaNeil"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["internoCastello20"]
        rx = GlobalHWVar.gpx * 12
        ry = GlobalHWVar.gpy * 9
        nrob = 2
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipoId == "Neil-0":
                if personaggio.x == GlobalHWVar.gpx * 15 and personaggio.y == GlobalHWVar.gpy * 12 and personaggio.direzione == "d":
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
            evitaTurnoDiColco = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRipresoImpoDaNeil"] and stanza == GlobalGameVar.dictStanze["internoCastello19"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoUscitaStudioDiNeil"] and stanza == GlobalGameVar.dictStanze["internoCastello19"] and y == GlobalHWVar.gpy * 8:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sbloccatoTunnelDiRod"] and stanza == GlobalGameVar.dictStanze["internoCastello20"] and y == GlobalHWVar.gpy * 7:
        if not GlobalHWVar.canaleSoundBattitoCardiaco.get_busy():
            GlobalHWVar.canaleSoundBattitoCardiaco.play(GlobalSndVar.rumoreBattitoCardiaco, -1)
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["avviatoBattitoCardiacoPreConsegnaStrumenti"] and stanza == GlobalGameVar.dictStanze["internoCastello20"] and y == GlobalHWVar.gpy * 8:
        personaggioGirato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "Neil":
                if personaggio.direzione == "a":
                    personaggioGirato = True
                elif personaggio.percorso != ["aGira", "mantieniPosizione"]:
                    personaggio.percorso = ["aGira", "mantieniPosizione"]
                    personaggio.numeroMovimento = 0
                break
        if personaggioGirato:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Neil-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
            if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["avviatoBattitoCardiacoPreConsegnaStrumenti"]:
                for personaggio in listaPersonaggi:
                    if personaggio.tipo == "Neil":
                        personaggio.percorso = ["a", "sGira", "mantieniPosizione"]
                        personaggio.numeroMovimento = 0
                        break
        else:
            avanzaIlTurnoSenzaMuoverti = True
            evitaTurnoDiColco = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["messoStrumentiSulTavoloDiNeil"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        avanzamentoStoria += 1
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoRaccoltaOggetto)
        avanzaIlTurnoSenzaMuoverti = True
        evitaTurnoDiColco = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["riprodottoSuonoStrumentiSulTavoloDiNeil"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Neil-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["messoImpoSulTavoloDopoConsegnaStrumenti"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        avanzamentoStoria += 1
        if dati[10] <= 0:
            dati[10] = 1
        if chiamarob:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoTeleColco)
            chiamarob = False
            i = 0
            while i < 2:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
        stanza = GlobalGameVar.dictStanze["internoCastello20"]
        cambiosta = True
        carim = True
        caricaTutto = True
        avanzaIlTurnoSenzaMuoverti = True
        evitaTurnoDiColco = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["rimossoImpoMessoSulTavoloDopoConsegnaStrumenti"] and stanza == GlobalGameVar.dictStanze["internoCastello20"] and x == GlobalHWVar.gpx * 11 and y == GlobalHWVar.gpy * 12:
        npers = 3
        avanzamentoStoria += 1
        avanzaIlTurnoSenzaMuoverti = True
        evitaTurnoDiColco = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tentatoDiAndarteneDaNeilConImpoPietra"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Neil-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoNeilSuImpoPietraNonConsegnata"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "Neil":
                if personaggio.x == GlobalHWVar.gpx * 12 and personaggio.y == GlobalHWVar.gpy * 9:
                    personaggioArrivato = True
                elif personaggio.percorso != ["a", "sGira", "sGira", "mantieniPosizione"]:
                    personaggio.percorso = ["a", "sGira", "sGira", "mantieniPosizione"]
                    personaggio.numeroMovimento = 0
                break
        if personaggioArrivato:
            avanzamentoStoria += 1
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoTeleColco)
            if dati[10] <= 0:
                dati[10] = 1
            dati[122] = 0
            chiamarob = True
            ultimoObbiettivoColco = []
            ultimoObbiettivoColco.append("Telecomando")
            ultimoObbiettivoColco.append(x)
            ultimoObbiettivoColco.append(y)
            ultimoObbiettivoColco.append("spostamento")
            GlobalHWVar.canaleSoundPassiColco.play(GlobalSndVar.rumoreCamminataColco)
            rx = GlobalHWVar.gpx * 14
            ry = GlobalHWVar.gpy * 11
            nrob = 3
            carim = True
            caricaTutto = True
            avanzaIlTurnoSenzaMuoverti = True
            evitaTurnoDiColco = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
            evitaTurnoDiColco = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["cliccatoImpoPietraPerFuggireDaNeilConImpo"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        if not (rx == GlobalHWVar.gpx * 12 and ry == GlobalHWVar.gpy * 12):
            avanzaIlTurnoSenzaMuoverti = True
        else:
            percorsoDaEseguire = ["a", "w", "w", "w", "w", "w", "w", "w", "w", "s"]
            avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioPercorsoPerUscireDalloStudioDiNeilConImpo"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        if x == GlobalHWVar.gpx * 10 and y == GlobalHWVar.gpy * 11:
            for personaggio in listaPersonaggi:
                if personaggio.tipo == "Neil":
                    personaggio.percorso = ["aGira", "mantieniPosizione"]
                    personaggio.numeroMovimento = 0
                    break
        elif x == GlobalHWVar.gpx * 10 and y == GlobalHWVar.gpy * 7:
            i = 0
            while i < len(porte):
                if porte[i] == GlobalGameVar.dictStanze["internoCastello20"] and porte[i + 1] == GlobalHWVar.gpx * 10 and porte[i + 2] == GlobalHWVar.gpy * 6:
                    if not porte[i + 3]:
                        porte[i + 3] = True
                        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoaperturaporteCastello)
                        carim = True
                        caricaTutto = True
                    break
                i += 4
            i = 0
            while i < len(tutteporte):
                if tutteporte[i] == GlobalGameVar.dictStanze["internoCastello20"] and tutteporte[i + 1] == GlobalHWVar.gpx * 10 and tutteporte[i + 2] == GlobalHWVar.gpy * 6:
                    if not tutteporte[i + 3]:
                        tutteporte[i + 3] = True
                    break
                i += 4
        elif x == GlobalHWVar.gpx * 10 and y == GlobalHWVar.gpy * 5 and npers == 4:
            avanzamentoStoria += 1
            i = 0
            while i < len(porte):
                if porte[i] == GlobalGameVar.dictStanze["internoCastello20"] and porte[i + 1] == GlobalHWVar.gpx * 10 and porte[i + 2] == GlobalHWVar.gpy * 6:
                    if porte[i + 3]:
                        porte[i + 3] = False
                        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonochiusuraporteCastello)
                    break
                i += 4
            i = 0
            while i < len(tutteporte):
                if tutteporte[i] == GlobalGameVar.dictStanze["internoCastello20"] and tutteporte[i + 1] == GlobalHWVar.gpx * 10 and tutteporte[i + 2] == GlobalHWVar.gpy * 6:
                    if tutteporte[i + 3]:
                        tutteporte[i + 3] = False
                    break
                i += 4
            percorsoDaEseguire = []
            carim = True
            caricaTutto = True
            avanzaIlTurnoSenzaMuoverti = True
            evitaTurnoDiColco = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoDalloStudioDiNeilConImpo"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoUscitoDalloStudioDiNeilConImpo"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipoId == "ServoSpada-9":
                if personaggio.x == GlobalHWVar.gpx * 2 and personaggio.y == GlobalHWVar.gpy * 4 and personaggio.direzione == "a":
                    personaggioArrivato = True
                elif personaggio.percorso != ["w", "aGira", "mantieniPosizione"] and x == GlobalHWVar.gpx * 8:
                    personaggio.percorso = ["w", "aGira", "mantieniPosizione"]
                    personaggio.numeroMovimento = 0
                break
        if personaggioArrivato:
            listaNemiciTotali = []
            listaPersonaggiTotali = []
            stanzeGiaVisitate = []
            avanzamentoStoria += 1
            stanza = GlobalGameVar.dictStanze["internoCastello20"]
            cambiosta = True
            carim = True
            caricaTutto = True
            avanzaIlTurnoSenzaMuoverti = True
            evitaTurnoDiColco = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["chiusoPortaInternoCastello20DaSoldato"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "ServoSpada-9", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoSoldatoInternoCastello20CheChiudePorta"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        nemicoAncoraVivo = False
        spawnCadavereX = 0
        spawnCadavereY = 0
        for nemico in listaNemici:
            if nemico.tipo == "ServoSpada":
                if nemico.vita > 0:
                    nemicoAncoraVivo = True
                spawnCadavereX = nemico.x
                spawnCadavereY = nemico.y
                break
        if not nemicoAncoraVivo:
            if spawnCadavereX == GlobalHWVar.gpx * 2 and spawnCadavereY == GlobalHWVar.gpy * 4:
                spawnCadavereX = GlobalHWVar.gpx * 2
                spawnCadavereY = GlobalHWVar.gpy * 3
            if (spawnCadavereX == x and spawnCadavereY == y) or (spawnCadavereX == rx and spawnCadavereY == ry):
                spawnCadavereX = GlobalHWVar.gpx * 2
                spawnCadavereY = GlobalHWVar.gpy * 5
            if (spawnCadavereX == x and spawnCadavereY == y) or (spawnCadavereX == rx and spawnCadavereY == ry):
                spawnCadavereX = GlobalHWVar.gpx * 3
                spawnCadavereY = GlobalHWVar.gpy * 4
            while (spawnCadavereX == x and spawnCadavereY == y) or (spawnCadavereX == rx and spawnCadavereY == ry):
                spawnCadavereX += GlobalHWVar.gpx * 1
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(spawnCadavereX, spawnCadavereY, "s", "OggettoDictCadavereSoldatoCastello" + str(random.randint(1, 3)) + "-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggiTotali.append(personaggio)
            listaPersonaggi.append(personaggio)
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoAperturaPortaInternoCastello20"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        for personaggio in listaPersonaggiTotali:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello20"] and personaggio.tipo == "OggettoPortaCastelloChiusa":
                listaPersonaggiTotali.remove(personaggio)
                break
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello20"] and personaggio.tipo == "OggettoPortaCastelloChiusa":
                listaPersonaggi.remove(personaggio)
                break
        avanzamentoStoria += 1
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoaperturaporteCastello)
        stanza = GlobalGameVar.dictStanze["internoCastello19"]
        cambiosta = True
        carim = True
        caricaTutto = True
        avanzaIlTurnoSenzaMuoverti = True
        evitaTurnoDiColco = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["apertoPortaInternoCastello20AndandoInInternoCastello19"] and stanza == GlobalGameVar.dictStanze["internoCastello19"]:
        GlobalHWVar.canaleSoundBattitoCardiaco.stop()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["apertoPortaInternoCastello20AndandoInInternoCastello19"]:
            GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni)
            GlobalHWVar.canaleSoundCanzone.play(canzone, -1)
            # chiudo tutte le porte nel castello (per la fuga)
            i = 0
            while i < len(tutteporte):
                if GlobalGameVar.dictStanze["internoCastello1"] <= tutteporte[i] <= GlobalGameVar.dictStanze["internoCastello21"]:
                    tutteporte[i + 3] = False
                i += 4
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRodArrivoAlCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello1"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["monologoRodArrivoAlCastello"]:
            # apro tutte le porte nel castello (per far andare Rod dove vuole (senza chiavi))
            i = 0
            while i < len(tutteporte):
                if GlobalGameVar.dictStanze["internoCastello1"] <= tutteporte[i] <= GlobalGameVar.dictStanze["internoCastello7"] or GlobalGameVar.dictStanze["internoCastello9"] <= tutteporte[i] <= GlobalGameVar.dictStanze["internoCastello19"]:
                    tutteporte[i + 3] = True
                i += 4
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRodNotatoSangueNelCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello2"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRodNotatoPianoAscensoreAperto"] and stanza == GlobalGameVar.dictStanze["internoCastello21"] and y == GlobalHWVar.gpy * 4:
        GlobalHWVar.canaleSoundPassiRallo.stop()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Neil-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRodNeil1"] and stanza == GlobalGameVar.dictStanze["internoCastello21"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello21"] and personaggio.tipo == "Neil":
                if personaggio.direzione == "w":
                    personaggioArrivato = True
                else:
                    personaggio.percorso = ["wGira", "mantieniPosizione"]
                break
        if personaggioArrivato:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Neil-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRodNeil2"] and stanza == GlobalGameVar.dictStanze["internoCastello21"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello21"] and personaggio.tipo == "Neil":
                if personaggio.direzione == "s":
                    personaggioArrivato = True
                else:
                    personaggio.percorso = ["sGira", "mantieniPosizione"]
                break
        if personaggioArrivato:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Neil-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRodNeil3"] and stanza == GlobalGameVar.dictStanze["internoCastello21"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        if npers != 3:
            npers = 3
            avanzaIlTurnoSenzaMuoverti = True
            carim = True
            caricaTutto = True
        else:
            avanzamentoStoria += 1
            percorsoDaEseguire = []
            vetNemiciSoloConXeY = []
            for personaggio in listaPersonaggi:
                vetNemiciSoloConXeY.append(personaggio.x)
                vetNemiciSoloConXeY.append(personaggio.y)
            xDestinazione = GlobalHWVar.gpx * 19
            yDestinazione = GlobalHWVar.gpy * 2
            percorsoTrovato = GenericFunc.pathFinding(x, y, xDestinazione, yDestinazione, vetNemiciSoloConXeY, casevisteEntrateIncluse)
            if percorsoTrovato and percorsoTrovato != "arrivato" and len(percorsoTrovato) >= 4 and (percorsoTrovato[len(percorsoTrovato) - 4] != x or percorsoTrovato[len(percorsoTrovato) - 3] != y):
                xVirtuale = x
                yVirtuale = y
                i = len(percorsoTrovato) - 2
                while i >= 0:
                    if percorsoTrovato[i] > xVirtuale:
                        percorsoDaEseguire.append("d")
                    elif percorsoTrovato[i] < xVirtuale:
                        percorsoDaEseguire.append("a")
                    elif percorsoTrovato[i + 1] > yVirtuale:
                        percorsoDaEseguire.append("s")
                    elif percorsoTrovato[i + 1] < yVirtuale:
                        percorsoDaEseguire.append("w")
                    xVirtuale = percorsoTrovato[i]
                    yVirtuale = percorsoTrovato[i + 1]
                    i -= 2
                if xVirtuale == GlobalHWVar.gpx * 18:
                    percorsoDaEseguire.append("d")
                    percorsoDaEseguire.append("w")
                elif xVirtuale == GlobalHWVar.gpx * 20:
                    percorsoDaEseguire.append("a")
                    percorsoDaEseguire.append("w")
                elif yVirtuale == GlobalHWVar.gpy * 3:
                    percorsoDaEseguire.append("w")
                    percorsoDaEseguire.append("w")
            else:
                print ("Percorso Rallo verso uscita internoCastello21 non trovato")
                percorsoDaEseguire = []
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoDaInternoCastello21ConRod"] and stanza == GlobalGameVar.dictStanze["internoCastello19"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRiflessioneRodDopoUscitaDaInternoCastello21"] and stanza == GlobalGameVar.dictStanze["internoCastello19"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        avanzamentoStoria += 1
        percorsoDaEseguire = ["s", "s", "s"]
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["rientratoInInternoCastello21ConRod"] and stanza == GlobalGameVar.dictStanze["internoCastello21"] and len(percorsoDaEseguire) == 0:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Neil-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRodNeil4"] and stanza == GlobalGameVar.dictStanze["internoCastello21"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello21"] and personaggio.tipo == "Neil":
                if personaggio.direzione == "w":
                    personaggioArrivato = True
                else:
                    personaggio.percorso = ["wGira", "mantieniPosizione"]
                break
        if personaggioArrivato:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Neil-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRodNeil5"] and stanza == GlobalGameVar.dictStanze["internoCastello21"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello21"] and personaggio.tipo == "Neil":
                if personaggio.direzione == "s":
                    personaggioArrivato = True
                else:
                    personaggio.percorso = ["sGira", "mantieniPosizione"]
                break
        if personaggioArrivato:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Neil-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRodNeil6"] and stanza == GlobalGameVar.dictStanze["internoCastello21"]:
        GlobalHWVar.canaleSoundPassiRallo.stop()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        if y == GlobalHWVar.gpy * 4:
            percorsoDaEseguire = ["w"]
        elif y == GlobalHWVar.gpy * 3 and npers != 4:
            npers = 4
            avanzaIlTurnoSenzaMuoverti = True
            carim = True
            caricaTutto = True
        elif y == GlobalHWVar.gpy * 3 and npers == 4:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Neil-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRodNeil7"] and stanza == GlobalGameVar.dictStanze["internoCastello21"]:
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["internoCastello21"]
        cambiosta = True
        carim = True
        caricaTutto = True
        i = 0
        while i < 2:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti / 10.0 * 9.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti / 10.0 * 8.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti / 10.0 * 7.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti / 10.0 * 6.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti / 10.0 * 5.0], False)
        # oscuro lo schermo lentamente
        FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=False, tipoOscuramento=5)
        # inserisci suoni di transizione per resuscitare
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.canaleSoundMelodieEventi.set_volume(0)
        GlobalHWVar.canaleSoundMelodieEventi.play(GlobalSndVar.rumoreSottofondoProcessoRianimazione, -1)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundMelodieEventi], [GlobalHWVar.volumeEffetti / 10.0 * 1.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundMelodieEventi], [GlobalHWVar.volumeEffetti / 10.0 * 2.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundMelodieEventi], [GlobalHWVar.volumeEffetti / 10.0 * 3.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundMelodieEventi], [GlobalHWVar.volumeEffetti / 10.0 * 4.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundMelodieEventi], [GlobalHWVar.volumeEffetti / 10.0 * 5.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundMelodieEventi], [GlobalHWVar.volumeEffetti / 10.0 * 6.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundMelodieEventi], [GlobalHWVar.volumeEffetti / 10.0 * 7.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundMelodieEventi], [GlobalHWVar.volumeEffetti / 10.0 * 8.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundMelodieEventi], [GlobalHWVar.volumeEffetti / 10.0 * 9.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundMelodieEventi], [GlobalHWVar.volumeEffetti], False)
        i = 0
        while i < 50:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreSpegnimentoMacchinarioRianimazione)
        i = 0
        while i < 50:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [0], False)
        GlobalHWVar.canaliSoundSottofondoAmbientale.arresta()
        GlobalHWVar.canaliSoundSottofondoAmbientale.settaVolume(GlobalHWVar.volumeEffetti)
        i = 0
        while i < 60:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreAperturaCellaRianimazione)
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreMovimentoVestiti)
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumorecamminata, -1)
        i = 0
        while i < 50:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreMovimentoVestiti)
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumorecamminata, -1)
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundInterazioni], [GlobalHWVar.volumeEffetti / 10.0 * 9.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundInterazioni], [GlobalHWVar.volumeEffetti / 10.0 * 8.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundInterazioni], [GlobalHWVar.volumeEffetti / 10.0 * 7.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundInterazioni], [GlobalHWVar.volumeEffetti / 10.0 * 6.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundInterazioni], [GlobalHWVar.volumeEffetti / 10.0 * 5.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundInterazioni], [GlobalHWVar.volumeEffetti / 10.0 * 4.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundInterazioni], [GlobalHWVar.volumeEffetti / 10.0 * 3.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundInterazioni], [GlobalHWVar.volumeEffetti / 10.0 * 2.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundInterazioni], [GlobalHWVar.volumeEffetti / 10.0 * 1.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundInterazioni], [0], False)
        GlobalHWVar.canaleSoundInterazioni.stop()
        GlobalHWVar.canaleSoundInterazioni.set_volume(GlobalHWVar.volumeEffetti)
        i = 0
        while i < 30:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundMelodieEventi], [GlobalHWVar.volumeEffetti / 10.0 * 9.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundMelodieEventi], [GlobalHWVar.volumeEffetti / 10.0 * 8.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundMelodieEventi], [GlobalHWVar.volumeEffetti / 10.0 * 7.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundMelodieEventi], [GlobalHWVar.volumeEffetti / 10.0 * 6.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundMelodieEventi], [GlobalHWVar.volumeEffetti / 10.0 * 5.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundMelodieEventi], [GlobalHWVar.volumeEffetti / 10.0 * 4.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundMelodieEventi], [GlobalHWVar.volumeEffetti / 10.0 * 3.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundMelodieEventi], [GlobalHWVar.volumeEffetti / 10.0 * 2.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundMelodieEventi], [GlobalHWVar.volumeEffetti / 10.0 * 1.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundMelodieEventi], [0], False)
        GlobalHWVar.canaleSoundMelodieEventi.stop()
        GlobalHWVar.canaleSoundMelodieEventi.set_volume(GlobalHWVar.volumeEffetti)
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        nonMostrarePersonaggio = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["risveglioSaraResuscitata"] and stanza == GlobalGameVar.dictStanze["internoCastello21"]:
        i = 0
        while i < 50:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["risveglioSaraResuscitata"]:
            stanza = GlobalGameVar.dictStanze["internoCastello21"]
            cambiosta = True
            carim = True
            caricaTutto = True
            # apro le porte nell'ufficio di Neil e nella stanza8 per accedere al tunnel (evitare di dover prendere chiavi)
            i = 0
            while i < len(tutteporte):
                if tutteporte[i] == GlobalGameVar.dictStanze["internoCastello20"] or tutteporte[i] == GlobalGameVar.dictStanze["internoCastello8"]:
                    tutteporte[i + 3] = True
                i += 4
            nonMostrarePersonaggio = False
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["alzataDalTavoloLaboratorioCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello21"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostRimozioneBendeCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello21"]:
        if x == GlobalHWVar.gpx * 26 and y == GlobalHWVar.gpy * 9:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            # npers: 1=d, 2=a, 3=w, 4=s
            if npers == 2:
                npers = 4
                avanzaIlTurnoSenzaMuoverti = True
                carim = True
                caricaTutto = True
            elif npers == 4:
                npers = 1
                avanzaIlTurnoSenzaMuoverti = True
                carim = True
                caricaTutto = True
            elif npers == 1:
                percorsoDaEseguire = ["w"]
        elif x == GlobalHWVar.gpx * 26 and y == GlobalHWVar.gpy * 8 and npers != 1:
            npers = 1
            avanzaIlTurnoSenzaMuoverti = True
            carim = True
            caricaTutto = True
        elif x == GlobalHWVar.gpx * 26 and y == GlobalHWVar.gpy * 8 and npers == 1:
            i = 0
            while i < 2:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreAttimoPericoloso)
            GlobalHWVar.canaleSoundBattitoCardiaco.play(GlobalSndVar.rumoreBattitoCardiaco, -1)
            i = 0
            while i < 1:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoSpecchioPostRianimazione1"] and stanza == GlobalGameVar.dictStanze["internoCastello21"]:
        if x == GlobalHWVar.gpx * 26 and y == GlobalHWVar.gpy * 8:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            percorsoDaEseguire = ["d"]
        elif x == GlobalHWVar.gpx * 27 and y == GlobalHWVar.gpy * 8:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoSpecchioPostRianimazione2"] and stanza == GlobalGameVar.dictStanze["internoCastello21"]:
        if npers == 1:
            i = 0
            while i < 2:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            npers = 2
            avanzaIlTurnoSenzaMuoverti = True
            carim = True
            caricaTutto = True
        elif npers == 2:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            avanzamentoStoria += 1
            npers = 1
            avanzaIlTurnoSenzaMuoverti = True
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["girataDavantiAlloSpecchioPostRianimazione"] and stanza == GlobalGameVar.dictStanze["internoCastello21"]:
        i = 0
        while i < 2:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoSpecchioPostRianimazione3"] and stanza == GlobalGameVar.dictStanze["internoCastello21"]:
        if x == GlobalHWVar.gpx * 27 and y == GlobalHWVar.gpy * 8 and len(percorsoDaEseguire) == 0:
            i = 0
            while i < 2:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            percorsoDaEseguire = ["a", "s"]
        elif x == GlobalHWVar.gpx * 26 and y == GlobalHWVar.gpy * 9:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoTentataLuciditaPostRianimazione"] and stanza == GlobalGameVar.dictStanze["internoCastello21"]:
        if x == GlobalHWVar.gpx * 26 and y == GlobalHWVar.gpy * 9:
            i = 0
            while i < 2:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            percorsoDaEseguire = ["w", "d"]
        elif x == GlobalHWVar.gpx * 27 and y == GlobalHWVar.gpy * 8:
            i = 0
            while i < 2:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoSpecchioPostRianimazione4"] and stanza == GlobalGameVar.dictStanze["internoCastello21"]:
        personaggioCreato = False
        personaggioArrivatoMeta = False
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipoId == "ServoLancia-14":
                personaggioCreato = True
                if personaggio.x == GlobalHWVar.gpx * 23 and personaggio.y == GlobalHWVar.gpy * 10 and npers != 2:
                    personaggioArrivatoMeta = True
                if personaggio.x == GlobalHWVar.gpx * 24 and personaggio.y == GlobalHWVar.gpy * 10:
                    personaggioArrivato = True
        if not personaggioCreato:
            percorsoPersonaggio = ["d", "d", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 10, "d", "ServoLancia-14", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            carim = True
            caricaTutto = True
        elif personaggioArrivatoMeta:
            npers = 2
            avanzaIlTurnoSenzaMuoverti = True
            carim = True
            caricaTutto = True
        elif not personaggioArrivato:
            avanzaIlTurnoSenzaMuoverti = True
        else:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "ServoLancia-14", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoConSoldatoPostRianimazione1"] and stanza == GlobalGameVar.dictStanze["internoCastello21"]:
        if not avanzaManualmentePercorsoDaEseguire:
            percorsoDaEseguire = ["a", "s", "a", "s", "a", "a", "a", "a", "w", "w", "w", "a", "a", "w", "w", "w", "w", "w", "w"]
            avanzaManualmentePercorsoDaEseguire = True
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello21"] and personaggio.tipo == "ServoLancia":
                    personaggio.percorso = ["a", "a", "a", "w", "w", "w", "a", "a", "w", "w", "w", "w", "w", "w"]
                    personaggio.numeroMovimento = 0
                    break
            avanzaIlTurnoSenzaMuoverti = True
        else:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["allontanatoSoldatoPostRianimazione"] and stanza == GlobalGameVar.dictStanze["internoCastello21"] and x == GlobalHWVar.gpx * 26 and y == GlobalHWVar.gpy * 9:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "ServoLancia-14", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoConSoldatoPostRianimazione2"] and stanza == GlobalGameVar.dictStanze["internoCastello21"] and x == GlobalHWVar.gpx * 21 and y == GlobalHWVar.gpy * 8:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "ServoLancia-14", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoConSoldatoPostRianimazione3"] and stanza == GlobalGameVar.dictStanze["internoCastello21"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipoId == "ServoLancia-14":
                if personaggio.x == GlobalHWVar.gpx * 19 and personaggio.y == GlobalHWVar.gpy * 2:
                    personaggioArrivato = True
        if personaggioArrivato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello21"] and personaggio.tipo == "ServoLancia":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello21"] and personaggio.tipo == "ServoLancia":
                    listaPersonaggi.remove(personaggio)
                    break
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["soldatoUscitoDaInternoCastello21PostRianimazione"] and stanza == GlobalGameVar.dictStanze["internoCastello19"]:
        percorsoDaEseguire = ["w", "d", "d", "w", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d"]
        avanzaManualmentePercorsoDaEseguire = True
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoDaInternoCastello21PostRianimazione"] and stanza == GlobalGameVar.dictStanze["internoCastello19"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipoId == "ServoLancia-14":
                if personaggio.x == GlobalHWVar.gpx * 29 and personaggio.y == GlobalHWVar.gpy * 13:
                    personaggioArrivato = True
        if personaggioArrivato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello19"] and personaggio.tipoId == "ServoLancia-14":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello19"] and personaggio.tipoId == "ServoLancia-14":
                    listaPersonaggi.remove(personaggio)
                    break
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["riapparsoImpoInternoCastello20PostRianimazione"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        percorsoDaEseguire = ["d", "d", "d", "d", "d", "d", "d", "d", "s", "s", "s", "s", "s", "d", "d", "d", "s"]
        avanzaManualmentePercorsoDaEseguire = True
        rx = GlobalHWVar.gpx * 15
        ry = GlobalHWVar.gpy * 13
        dati[10] = 0
        carim = True
        caricaTutto = True
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoDaInternoCastello19PostRianimazione"] and stanza == GlobalGameVar.dictStanze["internoCastello20"] and x == GlobalHWVar.gpx * 9 and y == GlobalHWVar.gpy * 4:
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello20"] and personaggio.tipo == "Bibliotecario":
                if personaggio.percorso != ["wGira", "mantieniPosizione"]:
                    personaggio.percorso = ["wGira", "mantieniPosizione"]
                    personaggio.numeroMovimento = 0
                break
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoDaInternoCastello19PostRianimazione"] and stanza == GlobalGameVar.dictStanze["internoCastello20"] and x == GlobalHWVar.gpx * 10 and y == GlobalHWVar.gpy * 8:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["uscitoDaInternoCastello19PostRianimazione"]:
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello20"] and personaggio.tipo == "Bibliotecario":
                    personaggio.percorso = ["sGira", "mantieniPosizione"]
                    personaggio.numeroMovimento = 0
                    break
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoConBibliotecarioPostRianimazione1"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        personaggioGirato = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello20"] and personaggio.tipo == "Bibliotecario":
                if personaggio.direzione == "s":
                    personaggioGirato = True
                break
        if personaggioGirato:
            avanzamentoStoria += 1
        else:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["voltatoBibliotecarioDopoIlDialogoPostRianimazione"] and stanza == GlobalGameVar.dictStanze["internoCastello20"] and x == GlobalHWVar.gpx * 10 and y == GlobalHWVar.gpy * 9:
        GlobalHWVar.canaleSoundPassiRallo.stop()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoDopoIgnoramentoDiBibliotecarioPostRianimazione"] and stanza == GlobalGameVar.dictStanze["internoCastello20"] and x == GlobalHWVar.gpx * 13 and y == GlobalHWVar.gpy * 9 and npers == 4:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["internoCastello20"]
        cambiosta = True
        carim = True
        caricaTutto = True
        nonMostrarePersonaggio = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sdraiataSulTavoloPostRianimazione"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello20"] and personaggio.tipo == "Neil":
                if personaggio.percorso != ["w", "w", "w", "a", "a", "sGira", "mantieniPosizione"]:
                    personaggio.percorso = ["w", "w", "w", "a", "a", "sGira", "mantieniPosizione"]
                    personaggio.numeroMovimento = 0
                elif personaggio.numeroMovimento == len(personaggio.percorso) - 1:
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Neil-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoConNeilPostRianimazione1"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello20"] and personaggio.tipo == "Neil":
                if personaggio.percorso != ["d", "wGira", "mantieniPosizione"]:
                    i = 0
                    while i < 10:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                    personaggio.percorso = ["d", "wGira", "mantieniPosizione"]
                    personaggio.numeroMovimento = 0
                elif personaggio.numeroMovimento == len(personaggio.percorso) - 1:
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoConBibliotecarioPostRianimazione2"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello20"] and personaggio.tipo == "Neil":
                if personaggio.percorso != ["a", "sGira", "mantieniPosizione"]:
                    i = 0
                    while i < 10:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                    personaggio.percorso = ["a", "sGira", "mantieniPosizione"]
                    personaggio.numeroMovimento = 0
                elif personaggio.numeroMovimento == len(personaggio.percorso) - 1:
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Neil-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoConNeilPostRianimazione2"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreIniezioneSiringa)
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundBattitoCardiaco], [GlobalHWVar.volumeEffetti / 10.0 * 5.0], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundBattitoCardiaco], [0], False)
        GlobalHWVar.canaleSoundBattitoCardiaco.stop()
        GlobalHWVar.canaleSoundBattitoCardiaco.set_volume(GlobalHWVar.volumeEffetti)
        for personaggio in listaPersonaggiTotali:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello20"] and personaggio.tipo == "Neil":
                listaPersonaggiTotali.remove(personaggio)
                break
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello20"] and personaggio.tipo == "Neil":
                listaPersonaggi.remove(personaggio)
                break
        # apro le porte nel palazzo di Rod (per evitare di dover prendere chiavi)
        i = 0
        while i < len(tutteporte):
            if tutteporte[i] == GlobalGameVar.dictStanze["palazzoDiRod2"]:
                tutteporte[i + 3] = True
            i += 4
        GlobalHWVar.canaliSoundSottofondoAmbientale.arresta()
        avanzamentoStoria += 1
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            stanza = GlobalGameVar.dictStanze["internoCastello20"]
            cambiosta = True
            carim = True
            caricaTutto = True
            nonMostrarePersonaggio = False
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["alzataDaTavoloPostBloccoTempo"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostTempoBloccato"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        if x == GlobalHWVar.gpx * 14 and y == GlobalHWVar.gpy * 11:
            percorsoDaEseguire = ["d", "s"]
        elif x == GlobalHWVar.gpx * 15 and y == GlobalHWVar.gpy * 12:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["presoImpoPietraPostRianimazione"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = GenericFunc.getStatistiche(dati)
        dati[10] = entot
        GlobalHWVar.canaleSoundAttacco.play(GlobalSndVar.suonoUsoCaricabatterie)
        avanzamentoStoria += 1
        nrob = 3
        carim = True
        caricaTutto = True
        avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ricaricatoImpoPostRianimazione"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoConImpoPostTempoBloccato"] and stanza == GlobalGameVar.dictStanze["internoCastello20"] and ((x == GlobalHWVar.gpx * 12 and y == GlobalHWVar.gpy * 9) or (x == GlobalHWVar.gpx * 11 and y == GlobalHWVar.gpy * 12)):
        GlobalHWVar.canaleSoundPassiRallo.stop()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoVistoBibliotecarioBloccato"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        if (x == GlobalHWVar.gpx * 12 and y == GlobalHWVar.gpy * 9) or (x == GlobalHWVar.gpx * 11 and y == GlobalHWVar.gpy * 12):
            if x == GlobalHWVar.gpx * 12 and y == GlobalHWVar.gpy * 9:
                percorsoDaEseguire = ["s", "a", "s", "a", "s", "a"]
            elif x == GlobalHWVar.gpx * 11 and y == GlobalHWVar.gpy * 12:
                percorsoDaEseguire = ["a", "a"]
        elif x == GlobalHWVar.gpx * 9 and y == GlobalHWVar.gpy * 12:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoAccantoABibliotecarioBloccato"] and stanza == GlobalGameVar.dictStanze["internoCastello19"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["lettoAppuntiNeilSuRianimazione"] and stanza == GlobalGameVar.dictStanze["internoCastello21"]:
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 8, "s", "OggettoAppuntiRatti-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        avanzamentoStoria += 1
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["lettoAppuntiNeilSuRatti"] and stanza == GlobalGameVar.dictStanze["internoCastello21"]:
        GlobalHWVar.canaleSoundPassiRallo.stop()
        if npers != 2:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            npers = 2
            avanzaIlTurnoSenzaMuoverti = True
            carim = True
            caricaTutto = True
        else:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostLetturaAppuntiNeilSuRatti"] and stanza == GlobalGameVar.dictStanze["internoCastello19"] and y == GlobalHWVar.gpy * 10:
        GlobalHWVar.canaleSoundPassiRallo.stop()
        if npers != 4:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            npers = 4
            avanzaIlTurnoSenzaMuoverti = True
            carim = True
            caricaTutto = True
        else:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPerImpoNonBloccatoPostTempoBloccato"] and stanza == GlobalGameVar.dictStanze["internoCastello2"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoScomparsaDiNeilPostTempoBloccato"] and stanza == GlobalGameVar.dictStanze["internoCastello1"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True

    # se un nemico ti vede, tutti sanno dove sei
    if GlobalGameVar.dictAvanzamentoStoria["monologoUscitaInternoCastello20Fuggendo"] <= avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
        listaObiettiviVisti = []
        for nemico in listaNemici:
            if nemico.inCasellaVista and nemico.obbiettivo[0] != "":
                listaObiettiviVisti.append([nemico.obbiettivo[1], nemico.obbiettivo[2]])
        if len(listaObiettiviVisti) > 0:
            for nemico in listaNemici:
                if nemico.inCasellaVista and nemico.obbiettivo[0] == "":
                    primoObiettivo = True
                    for obiettivoVisto in listaObiettiviVisti:
                        if primoObiettivo:
                            nemico.xPosizioneUltimoBersaglio = obiettivoVisto[0]
                            nemico.yPosizioneUltimoBersaglio = obiettivoVisto[1]
                            primoObiettivo = False
                        elif abs(nemico.x - obiettivoVisto[0]) + abs(nemico.y - obiettivoVisto[1]) < abs(nemico.x - nemico.xPosizioneUltimoBersaglio) + abs(nemico.y - nemico.yPosizioneUltimoBersaglio):
                            nemico.xPosizioneUltimoBersaglio = obiettivoVisto[0]
                            nemico.yPosizioneUltimoBersaglio = obiettivoVisto[1]

    return x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire
