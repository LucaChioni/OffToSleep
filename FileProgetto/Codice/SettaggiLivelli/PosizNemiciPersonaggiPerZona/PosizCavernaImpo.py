# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj
import Codice.GestioneNemiciPersonaggi.NemicoObj as NemicoObj


def setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria):
    if stanza == GlobalGameVar.dictStanze["caverna1"]:
        if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["resoOstileImpoInCaverna1"]:
            percorsoNemico = ["s", "a", "sGira", "", "", "", "d", "w", "d", "w", "dGira", "", "", "", "s", "a"]
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 4, "a", "RoboLeggero", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["caverna2"]:
        percorsoNemico = ["s", "", "", "", "", "", "d", "", "", "", "", "", "w", "", "", "", "", "", "a", "", "", "", "", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 6, "a", "RoboVolante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "", "", "", "a", "s", "aGira", "", "", "", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 10, "w", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "sGira", "", "", "", "", "d", "w", "dGira", "", "", "", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 7, "s", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["caverna3"]:
        percorsoNemico = ["a", "s", "", "", "", "", "w", "d", "w", "", "", "", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 4, "s", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "", "", "", "", "", "a", "", "", "", "", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 8, "a", "RoboVolante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["dGira"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 10, "d", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["caverna4"]:
        percorsoNemico = ["d", "s", "", "w", "a", "a", "w", "", "s", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 4, "d", "RoboPesante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "", "", "", "", "", "w", "", "", "", "", "", "a", "", "", "", "", "", "s", "", "", "", "", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 9, "s", "RoboVolante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "s", "d", "", "", "", "a", "w", "a", "wGira", "", "", "a", "s", "aGira", "", "", "", "w", "d", "wGira", "", "", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 11, "w", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["caverna5"]:
        percorsoNemico = ["a", "s", "", "", "w", "d", "w", "", "", "", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 5, "s", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "", "a", "a", "", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 4, "d", "RoboPesante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "", "", "", "", "", "w", "", "", "", "", "", "a", "", "", "", "", "", "a", "", "", "", "", "", "s", "", "", "", "", "", "d", "", "", "", "", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 8, "d", "RoboVolante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "s", "s", "", "", "", "w", "w", "d", "w", "", "", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 11, "s", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "", "", "", "s", "d", "s", "", "", "", "w", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 10, "a", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["caverna6"]:
        percorsoNemico = ["s", "aGira", "", "", "w", "", "", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 12, "w", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "aGira", "", "", "s", "aGira", "", "", "w", "aGira", "", "", "w", "", "", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 4, "w", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "aGira", "", "", "w", "", "", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 11, "w", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "", "", "", "s", "", "", "", "s", "", "", "", "a", "", "", "", "a", "", "", "", "a", "", "", "", "w", "", "", "", "w", "", "", "", "d", "", "", "", "d", "", "", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 9, "d", "RoboPesanteVolante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["wGira"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 7, "w", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["sGira"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 13, "s", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["caverna7"]:
        percorsoNemico = ["w", "dGira", "", "s", "a", "", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 7, "d", "RoboPesante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "", "", "", "a", "", "", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 9, "a", "RoboPesanteVolante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "a", "", "s", "aGira", "", "w", "aGira", "", "d", "d", "wGira", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 4, "w", "RoboPesante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "d", "d", "", "a", "a", "w", "a", "", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 7, "d", "RoboPesante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "d", "d", "sGira", "", "a", "a", "w", "a", "w", "", "s", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 6, "d", "RoboPesante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["caverna8"]:
        percorsoNemico = ["d", "wGira", "", "a", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 3, "a", "RoboPesante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "", "", "", "w", "", "", "", "w", "", "", "", "w", "", "", "", "d", "", "", "", "d", "", "", "", "d", "", "", "", "d", "", "", "", "d", "", "", "", "d", "", "", "", "s", "", "", "", "s", "", "", "", "s", "", "", "", "s", "", "", "", "a", "", "", "", "a", "", "", "", "a", "", "", "", "a", "", "", "", "a", "", "", "", "a", "", "", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 10, "a", "RoboPesanteVolante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "d", "d", "sGira", "", "d", "sGira", "", "a", "sGira", "", "a", "a", "s", "aGira", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, "a", "RoboPesante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["dGira"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 8, "d", "RoboTorre", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "", "", "", "s", "", "", "", "s", "", "", "", "s", "", "", "", "a", "", "", "", "a", "", "", "", "a", "", "", "", "a", "", "", "", "a", "", "", "", "a", "", "", "", "w", "", "", "", "w", "", "", "", "w", "", "", "", "w", "", "", "", "d", "", "", "", "d", "", "", "", "d", "", "", "", "d", "", "", "", "d", "", "", "", "d", "", "", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 6, "d", "RoboPesanteVolante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "wGira", "", "d", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 8, "d", "RoboPesante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["caverna9"]:
        percorsoNemico = ["d", "s", "d", "d", "s", "d", "", "", "a", "w", "a", "a", "w", "a", "w", "a", "a", "a", "", "", "d", "d", "d", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 9, "s", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["caverna10"]:
        percorsoNemico = ["d", "w", "d", "d", "w", "dGira", "", "", "s", "a", "a", "s", "a", "s", "a", "s", "a", "sGira", "", "", "d", "w", "d", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 7, "w", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["caverna11"]:
        percorsoNemico = ["dGira"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 7, "d", "RoboPesante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["aGira"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 8, "a", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["dGira", "", "", "", "", "", "wGira", "", "", "", "", "", "aGira", "", "", "", "", "", "sGira", "", "", "", "", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 11, "s", "RoboVolante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["caverna12"]:
        percorsoNemico = ["s", "", "", "", "w", "w", "a", "w", "", "", "s", "d", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 5, "s", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["wGira"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 5, "w", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "a", "a", "a", "", "", "d", "d", "d", "w", "d", "d", "d", "d", "", "", "a", "a", "a", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 14, "a", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "", "", "", "", "", "a", "", "", "", "", "", "s", "", "", "", "", "", "d", "", "", "", "", "", "d", "", "", "", "", "", "w", "", "", "", "", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 9, "w", "RoboVolante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "", "", "", "", "", "a", "", "", "", "", "", "w", "", "", "", "", "", "d", "", "", "", "", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 11, "d", "RoboVolante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "d", "w", "d", "d", "w", "d", "", "", "", "a", "s", "a", "a", "s", "a", "a", "s", "a", "", "", "", "d", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 6, "w", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["sGira"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 14, "s", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["caverna13"]:
        percorsoNemico = ["wGira"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 7, "w", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "", "", "", "", "", "s", "", "", "", "", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 12, "s", "RoboVolante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["aGira"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 3, "a", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "d", "wGira", "", "", "", "a", "a", "a", "a", "", "", "d", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9, "d", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "d", "sGira", "", "a", "a", "sGira", "", "a", "s", "a", "sGira", "", "d", "w", "d", "sGira", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 12, "s", "RoboPesante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "", "", "", "", "", "d", "", "", "", "", "", "d", "", "", "", "", "", "a", "", "", "", "", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 9, "a", "RoboVolante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["wGira"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 6, "w", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["dGira"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 13, "d", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["caverna14"]:
        percorsoNemico = ["a", "a", "w", "a", "a", "a", "a", "w", "aGira", "", "s", "d", "d", "d", "d", "s", "d", "d", "d", "d", "d", "", "a", "a", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 4, "a", "RoboPesante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "s", "s", "a", "sGira", "", "d", "w", "w", "d", "w", "d", "w", "dGira", "", "s", "a", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 12, "s", "RoboPesante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["dGira", "", "", "", "", "", "wGira", "", "", "", "", "", "aGira", "", "", "", "", "", "sGira", "", "", "", "", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 7, "s", "RoboVolante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["caverna15"]:
        percorsoNemico = ["sGira"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 6, "s", "RoboPesante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["wGira"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 6, "w", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["dGira"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 9, "d", "RoboPesante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["caverna16"]:
        percorsoNemico = ["aGira"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 3, "a", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "", "", "", "w", "w", "dGira", "", "", "", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 13, "s", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "w", "a", "wGira", "", "", "d", "s", "s", "s", "s", "aGira", "", "", "w", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, "w", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "", "", "", "d", "", "", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 7, "d", "RoboPesanteVolante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "sGira", "", "", "d", "sGira", "", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 10, "s", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["wGira"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 4, "w", "RoboPesante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "", "", "", "w", "", "", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 8, "w", "RoboPesanteVolante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["dGira"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 14, "d", "RoboPesante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "", "", "", "a", "a", "a", "s", "", "", "w", "w", "w", "a", "w", "", "", "", "s", "d", "s", "d", "s", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 8, "d", "RoboLeggero", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["caverna17"]:
        percorsoNemico = ["wGira"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 3, "w", "RoboPesante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "", "", "", "w", "", "", "", "s", "", "", "", "s", "", "", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 10, "s", "RoboPesanteVolante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "", "", "", "s", "", "", "", "s", "", "", "", "a", "", "", "", "w", "", "", "", "w", "", "", "", "w", "", "", "", "d", "", "", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 8, "d", "RoboPesanteVolante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["aGira"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 15, "a", "RoboPesante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "", "", "", "d", "", "", "", "w", "", "", "", "a", "", "", "", "a", "", "", "", "s", "", "", ""]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 9, "s", "RoboPesanteVolante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["wGira"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 4, "w", "RoboPesante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["dGira"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 12, "d", "RoboPesante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["wGira"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 4, "w", "RoboPesante", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)

    return listaNemiciTotali, listaNemici


def setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi):
    if stanza == GlobalGameVar.dictStanze["caverna1"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["resoOstileImpoInCaverna1"]:
            percorsoPersonaggio = ["s", "a", "sGira", "", "", "", "d", "w", "d", "w", "dGira", "", "", "", "s", "a"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 4, "a", "RoboLeggero-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 6, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 3, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["caverna2"]:
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 7, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 9, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 6, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 11, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 10, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 8, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 14, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 6, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["caverna3"]:
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 6, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 10, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["caverna4"]:
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 2, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 6, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 8, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 7, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 12, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 10, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 12, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["caverna5"]:
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 7, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 3, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 4, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 10, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 4, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 13, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 9, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 8, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 12, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["caverna6"]:
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 13, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 10, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 11, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 8, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 5, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 6, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 3, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 12, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 3, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 10, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 6, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 14, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["caverna7"]:
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 7, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 6, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 4, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 10, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 7, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 3, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 8, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 11, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 4, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 8, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["caverna8"]:
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 6, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 11, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 13, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 3, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 2, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 15, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 14, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 7, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 8, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 13, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["caverna9"]:
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 8, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 11, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["caverna10"]:
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 10, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 5, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["caverna11"]:
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 7, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 8, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["caverna12"]:
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 2, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 7, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 4, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 15, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 7, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 14, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 4, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 15, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["caverna13"]:
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 6, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 9, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 3, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 8, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 14, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 13, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 13, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 5, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 13, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["caverna14"]:
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 4, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 10, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["caverna15"]:
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 7, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 5, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 9, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["caverna16"]:
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 3, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 7, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 15, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 12, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 11, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 11, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 3, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 4, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 14, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 10, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 8, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["caverna17"]:
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 15, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 3, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 3, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 12, "s", "OggettoCumuloImpo-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)

    return listaPersonaggiTotali, listaPersonaggi
