# -*- coding: utf-8 -*-

from NemicoObj import *
from PersonaggioObj import *


def caricaNemiciNellaStanza(avanzamentoStoria, stanza, stanzeGiaVisitate, listaNemiciTotali, listaPersonaggiTotali):
    listaNemici = []
    if not stanza in stanzeGiaVisitate:
        if stanza == 1:
            percorsoNemico = ["w", "a", "a", "s", "d", "d"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 3, "a", "SerpeVerde", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["w", "a", "a", "s", "d", "d"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 5, "s", "LupoGrigio", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["w", "a", "a", "s", "d", "d"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 7, "s", "Cinghiale", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["w", "a", "a", "s", "d", "d"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 12, "a", "LupoBianco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["w", "a", "a", "s", "d", "d"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 14, "d", "LupoNero", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["w", "a", "a", "s", "d", "d"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4, "s", "Pipistrello", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["w", "a", "a", "s", "d", "d"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 29, GlobalVar.gsy // 18 * 15, "w", "Orco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
        if stanza == 2:
            percorsoNemico = ["w", "a", "a", "s", "d", "d"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 29, GlobalVar.gsy // 18 * 15, "w", "Orco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
    else:
        for nemico in listaNemiciTotali:
            if nemico.stanzaDiAppartenenza == stanza:
                listaNemici.append(nemico)
    nmost = len(listaNemici)

    listaPersonaggi = []
    if not stanza in stanzeGiaVisitate:
        if stanza == 2:
            percorsoPersonaggio = ["w", "", "d", "s", "a"]
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 4, "d", "Mercante", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 3, "a", "Alieno1", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
    else:
        for personaggio in listaPersonaggiTotali:
            if personaggio.stanzaDiAppartenenza == stanza:
                listaPersonaggi.append(personaggio)

    if not stanza in stanzeGiaVisitate:
        stanzeGiaVisitate.append(stanza)

    return nmost, listaNemici, listaPersonaggi, listaNemiciTotali, listaPersonaggiTotali
