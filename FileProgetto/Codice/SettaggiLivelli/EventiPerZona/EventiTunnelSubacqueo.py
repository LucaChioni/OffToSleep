# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.GestioneMenu.MenuDialoghi as MenuDialoghi
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj


def gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire):
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoVistoIngressoTunnelSubaqueoAperto"] and stanza == GlobalGameVar.dictStanze["tunnelSubacqueo1"] and x == GlobalHWVar.gpx * 15:
        # npers: 1=d, 2=a, 3=w, 4=s
        if npers == 1:
            if y == GlobalHWVar.gpx * 8:
                npers = 3
                carim = True
                caricaTutto = True
            elif y == GlobalHWVar.gpx * 9:
                npers = 3
                carim = True
                caricaTutto = True
            elif y == GlobalHWVar.gpx * 10:
                npers = 4
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
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostApparizioneStanzaNelCalcolatore3"] and stanza == GlobalGameVar.dictStanze["tunnelSubacqueo1"] and x == GlobalHWVar.gpx * 11:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoVistoPortaLaboratorioAggiustata"] and stanza == GlobalGameVar.dictStanze["tunnelSubacqueo1"]:
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
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoConfusoSuComeOltrepassareLaPortaDelLaboratorio"] and stanza == GlobalGameVar.dictStanze["tunnelSubacqueo1"]:
        avanzamentoStoria += 1
        # npers: 1=d, 2=a, 3=w, 4=s
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        npers = 2
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["NeilUscitoDaInternoCastello8PostAvvioSequenzaNelCalcolatore"] and stanza == GlobalGameVar.dictStanze["tunnelSubacqueo1"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipoId == "Neil-0":
                if personaggio.x == GlobalHWVar.gpx * 29 and personaggio.y == GlobalHWVar.gpy * 9:
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.tipoId == "Neil-0":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.tipoId == "Neil-0":
                    listaPersonaggi.remove(personaggio)
                    break
            carim = True
            caricaTutto = True
            avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["NeilUscitoDaTunnelSubaqueo1PostAvvioSequenzaNelCalcolatore"] and stanza == GlobalGameVar.dictStanze["tunnelSubacqueo2"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipoId == "Neil-0":
                if personaggio.x == GlobalHWVar.gpx * 29 and personaggio.y == GlobalHWVar.gpy * 9:
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.tipoId == "Neil-0":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.tipoId == "Neil-0":
                    listaPersonaggi.remove(personaggio)
                    break
            carim = True
            caricaTutto = True
            avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo2PostSecondaSparizioneDiNeilDalLaboratorio"] and stanza == GlobalGameVar.dictStanze["tunnelSubacqueo1"] and x == GlobalHWVar.gpx * 27:
        personaggioCreato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "Bibliotecario":
                personaggioCreato = True
                break
        if not personaggioCreato:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoPortaLaboratorioSegretoDiNeil)
            percorsoPersonaggio = ["d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 9, "d", "Bibliotecario-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            GlobalHWVar.canaleSoundPassiPersonaggi.play(GlobalSndVar.rumoreMovimentoPersonaggi)
            carim = True
            caricaTutto = True
        else:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivatoRenéNelTunnelSubacqueo1"] and stanza == GlobalGameVar.dictStanze["tunnelSubacqueo1"]:
        # npers: 1=d, 2=a, 3=w, 4=s
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "Bibliotecario":
                if personaggio.x >= GlobalHWVar.gpx * 25:
                    if x == GlobalHWVar.gpx * 27 and y == GlobalHWVar.gpy * 9 and len(percorsoDaEseguire) == 0:
                        percorsoDaEseguire = ["s"]
                    elif x == GlobalHWVar.gpx * 27 and y == GlobalHWVar.gpy * 8 and npers != 4:
                        npers = 4
                        carim = True
                        caricaTutto = True
                    elif x == GlobalHWVar.gpx * 27 and y == GlobalHWVar.gpy * 10 and npers != 3:
                        npers = 3
                        carim = True
                        caricaTutto = True
                    elif personaggio.x == GlobalHWVar.gpx * 29 and personaggio.y == GlobalHWVar.gpy * 9:
                        personaggioArrivato = True
                break
        if personaggioArrivato:
            if npers != 1:
                npers = 1
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["tunnelSubacqueo1"] and personaggio.tipo == "Bibliotecario":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["tunnelSubacqueo1"] and personaggio.tipo == "Bibliotecario":
                    listaPersonaggi.remove(personaggio)
                    break
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
        elif len(percorsoDaEseguire) == 0:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivatoRenéNelTunnelSubacqueo2"] and stanza == GlobalGameVar.dictStanze["tunnelSubacqueo2"]:
        # npers: 1=d, 2=a, 3=w, 4=s
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "Bibliotecario":
                if personaggio.x == GlobalHWVar.gpx * 29 and personaggio.y == GlobalHWVar.gpy * 9:
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["tunnelSubacqueo2"] and personaggio.tipo == "Bibliotecario":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["tunnelSubacqueo2"] and personaggio.tipo == "Bibliotecario":
                    listaPersonaggi.remove(personaggio)
                    break
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoRenéDaLaboratorioDiNeilPreFineDelMondo"] and stanza == GlobalGameVar.dictStanze["tunnelSubacqueo2"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "BibliotecarioOperato":
                if personaggio.x == GlobalHWVar.gpx * 2 and personaggio.y == GlobalHWVar.gpy * 9:
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["tunnelSubacqueo2"] and personaggio.tipo == "BibliotecarioOperato":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["tunnelSubacqueo2"] and personaggio.tipo == "BibliotecarioOperato":
                    listaPersonaggi.remove(personaggio)
                    break
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoRenéDaTunnelSubaqueo2PreFineDelMondo"] and stanza == GlobalGameVar.dictStanze["tunnelSubacqueo1"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "BibliotecarioOperato":
                if personaggio.x == GlobalHWVar.gpx * 2 and personaggio.y == GlobalHWVar.gpy * 9:
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoPortaLaboratorioSegretoDiNeil)
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["tunnelSubacqueo1"] and personaggio.tipo == "BibliotecarioOperato":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["tunnelSubacqueo1"] and personaggio.tipo == "BibliotecarioOperato":
                    listaPersonaggi.remove(personaggio)
                    break
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True

    return x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire
