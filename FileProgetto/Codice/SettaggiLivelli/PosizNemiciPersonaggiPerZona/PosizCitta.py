# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj


def setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria):
    return listaNemiciTotali, listaNemici


def setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria):
    if stanza == GlobalGameVar.dictStanze["città1"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["entratoInCittà"]:
            percorsoPersonaggio = ["w", "w", "w", "w", "w", "", "", "a", "s", "s", "s", "s", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 8, "d", "PadreUfficialeServizio", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 2, "s", "GuardiaCitta", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    if stanza == GlobalGameVar.dictStanze["città2"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCittà2"]:
            percorsoPersonaggio = ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "w", "a", "a", "a", "a", "a", "a", "a", "a", "s", "a", "a", "a"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 7, "d", "PadreUfficialeServizio", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
    if stanza == GlobalGameVar.dictStanze["città3"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCittà3"]:
            percorsoPersonaggio = ["a", "a", "a", "a", "a", "a", "a", "a", "a", "w", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 9, "d", "PadreUfficialeServizio", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
    if stanza == GlobalGameVar.dictStanze["città4"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCittà4"]:
            percorsoPersonaggio = ["a", "a", "a", "a", "w", "w", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "w", "w", "w", "w", "w", "w", "w"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 14, "d", "PadreUfficialeServizio", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)

    return listaPersonaggiTotali, listaPersonaggi
