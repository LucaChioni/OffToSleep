# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj


def setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria):
    return listaNemiciTotali, listaNemici


def setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria):
    if stanza == GlobalGameVar.dictStanze["biblioteca1"]:
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 11, "d", "AssistBiblioteca-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 11, "d", "OggettoAssistBiblioteca-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["", "a", "wGira", "", "", "", "", "a", "wGira", "", "", "d", "d", "wGira", "", ""]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, "w", "Ragazzo3-9", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 12, "s", "AssistBiblioteca-1", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["", "s", "s", "aGira", "", "", "", "w", "w", "w", "aGira", "", "w", "aGira", "", "", "", "s", "s", "aGira", ""]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 5, "a", "Ragazzo1-15", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["", "", "w", "dGira", "", "", "", "", "w", "w", "dGira", "", "", "s", "s", "s", "s", "dGira", "", "", "", "", "", "", "w", "dGira", ""]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 8, "d", "Ragazza3-8", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["biblioteca2"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["andatoNelloStudioDelBibliotecario"]:
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 8, "s", "Bibliotecario-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["", "s", "s", "aGira", "", "", "", "w", "w", "w", "w", "aGira", "w", "aGira", "", "", "s", "aGira", "", "s", "s", "aGira", "", ""]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, "a", "Ragazzo1-16", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["w", "mantieniPosizione"]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 2, "w", "Ragazza1-10", stanza, avanzamentoStoria, percorsoPersonaggio)
        personaggio.numeroMovimento = 1
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = ["", "", "s", "dGira", "", "", "w", "w", "w", "dGira", "", "", "", "w", "w", "dGira", "", "", "s", "s", "s", "s", "dGira", ""]
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 13, "d", "Ragazzo2-7", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["andatoNelloStudioDelBibliotecario"]:
            percorsoPersonaggio = ["a", "a", "a", "a", "a", "w", "w", "a", "d", "d", "d", "w", "sGira"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 9, "d", "Bibliotecario-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sedutaInBiblioteca"]:
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 9, "s", "Bibliotecario-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 8, "a", "OggettoLucySeduta-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 9, "s", "OggettoMocio-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 10, "s", "OggettoVomito-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["alzataDallaSediaInBiblioteca"]:
            percorsoPersonaggio = ["a", "a", "a", "a", "s", "s", "s", "d", "s", "d", "d", "w", "dGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 9, "s", "Bibliotecario-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 10, "s", "OggettoMocio-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 10, "s", "OggettoVomito-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        elif avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["alzataDallaSediaInBiblioteca"]:
            percorsoPersonaggio = ["a", "a", "a", "a", "s", "s", "s", "d", "s", "d", "d", "w", "dGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 9, "s", "Bibliotecario-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 10, "s", "OggettoMocio-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 10, "s", "OggettoVomito-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, "d", "OggettoLibreriaRegistri-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 5, "s", "OggettoRegistroBiblioteca-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 10, "d", "OggettoVomito-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)

    return listaPersonaggiTotali, listaPersonaggi
