# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.GestioneNemiciPersonaggi.NemicoObj as NemicoObj


def setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria):
    if stanza == GlobalGameVar.dictStanze["selvaArida1"]:
        percorsoNemico = ["s", "s", "a", "a", "a", "w", "w", "w", "d", "d", "d", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 6, "s", "TartarugaVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)

    return listaNemiciTotali, listaNemici


def setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria):
    return listaPersonaggiTotali, listaPersonaggi
