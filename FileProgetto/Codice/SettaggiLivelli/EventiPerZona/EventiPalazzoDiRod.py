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


def gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire):
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoMetaPassoMontano"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod1"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "Mercante" and personaggio.x == GlobalHWVar.gpx * 19 and personaggio.y == GlobalHWVar.gpy * 12 and personaggio.direzione == "s":
                personaggioArrivato = True
                break
        if personaggioArrivato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["palazzoDiRod1"] and personaggio.tipo == "Mercante":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["palazzoDiRod1"] and personaggio.tipo == "Mercante":
                    listaPersonaggi.remove(personaggio)
                    break
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumorePortoniCambioStanza)
        avanzaIlTurnoSenzaMuoverti = True
        evitaTurnoDiColco = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["rodEntratoNelPalazzo"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod1"]:
        i = 0
        while i < 15:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["arrivoCasaUfficiale"]:
            GlobalHWVar.canaleSoundCanzone.play(canzone, -1)
            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [GlobalHWVar.volumeCanzoni], False, posizioneCanaleMusica=0)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPreBussataPalazzo"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod1"]:
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreBussareCitta)
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Mercante-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["bussatoAlPalazzoDiRodConDialogo"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod1"]:
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["palazzoDiRod2"]
        nrob = 3
        cambiosta = True
        carim = True
        caricaTutto = True
        avanzaIlTurnoSenzaMuoverti = True
        evitaTurnoDiColco = True
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumorePortoniCambioStanza)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["entratoInPalazzoDiRod"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod2"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Mercante-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRodDopoEssereEntratoNelPalazzo"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod2"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["palazzoDiRod2"] and personaggio.tipo == "Mercante":
                if personaggio.numeroMovimento == len(personaggio.percorso) - 1:
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            avanzamentoStoria += 1
        avanzaIlTurnoSenzaMuoverti = True
        evitaTurnoDiColco = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["presiStrumentiPerStudiareImpo"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod2"]:
        # azzero avanzamentoDialogo di Rod
        for personaggio in listaPersonaggiTotali:
            if personaggio.tipo == "Mercante" and personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["palazzoDiRod2"]:
                personaggio.avanzamentoDialogo = 0
                break
        i = 0
        while i < len(listaAvanzamentoDialoghi):
            if listaAvanzamentoDialoghi[i] == "Mercante-0":
                listaAvanzamentoDialoghi[i + 1] = 0
                break
            i += 2
        # giro Rod verso i fogli
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "Mercante":
                personaggio.percorso = ["dGira", "mantieniPosizione"]
                personaggio.numeroMovimento = 0
                break
        monetePossedute -= GlobalGameVar.monetePerGliStumentiPerNeil
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dateMonetePerStrumentiPerStudiareImpo"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod2"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Mercante-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRodAperturaRetroPalazzo"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod2"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Mercante-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoConclusivoRodAlPalazzo"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod5"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod2"]:
        if not GlobalHWVar.canaleSoundInterazioni.get_busy():
            GlobalHWVar.canaleSoundInterazioni.set_volume(0)
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreScorrimentoMatitaEnigmi, -1)
            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundInterazioni], [GlobalHWVar.volumeEffetti], False, posizioneCanaleMusica=0)
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRodSuImpoNonVivi"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod2"]:
        if GlobalHWVar.canaleSoundInterazioni.get_busy():
            GlobalHWVar.canaleSoundInterazioni.stop()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRodCercandoSaraAlPalazzo1"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod2"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        if npers == 1:
            npers = 2
            avanzaIlTurnoSenzaMuoverti = True
            carim = True
            caricaTutto = True
        elif npers == 2:
            npers = 4
            avanzaIlTurnoSenzaMuoverti = True
            carim = True
            caricaTutto = True
        elif npers == 4:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRodCercandoSaraAlPalazzo2"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod5"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoFreddoNonPercepitoPassoMontanoPostTempoBloccato"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod1"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoPalazzo1PostEsplosioneVulcano"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod2"]:
        # azzero avanzamentoDialogo di Rod
        for personaggio in listaPersonaggiTotali:
            if personaggio.tipo == "Mercante":
                personaggio.avanzamentoDialogo = 0
                break
        i = 0
        while i < len(listaAvanzamentoDialoghi):
            if listaAvanzamentoDialoghi[i] == "Mercante-0":
                listaAvanzamentoDialoghi[i + 1] = 0
                break
            i += 2
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoEntrataPalazzoDiRodConTempoBloccato"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod3"] and x == GlobalHWVar.gpx * 17 and y == GlobalHWVar.gpy * 8:
        GlobalHWVar.canaleSoundPassiRallo.stop()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif GlobalGameVar.dictAvanzamentoStoria["monologoEntrataPalazzoDiRodConTempoBloccato"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoVistoLevaNelPalazzoDiRod"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod4"]:
        avanzamentoDialogoAmmassoImpo = 0
        i = 0
        while i < len(listaAvanzamentoDialoghi):
            if listaAvanzamentoDialoghi[i] == "OggettoMucchioImpo-0":
                avanzamentoDialogoAmmassoImpo = listaAvanzamentoDialoghi[i + 1]
                break
            i += 2
        if avanzamentoDialogoAmmassoImpo == 0 and x == GlobalHWVar.gpx * 16 and y == GlobalHWVar.gpy * 8:
            GlobalHWVar.canaleSoundPassiRallo.stop()
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoMucchioImpo-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
            if personaggio.avanzamentoDialogo == 1:
                percorsoDaEseguire = ["w", "d", "d", "d", "d", "w"]
            else:
                avanzaIlTurnoSenzaMuoverti = True
                evitaTurnoDiColco = True
        elif avanzamentoDialogoAmmassoImpo == 1 and x == GlobalHWVar.gpx * 20 and y == GlobalHWVar.gpy * 7 and npers == 3:
            GlobalHWVar.canaleSoundPassiRallo.stop()
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoMucchioImpo-0", stanza, avanzamentoStoria, False, avanzamentoDialogo=avanzamentoDialogoAmmassoImpo)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        elif avanzamentoDialogoAmmassoImpo >= 2:
            portaAperta = False
            i = 0
            while i < len(porte):
                if porte[i] == GlobalGameVar.dictStanze["palazzoDiRod4"] and porte[i + 1] == GlobalHWVar.gpx * 15 and porte[i + 2] == GlobalHWVar.gpx * 4:
                    portaAperta = porte[i + 3]
                    break
                i += 4
            if portaAperta:
                i = 0
                while i < 5:
                    pygame.time.wait(100)
                    inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                    i += 1
                personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
                avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
                caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tiratoLeva"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod4"]:
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["palazzoDiRod4"]
        cambiosta = True
        carim = True
        caricaTutto = True
        avanzaIlTurnoSenzaMuoverti = True
        evitaTurnoDiColco = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sbloccatoCaverna"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod4"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostAttaccoDiImpoOstile"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod1"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoRenéDaTunnelDiRod1PreFineDelMondo"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod5"]:
        avanzamentoStoria += 1
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumorePortoniCambioStanza)
        percorsoPersonaggio = ["d", "d", "d", "s", "d", "sGira", "dGira", "d", "d", "d", "d", "d", "d", "sGira", "dGira", "a", "a", "a", "a", "a", "dGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 5, "s", "MercanteFuturo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoRodDalPalazzoPreLancioMissile"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod5"]:
        personaggioArrivato = False
        personaggioAppenaCreato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "MercanteFuturo":
                if personaggio.x == GlobalHWVar.gpx * 14 and personaggio.y == GlobalHWVar.gpy * 5 and personaggio.direzione == "s":
                    personaggioAppenaCreato = True
                elif personaggio.x == GlobalHWVar.gpx * 18 and personaggio.y == GlobalHWVar.gpy * 6 and personaggio.direzione == "d":
                    i = 0
                    while i < 5:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                elif personaggio.x == GlobalHWVar.gpx * 18 and personaggio.y == GlobalHWVar.gpy * 6 and personaggio.direzione == "s":
                    personaggioArrivato = True
                break
        if personaggioAppenaCreato:
            i = 0
            while i < 2:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            GlobalHWVar.canaleSoundMelodieEventi.set_volume(0)
            GlobalHWVar.canaleSoundMelodieEventi.play(canzone, -1)
            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundMelodieEventi], [GlobalHWVar.volumeCanzoni], False, posizioneCanaleMusica=0)
            i = 0
            while i < 3:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            avanzaIlTurnoSenzaMuoverti = True
        elif personaggioArrivato:
            i = 0
            while i < 15:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "BibliotecarioOperato-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRenéRod1PreLancioMissile"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod5"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "MercanteFuturo":
                if personaggio.x == GlobalHWVar.gpx * 18 and personaggio.y == GlobalHWVar.gpy * 6 and personaggio.direzione == "s":
                    i = 0
                    while i < 5:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                elif personaggio.x == GlobalHWVar.gpx * 18 and personaggio.y == GlobalHWVar.gpy * 6 and personaggio.direzione == "d":
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            i = 0
            while i < 10:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "BibliotecarioOperato-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRenéRod2PreLancioMissile"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod5"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "MercanteFuturo":
                if personaggio.x == GlobalHWVar.gpx * 18 and personaggio.y == GlobalHWVar.gpy * 6 and personaggio.direzione == "d":
                    i = 0
                    while i < 5:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                elif personaggio.x == GlobalHWVar.gpx * 24 and personaggio.y == GlobalHWVar.gpy * 6 and personaggio.direzione == "d":
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRod1PreLancioMissile"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod5"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "MercanteFuturo":
                if personaggio.x == GlobalHWVar.gpx * 24 and personaggio.y == GlobalHWVar.gpy * 6 and personaggio.direzione == "d":
                    i = 0
                    while i < 5:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                elif personaggio.x == GlobalHWVar.gpx * 24 and personaggio.y == GlobalHWVar.gpy * 6 and personaggio.direzione == "s":
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            i = 0
            while i < 2:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "BibliotecarioOperato-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRenéRod3PreLancioMissile"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod5"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "MercanteFuturo":
                if personaggio.x == GlobalHWVar.gpx * 24 and personaggio.y == GlobalHWVar.gpy * 6 and personaggio.direzione == "s":
                    i = 0
                    while i < 3:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                elif personaggio.x == GlobalHWVar.gpx * 24 and personaggio.y == GlobalHWVar.gpy * 6 and personaggio.direzione == "d":
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            screen = GlobalHWVar.schermo.copy()
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
            if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["dialogoRenéRod3PreLancioMissile"]:
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
                GlobalHWVar.aggiornaSchermo()
                i = 0
                while i < 10:
                    pygame.time.wait(100)
                    inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                    i += 1
                GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreSbloccoPorta)
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRod2PreLancioMissile"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod5"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "MercanteFuturo":
                if personaggio.x == GlobalHWVar.gpx * 20 and personaggio.y == GlobalHWVar.gpy * 6 and personaggio.direzione == "a" and npers != 1:
                    # npers: 1=d, 2=a, 3=w, 4=s
                    npers = 1
                    carim = True
                    caricaTutto = True
                elif personaggio.x == GlobalHWVar.gpx * 19 and personaggio.y == GlobalHWVar.gpy * 6 and personaggio.direzione == "d":
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            avanzamentoStoria += 1
            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.9], False, posizioneCanaleMusica=0)
            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.8], False, posizioneCanaleMusica=0)
            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.7], False, posizioneCanaleMusica=0)
            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.6], False, posizioneCanaleMusica=0)
            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.5], False, posizioneCanaleMusica=0)
            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.4], False, posizioneCanaleMusica=0)
            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.3], False, posizioneCanaleMusica=0)
            # animazione lancio missile
            pathImgs = "Risorse/Immagini/Scenari/Stanza" + str(stanza) + "/Animazioni/LancioMissile/"
            coordinateImgAnimata = (0, 0)
            dimensioniImgAnimata = (GlobalHWVar.gsx, GlobalHWVar.gsy)
            listaAudio = [0, GlobalSndVar.rumoreLancioMissile]
            FunzioniGraficheGeneriche.animaEvento(pathImgs, coordinateImgAnimata, dimensioniImgAnimata, listaAudio, tuttoSchermo=True, battito=69)
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["avvioLancioMissileNucleare"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod5"]:
        i = 0
        while i < 100:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        # animazione esplosione missile
        pathImgs = "Risorse/Immagini/Scenari/Stanza" + str(stanza) + "/Animazioni/EsplosioneMissile/"
        coordinateImgAnimata = (0, 0)
        dimensioniImgAnimata = (GlobalHWVar.gsx, GlobalHWVar.gsy)
        listaAudio = [24, GlobalSndVar.rumoreEsplosioneMissile]
        FunzioniGraficheGeneriche.animaEvento(pathImgs, coordinateImgAnimata, dimensioniImgAnimata, listaAudio, tuttoSchermo=True, battito=145)
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, (54, 35, 21))
        GlobalHWVar.aggiornaSchermo()
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["stanzaEsplosa"]
        cambiosta = True
        carim = True
        caricaTutto = True
        GlobalHWVar.nonAggiornareSchermo = True

    return x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire
