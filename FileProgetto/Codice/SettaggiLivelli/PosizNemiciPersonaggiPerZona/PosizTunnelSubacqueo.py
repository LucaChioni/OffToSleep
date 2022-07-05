# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj


def setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria):
    return listaNemiciTotali, listaNemici


def setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi):
    if stanza == GlobalGameVar.dictStanze["tunnelSubacqueo1"]:
        if not GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 8, "s", "OggettoPortaSfondata-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["NeilUscitoDaInternoCastello8PostAvvioSequenzaNelCalcolatore"]:
            percorsoPersonaggio = ["d", "d", "d", "d", "d", "d", "d"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 9, "d", "Neil-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoRenéDaTunnelSubaqueo2PreFineDelMondo"]:
            percorsoPersonaggio = ["a"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 9, "a", "BibliotecarioOperato-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["tunnelSubacqueo2"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["NeilUscitoDaTunnelSubaqueo1PostAvvioSequenzaNelCalcolatore"]:
            percorsoPersonaggio = ["d", "d", "d"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 9, "d", "Neil-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivatoRenéNelTunnelSubacqueo2"]:
            percorsoPersonaggio = ["d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 9, "d", "Bibliotecario-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoRenéDaLaboratorioDiNeilPreFineDelMondo"]:
            percorsoPersonaggio = ["a"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 9, "a", "BibliotecarioOperato-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)

    return listaPersonaggiTotali, listaPersonaggi
