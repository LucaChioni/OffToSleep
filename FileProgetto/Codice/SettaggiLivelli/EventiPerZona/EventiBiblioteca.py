# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.GestioneMenu.MenuDialoghi as MenuDialoghi
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche


def gestioneEventi(stanza, x, y, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse):
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["rimosse300Monete"] and stanza == GlobalGameVar.dictStanze["biblioteca1"] and y == GlobalHWVar.gpy * 11:
        screen = GlobalHWVar.schermo.copy().convert()
        if npers != 2:
            npers = 2
            avanzaIlTurnoSenzaMuoverti = True
            carim = True
        if not avanzaIlTurnoSenzaMuoverti:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "AssistBiblioteca-0", stanza, avanzamentoStoria, False)
            while avanzamentoStoria != GlobalGameVar.dictAvanzamentoStoria["rifiutatoDallaBiblioteca"]:
                avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
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
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
            percorsoDaEseguire = ["s"]
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoDopoArrivoInBiblioteca"] and stanza == GlobalGameVar.dictStanze["biblioteca1"] and y == GlobalHWVar.gpy * 11:
        if npers != 2:
            npers = 2
            avanzaIlTurnoSenzaMuoverti = True
            carim = True
        if not avanzaIlTurnoSenzaMuoverti:
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "AssistBiblioteca-0", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
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
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
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
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.suonoRaccoltaOggetto)
            caricaTutto = True
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
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
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
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
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
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["vomitatoInBiblioteca"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoBibliotecarioPostVomito"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        nonMostrarePersonaggio = True
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["biblioteca3"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sedutaInBiblioteca"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Bibliotecario-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
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
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
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
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tranquillizzataDopoDialogoBibliotecario"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        nonMostrarePersonaggio = False
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["biblioteca3"]
        x = GlobalHWVar.gpx * 19
        y = GlobalHWVar.gpy * 7
        npers = 2
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["alzataDallaSediaInBiblioteca"] and stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        avanzamentoStoria += 1
        GlobalHWVar.canaleSoundCanzone.set_volume(0)
        GlobalHWVar.canaleSoundCanzone.play(canzone, -1)
        i = 0
        while i < GlobalHWVar.volumeCanzoni:
            GlobalHWVar.canaleSoundCanzone.set_volume(i)
            i += GlobalHWVar.volumeCanzoni / 10
            pygame.time.wait(30)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
        GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni)
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
            listaAudio = [0, GlobalSndVar.rumoreScavare]
            FunzioniGraficheGeneriche.animaEvento(pathImgs, coordinateImgAnimata, listaAudio)

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
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
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
            listaAudio = [0, GlobalSndVar.rumoreScavare]
            FunzioniGraficheGeneriche.animaEvento(pathImgs, coordinateImgAnimata, listaAudio)

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
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
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
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["spiegazioneEnigmaBibliotecario4"] and stanza == GlobalGameVar.dictStanze["biblioteca3"] and GlobalGameVar.datiEnigmaBibliotecario["reset"]:
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

    return x, y, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire
