# -*- coding: utf-8 -*-

from NemicoObj import *
from PersonaggioObj import *


def caricaNemiciEPersonaggi(avanzamentoStoria, stanza, stanzaVecchia, stanzeGiaVisitate, listaNemiciTotali, listaPersonaggiTotali):
    if stanzaVecchia != 0 and ((stanza in GlobalVar.vetStanzePacifiche and stanzaVecchia not in GlobalVar.vetStanzePacifiche) or (stanza not in GlobalVar.vetStanzePacifiche and stanzaVecchia in GlobalVar.vetStanzePacifiche)):
        listaNemiciTotali = []
        listaPersonaggiTotali = []
        stanzeGiaVisitate = []

    listaNemici = []
    if not stanza in stanzeGiaVisitate:
        if stanza == GlobalVar.dictStanze["sognoSara2"]:
            percorsoNemico = ["s", "d", "d", "w", "w", "w", "a", "a", "s", "s"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 7, "s", "Orco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["s", "s", "w", "w"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 2, "s", "Orco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["d", "d", "d", "d", "a", "a", "a", "a"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 4, "d", "Orco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
        if stanza == GlobalVar.dictStanze["sognoSara3"]:
            percorsoNemico = ["a", "a", "a", "w", "w", "w", "d", "d", "d", "s", "s", "s"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 8, "s", "Pipistrello", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["d", "d", "s", "s", "s", "d", "a", "a", "a", "s", "a", "w", "w", "w", "w", "d"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 5, "d", "Pipistrello", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["w", "a", "s", "a", "d", "d"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 10, "w", "Orco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
        if stanza == GlobalVar.dictStanze["forestaCadetta1"]:
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                percorsoNemico = ["s", "s", "a", "a", "a", "w", "w", "w", "d", "d", "d", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 6, "s", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "a", "s", "s", "d", "d", "w", "d", "d", "w", "w", "a", "a", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 4, "s", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "a", "s", "s", "d", "d", "d", "w", "w", "a"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 12, "a", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "s", "w", "w"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 11, "w", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "s", "a", "a", "a", "a", "w", "d", "d"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 9, "d", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "s", "s", "w"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 4, "w", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
            else:
                percorsoNemico = ["s", "s", "a", "a", "a", "w", "w", "w", "d", "d", "d", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 6, "s", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "s", "d", "d", "d", "d", "w", "w", "w", "w", "a", "a", "s", "s", "a", "a"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 4, "a", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "a", "s", "s", "d", "d", "w", "d", "d", "w", "w", "a", "a", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 4, "s", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "d", "d", "s", "s", "a", "a", "w"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 10, "w", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "a", "s", "s", "d", "d", "d", "w", "w", "a"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 12, "a", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "s", "w", "w"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 11, "w", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "w", "s", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 13, "s", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "a", "a", "a", "a", "d", "d"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 12, "d", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "s", "s", "d", "d", "d", "w", "w", "a", "w", "w", "a", "s", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 13, "s", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "s", "a", "a", "a", "a", "w", "d", "d"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 9, "d", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "w", "w", "a", "a", "a", "s", "s", "d"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 5, "d", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "s", "s", "w"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 4, "w", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
        if stanza == GlobalVar.dictStanze["forestaCadetta2"]:
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                percorsoNemico = ["w", "s", "s", "w"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 26, GlobalVar.gsy // 18 * 14, "w", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "a", "a", "a", "w", "w", "d", "d", "s", "d"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 14, "d", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "w", "w", "w", "a", "s", "s", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 6, "s", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "w", "d", "d", "s", "s", "a", "w"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 3, "w", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "d", "d", "w", "w", "a", "a", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 3, "s", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "d", "s", "s", "a", "w"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 8, "w", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
            else:
                percorsoNemico = ["a", "w", "d", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 12, "s", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "s", "s", "w"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 26, GlobalVar.gsy // 18 * 14, "w", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "w", "a", "a", "s", "d"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 15, "d", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "w", "w", "d", "s", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 13, "s", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "a", "a", "a", "w", "w", "d", "d", "s", "d"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 14, "d", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "w", "w", "a", "a", "s", "s", "d"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 7, "d", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "w", "w", "w", "a", "s", "s", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 28, GlobalVar.gsy // 18 * 6, "s", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "w", "d", "d", "s", "s", "s", "s", "w", "w", "a", "a"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 4, "a", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "w", "d", "d", "s", "s", "a", "w"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 3, "w", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "w", "d", "s", "s", "s", "a", "w"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 5, "w", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "a", "a", "a", "d", "d"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 7, "d", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "d", "d", "w", "w", "a", "a", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 3, "s", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "d", "d", "d", "a", "a"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 10, "a", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "d", "s", "s", "a", "w"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 8, "w", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "d", "w", "w", "a", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 12, "s", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
        if stanza == GlobalVar.dictStanze["forestaCadetta3"]:
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                percorsoNemico = ["a", "w", "w", "d", "s", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 7, "s", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "w", "w", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 5, "s", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "w", "w", "w", "a", "a", "a", "s", "s", "s", "d"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 6, "d", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "a", "a", "a", "d"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 13, "d", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "a", "a", "a", "w", "w", "d", "d", "d", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 12, "s", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "w", "w", "w", "a", "a", "s", "s", "s", "d"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 13, "d", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
            else:
                percorsoNemico = ["a", "w", "w", "d", "d", "s", "s", "a"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 6, "a", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "w", "s", "d"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 5, "d", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "w", "w", "d", "s", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 7, "s", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "a", "d", "d", "d", "d", "a", "a"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 7, "a", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "d", "w", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 7, "s", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "w", "w", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 5, "s", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "w", "a", "a", "a", "s", "s", "s", "w", "w", "w", "d", "d", "d", "s", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 4, "s", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "w", "w", "w", "a", "a", "a", "s", "s", "s", "d"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 6, "d", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "a", "d", "d"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 11, "d", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "w", "d", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 11, "s", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "a", "a", "a", "d"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 13, "d", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "a", "a", "a", "w", "w", "d", "d", "d", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 12, "s", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "d", "a", "a", "a", "a", "d"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 14, "d", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "a", "a"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 14, "a", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "a", "w", "d"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 11, "d", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "w", "w", "w", "a", "a", "s", "s", "s", "d"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 13, "d", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
        if stanza == GlobalVar.dictStanze["forestaCadetta4"]:
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                percorsoNemico = ["d", "w", "w", "d", "d", "s", "s", "s", "s", "a", "a", "a", "w", "w"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 26, GlobalVar.gsy // 18 * 6, "w", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "a", "a", "a", "w", "w", "d", "w", "d", "d", "s", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4, "s", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "a", "a", "s", "s", "d", "d", "w", "d", "w"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 3, "w", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "d", "w", "w", "w", "w", "a", "a", "a", "a", "a", "a", "a", "s", "s", "s", "s", "s", "d", "d", "d", "d", "w"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 21, GlobalVar.gsy // 18 * 12, "w", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
            else:
                percorsoNemico = ["d", "w", "w", "d", "d", "s", "s", "s", "s", "a", "a", "a", "w", "w"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 26, GlobalVar.gsy // 18 * 6, "w", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "a", "a", "a", "d", "d"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 6, "d", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 4, "s", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "a", "a", "a", "w", "w", "d", "w", "d", "d", "s", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 4, "s", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "d", "w", "w", "w", "a", "a", "a", "s", "a", "s", "s", "d"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 13, GlobalVar.gsy // 18 * 5, "d", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "a", "a", "s", "s", "d", "d", "w", "d", "w"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 3, "w", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "d", "d", "d", "s", "s", "a", "a", "w", "a"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 7, "a", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "a", "a"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 11, "a", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "s", "s", "w", "w", "a"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 9, "a", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "d", "w", "w", "w", "w", "a", "a", "a", "a", "a", "a", "a", "s", "s", "s", "s", "s", "d", "d", "d", "d", "w"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 21, GlobalVar.gsy // 18 * 12, "w", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "w", "d", "w", "s", "a", "s", "d"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 11, "d", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
        if stanza == GlobalVar.dictStanze["forestaCadetta6"]:
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                percorsoNemico = ["d", "d", "d", "d", "s", "s", "a", "a", "s", "a", "a", "a", "a", "a", "w", "w", "w", "d", "d", "d"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 7, "d", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "s", "a", "s", "s", "d", "d", "d", "s", "d", "d", "d", "w", "w", "w", "a", "a", "w", "a", "a"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 11, "a", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "w", "w", "d", "d", "d", "d", "s", "s", "a", "s", "s", "a", "a", "w", "w"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 4, "w", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "s", "s", "a", "a", "a", "w", "w", "w", "w", "s", "s", "s", "s", "d", "d", "d", "w", "w", "w"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 12, "w", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "s", "d", "d", "w", "w", "w", "a", "a", "a", "a", "s", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 4, "s", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "s", "d", "d", "w", "d", "w", "w", "w", "a", "a", "a", "s", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 26, GlobalVar.gsy // 18 * 13, "s", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
            else:
                percorsoNemico = ["a", "a", "w", "w", "w", "d", "d", "d", "d", "d", "d", "d", "s", "s", "a", "a", "s", "a", "a", "a"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 10, "a", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "d", "d", "s", "s", "a", "a", "s", "a", "a", "a", "a", "a", "w", "w", "w", "d", "d", "d"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 7, "d", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "s", "a", "s", "s", "d", "d", "d", "s", "d", "d", "d", "w", "w", "w", "a", "a", "w", "a", "a"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 11, "a", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "s", "s", "d", "d", "d", "w", "w", "w", "a", "w", "a", "a", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 9, "s", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "w", "w", "d", "d", "d", "d", "s", "s", "a", "s", "s", "a", "a", "w", "w"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 4, "w", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "d", "d", "d", "d", "w", "w", "a", "a", "a", "a", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 6, "s", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "s", "s", "a", "a", "a", "w", "w", "w", "w", "s", "s", "s", "s", "d", "d", "d", "w", "w", "w"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 12, "w", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "s", "d", "d", "w", "w", "w", "a", "a", "a", "a", "s", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 4, "s", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "s", "a", "a", "s", "d", "d", "w", "w", "w"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 10, "w", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "s", "d", "d", "w", "d", "w", "w", "w", "a", "a", "a", "s", "s"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 26, GlobalVar.gsy // 18 * 13, "s", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "d", "d", "s", "s", "a", "a", "a", "s", "w", "w", "d"]
                nemico = NemicoObj(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 6, "d", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
        if stanza == GlobalVar.dictStanze["forestaCadetta7"] and not stanzaVecchia == GlobalVar.dictStanze["forestaCadetta7"]:
            percorsoNemico = ["w", "d", "d", "s", "s", "a", "a", "a", "a", "a", "w", "d", "d", "d"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 7, "d", "LupoNero", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["a", "a", "a", "a", "s", "s", "s", "d", "d", "s", "s", "s", "d", "d", "d", "d", "w", "w", "w", "w", "w", "w", "a", "a"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 8, "a", "LupoNero", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["d", "d", "d", "d", "w", "w", "w", "w", "w", "w", "a", "a", "a", "a", "a", "a", "s", "s", "s", "d", "d", "s", "s", "s"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 25, GlobalVar.gsy // 18 * 14, "s", "LupoNero", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["w", "a", "w", "w", "d", "s", "d", "s", "s", "a"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 27, GlobalVar.gsy // 18 * 13, "a", "LupoNero", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["a", "s", "s", "d", "d", "d", "w", "d", "d", "w", "w", "a", "a", "s", "a", "a"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 10, "a", "LupoNero", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["a", "a", "a", "a", "a", "w", "a", "a", "s", "s", "d", "d", "d", "d", "w", "w", "d", "w", "d", "d", "s", "s"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 14, "s", "LupoNero", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["d", "d", "s", "s", "a", "a", "s", "a", "w", "w", "w", "d"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 9, "d", "LupoNero", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["s", "a", "a", "a", "a", "w", "w", "d", "d", "d", "d", "s"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 4, "s", "LupoNero", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["d", "d", "s", "a", "a", "a", "", "w", "d"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 6, "d", "Cinghiale", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
        if stanza == GlobalVar.dictStanze["forestaCadetta8"]:
            percorsoNemico = ["a", "w", "w", "w", "a", "a", "s", "s", "d", "d", "d", "w", "d", "d", "s", "d", "s", "s", "a", "a", "a", "w"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 7, "w", "LupoNero", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["d", "d", "d", "s", "s", "s", "a", "a", "w", "w", "d", "w", "w", "a", "a", "a", "a", "a", "w", "w", "d", "d", "d", "s", "s", "s"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 26, GlobalVar.gsy // 18 * 5, "s", "LupoNero", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["d", "d", "d", "d", "d", "s", "a", "a", "a", "a", "a", "w"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 20, GlobalVar.gsy // 18 * 10, "w", "LupoBianco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["d", "s", "s", "s", "a", "a", "a", "w", "w", "w", "d", "d"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 12, "d", "LupoBianco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["a", "a", "s", "s", "d", "d", "d", "w", "w", "w", "w", "a", "a", "s", "d", "s"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 13, "s", "LupoGrigio", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["d", "s", "a", "s", "s", "a", "w", "w", "w", "d"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 13, GlobalVar.gsy // 18 * 7, "d", "TartarugaMarrone", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["s", "s", "a", "a", "s", "a", "w", "w", "w", "a", "w", "d", "d", "d", "d", "d", "s", "a"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 3, "a", "LupoGrigio", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["w", "a", "a", "a", "s", "s", "a", "s", "s", "d", "d", "w", "w", "d", "d", "w"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 10, GlobalVar.gsy // 18 * 5, "w", "LupoGrigio", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["d", "d", "a", "a", "s", "a", "a", "d", "d", "w"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 8, "w", "TartarugaMarrone", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["s", "a", "s", "s", "w", "w", "a", "w", "w", "d", "d", "s"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 3, "s", "TartarugaVerde", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["s", "s", "a", "a", "w", "d", "w", "d"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 12, "d", "TartarugaVerde", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["d", "d", "w", "d", "w", "w", "w", "a", "a", "a", "w", "a", "a", "s", "s", "s", "s", "s", "d", "d"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 15, "d", "TartarugaVerde", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["a", "s", "s", "d", "d", "d", "d", "w", "a", "w", "a", "a"]
            nemico = NemicoObj(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 13, "a", "TartarugaVerde", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
    else:
        for nemico in listaNemiciTotali:
            if nemico.stanzaDiAppartenenza == stanza:
                listaNemici.append(nemico)

    listaPersonaggi = []
    if not stanza in stanzeGiaVisitate:
        if stanza == GlobalVar.dictStanze["casaSamSara1"]:
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 7, GlobalVar.gsy // 18 * 13, "a", "OggettoLettoSara", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 3, "d", "OggettoLavandinoCucina", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 8, GlobalVar.gsy // 18 * 2, "s", "OggettoLavandinoBagno", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 5, "a", "OggettoScaffaleBicchieriA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 6, "a", "OggettoScaffaleBicchieriB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 19, GlobalVar.gsy // 18 * 7, "a", "OggettoScaffaleBicchieriC", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 14, "w", "OggettoComodinoSara", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 15, "w", "OggettoFinestraA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 15, "w", "OggettoFinestraB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 3, GlobalVar.gsy // 18 * 12, "d", "OggettoLettoSam", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 13, "d", "OggettoComodinoSam", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 5, GlobalVar.gsy // 18 * 3, "s", "OggettoDocciaA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 3, "s", "OggettoDocciaB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 6, GlobalVar.gsy // 18 * 2, "s", "OggettoDocciaC", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 2, "d", "OggettoGabinettoA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 3, "d", "OggettoGabinettoB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 4, "d", "OggettoGabinettoC", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 4, "s", "OggettoCaminoA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 4, "s", "OggettoCaminoB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 4, "s", "OggettoCaminoC", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 5, "s", "OggettoCaminoD", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 6, "s", "OggettoCaminoE", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 6, "s", "OggettoCaminoF", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 14, GlobalVar.gsy // 18 * 6, "s", "OggettoCaminoG", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 2, "s", "OggettoScaffaleCucinaA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 2, "s", "OggettoScaffaleCucinaB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 2, "s", "OggettoScaffaleCucinaC", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 7, "d", "OggettoTavolinoFiori", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 6, "d", "OggettoComodinoMamma", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 7, "w", "OggettoLettoGenitoriA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 7, "w", "OggettoLettoGenitoriB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 8, "d", "OggettoLettoGenitoriC", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 24, GlobalVar.gsy // 18 * 9, "s", "OggettoLettoGenitoriD", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 9, "s", "OggettoLettoGenitoriE", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 22, GlobalVar.gsy // 18 * 10, "d", "OggettoComodinoBabbo", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        if stanza == GlobalVar.dictStanze["casaSamSara2"]:
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                percorsoPersonaggio = ["d", "d", "s", "s", "d", "s", "s", "s", "a", "a", "w", "w", "a", "s", "a", "a", "a", "w", "w", "w", "d", "d", "w", "d"]
                personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 4, "d", "CaneCasa", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 1, GlobalVar.gsy // 18 * 3, "d", "OggettoCancellettoCasaA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 30, GlobalVar.gsy // 18 * 3, "a", "OggettoCancellettoCasaB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        if stanza == GlobalVar.dictStanze["casaSamSara3"]:
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 9, "s", "OggettoCancellettoCasaA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 10, "a", "OggettoCanaleCasaA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 11, "a", "OggettoCanaleCasaA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 12, "a", "OggettoCanaleCasaA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 13, "a", "OggettoCanaleCasaA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 14, "a", "OggettoCanaleCasaA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 11, GlobalVar.gsy // 18 * 15, "a", "OggettoCanaleCasaA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 10, "d", "OggettoCanaleCasaB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 11, "d", "OggettoCanaleCasaB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 12, "d", "OggettoCanaleCasaB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 13, "d", "OggettoCanaleCasaB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 14, "d", "OggettoCanaleCasaB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 12, GlobalVar.gsy // 18 * 15, "d", "OggettoCanaleCasaB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        if stanza == GlobalVar.dictStanze["casaSamSara4"]:
            if GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria <= GlobalVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                percorsoPersonaggio = []
                personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 10, "s", "CaneCasa", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
        if stanza == GlobalVar.dictStanze["forestaCadetta5"]:
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                percorsoPersonaggio = ["a"]
                personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 10, "a", "FiglioUfficiale", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                percorsoPersonaggio = []
                personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 7, "s", "OggettoSiepe", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 9, "s", "OggettoFuoco", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 17, GlobalVar.gsy // 18 * 10, "s", "OggettoMucchioLegna", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 18, GlobalVar.gsy // 18 * 9, "s", "OggettoCibo", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        if stanza == GlobalVar.dictStanze["forestaCadetta6"]:
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 9, GlobalVar.gsy // 18 * 4, "s", "OggettoLegna", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 23, GlobalVar.gsy // 18 * 8, "s", "OggettoLegna", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 29, GlobalVar.gsy // 18 * 15, "s", "OggettoLegna", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        if stanza == GlobalVar.dictStanze["forestaCadetta7"]:
            if avanzamentoStoria < GlobalVar.dictAvanzamentoStoria["sotterratoMichael"]:
                percorsoPersonaggio = []
                personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 4, GlobalVar.gsy // 18 * 7, "s", "OggettoPersonaCadavereMichael", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
            else:
                percorsoPersonaggio = []
                personaggio = PersonaggioObj(GlobalVar.gsx // 32 * 2, GlobalVar.gsy // 18 * 7, "d", "OggettoTombaMichael", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
    else:
        for personaggio in listaPersonaggiTotali:
            if personaggio.stanzaDiAppartenenza == stanza:
                listaPersonaggi.append(personaggio)

    if not stanza in stanzeGiaVisitate:
        stanzeGiaVisitate.append(stanza)

    return listaNemici, listaPersonaggi, stanzeGiaVisitate, listaNemiciTotali, listaPersonaggiTotali


def gestisciEventiStoria(avanzamentoStoria, stanza, npers, x, y, cambiosta, carim, caricaTutto, bottoneDown, movimentoPerMouse, impossibileAprirePorta, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiASam, tutteporte, stanzeGiaVisitate, oggettoRicevuto, visualizzaMenuMercante):
    if impossibileAprirePorta:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        caricaTutto = True

    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["inizio"] and stanza == GlobalVar.dictStanze["sognoSara1"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["dialogoSognoSara1"] and stanza == GlobalVar.dictStanze["sognoSara1"]:
        personaggio = PersonaggioObj(x, y, False, "Tutorial", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["aperturaPrimoCofanetto"] and stanza == GlobalVar.dictStanze["sognoSara1"]:
        personaggio = PersonaggioObj(x, y, False, "Tutorial", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["tutorialUtilizzoOggetti"] and stanza == GlobalVar.dictStanze["sognoSara2"]:
        personaggio = PersonaggioObj(x, y, False, "Tutorial", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["tutorialBattaglia"] and stanza == GlobalVar.dictStanze["sognoSara3"]:
        personaggio = PersonaggioObj(x, y, False, "Tutorial", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["tutorialOggettiBattaglia"] and stanza == GlobalVar.dictStanze["sognoSara3"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["dialogoSognoSara2"] and stanza == GlobalVar.dictStanze["sognoSara4"] and x == GlobalVar.gpx * 15 and y == GlobalVar.gpy * 8:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        stanza = GlobalVar.dictStanze["casaSamSara1"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["primoCambioPersonaggio"] and stanza == GlobalVar.dictStanze["casaSamSara1"]:
        pygame.time.wait(1000)
        personaggio = PersonaggioObj(x, y, False, "OggettoLettoSara", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["dialogoCasaSamSara1"] and stanza == GlobalVar.dictStanze["casaSamSara1"] and x == GlobalVar.gpx * 6 and y == GlobalVar.gpy * 8:
        personaggio = PersonaggioObj(x, y, False, "Tutorial", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["dialogoCasaSamSara2"] and stanza == GlobalVar.dictStanze["forestaCadetta1"]:
        personaggio = PersonaggioObj(x, y, False, "Tutorial", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["ingressoForestaCadetta"] and stanza == GlobalVar.dictStanze["forestaCadetta1"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["tutorialCampoVisivo"] and stanza == GlobalVar.dictStanze["forestaCadetta2"]:
        personaggio = PersonaggioObj(x, y, False, "Tutorial", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["tutorialDifesa"] and stanza == GlobalVar.dictStanze["forestaCadetta4"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["quartaStanzaForestaCadetta"] and stanza == GlobalVar.dictStanze["forestaCadetta5"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["legnaReportataMichael"] and stanza == GlobalVar.dictStanze["forestaCadetta5"]:
        avanzamentoStoria += 1
        stanza = GlobalVar.dictStanze["forestaCadetta5"]
        cambiosta = True
        carim = True
        caricaTutto = True
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "FiglioUfficiale":
                personaggio.x = GlobalVar.gpx * 17
                personaggio.y = GlobalVar.gpy * 8
                personaggio.vx = personaggio.x
                personaggio.vy = personaggio.y
                personaggio.girati("s")
                break
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["inizioNotteForestaCadetta"] and stanza == GlobalVar.dictStanze["forestaCadetta5"]:
        pygame.time.wait(1000)
        personaggio = PersonaggioObj(x, y, False, "FiglioUfficiale", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["fineUltimoDialogoSam"] and stanza == GlobalVar.dictStanze["forestaCadetta5"]:
        percorsoNemico = ["w", "w"]
        nemico = NemicoObj(GlobalVar.gsx // 32 * 16, GlobalVar.gsy // 18 * 12, "w", "Cinghiale", stanza, percorsoNemico)
        nemico.mosseRimaste = 3
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = []
        nemico = NemicoObj(GlobalVar.gsx // 32 * 15, GlobalVar.gsy // 18 * 14, "w", "Cinghiale", stanza, percorsoNemico)
        nemico.mosseRimaste = -3
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        npers = 4
        personaggio = PersonaggioObj(x, y, False, "OggettoCinghiale", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["attaccoCinghiale"] and stanza == GlobalVar.dictStanze["forestaCadetta5"]:
        nemicoArrivato = False
        for nemico in listaNemici:
            if nemico.tipo == "Cinghiale" and nemico.mosseRimaste == 0:
                nemicoArrivato = True
                break
        if nemicoArrivato:
            GlobalVar.disegnaColoreSuTuttoLoSchermo(GlobalVar.nero)
            GlobalVar.canaleSoundCanzone.stop()
            GlobalVar.canaleSoundSottofondoAmbientale.stop()
            GlobalVar.aggiornaSchermo()
            i = 0
            while i < len(tutteporte):
                if tutteporte[i] == GlobalVar.dictStanze["casaSamSara1"] and tutteporte[i + 1] == GlobalVar.gpx * 6 and tutteporte[i + 2] == GlobalVar.gpx * 9:
                    tutteporte[i + 3] = False
                    break
                i += 4
            # 0-9 => oggetti / 10 => frecce / 11 => guanti / 12 => monete
            oggettiRimastiASam = [dati[31], dati[32], dati[33], dati[34], dati[35], dati[36], dati[37], dati[38], dati[39], dati[40], dati[132], dati[62], dati[131]]
            dati[31] = 2
            if dati[32] > 0:
                dati[32] = 0
            if dati[33] > 0:
                dati[33] = 0
            if dati[34] > 0:
                dati[34] = 0
            if dati[35] > 0:
                dati[35] = 0
            if dati[36] > 0:
                dati[36] = 0
            if dati[37] > 0:
                dati[37] = 0
            if dati[38] > 0:
                dati[38] = 0
            if dati[39] > 0:
                dati[39] = 0
            if dati[40] > 0:
                dati[40] = 0
            dati[132] = 0
            dati[62] = 0
            dati[131] = 0
            # tolgo gli eventuali guanti equipaggiati
            dati[129] = 0
            pygame.time.wait(1000)
            avanzamentoStoria += 1
            stanza = GlobalVar.dictStanze["casaSamSara1"]
            cambiosta = True
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and stanza == GlobalVar.dictStanze["casaSamSara1"]:
        pygame.time.wait(1000)
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["trovatoMappaDiario"] and stanza == GlobalVar.dictStanze["casaSamSara1"]:
        personaggio = PersonaggioObj(x, y, False, "Tutorial", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["tutorialMappaDiario"] and stanza == GlobalVar.dictStanze["casaSamSara1"] and x == GlobalVar.gpx * 6 and y == GlobalVar.gpy * 8:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["armaturaNonno4"] and stanza == GlobalVar.dictStanze["casaSamSara1"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["armaturaNonnoCompletata"] and stanza == GlobalVar.dictStanze["forestaCadetta1"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["ingressoForestaCadettaSara"] and stanza == GlobalVar.dictStanze["forestaCadetta5"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["accampamentoForestaAnalizzato"] and stanza == GlobalVar.dictStanze["forestaCadetta7"] and x == GlobalVar.gpx * 13 and y == GlobalVar.gpy * 6:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["incontratoBrancoLupiNeri"] and stanza == GlobalVar.dictStanze["forestaCadetta7"] and x == GlobalVar.gpx * 13 and y == GlobalVar.gpy * 10:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["incontratoCinghiale"] and stanza == GlobalVar.dictStanze["forestaCadetta7"]:
        campoRipulito = True
        for nemico in listaNemici:
            if nemico.vita > 0 and nemico.inCasellaVista:
                campoRipulito = False
                break
        if campoRipulito:
            avanzamentoStoria += 1
            caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["cinghialeUcciso"] and stanza == GlobalVar.dictStanze["forestaCadetta7"]:
        campoRipulito = True
        for nemico in listaNemici:
            if nemico.vita > 0 and nemico.inCasellaVista:
                campoRipulito = False
                break
        if not campoRipulito:
            avanzamentoStoria -= 1
            caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["cadavereMichaelDepredato"] and stanza == GlobalVar.dictStanze["forestaCadetta7"]:
        # oggettiRimastiASam: 0-9 => oggetti / 10 => frecce / 11 => guanti / 12 => monete
        dati[31] += oggettiRimastiASam[0]
        dati[32] += oggettiRimastiASam[1]
        dati[33] += oggettiRimastiASam[2]
        dati[34] += oggettiRimastiASam[3]
        dati[35] += oggettiRimastiASam[4]
        dati[36] += oggettiRimastiASam[5]
        dati[37] += oggettiRimastiASam[6]
        dati[38] += oggettiRimastiASam[7]
        dati[39] += oggettiRimastiASam[8]
        dati[40] += oggettiRimastiASam[9]
        dati[132] += oggettiRimastiASam[10]
        if dati[132] > 1:
            dati[132] = 1
        if dati[62] <= 0:
            dati[62] = oggettiRimastiASam[11]
        dati[131] += oggettiRimastiASam[12]
        # il soldato ti lascia la sua spada/armatura/scudo
        dati[43] = 1
        dati[53] = 1
        dati[58] = 1
        avanzamentoStoria += 1
        i = 0
        while i < len(stanzeGiaVisitate):
            if stanzeGiaVisitate[i] == stanza:
                del stanzeGiaVisitate[i]
            i += 1
        i = 0
        while i < len(listaPersonaggiTotali):
            if listaPersonaggiTotali[i].stanzaDiAppartenenza == GlobalVar.dictStanze["forestaCadetta7"]:
                del listaPersonaggiTotali[i]
            else:
                i += 1
        i = 0
        while i < len(listaNemiciTotali):
            if listaNemiciTotali[i].stanzaDiAppartenenza == GlobalVar.dictStanze["forestaCadetta7"]:
                del listaNemiciTotali[i]
            else:
                i += 1
        stanza = GlobalVar.dictStanze["forestaCadetta7"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["sotterratoMichael"] and stanza == GlobalVar.dictStanze["forestaCadetta7"]:
        pygame.time.wait(1000)
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        caricaTutto = True
    elif avanzamentoStoria == GlobalVar.dictAvanzamentoStoria["monologoDopoTombaMichael"] and stanza == GlobalVar.dictStanze["forestaCadetta8"]:
        personaggio = PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante = dialoga(avanzamentoStoria, personaggio)
        caricaTutto = True

    if caricaTutto:
        bottoneDown = False
    return avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiASam, tutteporte, oggettoRicevuto, visualizzaMenuMercante
