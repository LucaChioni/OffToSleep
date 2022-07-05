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
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"]:
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoLettoSara-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"]:
            GlobalHWVar.canaleSoundCanzone.play(canzone, -1)
            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [GlobalHWVar.volumeCanzoni], False, posizioneCanaleMusica=0)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoCasaHansSara1"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"] and x == GlobalHWVar.gpx * 6 and y == GlobalHWVar.gpy * 8:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Tutorial-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"]:
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["trovatoMappaDiario"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Tutorial-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialMappaDiario"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"] and x == GlobalHWVar.gpx * 6 and y == GlobalHWVar.gpy * 8:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["armaturaNonno4"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioSognoCasaDavid"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "FratelloMaggiore" and personaggio.x == GlobalHWVar.gpx * 6 and personaggio.y == GlobalHWVar.gpy * 9:
                personaggioArrivato = True
                break
        if personaggioArrivato:
            avanzamentoStoria += 1
        else:
            i = 0
            while i < 15:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["hansUscitoCamerettaSognoCasaDavid"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "FratelloMaggiore-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoHansUscitoCamerettaSognoCasaDavid"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "FratelloMaggiore" and personaggio.x == GlobalHWVar.gpx * 9 and personaggio.y == GlobalHWVar.gpy * 8:
                personaggioArrivato = True
                break
        if personaggioArrivato:
            avanzamentoStoria += 1
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["hansAllontanatoCamerettaSognoCasaDavid"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "FratelloMaggiore" and personaggio.x == GlobalHWVar.gpx * 16 and personaggio.y == GlobalHWVar.gpy * 15 and personaggio.direzione == "s":
                personaggioArrivato = True
                break
        if personaggioArrivato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara1"] and personaggio.tipo == "FratelloMaggiore":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara1"] and personaggio.tipo == "FratelloMaggiore":
                    listaPersonaggi.remove(personaggio)
                    break
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumorePortoniCambioStanza)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["hansUscitoCasaSognoCasaDavid"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"] and (x == GlobalHWVar.gpy * 16 or x == GlobalHWVar.gpy * 17) and y == GlobalHWVar.gpy * 15:
        GlobalHWVar.canaleSoundPassiRallo.stop()
        nonMostrarePersonaggio = True
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["casaDavid3"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "FratelloMaggiore" and personaggio.x == GlobalHWVar.gpx * 6 and personaggio.y == GlobalHWVar.gpy * 9:
                personaggioArrivato = True
                break
        if personaggioArrivato:
            avanzamentoStoria += 1
        else:
            i = 0
            while i < 15:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["hansUscitoCamerettaSognoCastello"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "FratelloMaggiore-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoHansUscitoCamerettaSognoCastello"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "FratelloMaggiore" and personaggio.x == GlobalHWVar.gpx * 9 and personaggio.y == GlobalHWVar.gpy * 8:
                personaggioArrivato = True
                break
        if personaggioArrivato:
            avanzamentoStoria += 1
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["hansAllontanatoCamerettaSognoCastello"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "FratelloMaggiore" and personaggio.x == GlobalHWVar.gpx * 16 and personaggio.y == GlobalHWVar.gpy * 15 and personaggio.direzione == "s":
                personaggioArrivato = True
                break
        if personaggioArrivato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara1"] and personaggio.tipo == "FratelloMaggiore":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara1"] and personaggio.tipo == "FratelloMaggiore":
                    listaPersonaggi.remove(personaggio)
                    break
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumorePortoniCambioStanza)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["hansUscitoCasaSognoCastello"] and stanza == GlobalGameVar.dictStanze["casaHansSara2"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "FratelloMaggiore" and personaggio.y == GlobalHWVar.gpy * 15:
                personaggioArrivato = True
                break
        if personaggioArrivato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara2"] and personaggio.tipo == "FratelloMaggiore":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara2"] and personaggio.tipo == "FratelloMaggiore":
                    listaPersonaggi.remove(personaggio)
                    break
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPerTornareIndietroAPrimaDelloScoppioDelMissileACasa"] and stanza == GlobalGameVar.dictStanze["casaHansSara2"]:
        xSpawn = GlobalHWVar.gpx * 18
        ySpawn = GlobalHWVar.gpy * 9
        nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "w", "concludi", nonMostrarePersonaggio, carim, caricaTutto)
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroAPrimaDelloScoppioDelMissileACasa"] and stanza == GlobalGameVar.dictStanze["casaHansSara2"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "CaneCasa":
                if personaggio.x == GlobalHWVar.gpx * 14 and personaggio.y == GlobalHWVar.gpy * 8 and npers != 2:
                    # npers: 1=d, 2=a, 3=w, 4=s
                    npers = 2
                    carim = True
                    caricaTutto = True
                elif personaggio.x == GlobalHWVar.gpx * 15 and personaggio.y == GlobalHWVar.gpy * 11:
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            personaggioCreato = False
            for personaggio in listaPersonaggi:
                if personaggio.tipo == "Madre":
                    personaggioCreato = True
                    break
            if not personaggioCreato:
                percorsoPersonaggio = ["", "", "", "s", "dGira", "", "", "s", "s", "s", "s"]
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 4, "s", "Madre-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                carim = True
                caricaTutto = True
                GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumorePortoniCambioStanza)
            else:
                i = 0
                while i < 5:
                    pygame.time.wait(100)
                    inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                    i += 1
                personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Madre-0", stanza, avanzamentoStoria, False)
                avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
                caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoMadre1PreScoppioMissileSecondaVolta"] and stanza == GlobalGameVar.dictStanze["casaHansSara2"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "CaneCasa":
                if personaggio.x == GlobalHWVar.gpx * 15 and personaggio.y == GlobalHWVar.gpy * 11 and npers != 3:
                    # npers: 1=d, 2=a, 3=w, 4=s
                    npers = 3
                    carim = True
                    caricaTutto = True
                elif personaggio.x == GlobalHWVar.gpx * 13 and personaggio.y == GlobalHWVar.gpy * 12:
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            i = 0
            while i < 1:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Madre-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoMadre2PreScoppioMissileSecondaVolta"] and stanza == GlobalGameVar.dictStanze["casaHansSara2"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "Madre":
                if personaggio.x == GlobalHWVar.gpx * 16 and personaggio.y == GlobalHWVar.gpy * 5 and personaggio.direzione == "d":
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.6], False, posizioneCanaleMusica=0)
            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaliSoundSottofondoAmbientale], [GlobalHWVar.volumeEffetti * 0.2], False, posizioneCanaleMusica=0)
            # animazione esplosione missile
            pathImgs = "Risorse/Immagini/Scenari/Stanza" + str(stanza) + "/Animazioni/EsplosioneMissilePt1/"
            coordinateImgAnimata = (0, 0)
            dimensioniImgAnimata = (GlobalHWVar.gsx, GlobalHWVar.gsy)
            listaAudio = [24, GlobalSndVar.rumoreEsplosioneMissile]
            FunzioniGraficheGeneriche.animaEvento(pathImgs, coordinateImgAnimata, dimensioniImgAnimata, listaAudio, tuttoSchermo=True)
            i = 0
            while i < 50:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            avanzamentoStoria += 1
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["missileNucleareScoppiatoSecondaVolta"] and stanza == GlobalGameVar.dictStanze["casaHansSara2"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "Madre":
                if personaggio.x == GlobalHWVar.gpx * 16 and personaggio.y == GlobalHWVar.gpy * 8:
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            # animazione esplosione missile
            pathImgs = "Risorse/Immagini/Scenari/Stanza" + str(stanza) + "/Animazioni/EsplosioneMissilePt2/"
            coordinateImgAnimata = (0, 0)
            dimensioniImgAnimata = (GlobalHWVar.gsx, GlobalHWVar.gsy)
            listaAudio = []
            FunzioniGraficheGeneriche.animaEvento(pathImgs, coordinateImgAnimata, dimensioniImgAnimata, listaAudio, tuttoSchermo=True)
            screen = GlobalHWVar.schermo.copy().convert()
            GlobalHWVar.canaleSoundInterazioni.stop()
            GlobalHWVar.canaliSoundSottofondoAmbientale.arresta()
            GlobalHWVar.canaleSoundMelodieEventi.stop()
            while avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["missileNucleareScoppiatoSecondaVolta"]:
                personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
                avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
                caricaTutto = True
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
                GlobalHWVar.aggiornaSchermo()
            if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["missileNucleareScoppiatoSecondaVolta"]:
                # npers: 1=d, 2=a, 3=w, 4=s
                npers = 2
                stanza = GlobalGameVar.dictStanze["casaHansSara2"]
                cambiosta = True
                carim = True
                caricaTutto = True
                GlobalHWVar.nonAggiornareSchermo = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["stoppatoTempoCalcolatorePreDistruzioneDiCasaTua"] and stanza == GlobalGameVar.dictStanze["casaHansSara2"]:
        avanzamentoStoria += 1
        GlobalHWVar.nonAggiornareSchermo = False
        # ridisegno l'esplosione sulla stanza
        pathImgs = "Risorse/Immagini/Scenari/Stanza" + str(stanza) + "/Animazioni/EsplosioneMissilePt2/"
        coordinateImgAnimata = (0, 0)
        dimensioniImgAnimata = (GlobalHWVar.gsx, GlobalHWVar.gsy)
        listaAudio = []
        FunzioniGraficheGeneriche.animaEvento(pathImgs, coordinateImgAnimata, dimensioniImgAnimata, listaAudio, tuttoSchermo=True)

        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        image = pygame.Surface((GlobalHWVar.gsx, GlobalHWVar.gsy), flags=pygame.SRCALPHA)
        image.fill((0, 0, 0, 100))
        image = image.convert_alpha(GlobalHWVar.schermo)
        i = 0
        while i <= 5:
            GlobalHWVar.disegnaImmagineSuSchermo(image, (0, 0))
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, (30 + (i * 40), 30 + (i * 40), 30 + (i * 40)), (0, GlobalHWVar.gpy * 9), (GlobalHWVar.gsx, GlobalHWVar.gpy * 9), GlobalHWVar.gpy // 5)
            GlobalHWVar.aggiornaSchermo()
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
            i += 1
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
        GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (0, GlobalHWVar.gpy * 9), (GlobalHWVar.gsx, GlobalHWVar.gpy * 9), GlobalHWVar.gpy // 5)
        GlobalHWVar.aggiornaSchermo()

        stanza = GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]
        cambiosta = True
        carim = True
        caricaTutto = True
        nonMostrarePersonaggio = True
        GlobalHWVar.nonAggiornareSchermo = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["risalitoSulCalcolatorePostScopertaFineDelMondo"] and stanza == GlobalGameVar.dictStanze["casaHansSara2"]:
        # ridisegno l'esplosione sulla stanza
        pathImgs = "Risorse/Immagini/Scenari/Stanza" + str(stanza) + "/Animazioni/EsplosioneMissilePt2/"
        coordinateImgAnimata = (0, 0)
        dimensioniImgAnimata = (GlobalHWVar.gsx, GlobalHWVar.gsy)
        listaAudio = []
        FunzioniGraficheGeneriche.animaEvento(pathImgs, coordinateImgAnimata, dimensioniImgAnimata, listaAudio, tuttoSchermo=True)
        xSpawn = GlobalHWVar.gpx * 18
        ySpawn = GlobalHWVar.gpy * 9
        nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "a", "concludi", nonMostrarePersonaggio, carim, caricaTutto)
        avanzamentoStoria += 1
        GlobalHWVar.nonAggiornareSchermo = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoNelCalcolatoreACasaTua"] and stanza == GlobalGameVar.dictStanze["casaHansSara2"]:
        # ridisegno l'esplosione sulla stanza
        pathImgs = "Risorse/Immagini/Scenari/Stanza" + str(stanza) + "/Animazioni/EsplosioneMissilePt2/"
        coordinateImgAnimata = (0, 0)
        dimensioniImgAnimata = (GlobalHWVar.gsx, GlobalHWVar.gsy)
        listaAudio = []
        FunzioniGraficheGeneriche.animaEvento(pathImgs, coordinateImgAnimata, dimensioniImgAnimata, listaAudio, tuttoSchermo=True)
        GlobalHWVar.nonAggiornareSchermo = False
        GlobalHWVar.aggiornaSchermo()
        screen = GlobalHWVar.schermo.copy().convert()
        while avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoNelCalcolatoreACasaTua"]:
            i = 0
            while i < 10:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
            GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            GlobalHWVar.aggiornaSchermo()
        xSpawn = GlobalHWVar.gpx * 4
        ySpawn = GlobalHWVar.gpy * 13
        nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "a", "avvia", nonMostrarePersonaggio, carim, caricaTutto)
        nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "a", "compari", nonMostrarePersonaggio, carim, caricaTutto)
        stanza = GlobalGameVar.dictStanze["casaHansSara1"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPerTornareIndietroNelTempoAllaSeraDellInizioDelGioco"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"]:
        xSpawn = GlobalHWVar.gpx * 4
        ySpawn = GlobalHWVar.gpy * 13
        nonMostrarePersonaggio, carim, caricaTutto = FunzioniGraficheGeneriche.animaCambioScenaCalcolatore(xSpawn, ySpawn, "a", "concludi", nonMostrarePersonaggio, carim, caricaTutto)
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroNelTempoAllaSeraDellInizioDelGioco"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"]:
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
            while i < 10:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["riavviatoSequenzaEventiNellaSeraDellInizioDelGioco"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "FratelloMaggiore":
                if personaggio.x == GlobalHWVar.gpx * 6 and personaggio.y == GlobalHWVar.gpy * 13:
                    i = 0
                    while i < 5:
                        pygame.time.wait(100)
                        inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                        i += 1
                    avanzaIlTurnoSenzaMuoverti = True
                elif personaggio.x == GlobalHWVar.gpx * 16 and personaggio.y == GlobalHWVar.gpy * 15 and personaggio.direzione == "s":
                    personaggioArrivato = True
                elif personaggio.x < GlobalHWVar.gpx * 9:
                    avanzaIlTurnoSenzaMuoverti = True
                break
        if personaggioArrivato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara1"] and personaggio.tipo == "FratelloMaggiore":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara1"] and personaggio.tipo == "FratelloMaggiore":
                    listaPersonaggi.remove(personaggio)
                    break
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumorePortoniCambioStanza)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["HansUscitoDaCasa1NellaSeraDellInizioDelGioco"] and stanza == GlobalGameVar.dictStanze["casaHansSara2"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "FratelloMaggiore" and personaggio.y == GlobalHWVar.gpy * 15:
                personaggioArrivato = True
                break
        if personaggioArrivato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara2"] and personaggio.tipo == "FratelloMaggiore":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara2"] and personaggio.tipo == "FratelloMaggiore":
                    listaPersonaggi.remove(personaggio)
                    break
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["HansUscitoDaCasa2NellaSeraDellInizioDelGioco"] and stanza == GlobalGameVar.dictStanze["casaHansSara4"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "FratelloMaggiore" and personaggio.y == GlobalHWVar.gpy * 15:
                personaggioArrivato = True
                break
        if personaggioArrivato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara4"] and personaggio.tipo == "FratelloMaggiore":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara4"] and personaggio.tipo == "FratelloMaggiore":
                    listaPersonaggi.remove(personaggio)
                    break
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True

    return x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire
