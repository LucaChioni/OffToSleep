# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.GestioneMenu.MenuDialoghi as MenuDialoghi
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj


def gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire):
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoUscitoDalPalazzoDiRod"] and stanza == GlobalGameVar.dictStanze["tunnelDiRod1"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoUtilizzoLevaTunnelDiRod"] and stanza == GlobalGameVar.dictStanze["tunnelDiRod3"]:
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["tunnelDiRod3"]
        cambiosta = True
        carim = True
        caricaTutto = True
        avanzaIlTurnoSenzaMuoverti = True
        evitaTurnoDiColco = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoRenéDaAvampostoDiRod2PreFineDelMondo"] and stanza == GlobalGameVar.dictStanze["tunnelDiRod3"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "BibliotecarioOperato":
                if personaggio.x == GlobalHWVar.gpx * 12 and personaggio.y == GlobalHWVar.gpy * 2:
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["tunnelDiRod3"] and personaggio.tipo == "BibliotecarioOperato":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["tunnelDiRod3"] and personaggio.tipo == "BibliotecarioOperato":
                    listaPersonaggi.remove(personaggio)
                    break
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoRenéDaTunnelDiRod3PreFineDelMondo"] and stanza == GlobalGameVar.dictStanze["tunnelDiRod2"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "BibliotecarioOperato":
                if personaggio.x == GlobalHWVar.gpx * 13 and personaggio.y == GlobalHWVar.gpy * 2:
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["tunnelDiRod2"] and personaggio.tipo == "BibliotecarioOperato":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["tunnelDiRod2"] and personaggio.tipo == "BibliotecarioOperato":
                    listaPersonaggi.remove(personaggio)
                    break
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoRenéDaTunnelDiRod2PreFineDelMondo"] and stanza == GlobalGameVar.dictStanze["tunnelDiRod1"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "BibliotecarioOperato":
                if personaggio.x == GlobalHWVar.gpx * 9 and personaggio.y == GlobalHWVar.gpy * 2:
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["tunnelDiRod1"] and personaggio.tipo == "BibliotecarioOperato":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["tunnelDiRod1"] and personaggio.tipo == "BibliotecarioOperato":
                    listaPersonaggi.remove(personaggio)
                    break
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True

    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and stanza == GlobalGameVar.dictStanze["tunnelDiRod3"]:
        tiratoLevaTunnelDiRod = False
        i = 0
        while i < len(listaAvanzamentoDialoghi):
            if listaAvanzamentoDialoghi[i] == "OggettoLevaTunnelDiRod-0":
                if listaAvanzamentoDialoghi[i + 1] == 1:
                    listaAvanzamentoDialoghi[i + 1] = 2
                    tiratoLevaTunnelDiRod = True
                break
            i += 2
        if tiratoLevaTunnelDiRod:
            # aggiorno avanzamento dialogo della leva
            for personaggio in listaPersonaggi:
                if personaggio.tipoId == "OggettoLevaTunnelDiRod-0":
                    personaggio.avanzamentoDialogo = 2
                    break
            stanza = GlobalGameVar.dictStanze["tunnelDiRod3"]
            cambiosta = True
            carim = True
            caricaTutto = True
            avanzaIlTurnoSenzaMuoverti = True
            evitaTurnoDiColco = True

    return x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire
