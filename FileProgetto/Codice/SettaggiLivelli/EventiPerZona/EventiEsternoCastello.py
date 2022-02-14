# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.GestioneMenu.MenuDialoghi as MenuDialoghi
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj
import Codice.GestioneNemiciPersonaggi.NemicoObj as NemicoObj


def gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco):
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoUscitaLabirinto"] and stanza == GlobalGameVar.dictStanze["esternoCastello1"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoEsternoCastello"] and stanza == GlobalGameVar.dictStanze["esternoCastello2"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["convintoServoCastelloAperturaCancello"] and stanza == GlobalGameVar.dictStanze["esternoCastello2"]:
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["esternoCastello2"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["apertoCancelloPrincipaleCastello"] and stanza == GlobalGameVar.dictStanze["esternoCastello2"]:
        servoGiratoVersoDiTe = False
        for personaggio in listaPersonaggi:
            if personaggio.tipoId == "ServoLancia-3":
                if personaggio.direzione == "w":
                    servoGiratoVersoDiTe = True
                break
        if servoGiratoVersoDiTe:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "ServoLancia-3", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
            evitaTurnoDiColco = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["diaolgoServoLanciaDopoAperturaCancello"] and stanza == GlobalGameVar.dictStanze["esternoCastello2"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipoId == "ServoLancia-3" and personaggio.x == GlobalHWVar.gpx * 18 and personaggio.y == GlobalHWVar.gpy * 15:
                personaggioArrivato = True
                break
        if personaggioArrivato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.tipoId == "ServoLancia-3":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.tipoId == "ServoLancia-3":
                    listaPersonaggi.remove(personaggio)
                    break
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["servoLanciaAndatoInEsternoCastello4"] and stanza == GlobalGameVar.dictStanze["esternoCastello4"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipoId == "ServoLancia-3" and personaggio.x == GlobalHWVar.gpx * 16 and personaggio.y == GlobalHWVar.gpy * 15:
                personaggioArrivato = True
                break
        if personaggioArrivato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.tipoId == "ServoLancia-3":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.tipoId == "ServoLancia-3":
                    listaPersonaggi.remove(personaggio)
                    break
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["servoLanciaAndatoInEsternoCastello5"] and stanza == GlobalGameVar.dictStanze["esternoCastello5"] and (x == GlobalHWVar.gpx * 9 or x == GlobalHWVar.gpx * 10) and y == GlobalHWVar.gpy * 13 and equipaggiamentoIndossato:
        if npers != 2:
            npers = 2
            avanzaIlTurnoSenzaMuoverti = True
            carim = True
            caricaTutto = True
        if not avanzaIlTurnoSenzaMuoverti and len(percorsoDaEseguire) == 0:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "ServoLancia-3", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
            percorsoDaEseguire = ["w"]
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoNotatoAscensore"] and stanza == GlobalGameVar.dictStanze["esternoCastello5"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoUscitaCastello"] and stanza == GlobalGameVar.dictStanze["esternoCastello1"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoUscitaInternoCastello20Fuggendo"] and stanza == GlobalGameVar.dictStanze["esternoCastello1"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Neil-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["monologoUscitaInternoCastello20Fuggendo"]:
            GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni)
            GlobalHWVar.canaleSoundCanzone.play(canzone, -1)
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
            percorsoDaEseguire = []
            i = 0
            while i < 44:
                percorsoDaEseguire.append("d")
                i += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoNeilFuoriDalCastelloDuranteLaFuga"] and stanza == GlobalGameVar.dictStanze["esternoCastello3"] and x == GlobalHWVar.gpx * 17 and y == GlobalHWVar.gpy * 6:
        GlobalHWVar.canaleSoundPassiRallo.stop()
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["dialogoNeilFuoriDalCastelloDuranteLaFuga"]:
            percorsoDaEseguire = ["a"]
            carim = True
            percorsoPersonaggio = ["d"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 6, "d", "Neil-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 3, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 10, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 6, "d", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 2, "d", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 3, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 5, "d", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 7, "d", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 9, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 10, "d", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 11, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 5, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 7, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 10, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 3, "d", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 9, "d", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 11, "d", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivatoAlBordoLagoCastelloDuranteLaFuga"] and stanza == GlobalGameVar.dictStanze["esternoCastello3"] and x == GlobalHWVar.gpx * 16 and y == GlobalHWVar.gpy * 6:
        GlobalHWVar.canaleSoundPassiRallo.stop()
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Neil-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoNeilBordoLagoDuranteLaFuga"] and stanza == GlobalGameVar.dictStanze["esternoCastello3"]:
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "Neil":
                if personaggio.x == GlobalHWVar.gpx * 8 and personaggio.y == GlobalHWVar.gpy * 6:
                    avanzamentoStoria += 1
                break
        avanzaIlTurnoSenzaMuoverti = True
        evitaTurnoDiColco = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["avvicinatoNeilBordoLagoDuranteLaFuga"] and stanza == GlobalGameVar.dictStanze["esternoCastello3"]:
        if x == GlobalHWVar.gpx * 16 and y == GlobalHWVar.gpy * 6:
            percorsoDaEseguire = ["d"]
        else:
            GlobalHWVar.canaleSoundPassiRallo.stop()
            avanzamentoStoria += 1
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 6, "s", "OggettoSaraNelLago-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            nrob = 1
            nonMostrarePersonaggio = True
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["buttataNelLagoDuranteLaFuga"] and stanza == GlobalGameVar.dictStanze["esternoCastello3"]:
        GlobalHWVar.canaleSoundPassiNemiciPersonaggi.play(GlobalSndVar.rumoreMovimentoNemici)
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreTuffoLago)
        if GlobalHWVar.volumeCanzoni <= 0:
            i = 0
            while i < 1:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [0], False, posizioneCanaleMusica=0)
        GlobalHWVar.canaleSoundCanzone.stop()
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
        GlobalHWVar.aggiornaSchermo()
        GlobalHWVar.canaliSoundSottofondoAmbientale.arresta()
        i = 0
        while i < 50:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["palazzoDiRod2"]
        nonMostrarePersonaggio = False
        cambiosta = True
        carim = True
        aggiornaImgEquip = True
        caricaTutto = True

    return x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco
