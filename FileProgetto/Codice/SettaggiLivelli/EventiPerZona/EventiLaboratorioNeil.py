# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche
import Codice.GestioneMenu.MenuDialoghi as MenuDialoghi
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj


def gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire):
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoTunnelSubacqueo"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        GlobalHWVar.canaleSoundPassiRallo.stop()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoLaboratorioNeil"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"] and x == GlobalHWVar.gpx * 8:
        GlobalHWVar.canaleSoundPassiRallo.stop()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoNotatoCellaDiNeil"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        if x == GlobalHWVar.gpx * 8 and len(percorsoDaEseguire) == 0:
            if y == GlobalHWVar.gpy * 8:
                percorsoDaEseguire = ["d", "d", "d", "d", "d", "d", "d", "d", "d", "s", "d", "d", "d", "d"]
            elif y == GlobalHWVar.gpy * 9 or y == GlobalHWVar.gpy * 10:
                percorsoDaEseguire = ["d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d"]
            carim = True
            caricaTutto = True
        elif x == GlobalHWVar.gpx * 21:
            i = 0
            while i < 10:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoCellaNeil-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["interazioneConCellaDiNeil1"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreBussareVetro)
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoCellaNeil-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["interazioneConCellaDiNeil1"]:
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 11, "s", "OggettoLetteraInvitoReneLaboratorio-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["lettoLetteraInvitoReneLaboratorio"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 6, "s", "OggettoAppuntiIstruzioniCalcolatoreLaboratorio-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 7, "s", "OggettoAppuntiGenerici0Laboratorio-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        avanzamentoStoria += 1
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["interagitoConCalcolatoreDiEventi"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        avanzamentoStoria += 1
        nonMostrarePersonaggio = True
        stanza = GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sedutaSulCalcolatore"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostSedutaSulCalcolatore"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        avanzamentoStoria += 1
        # animazione indossamento casco (abbassamento linea dell'orizzonte dentro il casco)
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreIndossareCasco)
        FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=False)
        yLineaOrizzonte = 0
        while yLineaOrizzonte <= 9:
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.nero, (0, GlobalHWVar.gpy * (yLineaOrizzonte - 1)), (GlobalHWVar.gsx, GlobalHWVar.gpy * (yLineaOrizzonte - 1)), 5)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (0, GlobalHWVar.gpy * yLineaOrizzonte), (GlobalHWVar.gsx, GlobalHWVar.gpy * yLineaOrizzonte), 5)
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockDisegno.tick(GlobalHWVar.fpsAnimazioni)
            yLineaOrizzonte += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["messoCascoCalcolatore"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "NessunoPov-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True

    return x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire
