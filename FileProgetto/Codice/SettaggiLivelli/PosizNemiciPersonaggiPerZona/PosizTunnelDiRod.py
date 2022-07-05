# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj


def setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria):
    return listaNemiciTotali, listaNemici


def setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi):
    if stanza == GlobalGameVar.dictStanze["tunnelDiRod1"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoRenéDaTunnelDiRod2PreFineDelMondo"]:
            percorsoPersonaggio = ["w", "a", "w", "a", "w", "a", "w", "a", "a", "w", "a", "a", "w", "a", "a", "w", "a", "w", "a", "w", "a", "w", "w"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 13, "a", "BibliotecarioOperato-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["tunnelDiRod2"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoRenéDaTunnelDiRod3PreFineDelMondo"]:
            percorsoPersonaggio = ["w", "a", "w", "w", "w", "a", "w", "w", "a", "w", "w", "a", "w", "w"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 12, "w", "BibliotecarioOperato-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["tunnelDiRod3"]:
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 15, "s", "OggettoLevaTunnelDiRod-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoRenéDaAvampostoDiRod2PreFineDelMondo"]:
            percorsoPersonaggio = ["w", "a", "w", "a", "w", "a", "w", "w", "a", "w", "w", "a", "w", "w"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 11, "w", "BibliotecarioOperato-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)

    return listaPersonaggiTotali, listaPersonaggi
