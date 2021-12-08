# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj


def setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria):
    return listaNemiciTotali, listaNemici


def setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi):
    if stanza == GlobalGameVar.dictStanze["avampostoDiRod1"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["messaMappaLabirintoSulTavolo"]:
            percorsoPersonaggio = ["sGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 8, "s", "Mercante-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
            percorsoPersonaggio = ["dGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 5, "d", "Mercante-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        if GlobalGameVar.dictAvanzamentoStoria["creatoPersonaggioOggettoPerEnigmaMappaLabirinto"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["risoltoEnigmaMappaLabirinto"]:
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 9, "s", "OggettoEnigmaLabirinto-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        else:
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 9, "s", "OggettoTavoloMappaLabirinto-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 4, "s", "OggettoAttrezziRod-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 4, "s", "OggettoAttrezziRod-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 5, "s", "OggettoFogliProgettiRod-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 6, "s", "OggettoAttrezziRod-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 5, "s", "OggettoAttrezziRod-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 6, "s", "OggettoAttrezziRod-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 9, "s", "OggettoScatoloniRod-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["avampostoDiRod2"]:
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 4, "s", "OggettoTuboRod-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 5, "s", "OggettoTuboRod-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["avampostoDiRod3"]:
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 6, "s", "OggettoLibriInquinamentoRod-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 14, "s", "OggettoFinestraAvampostoDiRod-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 14, "s", "OggettoFinestraAvampostoDiRod-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 4, "s", "OggettoAppuntiLabirintoRod-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 7, "s", "OggettoAttrezziRod-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 4, "s", "OggettoPappaLibroSonoroMercante-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)

    return listaPersonaggiTotali, listaPersonaggi
