# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.GestioneMenu.MenuDialoghi as MenuDialoghi
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj
import Codice.GestioneNemiciPersonaggi.NemicoObj as NemicoObj


def gestioneEventi(stanza, x, y, avanzamentoStoria, dati, listaAvanzamentoDialoghi, listaPersonaggi, listaPersonaggiTotali, listaNemici, listaNemiciTotali, tutteporte, oggettiRimastiAHans, stanzeGiaVisitate, caricaTutto, cambiosta, carim, canzone, npers, bottoneDown, movimentoPerMouse, oggettoRicevuto, visualizzaMenuMercante, aggiornaImgEquip, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire):
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
        monetePossedute -= 100
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
        for nemico in listaNemici:
            if nemico.tipo == "Cittadino3" and nemico.vita > 0:
                aggressoreAncoraVivo = True
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
            avanzamentoStoria += 1
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
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uccisoPrimoAggressore"] and stanza == GlobalGameVar.dictStanze["città4"]:
        aggressoreAncoraVivo = False
        for nemico in listaNemici:
            if nemico.tipo == "Cittadino1" and nemico.vita > 0:
                aggressoreAncoraVivo = True
                break
        if not aggressoreAncoraVivo:
            avanzamentoStoria += 1
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uccisoSecondoAggressore"] and stanza == GlobalGameVar.dictStanze["città4"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno-0", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = MenuDialoghi.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True

    return avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, stanzeGiaVisitate, avanzaIlTurnoSenzaMuoverti, nonMostrarePersonaggio, monetePossedute, percorsoDaEseguire
