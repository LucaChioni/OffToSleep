# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.GestioneMenu.MenuDialoghi as MenuDialoghi
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj
import Codice.GestioneNemiciPersonaggi.NemicoObj as NemicoObj


def gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco):
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoCasaHansSara2"] and stanza == GlobalGameVar.dictStanze["forestaCadetta1"]:
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
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ingressoForestaCadettaSara"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
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
        if dati[132] > 1:
            dati[132] = 1
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

    return x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco
