# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.GestioneMenu.MenuDialoghi as MenuDialoghi
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj
import Codice.GestioneNemiciPersonaggi.NemicoObj as NemicoObj


def gestioneEventi(stanza, x, y, rx, ry, nrob, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, casevisteEntrateIncluse, equipaggiamentoIndossato, chiamarob, ultimoObbiettivoColco):
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["entratoInCittà"] and stanza == GlobalGameVar.dictStanze["città1"]:
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "PadreUfficialeServizio-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
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
            carim = True
            caricaTutto = True
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumorePortoniCambioStanza)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoDopoAlzatoDalLetto"] and stanza == GlobalGameVar.dictStanze["città4"]:
        # resetto avanzamento dialoghi dei 2 soldati all'ingresso città1
        i = 0
        while i < len(listaAvanzamentoDialoghi):
            if listaAvanzamentoDialoghi[i] == "GuardiaCitta-0" or listaAvanzamentoDialoghi[i] == "GuardiaCitta-1":
                listaAvanzamentoDialoghi[i + 1] = 0
            i += 2
        for personaggio in listaPersonaggi:
            i = 0
            while i < len(listaAvanzamentoDialoghi):
                if personaggio.tipoId == listaAvanzamentoDialoghi[i]:
                    personaggio.avanzamentoDialogo = listaAvanzamentoDialoghi[i + 1]
                    break
                i += 2
        for personaggio in listaPersonaggiTotali:
            i = 0
            while i < len(listaAvanzamentoDialoghi):
                if personaggio.tipoId == listaAvanzamentoDialoghi[i]:
                    personaggio.avanzamentoDialogo = listaAvanzamentoDialoghi[i + 1]
                    break
                i += 2

        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["chiestoDegliAlloggiAlMercante"] and stanza == GlobalGameVar.dictStanze["città6"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["cercatoHansInAlloggiProfughi"] and stanza == GlobalGameVar.dictStanze["città6"]:
        # resetto avanzamento dialoghi di tutti i cittadini a cui chiedo informazioni
        i = 0
        while i < len(listaAvanzamentoDialoghi):
            if listaAvanzamentoDialoghi[i] == "Ragazzo2-2":
                listaAvanzamentoDialoghi[i + 1] = 0
            elif listaAvanzamentoDialoghi[i] == "Ragazzo3-1":
                listaAvanzamentoDialoghi[i + 1] = 0
            i += 2
        for personaggio in listaPersonaggi:
            i = 0
            while i < len(listaAvanzamentoDialoghi):
                if personaggio.tipoId == listaAvanzamentoDialoghi[i]:
                    personaggio.avanzamentoDialogo = listaAvanzamentoDialoghi[i + 1]
                    break
                i += 2
        for personaggio in listaPersonaggiTotali:
            i = 0
            while i < len(listaAvanzamentoDialoghi):
                if personaggio.tipoId == listaAvanzamentoDialoghi[i]:
                    personaggio.avanzamentoDialogo = listaAvanzamentoDialoghi[i + 1]
                    break
                i += 2

        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dateMonetePerEntrareInConfraternita"] and stanza == GlobalGameVar.dictStanze["città5"]:
        monetePossedute -= GlobalGameVar.monetePerEntrareNellaConfraternita
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ricevutoCertificatoDalServo"] and stanza == GlobalGameVar.dictStanze["città4"]:
        GlobalHWVar.canaleSoundCanzone.play(canzone, -1)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [GlobalHWVar.volumeCanzoni], False, posizioneCanaleMusica=0)
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoCasaDavidDopoSuicidio"] and stanza == GlobalGameVar.dictStanze["città4"]:
        arrivatoDaAggressore = False
        for personaggio in listaPersonaggi:
            if personaggio.tipoId == "Ragazzo1-2":
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
                if personaggio.tipoId == "Ragazzo1-2":
                    if personaggio.percorso != ["aGira", "mantieniPosizione"]:
                        personaggio.percorso = ["aGira", "mantieniPosizione"]
                        personaggio.numeroMovimento = 0
                        avanzaIlTurnoSenzaMuoverti = True
                    break
            if not avanzaIlTurnoSenzaMuoverti:
                GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [0], False, posizioneCanaleMusica=0)
                GlobalHWVar.canaleSoundCanzone.stop()
                personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Ragazzo1-2", stanza, avanzamentoStoria, False)
                avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
                caricaTutto = True
                if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["uscitoCasaDavidDopoSuicidio"]:
                    for personaggio in listaPersonaggi:
                        if personaggio.tipoId == "Ragazzo3-2":
                            listaPersonaggi.remove(personaggio)
                            break
                    for personaggio in listaPersonaggiTotali:
                        if personaggio.tipoId == "Ragazzo3-2":
                            listaPersonaggiTotali.remove(personaggio)
                            break
                    percorsoNemico = []
                    nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 13, "d", "Cittadino3", stanza, percorsoNemico)
                    nemico.mosseRimaste = -1
                    listaNemiciTotali.append(nemico)
                    listaNemici.append(nemico)

                    percorsoDaEseguire = ["a"]
                    carim = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["incontratoIDueAggressori"] and stanza == GlobalGameVar.dictStanze["città4"]:
        if not GlobalHWVar.canaleSoundBattitoCardiaco.get_busy():
            GlobalHWVar.canaleSoundBattitoCardiaco.play(GlobalSndVar.rumoreBattitoCardiaco, -1)
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
                if personaggio.tipoId == "Ragazzo1-2":
                    if x == GlobalHWVar.gpx * 20 and personaggio.y == y:
                        personaggio.percorso = ["aGira", "mantieniPosizione"]
                        personaggio.numeroMovimento = 0
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
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Ragazzo1-2", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["uccisoPrimoAggressore"]:
            ySpawnSecondoAggressore = GlobalHWVar.gsy // 18 * 13
            for personaggio in listaPersonaggi:
                if personaggio.tipoId == "Ragazzo1-2":
                    listaPersonaggi.remove(personaggio)
                    break
            for personaggio in listaPersonaggiTotali:
                if personaggio.tipoId == "Ragazzo1-2":
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
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["uccisoSecondoAggressore"]:
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
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoDopoUccisioneAggressori"] and stanza == GlobalGameVar.dictStanze["città4"]:
        if x == GlobalHWVar.gpx * 27:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumorePortoniCambioStanza)
            percorsoPersonaggio = ["s"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gpx * 12, GlobalHWVar.gpy * 5, "s", "GuardiaCitta-18", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggiTotali.append(personaggio)
            listaPersonaggi.append(personaggio)
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoPrimaGuardia"] and stanza == GlobalGameVar.dictStanze["città4"]:
        if x == GlobalHWVar.gpx * 28:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumorePortoniCambioStanza)
            percorsoPersonaggio = ["s"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gpx * 11, GlobalHWVar.gpy * 5, "s", "GuardiaCitta-18", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggiTotali.append(personaggio)
            listaPersonaggi.append(personaggio)
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoSecondaGuardia"] and stanza == GlobalGameVar.dictStanze["città3"]:
        percorsoDaEseguire = ["d", "d", "d", "d", "d", "d", "w", "w", "w", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "w", "d", "d", "d", "d", "d", "w"]
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["fuggitoVersoCittà5"] and stanza == GlobalGameVar.dictStanze["città3"]:
        mercanteArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "Mercante":
                if personaggio.x == GlobalHWVar.gpx * 29 and personaggio.y == GlobalHWVar.gpy * 9:
                    mercanteArrivato = True
                break

        if mercanteArrivato:
            for personaggio in listaPersonaggi:
                if personaggio.tipo == "Mercante":
                    listaPersonaggi.remove(personaggio)
                    break
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["città3"] and personaggio.tipo == "Mercante":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            avanzamentoStoria += 1
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["mercanteFuggitoDopoOmicidio"] and stanza == GlobalGameVar.dictStanze["città5"]:
        percorsoDaEseguire = ["d", "d", "w", "w", "w", "d", "w", "d", "w", "d", "d", "d", "w", "w", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "w", "d", "d", "w", "d", "d"]
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["fuggitoVersoCittà7"] and stanza == GlobalGameVar.dictStanze["città7"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and stanza == GlobalGameVar.dictStanze["città7"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoUscitaSelvaAridaCercandoRod"] and stanza == GlobalGameVar.dictStanze["città9"]:
        i = 0
        while i < 5:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["monologoUscitaSelvaAridaCercandoRod"]:
            # resetto avanzamento dialoghi di tutti i cittadini che rimangono in città
            i = 0
            while i < len(listaAvanzamentoDialoghi):
                if listaAvanzamentoDialoghi[i] == "Ragazza3-0":
                    listaAvanzamentoDialoghi[i + 1] = 0
                elif listaAvanzamentoDialoghi[i] == "Ragazza1-1":
                    listaAvanzamentoDialoghi[i + 1] = 0
                elif listaAvanzamentoDialoghi[i] == "Ragazzo1-0":
                    listaAvanzamentoDialoghi[i + 1] = 0
                elif listaAvanzamentoDialoghi[i] == "Ragazzo2-2":
                    listaAvanzamentoDialoghi[i + 1] = 0
                elif listaAvanzamentoDialoghi[i] == "Ragazzo3-3":
                    listaAvanzamentoDialoghi[i + 1] = 0
                elif listaAvanzamentoDialoghi[i] == "Ragazzo1-4":
                    listaAvanzamentoDialoghi[i + 1] = 0
                elif listaAvanzamentoDialoghi[i] == "Ragazzo2-4":
                    listaAvanzamentoDialoghi[i + 1] = 0
                i += 2
            for personaggio in listaPersonaggi:
                i = 0
                while i < len(listaAvanzamentoDialoghi):
                    if personaggio.tipoId == listaAvanzamentoDialoghi[i]:
                        personaggio.avanzamentoDialogo = listaAvanzamentoDialoghi[i + 1]
                        break
                    i += 2
            for personaggio in listaPersonaggiTotali:
                i = 0
                while i < len(listaAvanzamentoDialoghi):
                    if personaggio.tipoId == listaAvanzamentoDialoghi[i]:
                        personaggio.avanzamentoDialogo = listaAvanzamentoDialoghi[i + 1]
                        break
                    i += 2
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoInCitta9CercandoRod"] and stanza == GlobalGameVar.dictStanze["città5"]:
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoImpo-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True

    return x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco
