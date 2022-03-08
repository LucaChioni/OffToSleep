# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj
import Codice.GestioneNemiciPersonaggi.NemicoObj as NemicoObj


def setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria):
    if stanza == GlobalGameVar.dictStanze["internoCastello1"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 6, "s", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 9, "s", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 5, "s", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 7, "s", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 3, "s", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 8, "s", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 4, "d", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 6, "s", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 8, "s", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 4, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 6, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 3, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 5, "d", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["internoCastello2"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 9, "a", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 11, "a", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 13, "w", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 10, "a", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 12, "a", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 9, "s", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 11, "d", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 12, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 10, "s", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["internoCastello3"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 9, "d", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 12, "w", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 3, "a", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 10, "s", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 4, "a", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 2, "a", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 12, "s", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 13, "s", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 11, "s", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["internoCastello4"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 4, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 4, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 3, "s", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 15, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 13, "s", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 10, "s", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 14, "s", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["internoCastello5"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 12, "d", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 4, "s", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 10, "d", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 5, "s", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 5, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 4, "s", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 10, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 11, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 12, "w", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 5, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["internoCastello6"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, "w", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 10, "w", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 7, "a", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["internoCastello7"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 10, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 9, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 12, "w", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 8, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 6, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 10, "w", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 8, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["internoCastello8"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 10, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 9, "d", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 8, "s", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 11, "s", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["internoCastello9"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 14, "w", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 13, "a", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 6, "w", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 14, "a", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13, "a", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 4, "a", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 5, "a", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["internoCastello10"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 10, "s", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 14, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9, "s", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 3, "a", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 2, "a", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 15, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 14, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["internoCastello11"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 3, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 10, "d", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 9, "d", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 11, "w", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 11, "w", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 3, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["internoCastello12"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 8, "s", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 12, "a", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 13, "a", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 12, "a", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 11, "a", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["internoCastello13"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 7, "w", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 12, "w", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11, "w", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 5, "a", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 4, "a", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 6, "a", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["internoCastello14"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 11, "a", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 9, "s", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13, "a", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 10, "a", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["internoCastello15"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 4, "a", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 11, "w", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 6, "a", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 10, "w", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 12, "a", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["internoCastello16"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 13, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 12, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 4, "s", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 14, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 3, "a", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 9, "s", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 8, "s", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 14, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 3, "a", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 4, "a", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 3, "a", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["internoCastello17"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 9, "s", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 13, "w", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 10, "w", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 3, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["internoCastello18"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 12, "a", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 13, "a", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["internoCastello19"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 13, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 12, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 14, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)

    return listaNemiciTotali, listaNemici


def setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi):
    if stanza == GlobalGameVar.dictStanze["internoCastello1"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] or avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
            if GlobalGameVar.dictAvanzamentoStoria["servoLanciaEntratoNelCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["servoLanciaTornatoAlCancello"]:
                percorsoPersonaggio = ["sGira", "mantieniPosizione"]
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, "s", "ServoLancia-3", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["dGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 8, "d", "ServoLancia-4", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["aGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 8, "a", "ServoArco-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 4, "s", "OggettoQuadro-2", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 5, "s", "OggettoQuadro-2", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 1, "s", "OggettoQuadro-1", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 12, "s", "OggettoQuadro-4", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["internoCastello2"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] or avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
            percorsoPersonaggio = ["aGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 14, "a", "ServoSpada-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 2, "s", "OggettoQuadro-5", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["internoCastello3"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] or avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
            percorsoPersonaggio = ["wGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 5, "w", "ServoArco-1", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 9, "s", "OggettoLibreriaCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 10, "s", "OggettoLibreriaCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11, "s", "OggettoLibreriaCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 12, "s", "OggettoLibreriaCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 13, "s", "OggettoLibreriaCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 14, "s", "OggettoLibreriaCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 3, "s", "OggettoQuadro-8", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 4, "s", "OggettoQuadro-8", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 1, "s", "OggettoQuadro-7", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 1, "s", "OggettoQuadro-7", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 9, "s", "OggettoQuadro-9", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["internoCastello4"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] or avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
            percorsoPersonaggio = ["sGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 3, "s", "ServoLancia-5", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 14, "s", "OggettoSpecchioCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 14, "s", "OggettoSpecchioCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 8, "s", "OggettoLavandinoCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 8, "s", "OggettoLavandinoCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 13, "s", "OggettoGabinettoCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 13, "s", "OggettoGabinettoCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 13, "s", "OggettoGabinettoCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 8, "s", "OggettoVascaCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 9, "s", "OggettoVascaCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 10, "s", "OggettoVascaCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 11, "s", "OggettoVascaCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2, "s", "OggettoQuadro-12", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 2, "s", "OggettoQuadro-11", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 10, "s", "OggettoQuadro-10", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 11, "s", "OggettoQuadro-10", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["internoCastello5"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] or avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
            percorsoPersonaggio = ["sGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 9, "s", "ServoArco-2", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 11, "s", "OggettoQuadro-13", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["internoCastello6"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] or avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
            percorsoPersonaggio = ["sGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 6, "s", "ServoSpada-1", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 15, "s", "OggettoQuadro-15", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 15, "s", "OggettoQuadro-15", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["internoCastello7"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] or avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["cenaCastelloServita"]:
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 8, "s", "OggettoSediaCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13, "s", "OggettoCarrelloCiboCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 13, "s", "OggettoCarrelloCiboCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 13, "s", "OggettoCarrelloCiboCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 14, "s", "OggettoCarrelloCiboCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 14, "s", "OggettoCarrelloCiboCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 14, "s", "OggettoCarrelloCiboCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioCenaAlCastello"]:
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 8, "s", "OggettoSaraSedutaCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["fineCenaAlCastello"]:
                percorsoPersonaggio = ["d", "d", "d", "d", "d"]
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 7, "a", "ServoLancia-13", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["dGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 4, "d", "ServoLancia-6", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["aGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 14, "a", "ServoArco-3", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 6, "s", "OggettoQuadro-17", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 7, "s", "OggettoQuadro-17", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 8, "s", "OggettoQuadro-17", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, "s", "OggettoCaminoCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 15, "s", "OggettoCaminoCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 15, "s", "OggettoCaminoCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 15, "s", "OggettoCaminoCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 15, "s", "OggettoCaminoCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 1, "s", "OggettoQuadro-16", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 12, "s", "OggettoQuadro-18", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 13, "s", "OggettoQuadro-18", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["internoCastello8"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] or avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
            percorsoPersonaggio = ["sGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 8, "s", "ServoArco-4", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 12, "s", "OggettoVasoCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["internoCastello9"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] or avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
            percorsoPersonaggio = ["sGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 7, "s", "ServoLancia-7", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 1, "s", "OggettoQuadro-2", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 1, "s", "OggettoQuadro-2", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 16, "s", "OggettoQuadro-1", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 16, "s", "OggettoQuadro-1", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 1, "s", "OggettoQuadro-3", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["internoCastello10"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] or avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
            percorsoPersonaggio = ["sGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, "s", "ServoLancia-8", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["sGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 13, "s", "ServoArco-5", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, "s", "OggettoLettoCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 5, "s", "OggettoLettoCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 4, "s", "OggettoLettoCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 5, "s", "OggettoLettoCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, "s", "OggettoArmadioCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 7, "s", "OggettoArmadioCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 7, "s", "OggettoArmadioCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 7, "s", "OggettoArmadioCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 3, "s", "OggettoComodinoCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 7, "s", "OggettoLavandinoCastello-1", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 7, "s", "OggettoLavandinoCastello-1", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 9, "s", "OggettoVascaCastello-1", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 9, "s", "OggettoVascaCastello-1", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 9, "s", "OggettoVascaCastello-1", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 9, "s", "OggettoVascaCastello-1", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 7, "s", "OggettoGabinettoCastello-1", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 7, "s", "OggettoGabinettoCastello-1", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 7, "s", "OggettoGabinettoCastello-1", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 16, "s", "OggettoQuadro-5", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 16, "s", "OggettoQuadro-5", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 1, "s", "OggettoQuadro-4", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["internoCastello11"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] or avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
            if GlobalGameVar.dictAvanzamentoStoria["dormitoNelCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["primoDialogoNeil"]:
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 14, "s", "OggettoFinestraCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 14, "s", "OggettoFinestraCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 14, "s", "OggettoFinestraCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 14, "s", "OggettoFinestraCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 14, "s", "OggettoFinestraCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14, "s", "OggettoFinestraCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 14, "s", "OggettoFinestraCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 14, "s", "OggettoFinestraCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["sGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, "s", "ServoSpada-2", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["sGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 2, "s", "ServoSpada-3", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 1, "s", "OggettoQuadro-6", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 1, "s", "OggettoQuadro-6", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["internoCastello12"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] or avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
            percorsoPersonaggio = ["wGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 13, "w", "ServoArco-6", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 1, "s", "OggettoQuadro-8", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 7, "s", "OggettoQuadro-9", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["internoCastello13"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] or avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
            percorsoPersonaggio = ["dGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 6, "d", "ServoArco-7", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 12, "s", "OggettoQuadro-13", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 3, "s", "OggettoBarcaCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 2, "s", "OggettoQuadro-12", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 11, "s", "OggettoQuadro-11", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["internoCastello14"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] or avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
            percorsoPersonaggio = ["dGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 12, "d", "ServoSpada-4", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 16, "s", "OggettoQuadro-15", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 8, "s", "OggettoQuadro-14", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 9, "s", "OggettoQuadro-14", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["internoCastello15"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] or avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
            percorsoPersonaggio = ["dGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 12, "d", "ServoLancia-9", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, "s", "OggettoQuadro-16", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, "s", "OggettoQuadro-16", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["internoCastello16"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] or avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
            if GlobalGameVar.dictAvanzamentoStoria["dormitoNelCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["primoDialogoNeil"]:
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 10, "s", "OggettoFinestraCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 11, "s", "OggettoFinestraCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 12, "s", "OggettoFinestraCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 13, "s", "OggettoFinestraCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["dGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 8, "d", "ServoSpada-5", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["sGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 13, "s", "ServoSpada-6", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["sGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 2, "s", "ServoLancia-10", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 3, "s", "OggettoQuadro-1", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4, "s", "OggettoQuadro-1", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 16, "s", "OggettoQuadro-2", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 16, "s", "OggettoQuadro-2", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 1, "s", "OggettoQuadro-18", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 1, "s", "OggettoQuadro-18", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["internoCastello17"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] or avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
            percorsoPersonaggio = ["sGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, "s", "ServoSpada-7", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 16, "s", "OggettoQuadro-3", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 1, "s", "OggettoQuadro-4", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["internoCastello18"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] or avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["guardiaCastelloChiusoPortaLibreriaInternoCastello18"]:
                percorsoPersonaggio = ["dGira", "mantieniPosizione"]
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 12, "d", "ServoLancia-12", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["dGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 11, "d", "ServoArco-8", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 6, "s", "OggettoLibreriaCastello-1", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, "s", "OggettoLibreriaCastello-2", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 9, "s", "OggettoLibreriaCastello-3", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 4, "s", "OggettoLibreriaCastello-4", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 13, "s", "OggettoLibreriaCastello-5", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 8, "s", "OggettoLibreriaCastello-6", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 1, "s", "OggettoQuadro-5", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 1, "s", "OggettoQuadro-5", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 16, "s", "OggettoQuadro-6", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["internoCastello19"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] or avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
            percorsoPersonaggio = ["dGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 4, "d", "ServoLancia-11", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["wGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 14, "w", "ServoSpada-8", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["soldatoUscitoDaInternoCastello21PostRianimazione"]:
            percorsoPersonaggio = ["d"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13, "d", "ServoLancia-14", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 9, "s", "OggettoFinestraCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 10, "s", "OggettoFinestraCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 11, "s", "OggettoFinestraCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 12, "s", "OggettoFinestraCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ripresoImpoDaNeil"]:
            percorsoPersonaggio = ["sGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 9, "s", "Neil-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
            percorsoPersonaggio = ["d", "d", "s", "s", "s", "dGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 9, "a", "Neil-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presiStrumentiPerStudiareImpo"]:
            percorsoPersonaggio = ["dGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 12, "d", "Neil-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["messoImpoSulTavoloDopoConsegnaStrumenti"]:
            percorsoPersonaggio = ["wGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, "w", "ServoSpada-9", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["wGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 9, "w", "Neil-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"]:
            percorsoPersonaggio = ["wGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, "w", "ServoSpada-9", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["sGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 9, "s", "Neil-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        elif GlobalGameVar.dictAvanzamentoStoria["chiusoPortaInternoCastello20DaSoldato"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["apertoPortaInternoCastello20AndandoInInternoCastello19"]:
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 4, "s", "OggettoPortaCastelloChiusa-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        elif GlobalGameVar.dictAvanzamentoStoria["risveglioSaraResuscitata"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            percorsoPersonaggio = ["wGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, "w", "ServoLancia-14", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 12, "d", "Neil-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 12, "s", "Mercante-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            percorsoPersonaggio = ["wGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 5, "w", "ServoLancia-14", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 12, "s", "Mercante-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 16, "s", "OggettoQuadro-11", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, "s", "OggettoQuadro-8", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 2, "s", "OggettoQuadro-10", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 2, "s", "OggettoQuadro-10", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 10, "s", "OggettoTavoloVuotoCastelloA-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 10, "s", "OggettoTavoloVuotoCastelloB-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 12, "s", "OggettoAppuntiNeilCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 10, "s", "OggettoTavoloAttrezziCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 10, "s", "OggettoTavoloAttrezziCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 10, "s", "OggettoTavoloAttrezziCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 10, "s", "OggettoTavoloAttrezziCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 2, "s", "OggettoQuadro-9", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["internoCastello21"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 7, "s", "Neil-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, "s", "OggettoArmadioRatti-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 3, "s", "OggettoArmadioRatti-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 4, "s", "OggettoArmadioRatti-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 5, "s", "OggettoArmadioRatti-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 6, "s", "OggettoArmadioRatti-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 7, "s", "OggettoArmadioRatti-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 8, "s", "OggettoArmadioRatti-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 9, "s", "OggettoArmadioRatti-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 10, "s", "OggettoArmadioRatti-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 11, "s", "OggettoArmadioRatti-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 6, "s", "OggettoAppuntiRattiA-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 8, "s", "OggettoAppuntiRattiB-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 14, "s", "OggettoAppuntiRattiC-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 12, "s", "OggettoValvolaMacchinario-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 8, "s", "OggettoAppuntiRianimazioneSara-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 12, "s", "OggettoCapsulaMacchinario-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 13, "s", "OggettoValvolaMacchinario-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 7, "s", "OggettoSpecchio-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)
        percorsoPersonaggio = []
        personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 8, "s", "OggettoSpecchio-0", stanza, avanzamentoStoria, percorsoPersonaggio)
        listaPersonaggi.append(personaggio)
        listaPersonaggiTotali.append(personaggio)

    return listaPersonaggiTotali, listaPersonaggi
