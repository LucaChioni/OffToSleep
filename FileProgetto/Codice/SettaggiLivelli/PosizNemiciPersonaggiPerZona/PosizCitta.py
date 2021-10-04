# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj


def setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria):
    return listaNemiciTotali, listaNemici


def setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi):
    if stanza == GlobalGameVar.dictStanze["città1"]:
        percorsoPersonaggio = ["sGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 2, "s", "GuardiaCitta-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["wGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 15, "w", "GuardiaCitta-1", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["entratoInCittà"]:
            percorsoPersonaggio = ["w", "w", "w", "w", "w", "", "", "a", "s", "s", "s", "s", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 8, "d", "PadreUfficialeServizio-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            percorsoPersonaggio = ["sGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 5, "s", "GuardiaCitta-2", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["wGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 12, "w", "GuardiaCitta-3", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["a", "wGira", "", "", "", "", "", "", "", "", "d", "wGira", "", "", ""]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 5, "w", "Ragazzo3-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["d", "sGira", "", "a", "a", "sGira", "", "", "", "d"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 12, "d", "Ragazzo2-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["a", "w", "a", "a", "sGira", "", "", "", "d", "d", "s", "d", "sGira", "", ""]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 12, "s", "Ragazza3-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["s", "s", "a", "a", "wGira", "", "", "", "", "d", "d", "w", "w", "aGira", "", "", ""]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 3, "a", "Ragazza1-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["città2"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCittà2"]:
            percorsoPersonaggio = ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "w", "a", "a", "a", "a", "a", "a", "a", "a", "s", "a", "a", "a"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 7, "d", "PadreUfficialeServizio-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            percorsoPersonaggio = ["s", "d", "s", "d", "s", "s", "", "", "", "w", "w", "a", "w", "a", "w", "w", "", "", "s"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 4, "s", "Ragazza1-1", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["d", "s", "aGira", "", "w", "a", "a", "a", "sGira", "", "", "d", "d"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 9, "d", "Ragazza3-1", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["a", "s", "a", "s", "a", "s", "s", "", "", "", "", "w", "w", "d", "w", "d", "w", "d", "w", "w", "", "", "s", "s"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 6, "s", "Ragazzo1-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["a", "a", "sGira", "", "", "", "d", "d", "d", "d", "d", "", "", "a", "a", "a"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 11, "a", "Ragazzo2-1", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["città3"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCittà3"]:
            percorsoPersonaggio = ["a", "a", "a", "a", "a", "a", "a", "a", "a", "w", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 9, "d", "PadreUfficialeServizio-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoSecondaGuardia"]:
                percorsoPersonaggio = ["d", "d"]
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 9, "a", "Mercante-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoIDueAggressori"] or avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["monologoDopoArrivoInBiblioteca"]:
                percorsoPersonaggio = ["dGira", "mantieniPosizione"]
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 5, "d", "Ragazzo3-1", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                percorsoPersonaggio = ["aGira", "mantieniPosizione"]
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 5, "a", "Ragazzo2-2", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["w", "w", "", "s", "s", ""]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 12, "s", "Ragazzo1-1", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["s", "", "", "w", "w", "a", "w", "w", "dGira", "", "", "", "s", "s", "d", "", "", "s"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 14, "s", "Ragazza1-2", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["città4"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 4, "s", "OggettoFinestraCasaDavid-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 4, "s", "OggettoFinestraCasaDavid-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4, "s", "OggettoFinestraCasaDavid-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 4, "s", "OggettoFinestraCasaDavid-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCittà4"]:
                percorsoPersonaggio = ["a", "a", "a", "a", "w", "w", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "w", "w", "w", "w", "w", "w", "w"]
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 14, "d", "PadreUfficialeServizio-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ricevutoCertificatoDalServo"]:
            percorsoPersonaggio = ["a", "a", "s", "d", "w", "w", "d", "s"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14, "s", "Ragazzo1-2", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["d", "w", "a", "s", "s", "a", "w", "d"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 14, "d", "Ragazzo3-2", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        elif GlobalGameVar.dictAvanzamentoStoria["ricevutoCertificatoDalServo"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["uccisoSecondoAggressore"]:
            percorsoPersonaggio = ["dGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 13, "d", "Ragazzo3-2", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["aGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 13, "a", "Ragazzo1-2", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["città5"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ricevutoCertificatoDalServo"]:
            percorsoPersonaggio = ["dGira", "", "sGira", "", "aGira", "", "sGira", ""]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 7, "s", "Mercante-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoIDueAggressori"] or avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["monologoDopoArrivoInBiblioteca"]:
            percorsoPersonaggio = ["a", "a", "s", "s", "s", "dGira", "", "", "w", "w", "w", "d", "d", "sGira", "", "", ""]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 12, "s", "Ragazzo3-3", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoIDueAggressori"]:
                percorsoPersonaggio = ["s", "d", "sGira", "", "", "", "", "", "a", "w", "a", "a", "sGira", "", "", "", "d", "d"]
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 11, "d", "Ragazza2-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
        if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["incontratoIDueAggressori"]:
            percorsoPersonaggio = ["sGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 7, "s", "OggettoPappaLibroSonoroMercante-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 7, "s", "OggettoCassaMercanteA-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 7, "s", "OggettoCassaMercanteB-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["dGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 9, "d", "Ragazzo2-3", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["aGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 9, "a", "Ragazza3-2", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["dGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 4, "d", "Ragazzo1-3", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["aGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 4, "a", "Ragazza1-3", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["città6"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ricevutoCertificatoDalServo"]:
            percorsoPersonaggio = ["sGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 3, "s", "Pazzo1-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["sGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 6, "s", "GuardiaCitta-4", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["sGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 6, "s", "GuardiaCitta-5", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["dGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 10, "d", "Ragazzo1-4", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["aGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 10, "a", "Ragazzo2-4", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["", "wGira", "sGira", "", "", "w", "s", "", ""]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 12, "s", "Ragazza1-4", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["aGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 9, "a", "Ragazza3-3", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["città7"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoIDueAggressori"] or avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"]:
            percorsoPersonaggio = ["dGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 11, "d", "Ragazza1-5", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["aGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 11, "a", "Ragazzo3-4", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["città8"]:
        percorsoPersonaggio = ["sGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 5, "s", "GuardiaCitta-6", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["dGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 3, "d", "GuardiaCitta-7", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["aGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 3, "a", "GuardiaCitta-8", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["sGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 5, "s", "GuardiaCitta-9", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["aGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 9, "a", "Ragazzo3-5", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["aGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 10, "a", "Ragazzo2-5", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["aGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 10, "a", "Ragazza3-4", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["a", "a", "s", "", "", "a", "a", "sGira", "", "d", "d", "sGira", "", "", "", "w", "d", "d", "d", "sGira", "", "", "d", "d", "d", "sGira", "", "w", "d", "d", "s", "s", "", "", "", "w", "w", "a", "a", "s", "", "a", "a", "a", "a", "sGira", "", ""]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 13, "s", "Ragazzo1-5", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["città9"]:
        percorsoPersonaggio = ["wGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 14, "w", "GuardiaCitta-10", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["wGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 14, "w", "GuardiaCitta-11", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["a", "a", "wGira", "", "", "", "d", "d", "d", "w", "d", "wGira", "", "", "a", "s", "a"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 4, "a", "Ragazza3-5", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["città10"]:
        percorsoPersonaggio = ["dGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 7, "d", "GuardiaCitta-12", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["dGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 11, "d", "GuardiaCitta-13", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["s", "s", "dGira", "", "w", "w", "a", "a", "sGira", "", "", "", "d", "d", "sGira", "", "", "", "", ""]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 5, "s", "Ragazzo3-6", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["wGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 7, "w", "Ragazza1-7", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)

    return listaPersonaggiTotali, listaPersonaggi
