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
        percorsoNemico = ["s", "", "d", "", "w", "", "d", "", "a", "", "s", "", "a", "", "w", "", "a", "", "w", "", "a", "", "s", "", "w", "", "d", "", "s", "", "d", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 5, "d", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "", "s", "", "d", "", "w", "", "d", "", "w", "", "a", "", "w", "", "a", "", "w", "", "d", "", "w", "", "a", "", "w", "", "a", "", "d", "", "s", "", "d", "", "s", "", "a", "", "s", "", "d", "", "s", "", "d", "", "s", "", "a", "", "s", "", "w", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 11, "w", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "", "s", "", "w", "", "d", "", "w", "", "d", "", "w", "", "s", "", "a", "", "s", ""]
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
        percorsoNemico = ["s", "", "a", "", "s", "", "a", "", "w", "", "a", "", "d", "", "w", "", "d", "", "w", "", "s", "", "d", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 9, "d", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "", "a", "", "s", "", "d", "", "a", "", "w", "", "d", "", "w", "", "a", "", "w", "", "a", "", "w", "", "a", "", "d", "", "s", "", "d", "", "s", "", "d", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 6, "d", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "", "s", "", "d", "", "s", "", "a", "", "s", "", "d", "", "s", "", "a", "", "w", "", "d", "", "w", "", "a", "", "w", "", "d", "", "w", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 10, "w", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["selvaArida3"]:
        percorsoNemico = ["a", "", "w", "", "a", "", "s", "", "a", "", "s", "", "d", "", "w", "", "d", "", "w", "", "d", "", "s", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 11, "s", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "a", "w", "s", "d", "d", "d", "d", "d", "s", "d", "a", "w", "a", "a", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 13, "a", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "", "a", "", "w", "", "a", "", "s", "", "a", "", "w", "", "d", "", "w", "", "d", "", "s", "", "d", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 4, "d", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "s", "a", "a", "s", "s", "w", "w", "d", "d", "w", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 7, "w", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "w", "d", "d", "d", "d", "s", "w", "a", "a", "a", "a", "s", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 5, "a", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14, "s", "RagnoRosso", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "d", "d", "a", "a", "a", "a", "a", "d", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 9, "d", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 4, "a", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 6, "a", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 5, "d", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["selvaArida4"]:
        percorsoNemico = ["s", "d", "d", "a", "a", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 6, "w", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "w", "w", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 13, "s", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "a", "d", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 10, "d", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "w", "a", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 8, "d", "RagnoRosso", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "d", "s", "w", "a", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 13, "w", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 4, "a", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "a", "d", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 6, "d", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "", "a", "", "w", "", "a", "", "s", "", "d", "", "w", "", "d", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 10, "d", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "", "s", "", "d", "", "a", "", "w", "", "a", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 14, "a", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "", "d", "", "s", "", "w", "", "a", "", "w", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 10, "w", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "", "w", "", "a", "", "d", "", "s", "", "d", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 13, "d", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "", "s", "", "d", "", "s", "", "w", "", "a", "", "w", "", "a", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 6, "a", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "", "w", "", "a", "", "w", "", "s", "", "d", "", "s", "", "d", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 8, "d", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["selvaArida5"]:
        percorsoNemico = ["d", "", "w", "", "d", "", "w", "", "s", "", "a", "", "s", "", "a", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 7, "a", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "", "d", "", "a", "", "w", "", "a", "", "w", "", "s", "", "d", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 12, "d", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "", "w", "", "a", "", "d", "", "s", "", "d", "", "s", "", "w", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 9, "w", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "d", "d", "w", "w", "s", "s", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 8, "a", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "a", "a", "d", "d", "d", "w", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 11, "s", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "s", "w", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9, "w", "RagnoRosso", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "", "w", "", "s", "", "d", "", "s", "", "d", "", "a", "", "w", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4, "w", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "", "d", "", "a", "", "s", "", "a", "", "s", "", "a", "", "d", "", "w", "", "d", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 3, "d", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "d", "d", "d", "d", "w", "w", "w", "s", "s", "s", "a", "a", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 14, "a", "RagnoRosso", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "d", "d", "w", "w", "w", "d", "a", "s", "s", "s", "a", "a", "s", "s", "s", "w", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 12, "w", "RagnoRosso", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "s", "w", "w", "w", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 4, "s", "RagnoRosso", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["selvaArida6"]:
        percorsoNemico = ["w", "s", "s", "s", "w", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 8, "w", "RagnoRosso", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "d", "a", "a", "a", "a", "d", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 9, "d", "RagnoRosso", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "s", "s", "w", "w", "w", "w", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 5, "s", "RagnoRosso", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "", "a", "", "s", "", "a", "", "s", "", "a", "", "d", "", "w", "", "d", "", "w", "", "d", "", "w", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 4, "w", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "", "d", "", "a", "", "w", "", "a", "", "w", "", "a", "", "w", "", "s", "", "d", "", "s", "", "d", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 10, "d", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "", "w", "", "a", "", "w", "", "s", "", "d", "", "s", "", "d", "", "s", "", "d", "", "s", "", "w", "", "a", "", "w", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 6, "w", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoUscitaSelva"]:
            percorsoNemico = ["s", "d", "d", "w", "s", "a", "a", "w"]
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 13, "w", "Scorpione", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["s", "a", "d", "w"]
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 10, "w", "Scorpione", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["d", "w", "s", "a"]
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 14, "a", "Scorpione", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["selvaArida7"]:
        percorsoNemico = ["s", "", "a", "", "s", "", "w", "", "d", "", "w", "", "d", "", "a", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 9, "a", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "", "w", "", "s", "", "a", "", "s", "", "a", "", "s", "", "w", "", "d", "", "w", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 12, "w", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "", "d", "", "s", "", "w", "", "a", "", "w", "", "a", "", "d", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 11, "d", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "", "s", "", "a", "", "w", "", "a", "", "d", "", "s", "", "d", "", "w", "", "d", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 4, "d", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "", "s", "", "a", "", "d", "", "w", "", "d", "", "w", "", "d", "", "w", "", "s", "", "a", "", "s", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 4, "s", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "", "d", "", "w", "", "s", "", "a", "", "s", "", "a", "", "s", "", "a", "", "d", "", "w", "", "d", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 7, "d", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 6, "w", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["selvaArida8"]:
        percorsoNemico = ["a", "d", "d", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 13, "a", "RagnoRosso", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "w", "w", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 10, "s", "RagnoRosso", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "", "s", "", "a", "", "s", "", "w", "", "d", "", "w", "", "d", "", "w", "", "d", "", "a", "", "s", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 5, "s", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "", "a", "", "w", "", "d", "", "w", "", "a", "", "d", "", "s", "", "a", "", "s", "", "d", "", "s", "", "a", "", "s", "", "w", "", "d", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 12, "d", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "", "w", "", "a", "", "d", "", "s", "", "d", "", "s", "", "d", "", "a", "", "w", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 13, "w", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "", "a", "", "w", "", "a", "", "s", "", "a", "", "d", "", "w", "", "d", "", "s", "", "d", "", "w", "", "d", "", "w", "", "s", "", "a", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 6, "a", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "", "w", "", "d", "", "w", "", "s", "", "a", "", "s", "", "a", "", "s", "", "a", "", "s", "", "a", "", "d", "", "w", "", "d", "", "w", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 8, "w", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "", "a", "", "s", "", "w", "", "d", "", "w", "", "d", "", "w", "", "d", "", "a", "", "s", "", "a", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 12, "a", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["selvaArida9"]:
        percorsoNemico = ["d", "d", "a", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 7, "a", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "s", "a", "a", "w", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 8, "d", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "", "s", "", "d", "", "s", "", "a", "", "w", "", "d", "", "w", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 4, "w", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "a", "w", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 12, "d", "RagnoRosso", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "d", "d", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 5, "a", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "", "a", "", "s", "", "a", "", "d", "", "w", "", "d", "", "w", "", "d", "", "s", "", "d", "", "w", "", "d", "", "a", "", "s", "", "a", "", "w", "", "a", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 12, "a", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "s", "s", "w", "w", "w", "w", "w", "w", "s", "s", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 5, "s", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "w", "s", "s", "s", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 6, "w", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "a", "s", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 10, "d", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "", "d", "", "s", "", "w", "", "a", "", "w", "", "a", "", "w", "", "s", "", "d", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 7, "d", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "w", "a", "w", "d", "d", "s", "s", "a", "s", "s", "d", "w", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 9, "a", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "d", "a", "s", "s", "d", "a", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 8, "w", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "w", "d", "d", "d", "w", "w", "s", "s", "a", "a", "a", "s", "s", "a", "s", "s", "w", "w", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 6, "d", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "", "w", "", "d", "", "s", "", "d", "", "s", "", "a", "", "s", "", "a", "", "s", "", "a", "", "s", "", "a", "", "w", "", "a", "", "w", "", "d", "", "w", "", "a", "", "w", "", "d", "", "w", "", "d", "", "s", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 10, "s", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "a", "w", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 7, "d", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "", "d", "", "a", "", "s", "", "d", "", "s", "", "a", "", "s", "", "a", "", "d", "", "w", "", "d", "", "w", "", "a", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 6, "a", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["selvaArida10"]:
        percorsoNemico = ["a", "", "s", "", "a", "", "d", "", "w", "", "d", "", "w", "", "d", "", "w", "", "s", "", "a", "", "s", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 4, "s", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "w", "w", "a", "s", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 13, "s", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "", "w", "", "d", "", "w", "", "d", "", "s", "", "d", "", "s", "", "a", "", "s", "", "a", "", "w", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 8, "w", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "", "w", "", "d", "", "w", "", "a", "", "d", "", "s", "", "a", "", "s", "", "d", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 5, "d", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "", "a", "", "w", "", "a", "", "d", "", "s", "", "d", "", "w", "", "d", "", "s", "", "w", "", "a", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 10, "a", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "", "s", "", "a", "", "d", "", "w", "", "a", "", "w", "", "s", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 8, "s", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "", "w", "", "s", "", "d", "", "s", "", "w", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 13, "w", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["selvaArida11"]:
        percorsoNemico = ["w", "d", "s", "s", "a", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 6, "w", "RagnoRosso", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "a", "a", "s", "d", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 6, "d", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "d", "d", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 7, "a", "RagnoRosso", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "d", "a", "a", "a", "a", "a", "a", "d", "d", "d", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9, "d", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "a", "a", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 11, "d", "RagnoRosso", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "d", "a", "a", "a", "a", "s", "w", "d", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 7, "d", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "w", "d", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 4, "s", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "s", "a", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 8, "w", "RagnoRosso", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "w", "w", "s", "s", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 9, "s", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "w", "d", "d", "s", "a", "a", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 8, "a", "RagnoRosso", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "s", "a", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 11, "w", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["selvaArida12"]:
        percorsoNemico = ["d", "a", "a", "s", "d", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 9, "w", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "a", "w", "a", "w", "d", "d", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 4, "s", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "", "s", "", "d", "", "w", "", "d", "", "w", "", "a", "", "s", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 13, "s", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "", "w", "", "a", "", "w", "", "s", "", "d", "", "s", "", "a", "", "s", "", "w", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 14, "w", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "w", "s", "s", "s", "s", "w", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 5, "w", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "", "d", "", "s", "", "w", "", "a", "", "w", "", "a", "", "d", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 11, "d", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "", "w", "", "a", "", "w", "", "a", "", "w", "", "a", "", "d", "", "s", "", "d", "", "s", "", "d", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 14, "d", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "", "s", "", "d", "", "s", "", "a", "", "s", "", "d", "", "w", "", "a", "", "w", "", "d", "", "w", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 10, "w", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "", "a", "", "w", "", "a", "", "w", "", "d", "", "w", "", "d", "", "s", "", "d", "", "s", "", "a", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 14, "a", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "s", "s", "a", "w", "w", "w", "w", "d", "d", "d", "s", "s", "a", "w", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 4, "a", "RagnoRosso", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "", "w", "", "a", "", "w", "", "s", "", "d", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 12, "d", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "", "w", "", "a", "", "w", "", "a", "", "d", "", "s", "", "d", "", "s", "", "d", "", "s", "", "d", "", "s", "", "w", "", "a", "", "w", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 12, "w", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "", "a", "", "s", "", "d", "", "s", "", "d", "", "w", "", "a", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 11, "a", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "", "d", "", "s", "", "d", "", "s", "", "d", "", "a", "", "w", "", "a", "", "w", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 8, "w", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "", "s", "", "a", "", "w", "", "a", "", "d", "", "s", "", "d", "", "w", "", "d", "", "w", "", "s", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 7, "s", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["selvaArida13"]:
        percorsoNemico = ["s", "", "d", "", "s", "", "w", "", "a", "", "w", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 8, "w", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "", "s", "", "a", "", "s", "", "d", "", "s", "", "w", "", "a", "", "w", "", "d", "", "w", "", "a", "", "w", "", "s", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 6, "s", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "", "d", "", "s", "", "d", "", "a", "", "w", "", "a", "", "s", "", "a", "", "s", "", "w", "", "d", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 14, "d", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = []
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 9, "a", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = []
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 12, "s", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "", "s", "", "d", "", "a", "", "w", "", "a", "", "w", "", "d", "", "a", "", "s", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 10, "s", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "", "d", "", "s", "", "d", "", "a", "", "w", "", "a", "", "w", "", "a", "", "d", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 13, "d", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "w", "a", "w", "d", "w", "s", "a", "s", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 6, "d", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = []
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 13, "d", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "w", "w", "a", "s", "s", "s", "s", "d", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 7, "w", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "d", "w", "a", "a", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 8, "s", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "d", "d", "d", "a", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 9, "a", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "s", "d", "w", "a", "a", "a", "w", "a", "s", "d", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 6, "d", "RagnoRosso", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "s", "w", "a", "a", "s", "w", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 11, "d", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "s", "s", "a", "a", "w", "d", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 8, "w", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "a", "s", "d", "d", "d", "w", "d", "w", "a", "a", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 6, "s", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "w", "w", "d", "s", "d", "d", "s", "a", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 4, "a", "RagnoRosso", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "w", "s", "s", "s", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 5, "w", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["selvaArida14"]:
        percorsoNemico = ["d", "", "w", "", "d", "", "w", "", "d", "", "a", "", "s", "", "a", "", "s", "", "a", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 7, "a", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 13, "w", "RagnoRosso", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "", "d", "", "w", "", "d", "", "a", "", "s", "", "a", "", "w", "", "a", "", "s", "", "a", "", "d", "", "w", "", "d", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 12, "d", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "", "w", "", "d", "", "s", "", "d", "", "w", "", "d", "", "a", "", "s", "", "a", "", "w", "", "a", "", "s", "", "a", "", "s", "", "a", "", "d", "", "w", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 5, "w", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "", "s", "", "a", "", "d", "", "w", "", "d", "", "w", "", "d", "", "s", "", "d", "", "w", "", "s", "", "a", "", "w", "", "a", "", "s", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 3, "s", "SerpeArancio", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "s", "a", "a", "w", "d", "w", "d", "d", "d", "s", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 6, "a", "RagnoRosso", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "d", "d", "s", "a", "a", "a", "s", "w", "a", "w", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 9, "d", "RagnoRosso", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "a", "w", "d", "d", "d", "s", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 8, "a", "RagnoRosso", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["selvaArida15"]:
        percorsoNemico = ["a", "", "s", "", "w", "", "d", "", "w", "", "d", "", "a", "", "s", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 12, "s", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "a", "a", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 6, "d", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "", "a", "", "d", "", "s", "", "d", "", "s", "", "d", "", "a", "", "w", "", "a", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13, "a", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "", "w", "", "s", "", "d", "", "s", "", "d", "", "a", "", "w", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 7, "w", "SerpeVerde", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "d", "d", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 9, "a", "RagnoNero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)

    return listaNemiciTotali, listaNemici


def setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi):
    return listaPersonaggiTotali, listaPersonaggi
