# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj


def setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria):
    return listaNemiciTotali, listaNemici


def setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi):
    if stanza == GlobalGameVar.dictStanze["stradaPerCittÃ 1"]:
        percorsoPersonaggio = ["aGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 11, "a", "GuardiaCitta-14", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, "s", "OggettoCartelloForesta-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2, "s", "OggettoCartelloForesta-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 7, "a", "OggettoCartelloStaccionata-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 8, "a", "OggettoCartelloStaccionata-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 10, "a", "OggettoCartelloBloccoStrada-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 13, "a", "OggettoCartelloStaccionata-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 14, "a", "OggettoCartelloStaccionata-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["stradaPerCittÃ 3"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["apertoPortaCittÃ "]:
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 8, "d", "OggettoBucoPorta-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 9, "d", "OggettoBucoPorta-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            percorsoPersonaggio = ["dGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 5, "d", "GuardiaCitta-15", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["dGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 12, "d", "GuardiaCitta-16", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)

    return listaPersonaggiTotali, listaPersonaggi
