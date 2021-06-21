# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.GestioneNemiciPersonaggi.NemicoObj as NemicoObj


def setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria):
    if stanza == GlobalGameVar.dictStanze["selvaArida1"]:
        percorsoNemico = ["d", "d", "a", "w", "s", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 6, "a", "RagnoRosso", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "w", "w", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 10, "s", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "d", "w", "d", "a", "s", "a", "w", "a", "w", "a", "s", "w", "d", "s", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 5, "d", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "s", "d", "w", "d", "w", "a", "w", "a", "w", "d", "w", "a", "w", "a", "d", "s", "d", "s", "a", "s", "d", "s", "d", "s", "a", "s", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 11, "w", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "s", "w", "d", "w", "d", "w", "s", "a", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 6, "s", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["selvaArida2"]:
        percorsoNemico = ["a", "d", "d", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 12, "a", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = []
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 3, "d", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "d", "d", "d", "w", "s", "a", "a", "a", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 9, "s", "RagnoRosso", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "a", "s", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 11, "d", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "a", "d", "d", "d", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 7, "a", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = []
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 14, "a", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "a", "a", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 6, "d", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = []
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, "a", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 4, "w", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "a", "s", "a", "w", "a", "d", "w", "d", "w", "s", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 9, "d", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "a", "s", "d", "a", "w", "d", "w", "a", "w", "a", "w", "a", "d", "s", "d", "s", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 6, "d", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "s", "d", "s", "a", "s", "d", "s", "a", "w", "d", "w", "a", "w", "d", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 10, "w", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)

    return listaNemiciTotali, listaNemici


def setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria):
    return listaPersonaggiTotali, listaPersonaggi
