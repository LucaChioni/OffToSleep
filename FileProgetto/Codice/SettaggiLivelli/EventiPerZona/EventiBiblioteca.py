# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.GestioneMenu.MenuDialoghi as MenuDialoghi
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche


def gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco):
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["rimosseMonetePerEntrareInConfraternita"] and stanza == GlobalGameVar.dictStanze["biblioteca1"] and y == GlobalHWVar.gpy * 11:
        screen = GlobalHWVar.schermo.copy().convert()
        if npers != 2:
            npers = 2
            avanzaIlTurnoSenzaMuoverti = True
            carim = True
        if not avanzaIlTurnoSenzaMuoverti:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "AssistBiblioteca-0", stanza, avanzamentoStoria, False)
            while not avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["rimosseMonetePerEntrareInConfraternita"]:
                avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            percorsoDaEseguire = ["s"]
        caricaTutto = True
    elif GlobalGameVar.dictAvanzamentoStoria["rifiutatoDallaBiblioteca"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoDopoArrivoInBiblioteca"] and stanza == GlobalGameVar.dictStanze["biblioteca1"] and y == GlobalHWVar.gpy * 11 and len(percorsoDaEseguire) == 0:
        if npers != 2:
            npers = 2
            avanzaIlTurnoSenzaMuoverti = True
            carim = True
        if not avanzaIlTurnoSenzaMuoverti:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "AssistBiblioteca-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            percorsoDaEseguire = ["s"]
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoDopoArrivoInBiblioteca"] and stanza == GlobalGameVar.dictStanze["biblioteca1"] and y == GlobalHWVar.gpy * 11:
        screen = GlobalHWVar.schermo.copy().convert()
        if npers != 2:
            npers = 2
            avanzaIlTurnoSenzaMuoverti = True
            carim = True
        if not avanzaIlTurnoSenzaMuoverti:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "AssistBiblioteca-0", stanza, avanzamentoStoria, False)
            while not avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["monologoDopoArrivoInBiblioteca"]:
                avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
                GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
            percorsoDaEseguire = ["w"]
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["incontratoBibliotecario"] and stanza == GlobalGameVar.dictStanze["biblioteca2"]:
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["biblioteca3"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["andatoNelloStudioDelBibliotecario"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoBibliotecarioArrivoNelloStudio"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"] and personaggio.tipo == "Bibliotecario":
                if personaggio.x == GlobalHWVar.gpx * 12 and personaggio.y == GlobalHWVar.gpy * 6:
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
            if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["dialogoBibliotecarioArrivoNelloStudio"]:
                GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoRaccoltaOggetto)
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["toltoRegistroBibliotecaDallaLibreria"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"] and personaggio.tipo == "Bibliotecario":
                if personaggio.x == GlobalHWVar.gpx * 15 and personaggio.y == GlobalHWVar.gpy * 6 and personaggio.direzione == "w":
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoRaccoltaOggetto)
            avanzamentoStoria += 1
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["messoRegistroBibliotecaSullaScrivania"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoBibliotecarioPreVomito1"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"] and personaggio.tipo == "Bibliotecario":
                if personaggio.x == GlobalHWVar.gpx * 15 and personaggio.y == GlobalHWVar.gpy * 6 and personaggio.direzione == "s":
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"] and personaggio.tipo == "Bibliotecario":
                    personaggio.percorso = ["s", "d", "s", "d"]
                    personaggio.numeroMovimento = 0
                    break
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoBibliotecarioPreVomito2"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"] and personaggio.tipo == "Bibliotecario":
                if personaggio.x == GlobalHWVar.gpx * 17 and personaggio.y == GlobalHWVar.gpy * 8:
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["vomitatoInBiblioteca"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoBibliotecarioPostVomito"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        nonMostrarePersonaggio = True
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["biblioteca3"]
        listaNemiciTotali = []
        listaPersonaggiTotali = []
        stanzeGiaVisitate = []
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sedutaInBiblioteca"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ripulitoVomito"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        bibliotecarioGiratoVersoDiTe = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"] and personaggio.tipo == "Bibliotecario":
                if personaggio.percorso != ["wGira", "w", "dGira", "fermati"]:
                    personaggio.percorso = ["wGira", "w", "dGira", "fermati"]
                    personaggio.numeroMovimento = 0
                if personaggio.direzione == "w":
                    bibliotecarioGiratoVersoDiTe = True
                break
        if bibliotecarioGiratoVersoDiTe:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["bibliotecarioVenutoVersoDiTe"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        bibliotecarioArrivatoDaTe = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"] and personaggio.tipo == "Bibliotecario":
                if personaggio.x == GlobalHWVar.gpx * 19 and personaggio.y == GlobalHWVar.gpy * 7 and personaggio.direzione == "d":
                    bibliotecarioArrivatoDaTe = True
                break
        if bibliotecarioArrivatoDaTe:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoBibliotecarioDuranteSeduta"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        nonMostrarePersonaggio = False
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["biblioteca3"]
        x = GlobalHWVar.gpx * 19
        y = GlobalHWVar.gpy * 7
        npers = 2
        listaNemiciTotali = []
        listaPersonaggiTotali = []
        stanzeGiaVisitate = []
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["alzataDallaSediaInBiblioteca"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        avanzamentoStoria += 1
        GlobalHWVar.canaleSoundCanzone.play(canzone, -1)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [GlobalHWVar.volumeCanzoni], False, posizioneCanaleMusica=0)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["spiegazioneEnigmaBibliotecario1"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        bibliotecarioGirato = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"] and personaggio.tipo == "Bibliotecario":
                if personaggio.direzione == "d":
                    bibliotecarioGirato = True
                else:
                    personaggio.percorso = ["dGira"]
                    personaggio.numeroMovimento = 0
                break
        if bibliotecarioGirato:
            pathImgs = "Risorse/Immagini/Scenari/Stanza" + str(stanza) + "/Animazioni/lancioPallaVel" + str(GlobalGameVar.datiEnigmaBibliotecario["velocità"]) + "/"
            coordinateImgAnimata = (GlobalHWVar.gpx * 17, GlobalHWVar.gpy * 11)
            dimensioniImgAnimata = (GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 1)
            listaAudio = [2, GlobalSndVar.rumoreLancioPallaBibliotecario, -1, GlobalSndVar.rumoreRitornoPallaBibliotecario]
            FunzioniGraficheGeneriche.animaEvento(pathImgs, coordinateImgAnimata, dimensioniImgAnimata, listaAudio)

            avanzaIlTurnoSenzaMuoverti = True
            avanzamentoStoria += 1
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["eseguitoEsperimentoDiProva1"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        bibliotecarioGirato = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"] and personaggio.tipo == "Bibliotecario":
                if personaggio.direzione == "s":
                    bibliotecarioGirato = True
                else:
                    personaggio.percorso = ["sGira"]
                    personaggio.numeroMovimento = 0
                break
        if bibliotecarioGirato:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["spiegazioneEnigmaBibliotecario2"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        bibliotecarioGirato = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"] and personaggio.tipo == "Bibliotecario":
                if personaggio.direzione == "d":
                    bibliotecarioGirato = True
                else:
                    personaggio.percorso = ["dGira"]
                    personaggio.numeroMovimento = 0
                break
        if bibliotecarioGirato:
            pathImgs = "Risorse/Immagini/Scenari/Stanza" + str(stanza) + "/Animazioni/lancioPallaVel" + str(GlobalGameVar.datiEnigmaBibliotecario["velocità"]) + "/"
            coordinateImgAnimata = (GlobalHWVar.gpx * 17, GlobalHWVar.gpy * 11)
            dimensioniImgAnimata = (GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 1)
            listaAudio = [2, GlobalSndVar.rumoreLancioPallaBibliotecario, -1, GlobalSndVar.rumoreRitornoPallaBibliotecario]
            FunzioniGraficheGeneriche.animaEvento(pathImgs, coordinateImgAnimata, dimensioniImgAnimata, listaAudio)

            avanzaIlTurnoSenzaMuoverti = True
            avanzamentoStoria += 1
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["eseguitoEsperimentoDiProva2"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        bibliotecarioGirato = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"] and personaggio.tipo == "Bibliotecario":
                if personaggio.direzione == "s":
                    bibliotecarioGirato = True
                else:
                    personaggio.percorso = ["sGira"]
                    personaggio.numeroMovimento = 0
                break
        if bibliotecarioGirato:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["spiegazioneEnigmaBibliotecario3"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        bibliotecarioGirato = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"] and personaggio.tipo == "Bibliotecario":
                if personaggio.percorso != ["aGira", "sGira", "mantieniPosizione"]:
                    personaggio.percorso = ["aGira", "sGira", "mantieniPosizione"]
                    personaggio.numeroMovimento = 0
                elif personaggio.direzione == "a":
                    bibliotecarioGirato = "a"
                elif personaggio.direzione == "s":
                    bibliotecarioGirato = "s"
                break
        if bibliotecarioGirato:
            if bibliotecarioGirato == "a":
                i = 0
                while i < 5:
                    pygame.time.wait(100)
                    inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                    i += 1
                avanzaIlTurnoSenzaMuoverti = True
            if bibliotecarioGirato == "s":
                for personaggio in listaPersonaggi:
                    if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"] and personaggio.tipo == "Bibliotecario":
                        personaggio.percorso = []
                        personaggio.numeroMovimento = 0
                        break
                avanzaIlTurnoSenzaMuoverti = True
                avanzamentoStoria += 1
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["scrittiDatiEnigmaBibliotecario"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["scrittiDatiEnigmaBibliotecario"]:
            GlobalGameVar.datiEnigmaBibliotecario["velocità"] = 3
            GlobalGameVar.datiEnigmaBibliotecario["soluzione"] = 2.25
            GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa1"] = 1.25
            GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa2"] = 1
            GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa3"] = 2.5
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"] and personaggio.tipo == "OggettoTavoloEnigmaBiblioteca":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"] and personaggio.tipo == "OggettoTavoloEnigmaBiblioteca":
                    listaPersonaggi.remove(personaggio)
                    break
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 11, "s", "OggettoEnigmaBiblioteca-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            carim = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["spiegazioneEnigmaBibliotecario4"] and stanza == GlobalGameVar.dictStanze["biblioteca3"] and GlobalGameVar.datiEnigmaBibliotecario["reset"]:
        bibliotecarioGirato = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"] and personaggio.tipo == "Bibliotecario":
                if personaggio.percorso != ["dGira", "aGira", "sGira", "mantieniPosizione"]:
                    personaggio.percorso = ["dGira", "aGira", "sGira", "mantieniPosizione"]
                    personaggio.numeroMovimento = 0
                elif personaggio.direzione == "d":
                    bibliotecarioGirato = "d"
                elif personaggio.direzione == "a":
                    bibliotecarioGirato = "a"
                elif personaggio.direzione == "s":
                    bibliotecarioGirato = "s"
                break
        if bibliotecarioGirato:
            if bibliotecarioGirato == "d":
                pathImgs = "Risorse/Immagini/Scenari/Stanza" + str(stanza) + "/Animazioni/lancioPallaVel" + str(GlobalGameVar.datiEnigmaBibliotecario["velocità"]) + "/"
                coordinateImgAnimata = (GlobalHWVar.gpx * 17, GlobalHWVar.gpy * 11)
                dimensioniImgAnimata = (GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 1)
                listaAudio = [2, GlobalSndVar.rumoreLancioPallaBibliotecario, -1, GlobalSndVar.rumoreRitornoPallaBibliotecario]
                FunzioniGraficheGeneriche.animaEvento(pathImgs, coordinateImgAnimata, dimensioniImgAnimata, listaAudio)
                avanzaIlTurnoSenzaMuoverti = True
            elif bibliotecarioGirato == "a":
                i = 0
                while i < 5:
                    pygame.time.wait(100)
                    inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                    i += 1
                if GlobalGameVar.datiEnigmaBibliotecario["velocità"] == 1:
                    GlobalGameVar.datiEnigmaBibliotecario["velocità"] = 2
                    GlobalGameVar.datiEnigmaBibliotecario["soluzione"] = 1
                    GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa1"] = 1.25
                    GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa2"] = 0.25
                    GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa3"] = 1.5
                elif GlobalGameVar.datiEnigmaBibliotecario["velocità"] == 2:
                    GlobalGameVar.datiEnigmaBibliotecario["velocità"] = 3
                    GlobalGameVar.datiEnigmaBibliotecario["soluzione"] = 2.25
                    GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa1"] = 1.25
                    GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa2"] = 1
                    GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa3"] = 2.5
                elif GlobalGameVar.datiEnigmaBibliotecario["velocità"] == 3:
                    GlobalGameVar.datiEnigmaBibliotecario["velocità"] = 4
                    GlobalGameVar.datiEnigmaBibliotecario["soluzione"] = 4
                    GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa1"] = 3.5
                    GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa2"] = 4.25
                    GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa3"] = 5
                elif GlobalGameVar.datiEnigmaBibliotecario["velocità"] == 4:
                    GlobalGameVar.datiEnigmaBibliotecario["velocità"] = 5
                    GlobalGameVar.datiEnigmaBibliotecario["soluzione"] = 6.25
                    GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa1"] = 5
                    GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa2"] = 4.75
                    GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa3"] = 5.5
                elif GlobalGameVar.datiEnigmaBibliotecario["velocità"] == 5:
                    GlobalGameVar.datiEnigmaBibliotecario["velocità"] = 1
                    GlobalGameVar.datiEnigmaBibliotecario["soluzione"] = 0.25
                    GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa1"] = 1
                    GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa2"] = 0.75
                    GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa3"] = 0.5
                avanzaIlTurnoSenzaMuoverti = True
            if bibliotecarioGirato == "s":
                for personaggio in listaPersonaggi:
                    if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"] and personaggio.tipo == "Bibliotecario":
                        personaggio.percorso = []
                        personaggio.numeroMovimento = 0
                        break
                GlobalGameVar.datiEnigmaBibliotecario["reset"] = False
                avanzaIlTurnoSenzaMuoverti = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["risoltoEnigmaBibliotecario"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        bibliotecarioGirato = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"] and personaggio.tipo == "Bibliotecario":
                if personaggio.percorso != ["dGira", "sGira", "mantieniPosizione"]:
                    personaggio.percorso = ["dGira", "sGira", "mantieniPosizione"]
                    personaggio.numeroMovimento = 0
                elif personaggio.direzione == "d":
                    bibliotecarioGirato = "d"
                elif personaggio.direzione == "s":
                    bibliotecarioGirato = "s"
                break
        if bibliotecarioGirato:
            if bibliotecarioGirato == "d":
                pathImgs = "Risorse/Immagini/Scenari/Stanza" + str(stanza) + "/Animazioni/lancioPallaVel" + str(GlobalGameVar.datiEnigmaBibliotecario["velocità"]) + "/"
                coordinateImgAnimata = (GlobalHWVar.gpx * 17, GlobalHWVar.gpy * 11)
                dimensioniImgAnimata = (GlobalHWVar.gpx * 5, GlobalHWVar.gpy * 1)
                listaAudio = [2, GlobalSndVar.rumoreLancioPallaBibliotecario, -1, GlobalSndVar.rumoreRitornoPallaBibliotecario]
                FunzioniGraficheGeneriche.animaEvento(pathImgs, coordinateImgAnimata, dimensioniImgAnimata, listaAudio)
                for personaggio in listaPersonaggiTotali:
                    if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"] and personaggio.tipo == "OggettoEnigmaBiblioteca":
                        listaPersonaggiTotali.remove(personaggio)
                        break
                for personaggio in listaPersonaggi:
                    if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"] and personaggio.tipo == "OggettoEnigmaBiblioteca":
                        listaPersonaggi.remove(personaggio)
                        break
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 11, "s", "OggettoTavoloEnigmaBiblioteca-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                avanzaIlTurnoSenzaMuoverti = True
                carim = True
            if bibliotecarioGirato == "s":
                for personaggio in listaPersonaggi:
                    if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"] and personaggio.tipo == "Bibliotecario":
                        personaggio.percorso = []
                        personaggio.numeroMovimento = 0
                        break
                avanzamentoStoria += 1
                avanzaIlTurnoSenzaMuoverti = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["eseguitaVerificaRisultatoEnigma"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [0], False, posizioneCanaleMusica=0)
        GlobalHWVar.canaleSoundCanzone.stop()
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"] and personaggio.tipo == "Bibliotecario":
                personaggio.percorso = ["s", "a", "a", "w", "w", "w", "w", "w", "d", "w", "fermati"]
                personaggio.numeroMovimento = 0
                break
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["chiestoDiPensareASceltaPassataNelDialogoBibliotecario"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["pensatoASceltaPassataNelDialogoBibliotecario"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoConclusivoEnigmaBibliotecario"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        avanzamentoStoria += 1
        GlobalHWVar.canaleSoundCanzone.play(canzone, -1)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [GlobalHWVar.volumeCanzoni], False, posizioneCanaleMusica=0)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ripartitaMusicaDopoPensatoASceltaPassataNelDialogoBibliotecario"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"] and personaggio.tipo == "Bibliotecario":
                if personaggio.x == GlobalHWVar.gpx * 15 and personaggio.y == GlobalHWVar.gpy * 6:
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoBibliotecarioControlloRegistri"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["biblioteca3"]
        x = GlobalHWVar.gpx * 14
        y = GlobalHWVar.gpx * 12
        npers = 1
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["andatoACercareImpo"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ricercaImpoDiBibliotecario1"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"] and personaggio.tipo == "Bibliotecario":
                if personaggio.x == GlobalHWVar.gpx * 16 and personaggio.y == GlobalHWVar.gpy * 12 and personaggio.direzione == "s":
                    personaggioArrivato = True
                break
        if personaggioArrivato:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
            if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["ricercaImpoDiBibliotecario1"]:
                avanzaIlTurnoSenzaMuoverti = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ricercaImpoDiBibliotecario2"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["biblioteca3"]
        rx = GlobalHWVar.gpx * 15
        ry = GlobalHWVar.gpy * 12
        nrob = 2
        cambiosta = True
        carim = True
        caricaTutto = True
        avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"]:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ricevutoImpoPietra"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = GenericFunc.getStatistiche(dati)
        dati[10] = entot
        GlobalHWVar.canaleSoundAttacco.play(GlobalSndVar.suonoUsoCaricabatterie)
        avanzamentoStoria += 1
        carim = True
        caricaTutto = True
        avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ricaricatoImpoDalBibliotecario"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        dati[32] = 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["introduzioneImpoDalBibliotecario"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Tutorial-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True

    return x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco
