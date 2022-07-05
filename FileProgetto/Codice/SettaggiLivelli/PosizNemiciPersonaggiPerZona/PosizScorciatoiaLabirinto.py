# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj


def setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria):
    return listaNemiciTotali, listaNemici


def setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi):
    if stanza == GlobalGameVar.dictStanze["scorciatoiaLabirinto1"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoRenéDaEsternoCastello1PreFineDelMondo"]:
            percorsoPersonaggio = ["a", "w", "a", "w", "a", "a", "w", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "w", "a", "a", "w"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 7, "w", "BibliotecarioOperato-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["scorciatoiaLabirinto2"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoRenéDaScorciatoiaLabirinto1PreFineDelMondo"]:
            percorsoPersonaggio = ["a", "w", "a", "a", "a", "w", "w", "w", "w", "w", "w", "w", "d", "w", "d", "w", "d", "w"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13, "a", "BibliotecarioOperato-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)

    return listaPersonaggiTotali, listaPersonaggi
