# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj


def setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria):
    return listaNemiciTotali, listaNemici


def setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria):
    if stanza == GlobalGameVar.dictStanze["città1"]:
        percorsoPersonaggio = ["s", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 2, "s", "GuardiaCitta-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["w", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 15, "w", "GuardiaCitta-1", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["entratoInCittà"]:
            percorsoPersonaggio = ["w", "w", "w", "w", "w", "", "", "a", "s", "s", "s", "s", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 8, "d", "PadreUfficialeServizio-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            percorsoPersonaggio = ["s", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 5, "s", "GuardiaCitta-2", stanza, avanzamentoStoria, percorsoPersonaggio)
            personaggio.numeroMovimento = 1
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["w", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 12, "w", "GuardiaCitta-3", stanza, avanzamentoStoria, percorsoPersonaggio)
            personaggio.numeroMovimento = 1
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["d", "", "", "a", "a", "a", "a", "s", "aGira", "", "", "w", "d", "d", "d"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 5, "d", "Ragazzo1-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["d", "d", "d", "s", "", "", "", "w", "a", "a", "a", "sGira", "", ""]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 11, "s", "Ragazzo1-1", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["d", "sGira", "", "a", "a", "sGira", "", "", "", "d"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 12, "d", "Ragazzo2-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["s", "s", "a", "a", "wGira", "", "", "", "", "d", "d", "w", "w", "aGira", "", "", ""]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 3, "a", "Ragazzo3-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["a", "wGira", "", "", "", "", "", "", "", "", "d", "wGira", "", "", ""]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 5, "w", "Ragazza1-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["a", "w", "a", "a", "sGira", "", "", "", "d", "d", "s", "d", "sGira", "", ""]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 12, "s", "Ragazza3-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
    if stanza == GlobalGameVar.dictStanze["città2"]:
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
            percorsoPersonaggio = ["d", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 4, "d", "Ragazzo3-1", stanza, avanzamentoStoria, percorsoPersonaggio)
            personaggio.numeroMovimento = 1
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["w", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 5, "w", "Ragazzo1-2", stanza, avanzamentoStoria, percorsoPersonaggio)
            personaggio.numeroMovimento = 1
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["a", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 4, "a", "Ragazza1-2", stanza, avanzamentoStoria, percorsoPersonaggio)
            personaggio.numeroMovimento = 1
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["d", "s", "aGira", "", "w", "a", "a", "a", "sGira", "", "", "d", "d"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 9, "d", "Ragazza3-1", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["a", "s", "a", "s", "a", "s", "s", "", "", "", "", "w", "w", "d", "w", "d", "w", "d", "w", "w", "", "", "s", "s"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 6, "s", "Ragazzo1-3", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["a", "a", "sGira", "", "", "", "d", "d", "d", "d", "d", "", "", "a", "a", "a"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 11, "a", "Ragazzo2-1", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["d", "", "", "", "", "a", "a", "a", "w", "", "", "s", "d", "d"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 4, "d", "Ragazza3-2", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
    if stanza == GlobalGameVar.dictStanze["città3"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCittà3"]:
            percorsoPersonaggio = ["a", "a", "a", "a", "a", "a", "a", "a", "a", "w", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 9, "d", "PadreUfficialeServizio-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            percorsoPersonaggio = ["d", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, "d", "Ragazza3-3", stanza, avanzamentoStoria, percorsoPersonaggio)
            personaggio.numeroMovimento = 1
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["a", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 6, "a", "Ragazzo2-2", stanza, avanzamentoStoria, percorsoPersonaggio)
            personaggio.numeroMovimento = 1
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["w", "w", "", "s", "s", ""]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 12, "s", "Ragazzo1-4", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["d", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 5, "d", "Ragazzo3-2", stanza, avanzamentoStoria, percorsoPersonaggio)
            personaggio.numeroMovimento = 1
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["w", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 6, "w", "Ragazzo3-3", stanza, avanzamentoStoria, percorsoPersonaggio)
            personaggio.numeroMovimento = 1
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["a", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 5, "a", "Ragazzo1-5", stanza, avanzamentoStoria, percorsoPersonaggio)
            personaggio.numeroMovimento = 1
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["s", "", "", "w", "w", "a", "w", "w", "dGira", "", "", "", "s", "s", "d", "", "", "s"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 14, "s", "Ragazza1-3", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
    if stanza == GlobalGameVar.dictStanze["città4"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCittà4"]:
            percorsoPersonaggio = ["a", "a", "a", "a", "w", "w", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "w", "w", "w", "w", "w", "w", "w"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 14, "d", "PadreUfficialeServizio-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ricevutoCertificatoDalServo"]:
            percorsoPersonaggio = ["d", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14, "d", "Ragazzo1-6", stanza, avanzamentoStoria, percorsoPersonaggio)
            personaggio.numeroMovimento = 1
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["a", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 14, "a", "Ragazzo3-4", stanza, avanzamentoStoria, percorsoPersonaggio)
            personaggio.numeroMovimento = 1
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        elif GlobalGameVar.dictAvanzamentoStoria["ricevutoCertificatoDalServo"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["uccisoSecondoAggressore"]:
            percorsoPersonaggio = ["d", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 13, "d", "Ragazzo3-4", stanza, avanzamentoStoria, percorsoPersonaggio)
            personaggio.numeroMovimento = 1
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["a", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 13, "a", "Ragazzo1-6", stanza, avanzamentoStoria, percorsoPersonaggio)
            personaggio.numeroMovimento = 1
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
    if stanza == GlobalGameVar.dictStanze["città5"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"]:
            percorsoPersonaggio = ["dGira", "", "sGira", "", "aGira", "", "sGira", ""]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 7, "s", "Mercante-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["d", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 10, "d", "Ragazzo2-3", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["s", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 9, "s", "Ragazza3-4", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["a", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 10, "a", "Ragazza1-4", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["a", "a", "s", "s", "s", "dGira", "", "", "w", "w", "w", "d", "d", "sGira", "", "", ""]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 12, "s", "Ragazzo1-7", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["s", "d", "sGira", "", "", "", "", "", "a", "w", "a", "a", "sGira", "", "", "", "d", "d"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 11, "d", "Ragazza2-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["d", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 4, "d", "Ragazzo1-8", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["a", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 4, "a", "Ragazza1-5", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["d", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 9, "d", "Ragazzo1-9", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    if stanza == GlobalGameVar.dictStanze["città6"]:
        percorsoPersonaggio = ["s", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 6, "s", "GuardiaCitta-4", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["s", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 6, "s", "GuardiaCitta-5", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["d", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 10, "d", "Ragazzo1-10", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["a", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 10, "a", "Ragazzo2-4", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["", "wGira", "sGira", "", "", "w", "s", "", ""]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 12, "s", "Ragazza1-6", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["a", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 9, "a", "Ragazza3-5", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    if stanza == GlobalGameVar.dictStanze["città7"]:
        percorsoPersonaggio = ["d", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 11, "d", "Ragazzo1-11", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["s", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 10, "s", "Ragazza1-7", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["a", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 11, "a", "Ragazzo3-5", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    if stanza == GlobalGameVar.dictStanze["città8"]:
        percorsoPersonaggio = ["s", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 5, "s", "GuardiaCitta-6", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["s", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 5, "s", "GuardiaCitta-7", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["d", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 3, "d", "GuardiaCitta-8", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["a", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 3, "a", "GuardiaCitta-9", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["s", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 5, "s", "GuardiaCitta-10", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["s", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 5, "s", "GuardiaCitta-11", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["a", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 9, "a", "Ragazzo3-6", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["a", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 10, "a", "Ragazzo2-5", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["a", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 10, "a", "Ragazza3-6", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["a", "a", "s", "", "", "a", "a", "sGira", "", "d", "d", "sGira", "", "", "", "w", "d", "d", "d", "sGira", "", "", "d", "d", "d", "sGira", "", "w", "d", "d", "s", "s", "", "", "", "w", "w", "a", "a", "s", "", "a", "a", "a", "a", "sGira", "", ""]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 13, "s", "Ragazzo1-12", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    if stanza == GlobalGameVar.dictStanze["città9"]:
        percorsoPersonaggio = ["w", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 14, "w", "GuardiaCitta-12", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["w", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 14, "w", "GuardiaCitta-13", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["d", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 6, "d", "Ragazza1-8", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["w", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 7, "w", "Ragazzo2-6", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["a", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 6, "a", "Ragazzo3-7", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["a", "a", "wGira", "", "", "", "d", "d", "d", "w", "d", "wGira", "", "", "a", "s", "a"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 4, "a", "Ragazza3-7", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["", "", "a", "a", "wGira", "", "", "", "a", "w", "", "", "", "s", "d", "d", "d", "", ""]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 4, "d", "Ragazzo1-13", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    if stanza == GlobalGameVar.dictStanze["città10"]:
        percorsoPersonaggio = ["d", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 7, "d", "GuardiaCitta-14", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["d", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 11, "d", "GuardiaCitta-15", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["s", "s", "dGira", "", "w", "w", "a", "a", "sGira", "", "", "", "d", "d", "sGira", "", "", "", "", ""]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 5, "s", "Ragazzo3-8", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["s", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 8, "s", "Ragazza1-9", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["w", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 10, "w", "Ragazzo1-14", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)

    return listaPersonaggiTotali, listaPersonaggi
