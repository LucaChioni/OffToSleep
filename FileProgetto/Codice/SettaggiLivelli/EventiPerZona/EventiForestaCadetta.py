# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.CaricaFileProgetto as CaricaFileProgetto
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche
import Codice.GestioneMenu.MenuDialoghi as MenuDialoghi
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj
import Codice.GestioneNemiciPersonaggi.NemicoObj as NemicoObj


def gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire):
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["messoBicchiereConAcquaSulComodino"] and stanza == GlobalGameVar.dictStanze["forestaCadetta1"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Tutorial-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ingressoForestaCadetta"] and stanza == GlobalGameVar.dictStanze["forestaCadetta1"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialCampoVisivo"] and stanza == GlobalGameVar.dictStanze["forestaCadetta2"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Tutorial-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialDifesa"] and stanza == GlobalGameVar.dictStanze["forestaCadetta4"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["quartaStanzaForestaCadetta"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["quintaStanzaForestaCadetta"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Tutorial-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["legnaReportataSam"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["forestaCadetta5"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioUltimoDialogoHans"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "FiglioUfficiale-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["fineUltimoDialogoHans"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        percorsoNemico = ["w", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 12, "w", "Cinghiale", stanza, percorsoNemico)
        nemico.attacco = GlobalGameVar.dannoMortale
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = []
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 14, "w", "Cinghiale", stanza, percorsoNemico)
        nemico.mosseRimaste = -3
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        avanzamentoStoria += 1
        npers = 4
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["creatoCinghialiForesta5"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        nemicoArrivato = False
        for nemico in listaNemici:
            if nemico.tipo == "Cinghiale" and nemico.y == GlobalHWVar.gpy * 11:
                nemicoArrivato = True
                break
        if nemicoArrivato:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoCinghiale-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["attaccoCinghiale"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        nemicoArrivato = False
        for nemico in listaNemici:
            if nemico.tipo == "Cinghiale" and nemico.y == GlobalHWVar.gpy * 10 and dati[5] <= 0:
                nemicoArrivato = True
                break
        if nemicoArrivato:
            GlobalHWVar.canaleSoundCanzone.stop()
            GlobalHWVar.canaliSoundSottofondoAmbientale.arresta()
            GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
            GlobalHWVar.aggiornaSchermo()
            i = 0
            while i < len(tutteporte):
                if tutteporte[i] == GlobalGameVar.dictStanze["casaHansSara1"] and tutteporte[i + 1] == GlobalHWVar.gpx * 6 and tutteporte[i + 2] == GlobalHWVar.gpx * 9:
                    tutteporte[i + 3] = False
                    break
                i += 4
            # 0-9 => oggetti / 10 => frecce / 11 => guanti / 12 => monete
            oggettiRimastiAHans = [dati[31], dati[32], dati[33], dati[34], dati[35], dati[36], dati[37], dati[38], dati[39], dati[40], dati[132], dati[62], dati[131]]
            dati[31] = 2
            if dati[32] > 0:
                dati[32] = 0
            if dati[33] > 0:
                dati[33] = 0
            if dati[34] > 0:
                dati[34] = 0
            if dati[35] > 0:
                dati[35] = 0
            if dati[36] > 0:
                dati[36] = 0
            if dati[37] > 0:
                dati[37] = 0
            if dati[38] > 0:
                dati[38] = 0
            if dati[39] > 0:
                dati[39] = 0
            if dati[40] > 0:
                dati[40] = 0
            dati[132] = 0
            dati[62] = 0
            dati[131] = 0
            # tolgo gli eventuali guanti equipaggiati
            dati[129] = 0
            i = 0
            while i < 20:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            avanzamentoStoria += 1
            stanza = GlobalGameVar.dictStanze["casaHansSara1"]
            cambiosta = True
            carim = True
            aggiornaImgEquip = True
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["armaturaNonnoCompletata"] and stanza == GlobalGameVar.dictStanze["forestaCadetta1"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Tutorial-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialSeppellireCadaveri"] and stanza == GlobalGameVar.dictStanze["forestaCadetta1"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ingressoForestaCadettaSara"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["accampamentoForestaAnalizzato2"] and stanza == GlobalGameVar.dictStanze["forestaCadetta7"] and x == GlobalHWVar.gpx * 13 and y == GlobalHWVar.gpy * 6:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["incontratoBrancoLupiNeri"] and stanza == GlobalGameVar.dictStanze["forestaCadetta7"] and x == GlobalHWVar.gpx * 13 and y == GlobalHWVar.gpy * 10:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["incontratoCinghiale"] and stanza == GlobalGameVar.dictStanze["forestaCadetta7"]:
        campoRipulito = True
        for nemico in listaNemici:
            if nemico.vita > 0 and nemico.inCasellaVista:
                campoRipulito = False
                break
        if campoRipulito:
            avanzamentoStoria += 1
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["cinghialeUcciso"] and stanza == GlobalGameVar.dictStanze["forestaCadetta7"]:
        campoRipulito = True
        for nemico in listaNemici:
            if nemico.vita > 0 and nemico.inCasellaVista:
                campoRipulito = False
                break
        if not campoRipulito:
            avanzamentoStoria -= 1
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["cadavereSamDepredato"] and stanza == GlobalGameVar.dictStanze["forestaCadetta7"]:
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundBattitoCardiaco], [0], False, posizioneCanaleMusica=0)
        GlobalHWVar.canaleSoundBattitoCardiaco.stop()
        GlobalHWVar.canaleSoundBattitoCardiaco.set_volume(GlobalHWVar.volumeEffetti)
        # oggettiRimastiAHans: 0-9 => oggetti / 10 => frecce / 11 => guanti / 12 => monete
        if oggettiRimastiAHans[0] > 0:
            dati[31] += oggettiRimastiAHans[0]
        if oggettiRimastiAHans[1] > 0:
            dati[32] += oggettiRimastiAHans[1]
        if oggettiRimastiAHans[2] > 0:
            dati[33] += oggettiRimastiAHans[2]
        if oggettiRimastiAHans[3] > 0:
            dati[34] += oggettiRimastiAHans[3]
        if oggettiRimastiAHans[4] > 0:
            dati[35] += oggettiRimastiAHans[4]
        if oggettiRimastiAHans[5] > 0:
            dati[36] += oggettiRimastiAHans[5]
        if oggettiRimastiAHans[6] > 0:
            dati[37] += oggettiRimastiAHans[6]
        if oggettiRimastiAHans[7] > 0:
            dati[38] += oggettiRimastiAHans[7]
        if oggettiRimastiAHans[8] > 0:
            dati[39] += oggettiRimastiAHans[8]
        if oggettiRimastiAHans[9] > 0:
            dati[40] += oggettiRimastiAHans[9]
        if oggettiRimastiAHans[10] > 0:
            dati[132] += oggettiRimastiAHans[10]
        if dati[132] > GlobalGameVar.frecceMaxPerFaretra[dati[133]]:
            dati[132] = GlobalGameVar.frecceMaxPerFaretra[dati[133]]
        if dati[62] <= 0 and oggettiRimastiAHans[11] > 0:
            dati[62] = oggettiRimastiAHans[11]
        if oggettiRimastiAHans[12] > 0:
            dati[131] += oggettiRimastiAHans[12]
        # il soldato ti lascia la sua spada/armatura/scudo
        dati[43] = 1
        dati[53] = 1
        dati[58] = 1
        avanzamentoStoria += 1
        i = 0
        while i < len(stanzeGiaVisitate):
            if stanzeGiaVisitate[i] == stanza:
                del stanzeGiaVisitate[i]
            i += 1
        i = 0
        while i < len(listaPersonaggiTotali):
            if listaPersonaggiTotali[i].stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta7"]:
                del listaPersonaggiTotali[i]
            else:
                i += 1
        i = 0
        while i < len(listaNemiciTotali):
            if listaNemiciTotali[i].stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta7"]:
                del listaNemiciTotali[i]
            else:
                i += 1
        stanza = GlobalGameVar.dictStanze["forestaCadetta7"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sotterratoSam"] and stanza == GlobalGameVar.dictStanze["forestaCadetta7"]:
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["rimessaMusicaDopoTombaSam"] and stanza == GlobalGameVar.dictStanze["forestaCadetta9"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoHansFuoriCasaSognoCastello"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"] and y == GlobalHWVar.gpy * 8:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoLinoMortoSognoCastello"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        percorsoNemico = ["a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 8, "a", "Cittadino1", stanza, percorsoNemico)
        nemico.difesa = GlobalGameVar.dannoMortale
        nemico.mosseRimaste = -1
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "a", "s", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 9, "a", "Cittadino3", stanza, percorsoNemico)
        nemico.difesa = GlobalGameVar.dannoMortale
        nemico.mosseRimaste = -1
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        avanzamentoStoria += 1
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["apparsiAggressoriForestaSognoCastello"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        for nemico in listaNemici:
            if (nemico.tipo == "Cittadino1" or nemico.tipo == "Cittadino3") and nemico.mosseRimaste > 0:
                nemico.mosseRimaste -= 1
        nemicoArrivato = False
        for nemico in listaNemici:
            if nemico.tipo == "Cittadino1" and nemico.x == GlobalHWVar.gpx * 17 and nemico.y == GlobalHWVar.gpy * 8:
                nemicoArrivato = True
                break
        if nemicoArrivato:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Ragazzo1-8", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialoghiAggressoriForestaCasaSognoCastello"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        for nemico in listaNemici:
            if (nemico.tipo == "Cittadino1" or nemico.tipo == "Cittadino3") and nemico.mosseRimaste > 0:
                nemico.mosseRimaste -= 1
        if x == GlobalHWVar.gpx * 15 and y == GlobalHWVar.gpy * 15:
            GlobalHWVar.canaleSoundPassiRallo.stop()
            nonMostrarePersonaggio = True
            avanzamentoStoria += 1
            stanza = GlobalGameVar.dictStanze["internoCastello10"]
            cambiosta = True
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["HansUscitoDaCasa4NellaSeraDellInizioDelGioco"] and stanza == GlobalGameVar.dictStanze["forestaCadetta1"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "FratelloMaggiore" and personaggio.x == GlobalHWVar.gpx * 2 and personaggio.y == GlobalHWVar.gpy * 4 and personaggio.direzione == "a":
                personaggioArrivato = True
                break
        if personaggioArrivato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta1"] and personaggio.tipo == "FratelloMaggiore":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta1"] and personaggio.tipo == "FratelloMaggiore":
                    listaPersonaggi.remove(personaggio)
                    break
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["HansUscitoDaForestaCadetta1NellaSeraDellInizioDelGioco"] and stanza == GlobalGameVar.dictStanze["forestaCadetta2"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "FratelloMaggiore" and personaggio.x == GlobalHWVar.gpx * 12 and personaggio.y == GlobalHWVar.gpy * 15 and personaggio.direzione == "s":
                personaggioArrivato = True
                break
        if personaggioArrivato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta2"] and personaggio.tipo == "FratelloMaggiore":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta2"] and personaggio.tipo == "FratelloMaggiore":
                    listaPersonaggi.remove(personaggio)
                    break
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["HansUscitoDaForestaCadetta2NellaSeraDellInizioDelGioco"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        # npers: 1=d, 2=a, 3=w, 4=s
        if x == GlobalHWVar.gpy * 18 and y == GlobalHWVar.gpy * 7:
            percorsoDaEseguire = ["d"]
        elif x == GlobalHWVar.gpy * 19 and y == GlobalHWVar.gpy * 7:
            percorsoDaEseguire = ["s"]
        elif x == GlobalHWVar.gpy * 19 and y == GlobalHWVar.gpy * 8 and npers == 4:
            npers = 2
            carim = True
            caricaTutto = True
        elif x == GlobalHWVar.gpy * 19 and y == GlobalHWVar.gpy * 8 and npers == 2:
            avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivataInForestaCadetta5Calcolatore"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "FiglioUfficiale-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoHansSamCalcolatore"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        percorsoNemico = ["w", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 12, "w", "Cinghiale", stanza, percorsoNemico)
        nemico.attacco = GlobalGameVar.dannoMortale
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = []
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 14, "w", "Cinghiale", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta5"] and personaggio.tipo == "FratelloMaggiore":
                personaggio.girati("s")
                break
        avanzamentoStoria += 1
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["comparsiCinghialiForestaCalcolatore"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        nemicoArrivato = False
        for nemico in listaNemici:
            if nemico.tipo == "Cinghiale" and nemico.y == GlobalHWVar.gpy * 11:
                nemicoArrivato = True
                break
        if nemicoArrivato:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoCinghiale-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoCinghialeCalcolatore"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        nemicoArrivato = False
        for nemico in listaNemici:
            if nemico.tipo == "Cinghiale" and nemico.y == GlobalHWVar.gpy * 10:
                nemicoArrivato = True
                break
        if nemicoArrivato:
            # animazione attacco del cinghiale ad Hans + spegnimento falò
            pathImgs = "Risorse/Immagini/Scenari/Stanza" + str(stanza) + "/Animazioni/AttaccoCinghiale/"
            coordinateImgAnimata = (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 7)
            dimensioniImgAnimata = (GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 5)
            listaAudio = [0, GlobalSndVar.rumoreAttaccoCinghialeAdHans]
            FunzioniGraficheGeneriche.animaEvento(pathImgs, coordinateImgAnimata, dimensioniImgAnimata, listaAudio, battito=8)
            avanzamentoStoria += 1
            stanza = GlobalGameVar.dictStanze["forestaCadetta5"]
            cambiosta = True
            carim = True
            caricaTutto = True
            GlobalHWVar.nonAggiornareSchermo = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["colpitoHansDalCinghialeCalcolatore"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        if GlobalHWVar.nonAggiornareSchermo:
            GlobalHWVar.nonAggiornareSchermo = False
            GlobalHWVar.aggiornaSchermo()
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "FiglioUfficiale":
                if personaggio.percorso != ["", "", "sGira", "", "", "d", "d", "s", "s", "a", "s", "a", "s", "a", "s", "s", "a", "s"]:
                    personaggio.percorso = ["", "", "sGira", "", "", "d", "d", "s", "s", "a", "s", "a", "s", "a", "s", "s", "a", "s"]
                if personaggio.x == GlobalHWVar.gpx * 18 and personaggio.y == GlobalHWVar.gpy * 8:
                    percorsoDaEseguire = ["w"]
                elif personaggio.x == GlobalHWVar.gpx * 15 and personaggio.y == GlobalHWVar.gpy * 15 and personaggio.direzione == "s":
                    personaggioArrivato = True
                break
        # npers: 1=d, 2=a, 3=w, 4=s
        if x == GlobalHWVar.gpx * 19 and y == GlobalHWVar.gpy * 7 and npers != 4:
            npers = 4
            carim = True
            caricaTutto = True
        elif personaggioArrivato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta5"] and personaggio.tipo == "FiglioUfficiale":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta5"] and personaggio.tipo == "FiglioUfficiale":
                    listaPersonaggi.remove(personaggio)
                    break
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
        elif len(percorsoDaEseguire) == 0:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["SamScappatoDaForesta5PostUccisioneHansCalcolatore"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        if GlobalHWVar.nonAggiornareSchermo:
            GlobalHWVar.nonAggiornareSchermo = False
            GlobalHWVar.aggiornaSchermo()
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "Cinghiale":
                if personaggio.x == GlobalHWVar.gpx * 15 and personaggio.y == GlobalHWVar.gpy * 15 and personaggio.direzione == "s":
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta5"] and personaggio.tipo == "Cinghiale":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta5"] and personaggio.tipo == "Cinghiale":
                    listaPersonaggi.remove(personaggio)
                    break
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["secondoCinghialeUscitoDaForesta5PostUccisioneHansCalcolatore"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        personaggioCreato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "SaraArmaturaPelle":
                personaggioCreato = True
                break
        # npers: 1=d, 2=a, 3=w, 4=s
        if x == GlobalHWVar.gpx * 19 and y == GlobalHWVar.gpy * 7 and len(percorsoDaEseguire) == 0:
            i = 0
            while i < 10:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            percorsoDaEseguire = ["s"]
        elif x == GlobalHWVar.gpx * 19 and y == GlobalHWVar.gpy * 8 and npers != 2:
            i = 0
            while i < 10:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            npers = 2
            carim = True
            caricaTutto = True
        elif x == GlobalHWVar.gpx * 19 and y == GlobalHWVar.gpy * 8 and npers == 2 and len(percorsoDaEseguire) == 0:
            # animazione mancamento lieve
            FunzioniGraficheGeneriche.animaMancamento(intensita="lieve")
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            percorsoDaEseguire = ["a", "a"]
        elif x == GlobalHWVar.gpx * 17 and y == GlobalHWVar.gpy * 8 and len(percorsoDaEseguire) == 0:
            # animazione mancamento medio
            FunzioniGraficheGeneriche.animaMancamento(intensita="media")
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            percorsoDaEseguire = ["a"]
        elif x == GlobalHWVar.gpx * 16 and y == GlobalHWVar.gpy * 8 and npers != 3:
            # animazione mancamento molto lieve
            FunzioniGraficheGeneriche.animaMancamento(intensita="lieve")
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            npers = 3
            carim = True
            caricaTutto = True
        elif x == GlobalHWVar.gpx * 16 and y == GlobalHWVar.gpy * 8 and npers == 3:
            if not personaggioCreato:
                # animazione mancamento pesante
                FunzioniGraficheGeneriche.animaMancamento(intensita="pesanteOut")
                GlobalHWVar.nonAggiornareSchermo = True
                percorsoPersonaggio = ["s", "dGira", "aGira", "sGira", "s", "aGira", "s", "a", "s", "a", "a", "w", "w", "dGira", "w", "s", "wGira", "", "s", "s", "s", "s", "a", "s", "s"]
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 7, "s", "SaraArmaturaPelle-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                carim = True
                caricaTutto = True
            else:
                i = 0
                while i < 5:
                    pygame.time.wait(100)
                    inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                    i += 1
                # animazione mancamento pesante
                GlobalHWVar.nonAggiornareSchermo = False
                FunzioniGraficheGeneriche.animaMancamento(intensita="pesanteIn")
                avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["apparsaSaraInForesta5Calcolatore"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        if GlobalHWVar.nonAggiornareSchermo:
            GlobalHWVar.nonAggiornareSchermo = False
            GlobalHWVar.aggiornaSchermo()
        # npers: 1=d, 2=a, 3=w, 4=s
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "SaraArmaturaPelle":
                if personaggio.x == GlobalHWVar.gpx * 19 and personaggio.y == GlobalHWVar.gpy * 7 and personaggio.direzione == "s" and npers != 1:
                    npers = 1
                    carim = True
                    caricaTutto = True
                elif personaggio.x == GlobalHWVar.gpx * 19 and personaggio.y == GlobalHWVar.gpy * 8 and personaggio.direzione == "d":
                    i = 0
                    while i < 2:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                elif personaggio.x == GlobalHWVar.gpx * 19 and personaggio.y == GlobalHWVar.gpy * 8 and personaggio.direzione == "a":
                    i = 0
                    while i < 2:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                elif personaggio.x == GlobalHWVar.gpx * 19 and personaggio.y == GlobalHWVar.gpy * 8 and personaggio.direzione == "s":
                    i = 0
                    while i < 2:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                elif personaggio.x == GlobalHWVar.gpx * 19 and personaggio.y == GlobalHWVar.gpy * 9 and personaggio.direzione == "a":
                    i = 0
                    while i < 10:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                elif personaggio.x == GlobalHWVar.gpx * 19 and personaggio.y == GlobalHWVar.gpy * 10 and personaggio.direzione == "s" and npers != 4:
                    npers = 4
                    carim = True
                    caricaTutto = True
                elif personaggio.x == GlobalHWVar.gpx * 18 and personaggio.y == GlobalHWVar.gpy * 10 and personaggio.direzione == "a":
                    i = 0
                    while i < 10:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                elif personaggio.x == GlobalHWVar.gpx * 16 and personaggio.y == GlobalHWVar.gpy * 9 and personaggio.direzione == "d":
                    i = 0
                    while i < 10:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                    percorsoDaEseguire = ["d"]
                elif personaggio.x == GlobalHWVar.gpx * 16 and personaggio.y == GlobalHWVar.gpy * 8 and personaggio.direzione == "w" and npers != 2:
                    npers = 2
                    carim = True
                    caricaTutto = True
                elif personaggio.x == GlobalHWVar.gpx * 16 and personaggio.y == GlobalHWVar.gpy * 8 and personaggio.direzione == "w" and npers == 2:
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreLamentoHansCinghiale)
                    i = 0
                    while i < 20:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                elif personaggio.x == GlobalHWVar.gpx * 15 and personaggio.y == GlobalHWVar.gpy * 15 and personaggio.direzione == "s":
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta5"] and personaggio.tipo == "SaraArmaturaPelle":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta5"] and personaggio.tipo == "SaraArmaturaPelle":
                    listaPersonaggi.remove(personaggio)
                    break
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
        elif len(percorsoDaEseguire) == 0:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["SaraUscitaDaForestaCadetta5Calcolatore"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        # npers: 1=d, 2=a, 3=w, 4=s
        if npers != 3:
            npers = 3
            carim = True
            caricaTutto = True
        else:
            screen = GlobalHWVar.schermo.copy().convert()
            i = 0
            while i < 10:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
            if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["SaraUscitaDaForestaCadetta5Calcolatore"]:
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
                GlobalHWVar.aggiornaSchermo()
                xSpawn = GlobalHWVar.gpx * 17
                ySpawn = GlobalHWVar.gpy * 8
                nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "avvia", nonMostrarePersonaggio, carim, caricaTutto)
                nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "compari", nonMostrarePersonaggio, carim, caricaTutto)
                percorsoPersonaggio = ["w", "s", "wGira", "", "s", "s", "s", "s", "a", "s", "s"]
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 9, "d", "SaraArmaturaPelle-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                carim = True
                caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroPerUrloDiHans1Pt1"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        avanzamentoStoria += 1
        xSpawn = GlobalHWVar.gpx * 17
        ySpawn = GlobalHWVar.gpy * 8
        nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "concludi", nonMostrarePersonaggio, carim, caricaTutto)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroPerUrloDiHans1Pt2"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "SaraArmaturaPelle":
                if personaggio.x == GlobalHWVar.gpx * 16 and personaggio.y == GlobalHWVar.gpy * 8 and personaggio.direzione == "w":
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreLamentoHansCinghiale)
                    i = 0
                    while i < 20:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                elif personaggio.x == GlobalHWVar.gpx * 16 and personaggio.y == GlobalHWVar.gpy * 12 and personaggio.direzione == "s":
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            avanzamentoStoria += 1
            xSpawn = GlobalHWVar.gpx * 17
            ySpawn = GlobalHWVar.gpy * 8
            nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "avvia", nonMostrarePersonaggio, carim, caricaTutto)
            nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "compari", nonMostrarePersonaggio, carim, caricaTutto)
            for personaggio in listaPersonaggi:
                if personaggio.tipo == "SaraArmaturaPelle":
                    listaPersonaggi.remove(personaggio)
                    break
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta5"] and personaggio.tipo == "SaraArmaturaPelle":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            carim = True
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroPerUrloDiHans2Pt1"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        personaggioCreato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "SaraArmaturaPelle":
                personaggioCreato = True
                break
        if not personaggioCreato:
            percorsoPersonaggio = ["s", "wGira", "", "s", "s", "s", "s", "a", "s", "s"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 8, "w", "SaraArmaturaPelle-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            carim = True
            caricaTutto = True
        else:
            xSpawn = GlobalHWVar.gpx * 17
            ySpawn = GlobalHWVar.gpy * 8
            nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "concludi", nonMostrarePersonaggio, carim, caricaTutto)
            avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroPerUrloDiHans2Pt2"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "SaraArmaturaPelle":
                if personaggio.x == GlobalHWVar.gpx * 16 and personaggio.y == GlobalHWVar.gpy * 8 and personaggio.direzione == "w":
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreLamentoHansCinghiale)
                    i = 0
                    while i < 20:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            screen = GlobalHWVar.schermo.copy().convert()
            xSpawn = GlobalHWVar.gpx * 17
            ySpawn = GlobalHWVar.gpy * 8
            nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "avvia", nonMostrarePersonaggio, carim, caricaTutto)
            nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "compari", nonMostrarePersonaggio, carim, caricaTutto)
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "concludi", nonMostrarePersonaggio, carim, caricaTutto, personaggioGiaNelloScreen=True)
            avanzamentoStoria += 1
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroPerUrloDiHans3"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        avanzamentoStoria += 1
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreLamentoHansCinghiale)
        screen = GlobalHWVar.schermo.copy().convert()
        imgTrasparenza = pygame.Surface((GlobalHWVar.gsx, GlobalHWVar.gsy), pygame.SRCALPHA)
        imgStanzaLab = CaricaFileProgetto.loadImage("Risorse/Immagini/Scenari/Stanza" + str(GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]) + "/StanzaG.png", GlobalHWVar.gsx, GlobalHWVar.gsy, False)
        imgSbiancamentoSchermo = pygame.Surface((GlobalHWVar.gsx, GlobalHWVar.gsy), flags=pygame.SRCALPHA)
        i = 0
        while i <= 510:
            if i < 60:
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            elif 60 <= i < 85:
                if i == 60:
                    GlobalHWVar.canaliSoundSottofondoAmbientale.mettiInPausa()
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
                opacita = ((i - 60) * 15)
                if opacita > 255:
                    opacita = 255
                imgSbiancamentoSchermo.fill((255, 255, 255, opacita))
                GlobalHWVar.disegnaImmagineSuSchermo(imgSbiancamentoSchermo, (0, 0))
            elif 85 <= i < 110:
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.bianco)
            elif 110 <= i < 135:
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
                imgSbiancamentoSchermo.fill((255, 255, 255, 255 - ((i - 110) * 10)))
                GlobalHWVar.disegnaImmagineSuSchermo(imgSbiancamentoSchermo, (0, 0))
            elif 135 <= i < 200:
                if i == 135:
                    GlobalHWVar.canaliSoundSottofondoAmbientale.togliPausa()
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
                if i == 140:
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreLamentoHansCinghiale)
            elif 200 <= i < 225:
                if i == 200:
                    GlobalHWVar.canaliSoundSottofondoAmbientale.mettiInPausa()
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
                opacita = ((i - 200) * 15)
                if opacita > 255:
                    opacita = 255
                imgSbiancamentoSchermo.fill((255, 255, 255, opacita))
                GlobalHWVar.disegnaImmagineSuSchermo(imgSbiancamentoSchermo, (0, 0))
            elif 225 <= i < 250:
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.bianco)
            elif 250 <= i < 275:
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
                imgSbiancamentoSchermo.fill((255, 255, 255, 255 - ((i - 250) * 10)))
                GlobalHWVar.disegnaImmagineSuSchermo(imgSbiancamentoSchermo, (0, 0))
            elif 275 <= i < 340:
                if i == 275:
                    GlobalHWVar.canaliSoundSottofondoAmbientale.togliPausa()
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
                if i == 280:
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreLamentoHansCinghiale)
            elif 340 <= i < 365:
                if i == 340:
                    GlobalHWVar.canaliSoundSottofondoAmbientale.mettiInPausa()
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
                opacita = ((i - 340) * 15)
                if opacita > 255:
                    opacita = 255
                imgSbiancamentoSchermo.fill((255, 255, 255, opacita))
                GlobalHWVar.disegnaImmagineSuSchermo(imgSbiancamentoSchermo, (0, 0))
            elif 365 <= i < 390:
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.bianco)
            elif 390 <= i < 415:
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
                imgSbiancamentoSchermo.fill((255, 255, 255, 255 - ((i - 390) * 10)))
                GlobalHWVar.disegnaImmagineSuSchermo(imgSbiancamentoSchermo, (0, 0))
            elif 415 <= i < 480:
                if i == 415:
                    GlobalHWVar.canaliSoundSottofondoAmbientale.togliPausa()
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
                if i == 420:
                    GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreLamentoHansCinghiale)
            elif 480 <= i < 505:
                if i == 480:
                    GlobalHWVar.canaliSoundSottofondoAmbientale.mettiInPausa()
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
                opacita = ((i - 480) * 15)
                if opacita > 255:
                    opacita = 255
                imgSbiancamentoSchermo.fill((255, 255, 255, opacita))
                GlobalHWVar.disegnaImmagineSuSchermo(imgSbiancamentoSchermo, (0, 0))
            elif 505 <= i <= 510:
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.bianco)
            imgTrasparenza.fill((255, 255, 255, i // 2))
            imgStanzaLabTemp = imgStanzaLab.copy()
            imgStanzaLabTemp.blit(imgTrasparenza, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            GlobalHWVar.disegnaImmagineSuSchermo(imgStanzaLabTemp, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i += 1
        GlobalHWVar.disegnaImmagineSuSchermo(imgStanzaLab, (0, 0))
        GlobalHWVar.aggiornaSchermo()
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        c = 0
        while c <= 2:
            GlobalHWVar.canaliSoundSottofondoAmbientale.togliPausa()
            i = 0
            while i < 1:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreLamentoHansCinghiale)
            i = 0
            while i < 25:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            GlobalHWVar.canaliSoundSottofondoAmbientale.mettiInPausa()
            i = 0
            while i < 20:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            c += 1
        GlobalHWVar.canaliSoundSottofondoAmbientale.togliPausa()
        i = 0
        while i < 1:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreLamentoHansCinghiale)
        imgOscuramentoSchermo = pygame.Surface((GlobalHWVar.gsx, GlobalHWVar.gsy), flags=pygame.SRCALPHA)
        i = 0
        while i <= 510:
            if i == 60:
                GlobalHWVar.canaliSoundSottofondoAmbientale.mettiInPausa()
            elif i == 135:
                GlobalHWVar.canaliSoundSottofondoAmbientale.togliPausa()
            elif i == 140:
                GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreLamentoHansCinghiale)
            elif i == 215:
                GlobalHWVar.canaliSoundSottofondoAmbientale.mettiInPausa()
            elif i == 275:
                GlobalHWVar.canaliSoundSottofondoAmbientale.togliPausa()
            elif i == 280:
                GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreLamentoHansCinghiale)
            elif i == 355:
                GlobalHWVar.canaliSoundSottofondoAmbientale.mettiInPausa()
            elif i == 415:
                GlobalHWVar.canaliSoundSottofondoAmbientale.togliPausa()
            elif i == 420:
                GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreLamentoHansCinghiale)
            elif i == 495:
                GlobalHWVar.canaliSoundSottofondoAmbientale.mettiInPausa()
            GlobalHWVar.disegnaImmagineSuSchermo(imgStanzaLab, (0, 0))
            imgOscuramentoSchermo.fill((0, 0, 0, i // 2))
            GlobalHWVar.disegnaImmagineSuSchermo(imgOscuramentoSchermo, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i += 1
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
        GlobalHWVar.aggiornaSchermo()
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.canaliSoundSottofondoAmbientale.togliPausa()
        i = 0
        while i < 1:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreLamentoHansCinghiale)
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundInterazioni, GlobalHWVar.canaliSoundSottofondoAmbientale, GlobalHWVar.canaleSoundBattitoCardiaco], [GlobalHWVar.volumeEffetti * 0.9, GlobalHWVar.volumeEffetti * 0.9, GlobalHWVar.volumeEffetti * 0.9], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundInterazioni, GlobalHWVar.canaliSoundSottofondoAmbientale, GlobalHWVar.canaleSoundBattitoCardiaco], [GlobalHWVar.volumeEffetti * 0.8, GlobalHWVar.volumeEffetti * 0.8, GlobalHWVar.volumeEffetti * 0.8], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundInterazioni, GlobalHWVar.canaliSoundSottofondoAmbientale, GlobalHWVar.canaleSoundBattitoCardiaco], [GlobalHWVar.volumeEffetti * 0.7, GlobalHWVar.volumeEffetti * 0.7, GlobalHWVar.volumeEffetti * 0.7], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundInterazioni, GlobalHWVar.canaliSoundSottofondoAmbientale, GlobalHWVar.canaleSoundBattitoCardiaco], [GlobalHWVar.volumeEffetti * 0.6, GlobalHWVar.volumeEffetti * 0.6, GlobalHWVar.volumeEffetti * 0.6], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundInterazioni, GlobalHWVar.canaliSoundSottofondoAmbientale, GlobalHWVar.canaleSoundBattitoCardiaco], [GlobalHWVar.volumeEffetti * 0.5, GlobalHWVar.volumeEffetti * 0.5, GlobalHWVar.volumeEffetti * 0.5], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundInterazioni, GlobalHWVar.canaliSoundSottofondoAmbientale, GlobalHWVar.canaleSoundBattitoCardiaco], [GlobalHWVar.volumeEffetti * 0.4, GlobalHWVar.volumeEffetti * 0.4, GlobalHWVar.volumeEffetti * 0.4], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundInterazioni, GlobalHWVar.canaliSoundSottofondoAmbientale, GlobalHWVar.canaleSoundBattitoCardiaco], [GlobalHWVar.volumeEffetti * 0.3, GlobalHWVar.volumeEffetti * 0.3, GlobalHWVar.volumeEffetti * 0.3], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundInterazioni, GlobalHWVar.canaliSoundSottofondoAmbientale, GlobalHWVar.canaleSoundBattitoCardiaco], [GlobalHWVar.volumeEffetti * 0.2, GlobalHWVar.volumeEffetti * 0.2, GlobalHWVar.volumeEffetti * 0.2], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundInterazioni, GlobalHWVar.canaliSoundSottofondoAmbientale, GlobalHWVar.canaleSoundBattitoCardiaco], [GlobalHWVar.volumeEffetti * 0.1, GlobalHWVar.volumeEffetti * 0.1, GlobalHWVar.volumeEffetti * 0.1], False)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundInterazioni, GlobalHWVar.canaliSoundSottofondoAmbientale, GlobalHWVar.canaleSoundBattitoCardiaco], [0, 0, 0], False)
        GlobalHWVar.canaleSoundInterazioni.stop()
        GlobalHWVar.canaliSoundSottofondoAmbientale.arresta()
        GlobalHWVar.canaleSoundBattitoCardiaco.stop()
        GlobalHWVar.canaleSoundInterazioni.set_volume(GlobalHWVar.volumeEffetti)
        GlobalHWVar.canaliSoundSottofondoAmbientale.settaVolume(GlobalHWVar.volumeEffetti)
        GlobalHWVar.canaleSoundBattitoCardiaco.set_volume(GlobalHWVar.volumeEffetti)
        i = 0
        while i < 30:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        stanza = GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]
        cambiosta = True
        carim = True
        caricaTutto = True
        nonMostrarePersonaggio = True

    return x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire
