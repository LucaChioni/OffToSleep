# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj


def setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria):
    return listaNemiciTotali, listaNemici


def setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi):
    if stanza == GlobalGameVar.dictStanze["stradaPerPassoMontano1"]:
        percorsoPersonaggio = ["aGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 6, "a", "GuardiaCitta-21", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["aGira", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 11, "a", "GuardiaCitta-22", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)

    return listaPersonaggiTotali, listaPersonaggi
