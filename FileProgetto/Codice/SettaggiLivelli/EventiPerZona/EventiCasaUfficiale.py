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
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoCasaUfficiale"] and stanza == GlobalGameVar.dictStanze["casaDavid1"]:
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "PadreUfficialeServizio-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["arrivoCasaUfficiale"]:
            GlobalHWVar.canaleSoundCanzone.play(canzone, -1)
            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [GlobalHWVar.volumeCanzoni], False, posizioneCanaleMusica=0)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoArrivoCasaConDavid"] and stanza == GlobalGameVar.dictStanze["casaDavid1"]:
        padreArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "PadreUfficialeServizio":
                if personaggio.x == GlobalHWVar.gpx * 28 and personaggio.y == GlobalHWVar.gpy * 11:
                    padreArrivato = True
                break

        if padreArrivato:
            for personaggio in listaPersonaggi:
                if personaggio.tipo == "PadreUfficialeServizio":
                    listaPersonaggi.remove(personaggio)
                    break
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"] and personaggio.tipo == "PadreUfficialeServizio":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            avanzamentoStoria += 1
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoDavidPrimoPiano"] and stanza == GlobalGameVar.dictStanze["casaDavid2"]:
        padreArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "PadreUfficialeServizio":
                if personaggio.x == GlobalHWVar.gpx * 21 and personaggio.y == GlobalHWVar.gpy * 4:
                    padreArrivato = True
                break

        if padreArrivato:
            for personaggio in listaPersonaggi:
                if personaggio.tipo == "PadreUfficialeServizio":
                    personaggio.percorso = ["sGira", "mantieniPosizione"]
                    personaggio.numeroMovimento = 0
                    personaggio.girati("s")
                    break
            avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["presaChiaveStanzaDaLettoDavid"] and stanza == GlobalGameVar.dictStanze["casaDavid2"]:
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "PadreUfficialeServizio":
                personaggio.percorso = ["aGira", "mantieniPosizione"]
                personaggio.numeroMovimento = 0
            if personaggio.tipo == "ServoDavid" and personaggio.x == GlobalHWVar.gpx * 19 and personaggio.y == GlobalHWVar.gpx * 2:
                personaggio.percorso = ["s", "s", "d", "mantieniPosizione"]
                personaggio.numeroMovimento = 0
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioBagnoCasaDavid"] and stanza == GlobalGameVar.dictStanze["casaDavid3"]:
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [0], False, posizioneCanaleMusica=0)
        GlobalHWVar.canaleSoundCanzone.stop()
        dati[6] = 0
        dati[7] = 0
        dati[8] = 0
        dati[128] = 0
        dati[129] = 0
        dati[130] = 0
        esptot, pvtot, entot, attVicino, attLontano, dif, difro, par = GenericFunc.getStatistiche(dati)
        if dati[5] > pvtot:
            dati[5] = pvtot
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["casaDavid3"]
        cambiosta = True
        carim = True
        aggiornaImgEquip = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["fattoBagnoCasaDavid"] and stanza == GlobalGameVar.dictStanze["casaDavid3"]:
        GlobalHWVar.canaleSoundCanzone.play(canzone, -1)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [GlobalHWVar.volumeCanzoni], False, posizioneCanaleMusica=0)
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPreCambioPerCenaDavid"] and stanza == GlobalGameVar.dictStanze["casaDavid3"]:
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["casaDavid3"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"] and stanza == GlobalGameVar.dictStanze["casaDavid3"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sedutoACenaDavid"] and stanza == GlobalGameVar.dictStanze["casaDavid2"]:
        for personaggio in listaPersonaggiTotali:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and personaggio.tipo == "PadreUfficialeCasa":
                listaPersonaggiTotali.remove(personaggio)
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and personaggio.tipo == "MadreUfficiale":
                listaPersonaggiTotali.remove(personaggio)
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and personaggio.tipo == "PadreUfficialeCasa":
                listaPersonaggi.remove(personaggio)
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and personaggio.tipo == "MadreUfficiale":
                listaPersonaggi.remove(personaggio)
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["casaDavid2"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["cenaConDavidIniziata"] and stanza == GlobalGameVar.dictStanze["casaDavid2"]:
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "PadreUfficialeCasa-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoCenaDavid1"] and stanza == GlobalGameVar.dictStanze["casaDavid2"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "MadreUfficiale-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoCenaDavid2"] and stanza == GlobalGameVar.dictStanze["casaDavid2"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "PadreUfficialeCasa-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [0], False, posizioneCanaleMusica=0)
        GlobalHWVar.canaleSoundCanzone.stop()
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoCenaDavid3"] and stanza == GlobalGameVar.dictStanze["casaDavid2"]:
        personaggioGiaCreato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "MadreUfficiale":
                personaggioGiaCreato = True
                break
        if not personaggioGiaCreato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and personaggio.tipo == "OggettoMadreUfficialeSeduta":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and personaggio.tipo == "OggettoMadreUfficialeSeduta":
                    listaPersonaggi.remove(personaggio)
                    break
            percorsoPersonaggio = ["w", "w", "w", "w", "d", "w"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gpx * 8, GlobalHWVar.gpy * 7, "w", "MadreUfficiale-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggiTotali.append(personaggio)
            listaPersonaggi.append(personaggio)
            avanzaIlTurnoSenzaMuoverti = True
            carim = True
            caricaTutto = True
        else:
            personaggioArrivato = False
            for personaggio in listaPersonaggi:
                if personaggio.tipo == "MadreUfficiale" and personaggio.x == GlobalHWVar.gpx * 9 and personaggio.y == GlobalHWVar.gpy * 2:
                    personaggioArrivato = True
                    break
            if personaggioArrivato:
                for personaggio in listaPersonaggiTotali:
                    if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and personaggio.tipo == "MadreUfficiale":
                        listaPersonaggiTotali.remove(personaggio)
                        break
                for personaggio in listaPersonaggi:
                    if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and personaggio.tipo == "MadreUfficiale":
                        listaPersonaggi.remove(personaggio)
                        break
                GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumorePortoniCambioStanza)
                avanzamentoStoria += 1
                carim = True
                caricaTutto = True
            else:
                avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["mammaUfficialeUscitaDallaCena"] and stanza == GlobalGameVar.dictStanze["casaDavid2"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "PadreUfficialeCasa-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoCenaDavid4"] and stanza == GlobalGameVar.dictStanze["casaDavid2"]:
        personaggioGiaCreato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "PadreUfficialeCasa":
                personaggioGiaCreato = True
                break
        if not personaggioGiaCreato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and personaggio.tipo == "OggettoPadreUfficialeSeduto":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and personaggio.tipo == "OggettoPadreUfficialeSeduto":
                    listaPersonaggi.remove(personaggio)
                    break
            percorsoPersonaggio = ["d", "w", "d", "w", "d", "w", "d", "d", "d", "d", "sGira"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gpx * 20, GlobalHWVar.gpy * 7, "w", "PadreUfficialeCasa-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggiTotali.append(personaggio)
            listaPersonaggi.append(personaggio)
            avanzaIlTurnoSenzaMuoverti = True
            carim = True
            caricaTutto = True
        else:
            personaggioArrivato = False
            for personaggio in listaPersonaggi:
                if personaggio.tipo == "PadreUfficialeCasa" and personaggio.x == GlobalHWVar.gpx * 27 and personaggio.y == GlobalHWVar.gpy * 4 and personaggio.direzione == "s":
                    personaggioArrivato = True
                    break
            if personaggioArrivato:
                for personaggio in listaPersonaggiTotali:
                    if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and personaggio.tipo == "PadreUfficialeCasa":
                        listaPersonaggiTotali.remove(personaggio)
                        break
                for personaggio in listaPersonaggi:
                    if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and personaggio.tipo == "PadreUfficialeCasa":
                        listaPersonaggi.remove(personaggio)
                        break
                avanzamentoStoria += 1
                carim = True
                caricaTutto = True
            else:
                avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["padreUfficialeUscitoDallaCena"] and stanza == GlobalGameVar.dictStanze["casaDavid2"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["padreUfficialeUscitoDallaCena"]:
            # avanzo col dialogo il servo nella prima stanza (senn?? si bugga il dialogo)
            for personaggio in listaPersonaggiTotali:
                if personaggio.tipo == "ServoDavid" and personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"]:
                    personaggio.avanzamentoDialogo = 1
                    break
            i = 0
            while i < len(listaAvanzamentoDialoghi):
                if listaAvanzamentoDialoghi[i] == "ServoDavid-0":
                    listaAvanzamentoDialoghi[i + 1] = 1
                    break
                i += 2
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["andatoADormireCasaDavid"] and stanza == GlobalGameVar.dictStanze["casaDavid3"]:
        avanzamentoStoria += 1
        # chiudo tutte le porte di casaHansSara tranne la cameretta + apro la cameretta
        i = 0
        while i < len(tutteporte):
            if tutteporte[i] == GlobalGameVar.dictStanze["casaHansSara1"] and not (tutteporte[i + 1] == GlobalHWVar.gpx * 6 and tutteporte[i + 2] == GlobalHWVar.gpx * 9):
                tutteporte[i + 3] = False
            elif tutteporte[i] == GlobalGameVar.dictStanze["casaHansSara1"] and (tutteporte[i + 1] == GlobalHWVar.gpx * 6 and tutteporte[i + 2] == GlobalHWVar.gpx * 9):
                tutteporte[i + 3] = True
            i += 4
        # tolgo l'equipaggiamento (spada, scudo, armatura, arco, guanti e collana)
        dati[6] = 0
        dati[7] = 0
        dati[8] = 0
        dati[128] = 0
        dati[129] = 0
        dati[130] = 0
        stanza = GlobalGameVar.dictStanze["casaHansSara1"]
        cambiosta = True
        carim = True
        aggiornaImgEquip = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and stanza == GlobalGameVar.dictStanze["casaDavid3"]:
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "ServoDavid-2", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoServoRisveglioSecondoGiorno"] and stanza == GlobalGameVar.dictStanze["casaDavid3"]:
        nonMostrarePersonaggio = False
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["casaDavid3"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["alzatoDalLettoSecondoGiorno"] and stanza == GlobalGameVar.dictStanze["casaDavid3"]:
        GlobalHWVar.canaleSoundCanzone.play(canzone, -1)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [GlobalHWVar.volumeCanzoni], False, posizioneCanaleMusica=0)
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["rifiutatoDallaBiblioteca"] and stanza == GlobalGameVar.dictStanze["casaDavid2"] and x == GlobalHWVar.gpx * 25:
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "ServoDavid":
                if personaggio.percorso != ["d"]:
                    personaggio.percorso = ["d"]
                    personaggio.numeroMovimento = 0
                break
        avanzaIlTurnoSenzaMuoverti = True
        avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["vistoDalServo"] and stanza == GlobalGameVar.dictStanze["casaDavid2"]:
        servoArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "ServoDavid":
                if personaggio.x == GlobalHWVar.gpx * 24:
                    servoArrivato = True
                break
        if servoArrivato:
            GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [0], False, posizioneCanaleMusica=0)
            GlobalHWVar.canaleSoundCanzone.stop()
            personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "ServoDavid-1", stanza, avanzamentoStoria, False)
            avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
            caricaTutto = True
        else:
            avanzaIlTurnoSenzaMuoverti = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoServoCasaDavidDopoSuicidio"] and stanza == GlobalGameVar.dictStanze["casaDavid2"]:
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and personaggio.tipo == "ServoDavid":
                if personaggio.percorso != ["a", "a", "a", "a", "w", "w"]:
                    personaggio.percorso = ["a", "a", "a", "a", "w", "w"]
                    personaggio.numeroMovimento = 0
                break
        personaggioArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and personaggio.tipo == "ServoDavid" and personaggio.x == GlobalHWVar.gpx * 20 and personaggio.y == GlobalHWVar.gpy * 2:
                personaggioArrivato = True
                break
        if personaggioArrivato:
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and personaggio.tipo == "ServoDavid":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            for personaggio in listaPersonaggi:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and personaggio.tipo == "ServoDavid":
                    listaPersonaggi.remove(personaggio)
                    break
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumorePortoniCambioStanza)
            avanzamentoStoria += 1
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoConGuardiaCasaDavid"] and stanza == GlobalGameVar.dictStanze["casaDavid2"] and y == GlobalHWVar.gpy * 3 and (x == GlobalHWVar.gpx * 19 or x == GlobalHWVar.gpx * 20 or x == GlobalHWVar.gpx * 21):
        spawnServoX = GlobalHWVar.gpx * 20
        spawnServoY = GlobalHWVar.gpy * 2
        npers = 3
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(spawnServoX, spawnServoY, "s", "ServoDavid-1", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggiTotali.append(personaggio)
        listaPersonaggi.append(personaggio)
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumorePortoniCambioStanza)
        avanzamentoStoria += 1
        avanzaIlTurnoSenzaMuoverti = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["servoArrivaConCertificazione"] and stanza == GlobalGameVar.dictStanze["casaDavid2"]:
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "ServoDavid-1", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi, canzone)
        caricaTutto = True

    return x, y, rx, ry, nrob, avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, porte, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, evitaTurnoDiColco, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire, chiamarob, ultimoObbiettivoColco, avanzaManualmentePercorsoDaEseguire
