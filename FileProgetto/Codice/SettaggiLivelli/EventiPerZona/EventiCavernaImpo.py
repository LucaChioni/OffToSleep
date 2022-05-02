# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.GestioneMenu.MenuDialoghi as MenuDialoghi
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj
import Codice.GestioneNemiciPersonaggi.NemicoObj as NemicoObj


def gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire):
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostSbloccoCaverna"] and stanza == GlobalGameVar.dictStanze["caverna1"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoCaverna1"] and stanza == GlobalGameVar.dictStanze["caverna1"] and x == GlobalHWVar.gpx * 16 and y <= GlobalHWVar.gpx * 8:
        GlobalHWVar.canaleSoundPassiRallo.stop()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["vistoPrimoImpoNellaCaverna"] and stanza == GlobalGameVar.dictStanze["caverna1"]:
        # controllo se sei nel campo visivo dell'impo leggero in stanza1 per farlo diventare ostile
        nelCampoVisivo = False
        xSpawn = 0
        ySpawn = 0
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "RoboLeggero":
                if abs(x - personaggio.x) <= GlobalHWVar.gpx * 3 and abs(y - personaggio.y) <= GlobalHWVar.gpy * 3:
                    nelCampoVisivo = True
                    xSpawn = personaggio.x
                    ySpawn = personaggio.y
                break
        if nelCampoVisivo:
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["caverna1"] and personaggio.tipo == "RoboLeggero":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["caverna1"] and personaggio.tipo == "RoboLeggero":
                    listaPersonaggi.remove(personaggio)
                    break
            percorsoNemico = ["d"]
            nemico = NemicoObj.NemicoObj(xSpawn, ySpawn, "a", "RoboLeggero", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["resoOstileImpoInCaverna1"] and stanza == GlobalGameVar.dictStanze["caverna1"]:
        attaccatoDaNemico = False
        for nemico in listaNemici:
            if nemico.tipo == "RoboLeggero":
                if nemico.direzione != "a":
                    attaccatoDaNemico = True
                break
        if not attaccatoDaNemico:
            avanzaIlTurnoSenzaMuoverti = True
            evitaTurnoDiColco = True
        else:
            avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["attaccatoDaImpoInCaverna1"] and stanza == GlobalGameVar.dictStanze["caverna1"]:
        GlobalHWVar.canaleSoundPassiRallo.stop()
        i = 0
        while i < 2:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostAttaccoDiImpoOstile"] and stanza == GlobalGameVar.dictStanze["caverna1"]:
        nemicoAncoraVivo = False
        for nemico in listaNemici:
            if nemico.tipo == "RoboLeggero":
                nemicoAncoraVivo = True
                break
        if not nemicoAncoraVivo:
            GlobalHWVar.canaleSoundPassiRallo.stop()
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
            if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["monologoPostAttaccoDiImpoOstile"]:
                GlobalHWVar.canaleSoundCanzone.play(canzone, -1)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostAttaccoDiImpoOstile"] and (stanza == GlobalGameVar.dictStanze["caverna2"] or stanza == GlobalGameVar.dictStanze["caverna9"]):
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["monologoPostAttaccoDiImpoOstile"]:
            GlobalHWVar.canaleSoundCanzone.play(canzone, -1)

    # se un nemico ti vede, tutti sanno dove sei
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
