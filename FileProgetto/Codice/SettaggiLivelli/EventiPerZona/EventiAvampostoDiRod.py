# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.GestioneMenu.MenuDialoghi as MenuDialoghi
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj


def gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire):
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoUscitaSelva"] and stanza == GlobalGameVar.dictStanze["avampostoDiRod1"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dateMonetePerMappaLabirinto"] and stanza == GlobalGameVar.dictStanze["avampostoDiRod1"]:
        monetePossedute -= GlobalGameVar.monetePerLaMappaDelLabirinto
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["rimosseMonetePerMappaLabirinto"] and stanza == GlobalGameVar.dictStanze["avampostoDiRod1"]:
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["avampostoDiRod1"] and personaggio.tipo == "Mercante":
                personaggio.numeroMovimento = 0
                personaggio.percorso = []

                vetNemiciSoloConXeY = []
                for personaggioTemp in listaPersonaggi:
                    if not (personaggio.x == personaggioTemp.x and personaggio.y == personaggioTemp.y):
                        vetNemiciSoloConXeY.append(personaggio.x)
                        vetNemiciSoloConXeY.append(personaggio.y)
                vetNemiciSoloConXeY.append(x)
                vetNemiciSoloConXeY.append(y)
                vetNemiciSoloConXeY.append(rx)
                vetNemiciSoloConXeY.append(ry)
                if rx == GlobalHWVar.gpx * 6 and ry == GlobalHWVar.gpy * 5:
                    xDestinazione = GlobalHWVar.gpx * 6
                    yDestinazione = GlobalHWVar.gpy * 6
                else:
                    xDestinazione = GlobalHWVar.gpx * 6
                    yDestinazione = GlobalHWVar.gpy * 5
                percorsoTrovato = GenericFunc.pathFinding(personaggio.x, personaggio.y, xDestinazione, yDestinazione, vetNemiciSoloConXeY, casevisteEntrateIncluse)
                if percorsoTrovato and percorsoTrovato != "arrivato" and len(percorsoTrovato) >= 4 and (percorsoTrovato[len(percorsoTrovato) - 4] != personaggio.x or percorsoTrovato[len(percorsoTrovato) - 3] != personaggio.y):
                    personaggio.percorso.append("sGira")
                    xVirtuale = personaggio.x
                    yVirtuale = personaggio.y
                    i = len(percorsoTrovato) - 2
                    while i >= 0:
                        if percorsoTrovato[i] > xVirtuale:
                            personaggio.percorso.append("d")
                        elif percorsoTrovato[i] < xVirtuale:
                            personaggio.percorso.append("a")
                        elif percorsoTrovato[i + 1] > yVirtuale:
                            personaggio.percorso.append("s")
                        elif percorsoTrovato[i + 1] < yVirtuale:
                            personaggio.percorso.append("w")
                        xVirtuale = percorsoTrovato[i]
                        yVirtuale = percorsoTrovato[i + 1]
                        i -= 2
                    if xVirtuale == GlobalHWVar.gpx * 5 and yVirtuale == GlobalHWVar.gpy * 5:
                        personaggio.percorso.append("d")
                        personaggio.percorso.append("mantieniPosizione")
                    elif xVirtuale == GlobalHWVar.gpx * 6 and yVirtuale == GlobalHWVar.gpy * 6:
                        personaggio.percorso.append("w")
                        personaggio.percorso.append("dGira")
                        personaggio.percorso.append("mantieniPosizione")
                    elif xVirtuale == GlobalHWVar.gpx * 5 and yVirtuale == GlobalHWVar.gpy * 6:
                        personaggio.percorso.append("d")
                        personaggio.percorso.append("mantieniPosizione")
                    elif xVirtuale == GlobalHWVar.gpx * 6 and yVirtuale == GlobalHWVar.gpy * 7:
                        personaggio.percorso.append("w")
                        personaggio.percorso.append("dGira")
                        personaggio.percorso.append("mantieniPosizione")
                else:
                    print ("Percorso Mercante verso altro tavolo non trovato")
                break
        avanzamentoStoria += 1
        avanzaIlTurnoSenzaMuoverti = True
        evitaTurnoDiColco = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["messaMappaLabirintoSulTavolo"] and stanza == GlobalGameVar.dictStanze["avampostoDiRod1"]:
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoRaccoltaOggetto)
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["riprodottoSuonoMappaLabirintoSulTavolo"] and stanza == GlobalGameVar.dictStanze["avampostoDiRod1"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["avampostoDiRod1"] and personaggio.tipo == "Mercante":
                if personaggio.numeroMovimento == len(personaggio.percorso) - 1:
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            avanzamentoStoria += 1
        avanzaIlTurnoSenzaMuoverti = True
        evitaTurnoDiColco = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["copiataMappaLabirinto"] and stanza == GlobalGameVar.dictStanze["avampostoDiRod1"]:
        for personaggio in listaPersonaggiTotali:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["avampostoDiRod1"] and personaggio.tipo == "OggettoTavoloMappaLabirinto":
                listaPersonaggiTotali.remove(personaggio)
                break
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["avampostoDiRod1"] and personaggio.tipo == "OggettoTavoloMappaLabirinto":
                listaPersonaggi.remove(personaggio)
                break
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 9, "s", "OggettoEnigmaLabirinto-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggiTotali.append(personaggio)
        listaPersonaggi.append(personaggio)
        avanzamentoStoria += 1
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["risoltoEnigmaMappaLabirinto"] and stanza == GlobalGameVar.dictStanze["avampostoDiRod1"]:
        for personaggio in listaPersonaggiTotali:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["avampostoDiRod1"] and personaggio.tipo == "OggettoEnigmaLabirinto":
                listaPersonaggiTotali.remove(personaggio)
                break
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["avampostoDiRod1"] and personaggio.tipo == "OggettoEnigmaLabirinto":
                listaPersonaggi.remove(personaggio)
                break
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gpx * 7, GlobalHWVar.gpy * 9, "s", "OggettoTavoloMappaLabirinto-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggiTotali.append(personaggio)
        listaPersonaggi.append(personaggio)
        avanzamentoStoria += 1
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["eliminatoPersonaggioOggettoPerEnigmaMappaLabirinto"] and stanza == GlobalGameVar.dictStanze["avampostoDiRod1"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoMetaScorciatoiaLabirinto"] and stanza == GlobalGameVar.dictStanze["avampostoDiRod2"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoRetroAvampostoRod"] and stanza == GlobalGameVar.dictStanze["avampostoDiRod3"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["trovatoChiaveAvampostoDiRod"] and stanza == GlobalGameVar.dictStanze["avampostoDiRod1"]:
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostEsplosioneDelVulcano2"] and (stanza == GlobalGameVar.dictStanze["avampostoDiRod1"] or stanza == GlobalGameVar.dictStanze["avampostoDiRod2"]):
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True

    return x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire
