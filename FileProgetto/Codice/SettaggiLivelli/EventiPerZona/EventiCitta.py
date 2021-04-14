# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.GestioneMenu.MenuDialoghi as MenuDialoghi
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj
import Codice.GestioneNemiciPersonaggi.NemicoObj as NemicoObj


def gestioneEventi(stanza, x, y, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse):
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["entratoInCittà"] and stanza == GlobalGameVar.dictStanze["città1"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "PadreUfficialeServizio-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["primoDialogoDavid"] and stanza == GlobalGameVar.dictStanze["città1"]:
        padreUfficialeArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "PadreUfficialeServizio":
                if personaggio.x == GlobalHWVar.gpx * 2 and personaggio.y == GlobalHWVar.gpy * 7:
                    padreUfficialeArrivato = True
                break

        if padreUfficialeArrivato:
            for personaggio in listaPersonaggi:
                if personaggio.tipo == "PadreUfficialeServizio":
                    listaPersonaggi.remove(personaggio)
                    break
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["città1"] and personaggio.tipo == "PadreUfficialeServizio":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            avanzamentoStoria += 1
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCittà2"] and stanza == GlobalGameVar.dictStanze["città2"]:
        padreUfficialeArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "PadreUfficialeServizio":
                if personaggio.x == GlobalHWVar.gpx * 2 and personaggio.y == GlobalHWVar.gpy * 7:
                    padreUfficialeArrivato = True
                break

        if padreUfficialeArrivato:
            for personaggio in listaPersonaggi:
                if personaggio.tipo == "PadreUfficialeServizio":
                    listaPersonaggi.remove(personaggio)
                    break
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["città2"] and personaggio.tipo == "PadreUfficialeServizio":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            avanzamentoStoria += 1
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCittà3"] and stanza == GlobalGameVar.dictStanze["città3"]:
        padreUfficialeArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "PadreUfficialeServizio":
                if personaggio.x == GlobalHWVar.gpx * 2 and personaggio.y == GlobalHWVar.gpy * 8:
                    padreUfficialeArrivato = True
                break

        if padreUfficialeArrivato:
            for personaggio in listaPersonaggi:
                if personaggio.tipo == "PadreUfficialeServizio":
                    listaPersonaggi.remove(personaggio)
                    break
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["città3"] and personaggio.tipo == "PadreUfficialeServizio":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            avanzamentoStoria += 1
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCittà4"] and stanza == GlobalGameVar.dictStanze["città4"]:
        padreUfficialeArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "PadreUfficialeServizio":
                if personaggio.x == GlobalHWVar.gpx * 12 and personaggio.y == GlobalHWVar.gpy * 5:
                    padreUfficialeArrivato = True
                break

        if padreUfficialeArrivato:
            for personaggio in listaPersonaggi:
                if personaggio.tipo == "PadreUfficialeServizio":
                    listaPersonaggi.remove(personaggio)
                    break
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["città4"] and personaggio.tipo == "PadreUfficialeServizio":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            avanzamentoStoria += 1
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoDopoAlzatoDalLetto"] and stanza == GlobalGameVar.dictStanze["città4"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["chiestoDegliAlloggiAlMercante"] and stanza == GlobalGameVar.dictStanze["città6"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["date100MoneteAlMercante"] and stanza == GlobalGameVar.dictStanze["città5"]:
        monetePossedute -= 300
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ricevutoCertificatoDalServo"] and stanza == GlobalGameVar.dictStanze["città4"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoCasaDavidDopoSuicidio"] and stanza == GlobalGameVar.dictStanze["città4"]:
        arrivatoDaAggressore = False
        for personaggio in listaPersonaggi:
            if personaggio.tipoId == "Ragazzo1-6":
                if x == GlobalHWVar.gpx * 20 and personaggio.y == y:
                    arrivatoDaAggressore = True
                elif x >= GlobalHWVar.gpx * 16 and personaggio.y > y:
                    personaggio.percorso = ["w", "aGira", "mantieniPosizione"]
                    personaggio.numeroMovimento = 0
                elif x >= GlobalHWVar.gpx * 16 and personaggio.y < y:
                    personaggio.percorso = ["s", "aGira", "mantieniPosizione"]
                    personaggio.numeroMovimento = 0
                break

        if arrivatoDaAggressore:
            for personaggio in listaPersonaggi:
                if personaggio.tipoId == "Ragazzo1-6":
                    if personaggio.percorso != ["a", "mantieniPosizione"]:
                        personaggio.percorso = ["a", "mantieniPosizione"]
                        personaggio.numeroMovimento = 1
                        avanzaIlTurnoSenzaMuoverti = True
                    break
            if not avanzaIlTurnoSenzaMuoverti:
                i = GlobalHWVar.volumeCanzoni
                while i > 0:
                    GlobalHWVar.canaleSoundCanzone.set_volume(i)
                    i -= GlobalHWVar.volumeCanzoni / 10
                    pygame.time.wait(30)
                    inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                GlobalHWVar.canaleSoundCanzone.set_volume(0)
                GlobalHWVar.canaleSoundCanzone.stop()

                personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Ragazzo1-6", stanza, avanzamentoStoria, False)
                avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)

                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["incontratoIDueAggressori"]:
                    for personaggio in listaPersonaggi:
                        if personaggio.tipoId == "Ragazzo3-4":
                            listaPersonaggi.remove(personaggio)
                            break
                    for personaggio in listaPersonaggiTotali:
                        if personaggio.tipoId == "Ragazzo3-4":
                            listaPersonaggiTotali.remove(personaggio)
                            break
                    percorsoNemico = []
                    nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 13, "d", "Cittadino3", stanza, percorsoNemico)
                    nemico.mosseRimaste = -1
                    listaNemiciTotali.append(nemico)
                    listaNemici.append(nemico)

                    percorsoDaEseguire = ["a"]
                    carim = True
                caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["incontratoIDueAggressori"] and stanza == GlobalGameVar.dictStanze["città4"]:
        aggressoreAncoraVivo = False
        spawnCadavereX = 0
        spawnCadavereY = 0
        for nemico in listaNemici:
            if nemico.tipo == "Cittadino3":
                if nemico.vita > 0:
                    aggressoreAncoraVivo = True
                spawnCadavereX = nemico.x
                spawnCadavereY = nemico.y
                break
        if aggressoreAncoraVivo:
            for personaggio in listaPersonaggi:
                if personaggio.tipoId == "Ragazzo1-6":
                    if x == GlobalHWVar.gpx * 20 and personaggio.y == y:
                        personaggio.percorso = ["a", "mantieniPosizione"]
                        personaggio.numeroMovimento = 1
                    elif x >= GlobalHWVar.gpx * 16 and personaggio.y > y:
                        personaggio.percorso = ["w", "aGira", "mantieniPosizione"]
                        personaggio.numeroMovimento = 0
                    elif x >= GlobalHWVar.gpx * 16 and personaggio.y < y:
                        personaggio.percorso = ["s", "aGira", "mantieniPosizione"]
                        personaggio.numeroMovimento = 0
                    break
        else:
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(spawnCadavereX, spawnCadavereY, "s", "OggettoPersonaCittadino3Cadavere-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggiTotali.append(personaggio)
            listaPersonaggi.append(personaggio)
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uccisoPrimoAggressore"] and stanza == GlobalGameVar.dictStanze["città4"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Ragazzo1-6", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)

        ySpawnSecondoAggressore = GlobalHWVar.gsy // 18 * 13
        for personaggio in listaPersonaggi:
            if personaggio.tipoId == "Ragazzo1-6":
                listaPersonaggi.remove(personaggio)
                break
        for personaggio in listaPersonaggiTotali:
            if personaggio.tipoId == "Ragazzo1-6":
                ySpawnSecondoAggressore = personaggio.y
                listaPersonaggiTotali.remove(personaggio)
                break
        percorsoNemico = []
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 21, ySpawnSecondoAggressore, "a", "Cittadino1", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)

        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoDopoPrimoOmicidio"] and stanza == GlobalGameVar.dictStanze["città4"]:
        aggressoreAncoraVivo = False
        spawnCadavereX = 0
        spawnCadavereY = 0
        for nemico in listaNemici:
            if nemico.tipo == "Cittadino1":
                if nemico.vita > 0:
                    aggressoreAncoraVivo = True
                spawnCadavereX = nemico.x
                spawnCadavereY = nemico.y
                break
        if not aggressoreAncoraVivo:
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(spawnCadavereX, spawnCadavereY, "s", "OggettoPersonaCittadino1Cadavere-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggiTotali.append(personaggio)
            listaPersonaggi.append(personaggio)
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uccisoSecondoAggressore"] and stanza == GlobalGameVar.dictStanze["città4"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)

        vetNemiciSoloConXeY = []
        for personaggio in listaPersonaggi:
            vetNemiciSoloConXeY.append(personaggio.x)
            vetNemiciSoloConXeY.append(personaggio.y)
        xDestinazione = GlobalHWVar.gpx * 29
        yDestinazione = GlobalHWVar.gpy * 12
        percorsoTrovato = GenericFunc.pathFinding(x, y, xDestinazione, yDestinazione, vetNemiciSoloConXeY, casevisteEntrateIncluse)
        if percorsoTrovato and percorsoTrovato != "arrivato" and len(percorsoTrovato) >= 4 and (percorsoTrovato[len(percorsoTrovato) - 4] != x or percorsoTrovato[len(percorsoTrovato) - 3] != y):
            xVirtuale = x
            yVirtuale = y
            i = len(percorsoTrovato) - 2
            while i >= 0:
                if percorsoTrovato[i] > xVirtuale:
                    percorsoDaEseguire.append("d")
                elif percorsoTrovato[i] < xVirtuale:
                    percorsoDaEseguire.append("a")
                elif percorsoTrovato[i + 1] > yVirtuale:
                    percorsoDaEseguire.append("s")
                elif percorsoTrovato[i + 1] < yVirtuale:
                    percorsoDaEseguire.append("w")
                xVirtuale = percorsoTrovato[i]
                yVirtuale = percorsoTrovato[i + 1]
                i -= 2
            if xVirtuale == GlobalHWVar.gpx * 28:
                percorsoDaEseguire.append("d")
                percorsoDaEseguire.append("d")
            elif yVirtuale == GlobalHWVar.gpy * 11:
                percorsoDaEseguire.append("s")
                percorsoDaEseguire.append("d")
            elif yVirtuale == GlobalHWVar.gpy * 13:
                percorsoDaEseguire.append("w")
                percorsoDaEseguire.append("d")
        else:
            print ("Percorso Rallo verso uscita città4 non trovato")
            percorsoDaEseguire = []

        caricaTutto = True

    # togli la musica quando non desiderata (serve farlo in continuazione per evitare che riprenda quando carichi il salvataggio)
    if GlobalGameVar.dictAvanzamentoStoria["incontratoIDueAggressori"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["mostratoCertificatoPerIngressoBiblioteca"]:
        if GlobalHWVar.canaleSoundCanzone.get_busy():
            i = GlobalHWVar.volumeCanzoni
            while i > 0:
                GlobalHWVar.canaleSoundCanzone.set_volume(i)
                i -= GlobalHWVar.volumeCanzoni / 10
                pygame.time.wait(30)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            GlobalHWVar.canaleSoundCanzone.set_volume(0)
            GlobalHWVar.canaleSoundCanzone.stop()

    return avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire
