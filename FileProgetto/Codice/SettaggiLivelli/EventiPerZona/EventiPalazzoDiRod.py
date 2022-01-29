# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.GestioneMenu.MenuDialoghi as MenuDialoghi
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj


def gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco):
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
                personaggio.girati("d")
                break
        monetePossedute -= GlobalGameVar.monetePerGliStumentiPerNeil
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dateMonetePerStrumentiPerStudiareImpo"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod5"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True

    return x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco
