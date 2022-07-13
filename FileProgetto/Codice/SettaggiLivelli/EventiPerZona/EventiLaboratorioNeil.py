# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.CaricaFileProgetto as CaricaFileProgetto
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche
import Codice.GestioneMenu.MenuDialoghi as MenuDialoghi
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj


def gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, porte, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, casellePercorribiliPorteEscluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire):
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoTunnelSubacqueo"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        GlobalHWVar.canaleSoundPassiRallo.stop()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoLaboratorioNeil"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"] and x == GlobalHWVar.gpx * 8:
        GlobalHWVar.canaleSoundPassiRallo.stop()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoNotatoCellaDiNeil"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        if x == GlobalHWVar.gpx * 8 and len(percorsoDaEseguire) == 0:
            if y == GlobalHWVar.gpy * 8:
                percorsoDaEseguire = ["d", "d", "d", "d", "d", "d", "d", "d", "d", "s", "d", "d", "d", "d"]
            elif y == GlobalHWVar.gpy * 9 or y == GlobalHWVar.gpy * 10:
                percorsoDaEseguire = ["d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d"]
            carim = True
            caricaTutto = True
        elif x == GlobalHWVar.gpx * 21:
            i = 0
            while i < 10:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoCellaNeil-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["interazioneConCellaDiNeil1"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreBussareVetro)
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoCellaNeil-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["interazioneConCellaDiNeil1"]:
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 11, "s", "OggettoLetteraInvitoReneLaboratorio-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["lettoLetteraInvitoReneLaboratorio"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 6, "s", "OggettoAppuntiIstruzioniCalcolatoreLaboratorio-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 7, "s", "OggettoAppuntiGenerici0Laboratorio-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        avanzamentoStoria += 1
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["interagitoConCalcolatoreDiEventi"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        avanzamentoStoria += 1
        nonMostrarePersonaggio = True
        stanza = GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sedutaSulCalcolatore"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostSedutaSulCalcolatore"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        avanzamentoStoria += 1
        # animazione indossamento casco (abbassamento linea dell'orizzonte dentro il casco)
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreIndossareCasco)
        FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=False)
        yLineaOrizzonte = 0
        while yLineaOrizzonte <= 9:
            GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (0, GlobalHWVar.gpy * yLineaOrizzonte), (GlobalHWVar.gsx, GlobalHWVar.gpy * yLineaOrizzonte), GlobalHWVar.gpy // 5)
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockDisegno.tick(GlobalHWVar.fpsAnimazioni)
            yLineaOrizzonte += 1
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
        GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (0, GlobalHWVar.gpy * 9), (GlobalHWVar.gsx, GlobalHWVar.gpy * 9), GlobalHWVar.gpy // 5)
        GlobalHWVar.aggiornaSchermo()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.nonAggiornareSchermo = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["messoCascoCalcolatore"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        GlobalHWVar.nonAggiornareSchermo = False
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
        GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (0, GlobalHWVar.gpy * 9), (GlobalHWVar.gsx, GlobalHWVar.gpy * 9), GlobalHWVar.gpy // 5)
        GlobalHWVar.aggiornaSchermo()
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["messoCascoCalcolatore"]:
            GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (0, GlobalHWVar.gpy * 9), (GlobalHWVar.gsx, GlobalHWVar.gpy * 9), GlobalHWVar.gpy // 5)
            GlobalHWVar.aggiornaSchermo()
            i = 0
            while i < 2:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=False)
        GlobalHWVar.nonAggiornareSchermo = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["chiusoGliOcchiSulCalcolatore"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        GlobalHWVar.nonAggiornareSchermo = False
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
        GlobalHWVar.aggiornaSchermo()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["chiusoGliOcchiSulCalcolatore"]:
            GlobalHWVar.nonAggiornareSchermo = False
            GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
            GlobalHWVar.aggiornaSchermo()
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            xSpawn = GlobalHWVar.gpx * 15
            ySpawn = GlobalHWVar.gpy * 9
            nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "s", "avvia", nonMostrarePersonaggio, carim, caricaTutto)
            i = 0
            while i < 20:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["avviatoCalcolatore"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        avanzamentoStoria += 1
        xSpawn = GlobalHWVar.gpx * 15
        ySpawn = GlobalHWVar.gpy * 9
        nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "s", "compari", nonMostrarePersonaggio, carim, caricaTutto)
        GlobalHWVar.nonAggiornareSchermo = False
        # animazione girarsi su se stessi
        imgPersS = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        imgPersSb = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio1b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        imgPersD = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        imgPersDb = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio2b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        imgPersA = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio3.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        imgPersAb = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio3b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        imgPersW = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio4.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        imgPersWb = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio4b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.bianco, (xSpawn, ySpawn, GlobalHWVar.gpx, GlobalHWVar.gpy))
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersA, (xSpawn, ySpawn))
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersAb, (xSpawn, ySpawn))
        GlobalHWVar.aggiornaSchermo()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.bianco, (xSpawn, ySpawn, GlobalHWVar.gpx, GlobalHWVar.gpy))
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersW, (xSpawn, ySpawn))
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersWb, (xSpawn, ySpawn))
        GlobalHWVar.aggiornaSchermo()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.bianco, (xSpawn, ySpawn, GlobalHWVar.gpx, GlobalHWVar.gpy))
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersD, (xSpawn, ySpawn))
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersDb, (xSpawn, ySpawn))
        GlobalHWVar.aggiornaSchermo()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.bianco, (xSpawn, ySpawn, GlobalHWVar.gpx, GlobalHWVar.gpy))
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersS, (xSpawn, ySpawn))
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersSb, (xSpawn, ySpawn))
        GlobalHWVar.aggiornaSchermo()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.nonAggiornareSchermo = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["apparizioneNelCalcolatore"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        GlobalHWVar.nonAggiornareSchermo = False
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.bianco)
        imgPersS = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        imgPersSb = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio1b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersS, (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 9))
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersSb, (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 9))
        GlobalHWVar.aggiornaSchermo()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["apparizioneNelCalcolatore"]:
            GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.bianco)
            GlobalHWVar.disegnaImmagineSuSchermo(imgPersS, (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 9))
            GlobalHWVar.disegnaImmagineSuSchermo(imgPersSb, (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 9))
            GlobalHWVar.aggiornaSchermo()
            # tolgo l'equipaggiamento (spada, scudo, armatura, arco, guanti e collana)
            dati[6] = 0
            dati[7] = 0
            dati[8] = 0
            dati[128] = 0
            dati[129] = 0
            dati[130] = 0
            stanza = GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]
            cambiosta = True
            carim = True
            aggiornaImgEquip = True
            caricaTutto = True
        GlobalHWVar.nonAggiornareSchermo = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostApparizioneNelCalcolatore"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        xSpawn = GlobalHWVar.gpx * 15
        ySpawn = GlobalHWVar.gpy * 9
        nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "s", "concludi", nonMostrarePersonaggio, carim, caricaTutto)
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["apparizioneStanzaNelCalcolatore"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        GlobalHWVar.nonAggiornareSchermo = False
        GlobalHWVar.aggiornaSchermo()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sentitoVoceCalcolatore"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        # npers: 1=d, 2=a, 3=w, 4=s
        if npers == 4:
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
            npers = 1
            avanzaIlTurnoSenzaMuoverti = True
            carim = True
            caricaTutto = True
        elif npers == 1:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostApparizioneStanzaNelCalcolatore1"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        # npers: 1=d, 2=a, 3=w, 4=s
        if npers == 1:
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
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostApparizioneStanzaNelCalcolatore2"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"] and not (x == GlobalHWVar.gpx * 15 and y == GlobalHWVar.gpy * 9):
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["NeilUscitoDaTunnelSubaqueo2PostAvvioSequenzaNelCalcolatore"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["NeilUscitoDaTunnelSubaqueo2PostAvvioSequenzaNelCalcolatore"]:
            if y == GlobalHWVar.gpy * 7:
                percorsoDaEseguire = ["d", "s", "d", "d", "d", "d", "d", "d", "d", "d"]
            elif y == GlobalHWVar.gpy * 8:
                percorsoDaEseguire = ["d", "d", "d", "d", "d", "d", "d", "d", "d"]
            elif y == GlobalHWVar.gpy * 9:
                percorsoDaEseguire = ["d", "w", "d", "d", "d", "d", "d", "d", "d", "d"]
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoLaboratorioDiNeilDelPassato1"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"] and len(percorsoDaEseguire) == 0:
        # npers: 1=d, 2=a, 3=w, 4=s
        if npers == 1:
            npers = 3
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
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoLaboratorioDiNeilDelPassato2"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        GlobalHWVar.canaleSoundInterazioni.set_volume(GlobalHWVar.volumeEffetti / 2.0)
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "Neil":
                if personaggio.x == GlobalHWVar.gpx * 14 and personaggio.y == GlobalHWVar.gpy * 5 and personaggio.direzione == "d":
                    personaggioArrivato = True
                elif (personaggio.x == GlobalHWVar.gpx * 14 and personaggio.y == GlobalHWVar.gpy * 6) or (personaggio.x == GlobalHWVar.gpx * 15 and personaggio.y == GlobalHWVar.gpy * 3 and personaggio.direzione == "w"):
                    if not GlobalHWVar.canaleSoundInterazioni.get_busy():
                        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreAppoggioStrumentoEnigmi)
                        riprodottoRumoreAppoggioMatita = False
                        while not riprodottoRumoreAppoggioMatita:
                            if not GlobalHWVar.canaleSoundInterazioni.get_busy():
                                riprodottoRumoreAppoggioMatita = True
                            pygame.time.wait(10)
                            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreScorrimentoMatitaEnigmi, -1)
                        if personaggio.x == GlobalHWVar.gpx * 14 and personaggio.y == GlobalHWVar.gpy * 6:
                            tempoAttesa = 10
                        else:
                            tempoAttesa = 20
                        i = 0
                        while i < tempoAttesa:
                            pygame.time.wait(100)
                            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                            i += 1
                        GlobalHWVar.canaleSoundInterazioni.stop()
                elif personaggio.x == GlobalHWVar.gpx * 16 and personaggio.y == GlobalHWVar.gpy * 4 and personaggio.direzione == "d":
                    if not GlobalHWVar.canaleSoundInterazioni.get_busy():
                        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoRaccoltaOggetto)
                        i = 0
                        while i < 5:
                            pygame.time.wait(100)
                            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                            i += 1
                else:
                    GlobalHWVar.canaleSoundInterazioni.stop()
                break
        if personaggioArrivato:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreMovimentoVestiti)
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"] and personaggio.tipo == "Neil":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"] and personaggio.tipo == "Neil":
                    listaPersonaggi.remove(personaggio)
                    break
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
        GlobalHWVar.canaleSoundInterazioni.set_volume(GlobalHWVar.volumeEffetti)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sdraiatoNeilSulLettoDelLaboratorio"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["chiusoOcchiNeilSulLettoDelLaboratorio"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreIniezioneSiringa)
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]
        cambiosta = True
        carim = True
        caricaTutto = True
        GlobalHWVar.nonAggiornareSchermo = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["trasformatoLaboratorioDiNeil"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        # avanzo la storia per far ripartire l'audio ambientale in questo momento preciso
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["riavviatoSottofondoAmbientalePostTrasformazioneLaboratorio"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        if GlobalHWVar.nonAggiornareSchermo:
            GlobalHWVar.nonAggiornareSchermo = False
            GlobalHWVar.aggiornaSchermo()
        # npers: 1=d, 2=a, 3=w, 4=s
        if npers == 3:
            i = 0
            while i < 10:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            npers = 4
            carim = True
            caricaTutto = True
        elif npers == 4:
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
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo1PostTrasformazioneLaboratorio"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        if len(percorsoDaEseguire) == 0 and x == GlobalHWVar.gpx * 11 and y == GlobalHWVar.gpy * 8:
            percorsoDaEseguire = ["d", "d", "s", "d", "d", "d"]
        elif x == GlobalHWVar.gpx * 16 and y == GlobalHWVar.gpy * 9:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoCellaNeil-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoCellaNeilPostTrasformazioneLaboratorio1"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        # npers: 1=d, 2=a, 3=w, 4=s
        if npers == 1:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            npers = 3
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
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo2PostTrasformazioneLaboratorio"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        # npers: 1=d, 2=a, 3=w, 4=s
        if npers == 3:
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
            while i < 10:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoCellaNeil-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoCellaNeilPostTrasformazioneLaboratorio2"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        if GlobalHWVar.canaliSoundSottofondoAmbientale.getBusy():
            GlobalHWVar.canaliSoundSottofondoAmbientale.mettiInPausa()
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
        elif npers == 2:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            npers = 3
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
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoConCalcolatoreRaggiuntoMomentoPresente"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        # npers: 1=d, 2=a, 3=w, 4=s
        if npers == 3:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            npers = 2
            carim = True
            caricaTutto = True
        elif npers == 2:
            i = 0
            while i < 10:
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
            avanzamentoStoria += 1
            stanza = GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]
            cambiosta = True
            carim = True
            caricaTutto = True
            GlobalHWVar.nonAggiornareSchermo = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sparitoNeilDallaCellaDelLaboratorio"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        if GlobalHWVar.nonAggiornareSchermo:
            GlobalHWVar.nonAggiornareSchermo = False
            GlobalHWVar.aggiornaSchermo()
            GlobalHWVar.canaliSoundSottofondoAmbientale.togliPausa()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo1PostScomparsaNeilDallaCella"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        # npers: 1=d, 2=a, 3=w, 4=s
        if x == GlobalHWVar.gpx * 16 and y == GlobalHWVar.gpy * 9:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            percorsoDaEseguire = ["a"]
        elif npers == 2:
            i = 0
            while i < 2:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            npers = 1
            carim = True
            caricaTutto = True
        else:
            screen = GlobalHWVar.schermo.copy().convert()
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
            if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["monologo1PostScomparsaNeilDallaCella"]:
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
                npers = 4
                stanza = GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]
                cambiosta = True
                carim = True
                caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo2PostScomparsaNeilDallaCella"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        xSpawn = GlobalHWVar.gpx * 15
        ySpawn = GlobalHWVar.gpy * 9
        nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "s", "concludi", nonMostrarePersonaggio, carim, caricaTutto)
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroNelTempo10SecInLaboratorio"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        # npers: 1=d, 2=a, 3=w, 4=s
        if npers == 4:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            npers = 1
            carim = True
            caricaTutto = True
        elif npers == 1 and x == GlobalHWVar.gpx * 15 and y == GlobalHWVar.gpy * 9:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            percorsoDaEseguire = ["d", "d", "d", "d", "d"]
        elif len(percorsoDaEseguire) == 0:
            screen = GlobalHWVar.schermo.copy().convert()
            if GlobalHWVar.canaliSoundSottofondoAmbientale.getBusy():
                i = 0
                while i < 10:
                    pygame.time.wait(100)
                    inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                    i += 1
                GlobalHWVar.canaliSoundSottofondoAmbientale.mettiInPausa()
                i = 0
                while i < 10:
                    pygame.time.wait(100)
                    inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                    i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
            if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroNelTempo10SecInLaboratorio"]:
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
                GlobalHWVar.aggiornaSchermo()
                stanza = GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]
                cambiosta = True
                carim = True
                caricaTutto = True
                GlobalHWVar.nonAggiornareSchermo = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostTornatoIndietroNelTempo10SecInLaboratorio"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        if GlobalHWVar.nonAggiornareSchermo:
            GlobalHWVar.nonAggiornareSchermo = False
            GlobalHWVar.aggiornaSchermo()
            GlobalHWVar.canaliSoundSottofondoAmbientale.togliPausa()
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sparitoNeilDallaCellaDelLaboratorioSecondaVolta"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
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
        elif npers == 2 and x == GlobalHWVar.gpx * 20 and y == GlobalHWVar.gpy * 9:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            percorsoDaEseguire = ["a"]
        elif npers == 2 and len(percorsoDaEseguire) == 0:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo1PostSecondaSparizioneDiNeilDalLaboratorio"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
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
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivatoRenéNelLaboratorioDiNeil"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "Bibliotecario":
                if personaggio.x == GlobalHWVar.gpx * 10 and personaggio.y == GlobalHWVar.gpy * 8 and (personaggio.direzione == "d" or personaggio.direzione == "w" or personaggio.direzione == "s"):
                    i = 0
                    while i < 5:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                elif personaggio.x == GlobalHWVar.gpx * 10 and personaggio.y == GlobalHWVar.gpy * 8 and personaggio.direzione == "a":
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo1RenéNelLaboratorioDiNeil"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "Bibliotecario":
                if personaggio.x == GlobalHWVar.gpx * 6 and personaggio.y == GlobalHWVar.gpy * 8 and personaggio.direzione == "w":
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            i = 0
            while i < 20:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo2RenéNelLaboratorioDiNeil"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        personaggioArrivato = False
        personaggioInAttesa = 0
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "Bibliotecario":
                if personaggio.x == GlobalHWVar.gpx * 6 and personaggio.y == GlobalHWVar.gpy * 8 and personaggio.direzione == "w":
                    personaggioInAttesa = 10
                elif personaggio.x == GlobalHWVar.gpx * 5 and personaggio.y == GlobalHWVar.gpy * 8 and personaggio.direzione == "w":
                    personaggioInAttesa = 20
                elif personaggio.x == GlobalHWVar.gpx * 5 and personaggio.y == GlobalHWVar.gpy * 8 and personaggio.direzione == "s":
                    personaggioInAttesa = 2
                elif personaggio.x == GlobalHWVar.gpx * 5 and personaggio.y == GlobalHWVar.gpy * 10 and personaggio.direzione == "s":
                    personaggioInAttesa = 20
                elif personaggio.x == GlobalHWVar.gpx * 9 and personaggio.y == GlobalHWVar.gpy * 10 and personaggio.direzione == "s":
                    personaggioInAttesa = 20
                elif personaggio.x == GlobalHWVar.gpx * 9 and personaggio.y == GlobalHWVar.gpy * 10 and personaggio.direzione == "d" and personaggio.numeroMovimento == 22:
                    personaggioArrivato = True
                break
        if personaggioInAttesa > 0:
            i = 0
            while i < personaggioInAttesa:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
        elif personaggioArrivato:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo3RenéNelLaboratorioDiNeil"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        personaggioArrivato = False
        personaggioInAttesa = 0
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "Bibliotecario":
                if personaggio.x == GlobalHWVar.gpx * 9 and personaggio.y == GlobalHWVar.gpy * 10 and personaggio.direzione == "d":
                    personaggioInAttesa = 2
                if personaggio.x == GlobalHWVar.gpx * 11 and personaggio.y == GlobalHWVar.gpy * 10:
                    percorsoDaEseguire = ["d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d"]
                if personaggio.x == GlobalHWVar.gpx * 17 and personaggio.y == GlobalHWVar.gpy * 8 and npers != 3:
                    npers = 3
                    carim = True
                    caricaTutto = True
                elif personaggio.x == GlobalHWVar.gpx * 14 and personaggio.y == GlobalHWVar.gpy * 7 and personaggio.direzione == "w":
                    personaggioArrivato = True
                break
        if personaggioInAttesa > 0:
            i = 0
            while i < personaggioInAttesa:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
        elif personaggioArrivato:
            i = 0
            while i < 10:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        if len(percorsoDaEseguire) == 0:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo4RenéNelLaboratorioDiNeil"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "Bibliotecario":
                if personaggio.x == GlobalHWVar.gpx * 15 and personaggio.y == GlobalHWVar.gpy * 7 and personaggio.direzione == "w":
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            screen = GlobalHWVar.schermo.copy().convert()
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
            if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["monologo4RenéNelLaboratorioDiNeil"]:
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
                GlobalHWVar.aggiornaSchermo()
                stanza = GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]
                cambiosta = True
                carim = True
                caricaTutto = True
                GlobalHWVar.nonAggiornareSchermo = True
        avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sedutoSulCalcolatoreRenéNelLaboratorioDiNeil"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        if GlobalHWVar.nonAggiornareSchermo:
            GlobalHWVar.nonAggiornareSchermo = False
            GlobalHWVar.aggiornaSchermo()
        if len(percorsoDaEseguire) == 0:
            i = 0
            while i < 10:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoAttesaRenéSulCalcolatore1"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        screen = GlobalHWVar.schermo.copy().convert()
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoBibliotecarioCalcolatore-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["monologoAttesaRenéSulCalcolatore1"]:
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            # npers: 1=d, 2=a, 3=w, 4=s
            npers = 2
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoAttesaRenéSulCalcolatore2"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        # npers: 1=d, 2=a, 3=w, 4=s
        if npers == 2:
            i = 0
            while i < 10:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
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
            if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["monologoAttesaRenéSulCalcolatore2"]:
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
    elif GlobalGameVar.dictAvanzamentoStoria["passatoDieciMinAspettandoRenéSulCalcolatore"] <= avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["passatoUnGiornoAspettandoRenéSulCalcolatore"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        avanzamentoStoriaIniziale = avanzamentoStoria
        screen = GlobalHWVar.schermo.copy().convert()
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > avanzamentoStoriaIniziale:
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
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoTreGiorniAspettandoRenéSulCalcolatore"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        screen = GlobalHWVar.schermo.copy().convert()
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["passatoTreGiorniAspettandoRenéSulCalcolatore"]:
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
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["cambiatoStanzaPerAggiornareImgRenéSuCalcolatore"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        xSpawn = GlobalHWVar.gpx * 15
        ySpawn = GlobalHWVar.gpy * 9
        nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "concludi", nonMostrarePersonaggio, carim, caricaTutto)
        avanzamentoStoria += 1
    elif GlobalGameVar.dictAvanzamentoStoria["passatoUnMeseAspettandoRenéSulCalcolatore"] <= avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["passatoUnAnnoAspettandoRenéSulCalcolatore"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        avanzamentoStoriaIniziale = avanzamentoStoria
        screen = GlobalHWVar.schermo.copy().convert()
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > avanzamentoStoriaIniziale:
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
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoCinqueAnniAspettandoRenéSulCalcolatore"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        screen = GlobalHWVar.schermo.copy().convert()
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["passatoCinqueAnniAspettandoRenéSulCalcolatore"]:
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
            stanza = GlobalGameVar.dictStanze["stanzaEsplosa"]
            cambiosta = True
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo2NotatoTuttoDistruttoDopoDieciAnniDiAttesaPerRené"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        xSpawn = GlobalHWVar.gpx * 15
        ySpawn = GlobalHWVar.gpy * 9
        nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "s", "concludi", nonMostrarePersonaggio, carim, caricaTutto)
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        npers = 2
        carim = True
        caricaTutto = True
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroDieciAnniAspettandoRenéSulCalcolatore"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
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
        elif npers == 1:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
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
            if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroDieciAnniAspettandoRenéSulCalcolatore"]:
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
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoUnAnno1AspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        screen = GlobalHWVar.schermo.copy().convert()
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["passatoUnAnno1AspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"]:
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
            stanza = GlobalGameVar.dictStanze["stanzaEsplosa"]
            cambiosta = True
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPerTornareIndietroDopoDistruzioneDelMondo2"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        xSpawn = GlobalHWVar.gpx * 15
        ySpawn = GlobalHWVar.gpy * 9
        nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "concludi", nonMostrarePersonaggio, carim, caricaTutto)
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroSeiMesiAspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        screen = GlobalHWVar.schermo.copy().convert()
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroSeiMesiAspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"]:
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
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoUnMese1AspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        screen = GlobalHWVar.schermo.copy().convert()
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["passatoUnMese1AspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"]:
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
            stanza = GlobalGameVar.dictStanze["stanzaEsplosa"]
            cambiosta = True
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPerTornareIndietroDieciGiorniAspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        xSpawn = GlobalHWVar.gpx * 15
        ySpawn = GlobalHWVar.gpy * 9
        nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "concludi", nonMostrarePersonaggio, carim, caricaTutto)
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroDieciGiorniAspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        screen = GlobalHWVar.schermo.copy().convert()
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroDieciGiorniAspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"]:
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
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPerPassareUnGiornoAspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        xSpawn = GlobalHWVar.gpx * 15
        ySpawn = GlobalHWVar.gpy * 9
        nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "concludi", nonMostrarePersonaggio, carim, caricaTutto)
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoUnGiornoAspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        screen = GlobalHWVar.schermo.copy().convert()
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["passatoUnGiornoAspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"]:
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            npers = 2
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoNotatoRenéScomparsoDalCalcolatore"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        screen = GlobalHWVar.schermo.copy().convert()
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["monologoNotatoRenéScomparsoDalCalcolatore"]:
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            xSpawn = GlobalHWVar.gpx * 15
            ySpawn = GlobalHWVar.gpy * 9
            nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "a", "avvia", nonMostrarePersonaggio, carim, caricaTutto)
            nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "a", "compari", nonMostrarePersonaggio, carim, caricaTutto)
            stanza = GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]
            cambiosta = True
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPerTornareIndietroCinqueOreAspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        xSpawn = GlobalHWVar.gpx * 15
        ySpawn = GlobalHWVar.gpy * 9
        nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "a", "concludi", nonMostrarePersonaggio, carim, caricaTutto)
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroCinqueOreAspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        # npers: 1=d, 2=a, 3=w, 4=s
        if npers == 2:
            i = 0
            while i < 10:
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
            if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroCinqueOreAspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"]:
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
    elif GlobalGameVar.dictAvanzamentoStoria["passatoDueOreAspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"] <= avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["passatoUnOra1AspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        avanzamentoStoriaIniziale = avanzamentoStoria
        screen = GlobalHWVar.schermo.copy().convert()
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > avanzamentoStoriaIniziale:
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
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoUnOra2AspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        screen = GlobalHWVar.schermo.copy().convert()
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["passatoUnOra2AspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"]:
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
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPerPassareUnOra3AspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        xSpawn = GlobalHWVar.gpx * 15
        ySpawn = GlobalHWVar.gpy * 9
        nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "concludi", nonMostrarePersonaggio, carim, caricaTutto)
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoUnOra3AspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        screen = GlobalHWVar.schermo.copy().convert()
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["passatoUnOra3AspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"]:
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            npers = 2
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoNotatoAssenzaRenéCalcolatore2"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        # npers: 1=d, 2=a, 3=w, 4=s
        if npers == 2:
            i = 0
            while i < 10:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
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
            if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["monologoNotatoAssenzaRenéCalcolatore2"]:
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
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPerTornareIndietroDieciMinutiAspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        xSpawn = GlobalHWVar.gpx * 15
        ySpawn = GlobalHWVar.gpy * 9
        nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "concludi", nonMostrarePersonaggio, carim, caricaTutto)
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroDieciMinutiAspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        screen = GlobalHWVar.schermo.copy().convert()
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroDieciMinutiAspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"]:
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            GlobalHWVar.aggiornaSchermo()
            stanza = GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]
            cambiosta = True
            carim = True
            caricaTutto = True
            GlobalHWVar.nonAggiornareSchermo = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        if GlobalHWVar.nonAggiornareSchermo:
            GlobalHWVar.nonAggiornareSchermo = False
            GlobalHWVar.aggiornaSchermo()
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "BibliotecarioOperato":
                if personaggio.x == GlobalHWVar.gpx * 11 and personaggio.y == GlobalHWVar.gpy * 8:
                    personaggioArrivato = True
                if personaggio.x == GlobalHWVar.gpx * 13 and personaggio.y == GlobalHWVar.gpy * 7 and npers != 2:
                    npers = 2
                    carim = True
                    caricaTutto = True
                break
        if personaggioArrivato:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "BibliotecarioOperato-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoVistoRenéOperatoDopoCheèScesoDalCalcolatore"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "BibliotecarioOperato":
                if personaggio.x == GlobalHWVar.gpx * 2 and personaggio.y == GlobalHWVar.gpy * 8:
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"] and personaggio.tipo == "BibliotecarioOperato":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"] and personaggio.tipo == "BibliotecarioOperato":
                    listaPersonaggi.remove(personaggio)
                    break
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["riapertoGliOcchiSulCalcolatorePostStopTempoACasaTua"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        GlobalHWVar.nonAggiornareSchermo = False
        # animazione togliere il casco (alzo la linea dell'orizzonte dentro il casco)
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
        GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (0, GlobalHWVar.gpy * 9), (GlobalHWVar.gsx, GlobalHWVar.gpy * 9), GlobalHWVar.gpy // 5)
        GlobalHWVar.aggiornaSchermo()
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreIndossareCasco)
        yLineaOrizzonte = 9
        while yLineaOrizzonte >= 0:
            GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (0, GlobalHWVar.gpy * yLineaOrizzonte), (GlobalHWVar.gsx, GlobalHWVar.gpy * yLineaOrizzonte), GlobalHWVar.gpy // 5)
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockDisegno.tick(GlobalHWVar.fpsAnimazioni)
            yLineaOrizzonte -= 1
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
        GlobalHWVar.aggiornaSchermo()
        caricaTutto = True
        carim = True
        GlobalHWVar.nonAggiornareSchermo = True
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["toltoCascoCalcolatorePostScopertaFineDelMondo"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        if GlobalHWVar.nonAggiornareSchermo:
            GlobalHWVar.nonAggiornareSchermo = False
            FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=2)
            i = 0
            while i < 10:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
        else:
            avanzamentoStoria += 1
            stanza = GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]
            cambiosta = True
            carim = True
            caricaTutto = True
            nonMostrarePersonaggio = False
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["scesoDalCalcolatorePostScopertaFineDelMondo"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        # npers: 1=d, 2=a, 3=w, 4=s
        if x == GlobalHWVar.gpx * 15 and y == GlobalHWVar.gpy * 7 and npers == 4:
            i = 0
            while i < 5:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            percorsoDaEseguire = ["s"]
        elif x == GlobalHWVar.gpx * 15 and y == GlobalHWVar.gpy * 8 and npers == 4:
            i = 0
            while i < 10:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            npers = 3
            carim = True
            caricaTutto = True
        elif x == GlobalHWVar.gpx * 15 and y == GlobalHWVar.gpy * 8 and npers == 3:
            i = 0
            while i < 20:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            percorsoDaEseguire = ["w"]
        elif x == GlobalHWVar.gpx * 15 and y == GlobalHWVar.gpy * 7 and npers == 3:
            avanzamentoStoria += 1
            FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=False)
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreMovimentoVestiti)
            i = 0
            while i < 10:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreIndossareCasco)
            yLineaOrizzonte = 0
            while yLineaOrizzonte <= 9:
                GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
                GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (0, GlobalHWVar.gpy * yLineaOrizzonte), (GlobalHWVar.gsx, GlobalHWVar.gpy * yLineaOrizzonte), GlobalHWVar.gpy // 5)
                GlobalHWVar.aggiornaSchermo()
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                GlobalHWVar.clockDisegno.tick(GlobalHWVar.fpsAnimazioni)
                yLineaOrizzonte += 1
            GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (0, GlobalHWVar.gpy * 9), (GlobalHWVar.gsx, GlobalHWVar.gpy * 9), GlobalHWVar.gpy // 5)
            GlobalHWVar.aggiornaSchermo()
            FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=False)
            xSpawn = GlobalHWVar.gpx * 18
            ySpawn = GlobalHWVar.gpy * 9
            nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "a", "avvia", nonMostrarePersonaggio, carim, caricaTutto)
            nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "a", "compari", nonMostrarePersonaggio, carim, caricaTutto)
            stanza = GlobalGameVar.dictStanze["casaHansSara2"]
            cambiosta = True
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        avanzamentoStoria += 1
        # aumento il livello a 100 e riempio la vita al massimo
        dati[4] = 100
        esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = GenericFunc.getStatistiche(dati)
        dati[5] = pvtot
        dati[10] = entot
        i = 0
        while i < 30:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        stanza = GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]
        cambiosta = True
        carim = True
        caricaTutto = True
        nonMostrarePersonaggio = False
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["rialzataDalCalcolatore"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostPassatiMoltiAnniSulCalcolatore"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"] and x == GlobalHWVar.gpx * 9:
        if GlobalHWVar.canaleSoundPassiRallo.get_busy():
            GlobalHWVar.canaleSoundPassiRallo.stop()
        # npers: 1=d, 2=a, 3=w, 4=s
        if npers == 2:
            i = 0
            while i < 2:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            npers = 4
            carim = True
            caricaTutto = True
        else:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["oltreFinalePartenzaCalcolatore"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"] and GlobalGameVar.partitaAppenaAvviataPostFinale:
        i = 0
        while i < 30:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        stanza = GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]
        cambiosta = True
        carim = True
        caricaTutto = True
        nonMostrarePersonaggio = False

    return x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire
