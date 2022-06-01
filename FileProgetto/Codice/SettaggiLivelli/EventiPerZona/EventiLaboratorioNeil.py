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
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.nero, (0, GlobalHWVar.gpy * (yLineaOrizzonte - 1)), (GlobalHWVar.gsx, GlobalHWVar.gpy * (yLineaOrizzonte - 1)), 5)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (0, GlobalHWVar.gpy * yLineaOrizzonte), (GlobalHWVar.gsx, GlobalHWVar.gpy * yLineaOrizzonte), 5)
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockDisegno.tick(GlobalHWVar.fpsAnimazioni)
            yLineaOrizzonte += 1
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
        GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (0, GlobalHWVar.gpy * 9), (GlobalHWVar.gsx, GlobalHWVar.gpy * 9), 5)
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
        GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (0, GlobalHWVar.gpy * 9), (GlobalHWVar.gsx, GlobalHWVar.gpy * 9), 5)
        GlobalHWVar.aggiornaSchermo()
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "NessunoPov-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["messoCascoCalcolatore"]:
            GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (0, GlobalHWVar.gpy * 9), (GlobalHWVar.gsx, GlobalHWVar.gpy * 9), 5)
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
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "NessunoPov-0", stanza, avanzamentoStoria, False)
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
            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [0], False)
            GlobalHWVar.canaliSoundSottofondoAmbientale.arresta()
            GlobalHWVar.canaliSoundSottofondoAmbientale.settaVolume(GlobalHWVar.volumeEffetti)
            image = pygame.Surface((GlobalHWVar.gsx, GlobalHWVar.gsy), flags=pygame.SRCALPHA)
            image.fill((255, 255, 255, 50))
            image = image.convert_alpha(GlobalHWVar.schermo)
            i = 0
            while i <= 20:
                GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
                GlobalHWVar.aggiornaSchermo()
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
                i += 1
            GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.bianco)
            GlobalHWVar.aggiornaSchermo()
            i = 0
            while i < 20:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
        GlobalHWVar.nonAggiornareSchermo = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["avviatoCalcolatore"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        avanzamentoStoria += 1
        # animazione della tua apparizione nel calcolatore
        GlobalHWVar.nonAggiornareSchermo = False
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.bianco)
        GlobalHWVar.aggiornaSchermo()
        # carico le img per l'animazione
        imgPersS = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        imgPersSb = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio1b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        imgPersD = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio2.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        imgPersDb = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio2b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        imgPersA = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio3.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        imgPersAb = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio3b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        imgPersW = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio4.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        imgPersWb = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio4b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        image = pygame.Surface((GlobalHWVar.gpx, GlobalHWVar.gpy), flags=pygame.SRCALPHA)
        i = 0
        while i <= 255:
            GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.bianco, (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 9, GlobalHWVar.gpx, GlobalHWVar.gpy))
            GlobalHWVar.disegnaImmagineSuSchermo(imgPersS, (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 9))
            GlobalHWVar.disegnaImmagineSuSchermo(imgPersSb, (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 9))
            image.fill((255, 255, 255, 255 - i))
            GlobalHWVar.disegnaImmagineSuSchermo(image, (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 9))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i += 10
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        # animazione girarsi su se stessi
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.bianco, (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 9, GlobalHWVar.gpx, GlobalHWVar.gpy))
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersA, (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 9))
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersAb, (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 9))
        GlobalHWVar.aggiornaSchermo()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.bianco, (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 9, GlobalHWVar.gpx, GlobalHWVar.gpy))
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersW, (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 9))
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersWb, (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 9))
        GlobalHWVar.aggiornaSchermo()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.bianco, (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 9, GlobalHWVar.gpx, GlobalHWVar.gpy))
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersD, (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 9))
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersDb, (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 9))
        GlobalHWVar.aggiornaSchermo()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.bianco, (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 9, GlobalHWVar.gpx, GlobalHWVar.gpy))
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersS, (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 9))
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersSb, (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 9))
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
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "NessunoPov-0", stanza, avanzamentoStoria, False)
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
        avanzamentoStoria += 1
        GlobalHWVar.nonAggiornareSchermo = False
        imgPersS = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio1.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        imgPersSb = CaricaFileProgetto.loadImage('Risorse/Immagini/Personaggi/Sara5/Personaggio1b.png', GlobalHWVar.gpx, GlobalHWVar.gpy, True)
        screen = GlobalHWVar.schermo.copy().convert()
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.bianco)
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersS, (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 9))
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersSb, (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 9))
        GlobalHWVar.aggiornaSchermo()
        # animazione apparizione stanza
        image = pygame.Surface((GlobalHWVar.gsx, GlobalHWVar.gsy), flags=pygame.SRCALPHA)
        i = 0
        while i <= 255:
            GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.bianco)
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            image.fill((255, 255, 255, 255 - i))
            GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
            GlobalHWVar.disegnaImmagineSuSchermo(imgPersS, (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 9))
            GlobalHWVar.disegnaImmagineSuSchermo(imgPersSb, (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 9))
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i += 10
        GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersS, (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 9))
        GlobalHWVar.disegnaImmagineSuSchermo(imgPersSb, (GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 9))
        nonMostrarePersonaggio = False
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["apparizioneStanzaNelCalcolatore"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        GlobalHWVar.nonAggiornareSchermo = False
        GlobalHWVar.aggiornaSchermo()
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "NessunoPov-0", stanza, avanzamentoStoria, False)
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
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "NessunoPov-0", stanza, avanzamentoStoria, False)
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
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "NessunoPov-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostApparizioneStanzaNelCalcolatore2"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"] and x == GlobalHWVar.gpx * 14:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "NessunoPov-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True

    return x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire

# GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti], False)