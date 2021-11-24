# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.GestioneMenu.MenuDialoghi as MenuDialoghi
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj


def gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco):
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["servoLanciaAndatoInEsternoCastello5"] and stanza == GlobalGameVar.dictStanze["internoCastello1"]:
        if dati[10] <= 0:
            dati[10] = 1
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
        stanza = GlobalGameVar.dictStanze["internoCastello18"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["guardiaCastelloChiusoPortaLibreriaInternoCastello18"] and stanza == GlobalGameVar.dictStanze["internoCastello7"] and x == GlobalHWVar.gpx * 25:
        for personaggio in listaPersonaggi:
            if personaggio.tipoId == "ServoLancia-6" or personaggio.tipoId == "ServoArco-3":
                personaggio.avanzamentoDialogo = 2
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoConSediaSalaDaPranzoCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello7"]:
        # rimetto gli avanzamenti dei dialoghi dei soldati nella sala da pranzo a 1
        for personaggio in listaPersonaggi:
            if personaggio.tipoId == "ServoLancia-6" or personaggio.tipoId == "ServoArco-3":
                personaggio.avanzamentoDialogo = 1
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
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
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
        i = 0
        while i < len(tutteporte):
            if tutteporte[i] == GlobalGameVar.dictStanze["internoCastello10"] and tutteporte[i + 1] == GlobalHWVar.gpx * 8 and tutteporte[i + 2] == GlobalHWVar.gpy * 5:
                if tutteporte[i + 3]:
                    tutteporte[i + 3] = False
                break
            i += 4
        nonMostrarePersonaggio = True
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["internoCastello10"]
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
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ricevutoListaStrumentiDaNeil"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Neil-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ripresoImpoDaNeil"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["internoCastello20"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"] and stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRipresoImpoDaNeil"] and stanza == GlobalGameVar.dictStanze["internoCastello19"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True

    return x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco
