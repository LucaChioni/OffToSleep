# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche
import Codice.GestioneMenu.MenuDialoghi as MenuDialoghi
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj


def gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire):
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["aggiornatoStanzaPerDistruzioneDelMondo1"] and stanza == GlobalGameVar.dictStanze["stanzaEsplosa"]:
        xSpawn = GlobalHWVar.gpx * 15
        ySpawn = GlobalHWVar.gpy * 9
        nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "concludi", nonMostrarePersonaggio, carim, caricaTutto)
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoDieciAnniAspettandoRenéSulCalcolatore"] and stanza == GlobalGameVar.dictStanze["stanzaEsplosa"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo1NotatoTuttoDistruttoDopoDieciAnniDiAttesaPerRené"] and stanza == GlobalGameVar.dictStanze["stanzaEsplosa"]:
        # npers: 1=d, 2=a, 3=w, 4=s
        if npers == 3:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            npers = 2
            avanzaIlTurnoSenzaMuoverti = True
            carim = True
            caricaTutto = True
        elif npers == 2:
            i = 0
            while i < 10:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            npers = 1
            avanzaIlTurnoSenzaMuoverti = True
            carim = True
            caricaTutto = True
        elif npers == 1:
            i = 0
            while i < 10:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            npers = 4
            avanzaIlTurnoSenzaMuoverti = True
            carim = True
            caricaTutto = True
        elif npers == 4:
            screen = GlobalHWVar.schermo.copy().convert()
            i = 0
            while i < 10:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
            if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["monologo1NotatoTuttoDistruttoDopoDieciAnniDiAttesaPerRené"]:
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
                GlobalHWVar.aggiornaSchermo()
                i = 0
                while i < 5:
                    pygame.time.wait(100)
                    inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                    i += 1
                xSpawn = GlobalHWVar.gpx * 15
                ySpawn = GlobalHWVar.gpy * 9
                nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "s", "avvia", nonMostrarePersonaggio, carim, caricaTutto)
                nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "s", "compari", nonMostrarePersonaggio, carim, caricaTutto)
                stanza = GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]
                cambiosta = True
                carim = True
                caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoUnAnno2AspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"] and stanza == GlobalGameVar.dictStanze["stanzaEsplosa"]:
        xSpawn = GlobalHWVar.gpx * 15
        ySpawn = GlobalHWVar.gpy * 9
        nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "concludi", nonMostrarePersonaggio, carim, caricaTutto)
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["aggiornatoStanzaPerDistruzioneDelMondo2"] and stanza == GlobalGameVar.dictStanze["stanzaEsplosa"]:
        screen = GlobalHWVar.schermo.copy().convert()
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["aggiornatoStanzaPerDistruzioneDelMondo2"]:
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            xSpawn = GlobalHWVar.gpx * 15
            ySpawn = GlobalHWVar.gpy * 9
            nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "avvia", nonMostrarePersonaggio, carim, caricaTutto)
            nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "compari", nonMostrarePersonaggio, carim, caricaTutto)
            stanza = GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]
            cambiosta = True
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoUnMese2AspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"] and stanza == GlobalGameVar.dictStanze["stanzaEsplosa"]:
        xSpawn = GlobalHWVar.gpx * 15
        ySpawn = GlobalHWVar.gpy * 9
        nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "concludi", nonMostrarePersonaggio, carim, caricaTutto)
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["aggiornatoStanzaPerDistruzioneDelMondo3"] and stanza == GlobalGameVar.dictStanze["stanzaEsplosa"]:
        screen = GlobalHWVar.schermo.copy().convert()
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["aggiornatoStanzaPerDistruzioneDelMondo3"]:
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            xSpawn = GlobalHWVar.gpx * 15
            ySpawn = GlobalHWVar.gpy * 9
            nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "avvia", nonMostrarePersonaggio, carim, caricaTutto)
            nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "compari", nonMostrarePersonaggio, carim, caricaTutto)
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "concludi", nonMostrarePersonaggio, carim, caricaTutto, personaggioGiaNelloScreen=True)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroQuindiciGiorniAspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"] and stanza == GlobalGameVar.dictStanze["stanzaEsplosa"]:
        screen = GlobalHWVar.schermo.copy().convert()
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroQuindiciGiorniAspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"]:
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            xSpawn = GlobalHWVar.gpx * 15
            ySpawn = GlobalHWVar.gpy * 9
            nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "avvia", nonMostrarePersonaggio, carim, caricaTutto)
            nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "compari", nonMostrarePersonaggio, carim, caricaTutto)
            stanza = GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]
            cambiosta = True
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["missileNucleareScoppiato"] and stanza == GlobalGameVar.dictStanze["stanzaEsplosa"]:
        if GlobalHWVar.nonAggiornareSchermo:
            GlobalHWVar.nonAggiornareSchermo = False
        i = 0
        while i < 100:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        screen = GlobalHWVar.schermo.copy().convert()
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, (54, 35, 21))
        vetImg = []
        i = 0
        while i <= 100:
            image = pygame.Surface((GlobalHWVar.gsx, GlobalHWVar.gsy), flags=pygame.SRCALPHA)
            image.fill((54, 35, 21, 255 - (i * 2.5)))
            vetImg.append(image.convert_alpha(GlobalHWVar.schermo))
            i += 1
        i = 0
        while i < len(vetImg):
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(vetImg[i], (0, 0))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i += 1
        GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        GlobalHWVar.aggiornaSchermo()
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["conclusioneAnimazioneDistruzionePostScoppioMissile"] and stanza == GlobalGameVar.dictStanze["stanzaEsplosa"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostFineDelMondo1"] and stanza == GlobalGameVar.dictStanze["stanzaEsplosa"]:
        # npers: 1=d, 2=a, 3=w, 4=s
        if npers == 1:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            npers = 2
            avanzaIlTurnoSenzaMuoverti = True
            carim = True
            caricaTutto = True
        elif npers == 2:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            npers = 3
            avanzaIlTurnoSenzaMuoverti = True
            carim = True
            caricaTutto = True
        elif npers == 3:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            npers = 4
            avanzaIlTurnoSenzaMuoverti = True
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
            if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["monologoPostFineDelMondo1"]:
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
                GlobalHWVar.aggiornaSchermo()
                i = 0
                while i < 5:
                    pygame.time.wait(100)
                    inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                    i += 1
                xSpawn = GlobalHWVar.gpx * 15
                ySpawn = GlobalHWVar.gpy * 9
                nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "s", "avvia", nonMostrarePersonaggio, carim, caricaTutto)
                nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "s", "compari", nonMostrarePersonaggio, carim, caricaTutto)
                stanza = GlobalGameVar.dictStanze["stanzaEsplosa"]
                cambiosta = True
                carim = True
                caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostFineDelMondo2"] and stanza == GlobalGameVar.dictStanze["stanzaEsplosa"]:
        xSpawn = GlobalHWVar.gpx * 15
        ySpawn = GlobalHWVar.gpy * 9
        nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "s", "concludi", nonMostrarePersonaggio, carim, caricaTutto)
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["andatoACasaPerVedereLoScoppioDelMissile"] and stanza == GlobalGameVar.dictStanze["stanzaEsplosa"]:
        # npers: 1=d, 2=a, 3=w, 4=s
        if npers == 4:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            npers = 3
            avanzaIlTurnoSenzaMuoverti = True
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
            if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["andatoACasaPerVedereLoScoppioDelMissile"]:
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
                GlobalHWVar.aggiornaSchermo()
                i = 0
                while i < 5:
                    pygame.time.wait(100)
                    inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                    i += 1
                xSpawn = GlobalHWVar.gpx * 18
                ySpawn = GlobalHWVar.gpy * 9
                nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "avvia", nonMostrarePersonaggio, carim, caricaTutto)
                nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "compari", nonMostrarePersonaggio, carim, caricaTutto)
                stanza = GlobalGameVar.dictStanze["casaHansSara2"]
                cambiosta = True
                carim = True
                caricaTutto = True

    return x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire
