# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj
import Codice.GestioneNemiciPersonaggi.NemicoObj as NemicoObj


def setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria):
    if stanza == GlobalGameVar.dictStanze["passoMontano1"]:
        percorsoNemico = ["w", "d", "a", "s", "a", "s", "s", "w", "w", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 4, "d", "Struzzo", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "w", "w", "a", "s", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 6, "s", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "a", "a", "s", "s", "d", "w", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 10, "d", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "s", "d", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 12, "w", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "d", "d", "a", "s", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 11, "a", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "s", "d", "d", "w", "a", "w", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 10, "a", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "s", "d", "d", "w", "a", "w", "a", "a", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 7, "s", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["passoMontano2"]:
        percorsoNemico = ["d", "d", "s", "d", "s", "a", "a", "a", "w", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 11, "w", "Struzzo", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "d", "s", "d", "a", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 8, "a", "Struzzo", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "s", "s", "a", "w", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 9, "w", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "d", "w", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 7, "a", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "s", "a", "a", "w", "w", "d", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 5, "s", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "s", "w", "d", "w", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 4, "a", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "d", "a", "a", "a", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 7, "d", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["passoMontano3"]:
        percorsoNemico = ["w", "d", "w", "a", "s", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 13, "s", "Struzzo", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "d", "d", "a", "a", "a", "w", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 9, "d", "Struzzo", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "s", "d", "w", "a", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 11, "w", "Struzzo", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "w", "w", "w", "a", "s", "d", "s", "s", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 7, "d", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "s", "s", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 5, "w", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "w", "w", "d", "s", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 9, "s", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "a", "a", "s", "d", "s", "d", "d", "w", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 5, "a", "Struzzo", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "w", "d", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 3, "s", "Struzzo", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "s", "d", "d", "d", "w", "a", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 7, "a", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "s", "w", "w", "d", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 10, "s", "Struzzo", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "w", "a", "a", "w", "a", "s", "d", "s", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 6, "d", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "s", "s", "w", "w", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 8, "a", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["passoMontano4"]:
        percorsoNemico = ["w", "w", "d", "s", "d", "s", "a", "s", "a", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 7, "w", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "s", "w", "w", "d", "w", "a", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 4, "s", "Struzzo", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "d", "s", "s", "w", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 8, "a", "Struzzo", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "d", "w", "a", "s", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 6, "s", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "w", "w", "a", "s", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 9, "d", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "s", "s", "d", "d", "w", "a", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 4, "w", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "a", "a", "a", "d", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 8, "d", "Struzzo", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "d", "a", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 8, "w", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "d", "s", "a", "w", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 10, "a", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "w", "a", "w", "s", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 13, "s", "GufoBianco", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "s", "s", "a", "w", "a", "w", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 7, "d", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "w", "a", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 9, "s", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "d", "d", "a", "s", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 12, "a", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["passoMontano5"]:
        percorsoNemico = ["w", "a", "s", "a", "s", "d", "d", "d", "w", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 12, "a", "Casuario", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "d", "s", "a", "a", "a", "w", "w", "d", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 9, "s", "Struzzo", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "d", "s", "s", "a", "a", "w", "a", "d", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11, "d", "Struzzo", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "d", "s", "a", "s", "a", "w", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 5, "w", "Struzzo", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "a", "w", "d", "s", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 4, "d", "Struzzo", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "d", "a", "a", "w", "w", "d", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 8, "s", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "a", "w", "w", "s", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 7, "d", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "d", "w", "s", "s", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 10, "a", "Struzzo", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["passoMontano6"]:
        percorsoNemico = ["w", "a", "w", "s", "s", "s", "d", "s", "w", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 6, "w", "Struzzo", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "a", "s", "s", "d", "d", "d", "w", "w", "a", "s", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 10, "a", "Struzzo", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "w", "s", "s", "a", "d", "w", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 4, "a", "Struzzo", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["s", "s", "w", "a", "a", "w", "w", "s", "d", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 7, "d", "Casuario", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "w", "d", "w", "a", "w", "s", "a", "s", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 9, "s", "Struzzo", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["passoMontano7"]:
        percorsoNemico = ["a", "a", "s", "s", "d", "w", "d", "d", "w", "w", "a", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 4, "s", "GufoBianco", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "s", "d", "w", "d", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 6, "a", "GufoBianco", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "w", "d", "s", "s", "s", "a", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 12, "w", "GufoBianco", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "d", "s", "d", "a", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 9, "a", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "s", "a", "a", "a", "a", "w", "w", "d", "s", "d", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 11, "d", "GufoBianco", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "d", "d", "w", "a", "a", "a", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 10, "s", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "w", "a", "w", "a", "s", "s", "d", "s", "d", "d", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 7, "w", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "d", "w", "s", "s", "s", "a", "a", "w", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 4, "d", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "w", "s", "s", "s", "d", "d", "w", "a", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 5, "a", "Casuario", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "d", "s", "a", "a", "a", "w", "w", "d", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 3, "s", "Casuario", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["passoMontano8"]:
        percorsoNemico = ["d", "w", "d", "a", "a", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 9, "s", "GufoBianco", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "a", "a", "s", "d", "d", "d", "d", "d", "s", "w", "w", "a", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 6, "a", "Falco", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "a", "s", "s", "d", "d", "s", "d", "w", "w", "a", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 11, "a", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "d", "d", "s", "s", "s", "s", "a", "w", "a", "w", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 8, "w", "GufoMarrone", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "s", "a", "a", "w", "w", "d", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 4, "s", "GufoBianco", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "s", "d", "d", "w", "d", "a", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 3, "a", "GufoBianco", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["passoMontano9"]:
        percorsoNemico = ["d", "d", "d", "d", "d", "s", "a", "a", "a", "a", "a", "a", "w", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 11, "d", "Falco", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "a", "d", "w", "a", "w", "d", "d", "s", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 8, "s", "GufoBianco", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "d", "s", "s", "a", "a", "a", "d", "w", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 9, "d", "GufoBianco", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "d", "d", "s", "d", "a", "a", "s", "a", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 7, "w", "GufoBianco", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "w", "a", "s", "a", "d", "s", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 5, "d", "GufoBianco", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "w", "w", "d", "s", "d", "s", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 4, "a", "GufoBianco", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "a", "a", "a", "s", "d", "d", "d", "d", "d", "d", "w", "a", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 3, "a", "Falco", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
    elif stanza == GlobalGameVar.dictStanze["passoMontano10"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["uscitoDaPassoMontano"]:
            percorsoNemico = ["a", "a", "s", "s", "d", "d", "d", "d", "d", "w", "w", "a", "a", "a"]
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 11, "a", "Aquila", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
        percorsoNemico = ["d", "w", "w", "s", "s", "s", "a", "a", "w", "w", "d", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 9, "s", "GufoBianco", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["d", "s", "a", "a", "a", "a", "w", "d", "d", "w", "d", "s"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 5, "s", "Falco", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "s", "w", "w", "d", "s", "d", "d", "a", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 3, "a", "GufoBianco", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["a", "a", "s", "d", "d", "d", "s", "a", "s", "d", "d", "w", "w", "w", "a", "a"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 4, "a", "Falco", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = ["w", "d", "a", "a", "s", "a", "d", "d"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 9, "d", "GufoBianco", stanza, percorsoNemico)
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)

    return listaNemiciTotali, listaNemici


def setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi):
    if stanza == GlobalGameVar.dictStanze["passoMontano1"]:
        avanzamentoDialogoPazzo = 0
        i = 0
        while i < len(listaAvanzamentoDialoghi):
            if listaAvanzamentoDialoghi[i] == "Pazzo2-0":
                avanzamentoDialogoPazzo = listaAvanzamentoDialoghi[i + 1]
                break
            elif listaAvanzamentoDialoghi[i] == "Pazzo1-0":
                avanzamentoDialogoPazzo = listaAvanzamentoDialoghi[i + 1]
            i += 2
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["uscitoDaPassoMontano"] and 4 <= avanzamentoDialogoPazzo < 6:
            percorsoPersonaggio = ["dGira", "mantieniPosizione"]
            if GlobalGameVar.pazzoStrabico:
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 14, "d", "Pazzo2-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            else:
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 14, "d", "Pazzo1-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            personaggio.avanzamentoDialogo = avanzamentoDialogoPazzo
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)

    return listaPersonaggiTotali, listaPersonaggi
