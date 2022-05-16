# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche
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
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostUccisioneImpoOstile"] and stanza == GlobalGameVar.dictStanze["caverna18"]:
        GlobalHWVar.canaleSoundPassiRallo.stop()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoUltimaStanzaCavernaImpo"] and stanza == GlobalGameVar.dictStanze["caverna18"] and x <= GlobalHWVar.gpx * 20:
        xDestinazione = GlobalHWVar.gpx * 17
        yDestinazione = GlobalHWVar.gpy * 8
        GlobalHWVar.nonAggiornareSchermo = True
        if x == GlobalHWVar.gpx * 20 and npers == 2:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreTerremotoCavernaImpo)
            GlobalHWVar.canaleSoundPassiRallo.stop()
            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [GlobalHWVar.volumeCanzoni * 0.8], True, posizioneCanaleMusica=0)
            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [GlobalHWVar.volumeCanzoni * 0.6], True, posizioneCanaleMusica=0)
            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [GlobalHWVar.volumeCanzoni * 0.4], True, posizioneCanaleMusica=0)
            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [GlobalHWVar.volumeCanzoni * 0.2], True, posizioneCanaleMusica=0)
            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [0], True, posizioneCanaleMusica=0)
            GlobalHWVar.canaleSoundCanzone.stop()
            GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni)
            i = 0
            while i < 10:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [0], True)
            GlobalHWVar.canaliSoundSottofondoAmbientale.arresta()
            GlobalHWVar.canaliSoundSottofondoAmbientale.settaVolume(GlobalHWVar.volumeEffetti)
            FunzioniGraficheGeneriche.animaTremolioSchermo(nelVulcano=1)
        elif not (x == xDestinazione and y == yDestinazione):
            FunzioniGraficheGeneriche.animaTremolioSchermo(nelVulcano=2)
        else:
            FunzioniGraficheGeneriche.animaTremolioSchermo(nelVulcano=3)
        npers = 4
        if x == xDestinazione and y == yDestinazione:
            carim = True
            GlobalHWVar.nonAggiornareSchermo = False
            avanzamentoStoria += 1
        elif x == GlobalHWVar.gpx * 20 and y == GlobalHWVar.gpy * 5:
            y += GlobalHWVar.gpy
        elif x == GlobalHWVar.gpx * 19 and y == GlobalHWVar.gpy * 6:
            y += GlobalHWVar.gpy
        elif x != GlobalHWVar.gpx * 18:
            x -= GlobalHWVar.gpx
        elif x == GlobalHWVar.gpx * 18 and y == GlobalHWVar.gpy * 7:
            y += GlobalHWVar.gpy
        elif x == GlobalHWVar.gpx * 18 and y == GlobalHWVar.gpy * 8:
            x -= GlobalHWVar.gpx
        elif x == GlobalHWVar.gpx * 18 and y == GlobalHWVar.gpy * 9:
            y -= GlobalHWVar.gpy
        if x == GlobalHWVar.gpx * 18 and len(listaNemiciTotali) == 0:
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 6, "s", "RoboTorre", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 7, "s", "RoboTorre", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 8, "s", "RoboTorre", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 9, "s", "RoboTorre", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 10, "s", "RoboTorre", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 10, "s", "RoboTorre", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 10, "s", "RoboTorre", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 9, "s", "RoboTorre", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 8, "s", "RoboTorre", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 7, "s", "RoboTorre", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 6, "s", "RoboTorre", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 6, "s", "RoboTorre", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            carim = True
        evitaTurnoDiColco = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["terremotoUltimaStanzaCavernaImpo"] and stanza == GlobalGameVar.dictStanze["caverna18"]:
        if dati[5] > 0:
            avanzaIlTurnoSenzaMuoverti = True
            evitaTurnoDiColco = True
        else:
            esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = GenericFunc.getStatistiche(dati)
            dati[5] = pvtot
            GlobalHWVar.canaliSoundSottofondoAmbientale.arresta()
            GlobalHWVar.canaleSoundInterazioni.stop()
            GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
            GlobalHWVar.aggiornaSchermo()
            i = 0
            while i < 30:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            # tolgo l'equipaggiamento (spada, scudo, armatura, arco, guanti e collana)
            dati[6] = 0
            dati[7] = 0
            dati[8] = 0
            dati[128] = 0
            dati[129] = 0
            dati[130] = 0
            avanzamentoStoria += 1
            nonMostrarePersonaggio = True
            rx = GlobalHWVar.gpx * 13
            ry = GlobalHWVar.gpy * 4
            nrob = 3
            if dati[10] <= 0:
                dati[10] = 1
            dati[122] = 0
            if not chiamarob:
                chiamarob = True
                ultimoObbiettivoColco = []
                ultimoObbiettivoColco.append("Telecomando")
                ultimoObbiettivoColco.append(x)
                ultimoObbiettivoColco.append(y)
                ultimoObbiettivoColco.append("spostamento")
            stanza = GlobalGameVar.dictStanze["vulcano3"]
            cambiosta = True
            carim = True
            aggiornaImgEquip = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoVistoImpoNonOstili2"] and stanza == GlobalGameVar.dictStanze["caverna18"] and x == GlobalHWVar.gpx * 20:
        GlobalHWVar.canaleSoundPassiRallo.stop()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRiconosciutoIngressoVulcano1"] and stanza == GlobalGameVar.dictStanze["caverna18"]:
        # npers: 1=d, 2=a, 3=w, 4=s
        if npers == 1:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            npers = 2
            carim = True
            caricaTutto = True
        else:
            i = 0
            while i < 10:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRiconosciutoIngressoVulcano2"] and stanza == GlobalGameVar.dictStanze["caverna18"]:
        # npers: 1=d, 2=a, 3=w, 4=s
        if npers == 2:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            npers = 1
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
