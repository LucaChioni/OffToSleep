# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import GlobalSndVar
import GlobalGameVar
import GenericFunc
import NemicoObj
import PersonaggioObj


def caricaNemiciEPersonaggi(avanzamentoStoria, stanza, stanzaVecchia, stanzeGiaVisitate, listaNemiciTotali, listaPersonaggiTotali, listaAvanzamentoDialoghi, listaPersonaggi):
    if stanzaVecchia != 0 and ((stanza in GlobalGameVar.vetStanzePacifiche and stanzaVecchia not in GlobalGameVar.vetStanzePacifiche) or (stanza not in GlobalGameVar.vetStanzePacifiche and stanzaVecchia in GlobalGameVar.vetStanzePacifiche)):
        listaNemiciTotali = []
        listaPersonaggiTotali = []
        stanzeGiaVisitate = []

    listaNemici = []
    if not stanza in stanzeGiaVisitate:
        if stanza == GlobalGameVar.dictStanze["sognoLucy2"]:
            percorsoNemico = ["s", "d", "d", "w", "w", "w", "a", "a", "s", "s"]
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 7, "s", "Orco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["s", "s", "w", "w"]
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 2, "s", "Orco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["d", "d", "d", "d", "a", "a", "a", "a"]
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 4, "d", "Orco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
        if stanza == GlobalGameVar.dictStanze["sognoLucy3"]:
            percorsoNemico = ["a", "a", "a", "w", "w", "w", "d", "d", "d", "s", "s", "s"]
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 8, "s", "Pipistrello", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["d", "d", "s", "s", "s", "d", "a", "a", "a", "s", "a", "w", "w", "w", "w", "d"]
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 5, "d", "Pipistrello", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = ["w", "a", "s", "a", "d", "d"]
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 10, "w", "Orco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
        if stanza == GlobalGameVar.dictStanze["forestaCadetta1"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] or avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                percorsoNemico = ["s", "s", "a", "a", "a", "w", "w", "w", "d", "d", "d", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 6, "s", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "a", "s", "s", "d", "d", "w", "d", "d", "w", "w", "a", "a", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 4, "s", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "a", "s", "s", "d", "d", "d", "w", "w", "a"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 12, "a", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "s", "w", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 11, "w", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "s", "a", "a", "a", "a", "w", "d", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 9, "d", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "s", "s", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4, "w", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
            else:
                percorsoNemico = ["s", "s", "a", "a", "a", "w", "w", "w", "d", "d", "d", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 6, "s", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "s", "d", "d", "d", "d", "w", "w", "w", "w", "a", "a", "s", "s", "a", "a"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 4, "a", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "a", "s", "s", "d", "d", "w", "d", "d", "w", "w", "a", "a", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 4, "s", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "d", "d", "s", "s", "a", "a", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 10, "w", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "a", "s", "s", "d", "d", "d", "w", "w", "a"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 12, "a", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "s", "w", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 11, "w", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "w", "s", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 13, "s", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "a", "a", "a", "a", "d", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 12, "d", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "s", "s", "d", "d", "d", "w", "w", "a", "w", "w", "a", "s", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 13, "s", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "s", "a", "a", "a", "a", "w", "d", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 9, "d", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "w", "w", "a", "a", "a", "s", "s", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 5, "d", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "s", "s", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4, "w", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
        if stanza == GlobalGameVar.dictStanze["forestaCadetta2"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] or avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                percorsoNemico = ["w", "s", "s", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 14, "w", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "a", "a", "a", "w", "w", "d", "d", "s", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 14, "d", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "w", "w", "w", "a", "s", "s", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 6, "s", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "w", "d", "d", "s", "s", "a", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 3, "w", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "d", "d", "w", "w", "a", "a", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 3, "s", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "d", "s", "s", "a", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 8, "w", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
            else:
                percorsoNemico = ["a", "w", "d", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 12, "s", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "s", "s", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 14, "w", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "w", "a", "a", "s", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 15, "d", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "w", "w", "d", "s", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 13, "s", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "a", "a", "a", "w", "w", "d", "d", "s", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 14, "d", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "w", "w", "a", "a", "s", "s", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 7, "d", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "w", "w", "w", "a", "s", "s", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 28, GlobalHWVar.gsy // 18 * 6, "s", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "w", "d", "d", "s", "s", "s", "s", "w", "w", "a", "a"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 4, "a", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "w", "d", "d", "s", "s", "a", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 3, "w", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "w", "d", "s", "s", "s", "a", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 5, "w", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "a", "a", "a", "d", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 7, "d", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "d", "d", "w", "w", "a", "a", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 3, "s", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "d", "d", "d", "a", "a"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 10, "a", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "d", "s", "s", "a", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 8, "w", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "d", "w", "w", "a", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 12, "s", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
        if stanza == GlobalGameVar.dictStanze["forestaCadetta3"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] or avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                percorsoNemico = ["a", "w", "w", "d", "s", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 7, "s", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "w", "w", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 5, "s", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "w", "w", "w", "a", "a", "a", "s", "s", "s", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 6, "d", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "a", "a", "a", "w", "w", "d", "d", "d", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 12, "s", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "w", "w", "w", "a", "a", "s", "s", "s", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 13, "d", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
            else:
                percorsoNemico = ["a", "w", "w", "d", "d", "s", "s", "a"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 6, "a", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "w", "s", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 5, "d", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "w", "w", "d", "s", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 7, "s", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "a", "d", "d", "d", "d", "a", "a"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 7, "a", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "d", "w", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 7, "s", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "w", "w", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 5, "s", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "w", "a", "a", "a", "s", "s", "s", "w", "w", "w", "d", "d", "d", "s", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 4, "s", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "w", "w", "w", "a", "a", "a", "s", "s", "s", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 6, "d", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "a", "d", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 11, "d", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "w", "d", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11, "s", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "a", "a", "a", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 13, "d", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "a", "a", "a", "w", "w", "d", "d", "d", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 12, "s", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "d", "a", "a", "a", "a", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 14, "d", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "a", "a"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 14, "a", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "a", "w", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 11, "d", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "w", "w", "w", "a", "a", "s", "s", "s", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 13, "d", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
        if stanza == GlobalGameVar.dictStanze["forestaCadetta4"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] or avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                percorsoNemico = ["d", "w", "w", "d", "d", "s", "s", "s", "s", "a", "a", "a", "w", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 6, "w", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "a", "a", "a", "w", "w", "d", "w", "d", "d", "s", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 4, "s", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "a", "a", "s", "s", "d", "d", "w", "d", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 3, "w", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "d", "w", "w", "w", "w", "a", "a", "a", "a", "a", "a", "a", "s", "s", "s", "s", "s", "d", "d", "d", "d", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 12, "w", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
            else:
                percorsoNemico = ["d", "w", "w", "d", "d", "s", "s", "s", "s", "a", "a", "a", "w", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 6, "w", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "a", "a", "a", "d", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 6, "d", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 4, "s", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "a", "a", "a", "w", "w", "d", "w", "d", "d", "s", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 4, "s", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "d", "w", "w", "w", "a", "a", "a", "s", "a", "s", "s", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 5, "d", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "a", "a", "s", "s", "d", "d", "w", "d", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 3, "w", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "d", "d", "d", "s", "s", "a", "a", "w", "a"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 7, "a", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "a", "a"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 11, "a", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "s", "s", "w", "w", "a"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 9, "a", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "d", "w", "w", "w", "w", "a", "a", "a", "a", "a", "a", "a", "s", "s", "s", "s", "s", "d", "d", "d", "d", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 12, "w", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "w", "d", "w", "s", "a", "s", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 11, "d", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
        if stanza == GlobalGameVar.dictStanze["forestaCadetta6"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] or avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                percorsoNemico = ["d", "d", "d", "d", "s", "s", "a", "a", "s", "a", "a", "a", "a", "a", "w", "w", "w", "d", "d", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 7, "d", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "s", "a", "s", "s", "d", "d", "d", "s", "d", "d", "d", "w", "w", "w", "a", "a", "w", "a", "a"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 11, "a", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "w", "w", "d", "d", "d", "d", "s", "s", "a", "s", "s", "a", "a", "w", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 4, "w", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "s", "s", "a", "a", "a", "w", "w", "w", "w", "s", "s", "s", "s", "d", "d", "d", "w", "w", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 12, "w", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "s", "d", "d", "w", "w", "w", "a", "a", "a", "a", "s", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 4, "s", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "s", "d", "d", "w", "d", "w", "w", "w", "a", "a", "a", "s", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 13, "s", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
            else:
                percorsoNemico = ["a", "a", "w", "w", "w", "d", "d", "d", "d", "d", "d", "d", "s", "s", "a", "a", "s", "a", "a", "a"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 10, "a", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "d", "d", "s", "s", "a", "a", "s", "a", "a", "a", "a", "a", "w", "w", "w", "d", "d", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 7, "d", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "s", "a", "s", "s", "d", "d", "d", "s", "d", "d", "d", "w", "w", "w", "a", "a", "w", "a", "a"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 11, "a", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "s", "s", "d", "d", "d", "w", "w", "w", "a", "w", "a", "a", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 9, "s", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "w", "w", "d", "d", "d", "d", "s", "s", "a", "s", "s", "a", "a", "w", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 4, "w", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "d", "d", "d", "d", "w", "w", "a", "a", "a", "a", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 6, "s", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "s", "s", "a", "a", "a", "w", "w", "w", "w", "s", "s", "s", "s", "d", "d", "d", "w", "w", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 12, "w", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "s", "d", "d", "w", "w", "w", "a", "a", "a", "a", "s", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 4, "s", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "s", "a", "a", "s", "d", "d", "w", "w", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 10, "w", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "s", "d", "d", "w", "d", "w", "w", "w", "a", "a", "a", "s", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 13, "s", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "d", "d", "s", "s", "a", "a", "a", "s", "w", "w", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 6, "d", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
        if stanza == GlobalGameVar.dictStanze["forestaCadetta7"] and not stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta7"]:
            if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                percorsoNemico = ["a", "a", "a", "a", "s", "s", "s", "d", "d", "s", "s", "s", "d", "d", "d", "d", "w", "w", "w", "w", "w", "w", "a", "a"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 8, "a", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "d", "d", "w", "w", "w", "w", "w", "w", "a", "a", "a", "a", "a", "a", "s", "s", "s", "d", "d", "s", "s", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 14, "s", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "a", "a", "a", "a", "w", "a", "a", "s", "s", "d", "d", "d", "d", "w", "w", "d", "w", "d", "d", "s", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 14, "s", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "s", "a", "a", "a", "", "w", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 6, "d", "Cinghiale", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
            else:
                percorsoNemico = ["w", "d", "d", "s", "s", "a", "a", "a", "a", "a", "w", "d", "d", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 7, "d", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "a", "a", "a", "s", "s", "s", "d", "d", "s", "s", "s", "d", "d", "d", "d", "w", "w", "w", "w", "w", "w", "a", "a"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 8, "a", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "d", "d", "w", "w", "w", "w", "w", "w", "a", "a", "a", "a", "a", "a", "s", "s", "s", "d", "d", "s", "s", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 25, GlobalHWVar.gsy // 18 * 14, "s", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "a", "w", "w", "d", "s", "d", "s", "s", "a"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 27, GlobalHWVar.gsy // 18 * 13, "a", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "s", "s", "d", "d", "d", "w", "d", "d", "w", "w", "a", "a", "s", "a", "a"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 10, "a", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "a", "a", "a", "a", "w", "a", "a", "s", "s", "d", "d", "d", "d", "w", "w", "d", "w", "d", "d", "s", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 14, "s", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "s", "s", "a", "a", "s", "a", "w", "w", "w", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 9, "d", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "a", "a", "a", "a", "w", "w", "d", "d", "d", "d", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 4, "s", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "s", "a", "a", "a", "", "w", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 6, "d", "Cinghiale", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
        if stanza == GlobalGameVar.dictStanze["forestaCadetta8"]:
            if avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                percorsoNemico = ["d", "d", "d", "s", "s", "s", "a", "a", "w", "w", "d", "w", "w", "a", "a", "a", "a", "a", "w", "w", "d", "d", "d", "s", "s", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 5, "s", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "d", "d", "d", "s", "a", "a", "a", "a", "a", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 10, "w", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "a", "s", "s", "d", "d", "d", "w", "w", "w", "w", "a", "a", "s", "d", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13, "s", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "s", "a", "a", "s", "a", "w", "w", "w", "a", "w", "d", "d", "d", "d", "d", "s", "a"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 3, "a", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "a", "a", "s", "a", "a", "d", "d", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 8, "w", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "a", "s", "s", "w", "w", "a", "w", "w", "d", "d", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 3, "s", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "w", "d", "w", "w", "w", "a", "a", "a", "w", "a", "a", "s", "s", "s", "s", "s", "d", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 15, "d", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
            else:
                percorsoNemico = ["a", "w", "w", "w", "a", "a", "s", "s", "d", "d", "d", "w", "d", "d", "s", "d", "s", "s", "a", "a", "a", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 7, "w", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "d", "s", "s", "s", "a", "a", "w", "w", "d", "w", "w", "a", "a", "a", "a", "a", "w", "w", "d", "d", "d", "s", "s", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 26, GlobalHWVar.gsy // 18 * 5, "s", "LupoNero", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "d", "d", "d", "s", "a", "a", "a", "a", "a", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 10, "w", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "s", "s", "s", "a", "a", "a", "w", "w", "w", "d", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 12, "d", "LupoBianco", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "a", "s", "s", "d", "d", "d", "w", "w", "w", "w", "a", "a", "s", "d", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13, "s", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "s", "a", "s", "s", "a", "w", "w", "w", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 7, "d", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "s", "a", "a", "s", "a", "w", "w", "w", "a", "w", "d", "d", "d", "d", "d", "s", "a"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 3, "a", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["w", "a", "a", "a", "s", "s", "a", "s", "s", "d", "d", "w", "w", "d", "d", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 5, "w", "LupoGrigio", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "a", "a", "s", "a", "a", "d", "d", "w"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 8, "w", "TartarugaMarrone", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "a", "s", "s", "w", "w", "a", "w", "w", "d", "d", "s"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 3, "s", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["s", "s", "a", "a", "w", "d", "w", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 12, "d", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["d", "d", "w", "d", "w", "w", "w", "a", "a", "a", "w", "a", "a", "s", "s", "s", "s", "s", "d", "d"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 15, "d", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
                percorsoNemico = ["a", "s", "s", "d", "d", "d", "d", "w", "a", "w", "a", "a"]
                nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 13, "a", "TartarugaVerde", stanza, percorsoNemico)
                listaNemiciTotali.append(nemico)
                listaNemici.append(nemico)
    else:
        for nemico in listaNemiciTotali:
            if nemico.stanzaDiAppartenenza == stanza:
                listaNemici.append(nemico)

    # aggiorno il vettore listaAvanzamentoDialoghi per i personaggi della stanza precedente
    for personaggio in listaPersonaggi:
        personaggioPresente = False
        i = 0
        while i < len(listaAvanzamentoDialoghi):
            if personaggio.tipo == listaAvanzamentoDialoghi[i]:
                personaggio.avanzamentoDialogo = listaAvanzamentoDialoghi[i + 1]
                personaggioPresente = True
                break
            i += 2
        if not personaggioPresente:
            listaAvanzamentoDialoghi.append(personaggio.tipo)
            listaAvanzamentoDialoghi.append(personaggio.avanzamentoDialogo)

    listaPersonaggi = []
    if not stanza in stanzeGiaVisitate:
        if stanza == GlobalGameVar.dictStanze["casaHansLucy1"]:
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 13, "a", "OggettoLettoLucy", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 3, "d", "OggettoLavandinoCucina", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 2, "s", "OggettoLavandinoBagno", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 5, "a", "OggettoScaffaleBicchieriA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 6, "a", "OggettoScaffaleBicchieriB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 7, "a", "OggettoScaffaleBicchieriC", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 14, "w", "OggettoComodinoLucy", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 15, "w", "OggettoFinestraA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 15, "w", "OggettoFinestraB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 12, "d", "OggettoLettoHans", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 13, "d", "OggettoComodinoHans", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 2, "s", "OggettoVascaA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 6, GlobalHWVar.gsy // 18 * 2, "s", "OggettoVascaB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 2, "d", "OggettoGabinettoA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 3, "d", "OggettoGabinettoB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 4, "d", "OggettoGabinettoC", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 4, "s", "OggettoCaminoA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 4, "s", "OggettoCaminoB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 4, "s", "OggettoCaminoC", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 5, "s", "OggettoCaminoD", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 6, "s", "OggettoCaminoE", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 6, "s", "OggettoCaminoF", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 14, GlobalHWVar.gsy // 18 * 6, "s", "OggettoCaminoG", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 2, "s", "OggettoScaffaleCucinaA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 2, "s", "OggettoScaffaleCucinaB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, "s", "OggettoScaffaleCucinaC", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, "d", "OggettoTavolinoFiori", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 6, "d", "OggettoComodinoMamma", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 7, "w", "OggettoLettoGenitoriA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 7, "w", "OggettoLettoGenitoriB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 8, "d", "OggettoLettoGenitoriC", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 24, GlobalHWVar.gsy // 18 * 9, "s", "OggettoLettoGenitoriD", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 9, "s", "OggettoLettoGenitoriE", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 10, "d", "OggettoComodinoBabbo", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        if stanza == GlobalGameVar.dictStanze["casaHansLucy2"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                percorsoPersonaggio = ["d", "d", "s", "s", "d", "s", "s", "s", "a", "a", "w", "w", "a", "s", "a", "a", "a", "w", "w", "w", "d", "d", "w", "d"]
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 7, "d", "CaneCasa", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 6, "d", "OggettoCancellettoCasaA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 30, GlobalHWVar.gsy // 18 * 6, "a", "OggettoCancellettoCasaB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        if stanza == GlobalGameVar.dictStanze["casaHansLucy3"]:
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 9, "s", "OggettoCancellettoCasaA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 10, "a", "OggettoCanaleCasaA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 11, "a", "OggettoCanaleCasaA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 12, "a", "OggettoCanaleCasaA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 13, "a", "OggettoCanaleCasaA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 14, "a", "OggettoCanaleCasaA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 15, "a", "OggettoCanaleCasaA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 10, "d", "OggettoCanaleCasaB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 11, "d", "OggettoCanaleCasaB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 12, "d", "OggettoCanaleCasaB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 13, "d", "OggettoCanaleCasaB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 14, "d", "OggettoCanaleCasaB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 15, "d", "OggettoCanaleCasaB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        if stanza == GlobalGameVar.dictStanze["casaHansLucy4"]:
            if GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 10, "s", "CaneCasa", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
        if stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
                percorsoPersonaggio = ["a"]
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 10, "a", "FiglioUfficiale", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
            else:
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 7, "s", "OggettoSiepe", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 9, "s", "OggettoFuoco", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 17, GlobalHWVar.gsy // 18 * 10, "s", "OggettoMucchioLegna", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 9, "s", "OggettoCibo", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        if stanza == GlobalGameVar.dictStanze["forestaCadetta6"]:
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 9, GlobalHWVar.gsy // 18 * 4, "s", "OggettoLegnaA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 8, "s", "OggettoLegnaB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 15, "s", "OggettoLegnaC", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        if stanza == GlobalGameVar.dictStanze["forestaCadetta7"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sotterratoSam"]:
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 7, "s", "OggettoPersonaCadavereSam", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
            else:
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 7, "d", "OggettoTombaSam", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
        if stanza == GlobalGameVar.dictStanze["stradaPerCittà1"]:
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 11, "a", "GuardiaCitta", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 10, GlobalHWVar.gsy // 18 * 2, "s", "OggettoCartelloForestaA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 2, "s", "OggettoCartelloForestaB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 7, "a", "OggettoCartelloStaccionataA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 8, "a", "OggettoCartelloStaccionataB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 10, "a", "OggettoCartelloBloccoStrada", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 13, "a", "OggettoCartelloStaccionataA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 29, GlobalHWVar.gsy // 18 * 14, "a", "OggettoCartelloStaccionataB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        if stanza == GlobalGameVar.dictStanze["stradaPerCittà3"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["apertoPortaCittà"]:
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 8, "d", "OggettoBucoPortaA", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 1, GlobalHWVar.gsy // 18 * 9, "d", "OggettoBucoPortaB", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["apertoPortaCittà"]:
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 2, GlobalHWVar.gsy // 18 * 8, "d", "PadreUfficialeServizio", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
        if stanza == GlobalGameVar.dictStanze["casaDavid1"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["primoDialogoConDavid"]:
                percorsoPersonaggio = ["w", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "w", "w"]
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 14, "w", "PadreUfficialeServizio", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["d", "d", "d", "w", "", "s", "a", "a", "a", "a", "w", "", "s", "d"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 4, "d", "ServoDavid", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        if stanza == GlobalGameVar.dictStanze["casaDavid2"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"]:
                percorsoPersonaggio = ["a"]
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 4, "a", "PadreUfficialeServizio", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 7, "w", "MadreUfficiale", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                percorsoPersonaggio = ["d"]
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 4, "d", "ServoDavid", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
            elif GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cenaConDavidIniziata"]:
                percorsoPersonaggio = ["d"]
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 7, "d", "PadreUfficialeCasa", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                percorsoPersonaggio = ["a"]
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 7, "a", "MadreUfficiale", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 2, "s", "ServoDavid", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
            elif GlobalGameVar.dictAvanzamentoStoria["cenaConDavidIniziata"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineDialogoCenaDavid"]:
                percorsoPersonaggio = ["a"]
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 8, GlobalHWVar.gsy // 18 * 8, "d", "PadreUfficialeCasa", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 8, "a", "MadreUfficiale", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
                percorsoPersonaggio = []
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 2, "s", "ServoDavid", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
            else:
                percorsoPersonaggio = ["w", "d", "w", "d", "", "a", "s", "a", "s", "a", "a", "", "d", "d", "s", "d", "s", "d", "", "a", "w", "a", "w"]
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 9, "w", "ServoDavid", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
        if stanza == GlobalGameVar.dictStanze["casaDavid3"]:
            if GlobalGameVar.dictAvanzamentoStoria["andatoADormireCasaDavid"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineDialogoSaraNotturno"]:
                percorsoPersonaggio = ["w"]
                personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 9, "w", "MadreUfficiale", stanza, avanzamentoStoria, percorsoPersonaggio)
                listaPersonaggi.append(personaggio)
                listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 3, "s", "OggettoLettoCasaDavidA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 4, "s", "OggettoLettoCasaDavidB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 11, GlobalHWVar.gsy // 18 * 5, "s", "OggettoLettoCasaDavidC", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 5, "s", "OggettoLettoCasaDavidD", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 5, "s", "OggettoLettoCasaDavidE", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 4, "s", "OggettoLettoCasaDavidF", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 3, "s", "OggettoArmadioCasaDavidA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 4, "s", "OggettoArmadioCasaDavidB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 5, "s", "OggettoArmadioCasaDavidC", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 7, GlobalHWVar.gsy // 18 * 6, "s", "OggettoArmadioCasaDavidD", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 4, GlobalHWVar.gsy // 18 * 11, "s", "OggettoVascaCasaDavidA", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 5, GlobalHWVar.gsy // 18 * 11, "s", "OggettoVascaCasaDavidB", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
    else:
        for personaggio in listaPersonaggiTotali:
            if personaggio.stanzaDiAppartenenza == stanza:
                listaPersonaggi.append(personaggio)

    # aggiorno il vettore listaAvanzamentoDialoghi per i personaggi della stanza attuale
    for personaggio in listaPersonaggi:
        personaggioPresente = False
        i = 0
        while i < len(listaAvanzamentoDialoghi):
            if personaggio.tipo == listaAvanzamentoDialoghi[i]:
                personaggio.avanzamentoDialogo = listaAvanzamentoDialoghi[i + 1]
                personaggioPresente = True
                break
            i += 2
        if not personaggioPresente:
            listaAvanzamentoDialoghi.append(personaggio.tipo)
            listaAvanzamentoDialoghi.append(personaggio.avanzamentoDialogo)

    if not stanza in stanzeGiaVisitate:
        stanzeGiaVisitate.append(stanza)

    return listaNemici, listaPersonaggi, stanzeGiaVisitate, listaNemiciTotali, listaPersonaggiTotali, listaAvanzamentoDialoghi


def gestisciEventiStoria(avanzamentoStoria, stanza, npers, x, y, cambiosta, carim, caricaTutto, bottoneDown, movimentoPerMouse, impossibileAprirePorta, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, stanzeGiaVisitate, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip, canzone):
    if impossibileAprirePorta:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True

    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizio"] and stanza == GlobalGameVar.dictStanze["sognoLucy1"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoSognoLucy1"] and stanza == GlobalGameVar.dictStanze["sognoLucy1"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Tutorial", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["aperturaPrimoCofanetto"] and stanza == GlobalGameVar.dictStanze["sognoLucy1"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Tutorial", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialUtilizzoOggetti"] and stanza == GlobalGameVar.dictStanze["sognoLucy2"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Tutorial", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialBattaglia"] and stanza == GlobalGameVar.dictStanze["sognoLucy3"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Tutorial", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialOggettiBattaglia"] and stanza == GlobalGameVar.dictStanze["sognoLucy3"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoSognoLucy2"] and stanza == GlobalGameVar.dictStanze["sognoLucy4"] and x == GlobalHWVar.gpx * 15 and y == GlobalHWVar.gpy * 8:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        stanza = GlobalGameVar.dictStanze["casaHansLucy1"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"] and stanza == GlobalGameVar.dictStanze["casaHansLucy1"]:
        screen = GlobalHWVar.schermo.copy().convert()

        pygame.time.wait(1000)
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoLettoLucy", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)

        GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        GlobalHWVar.aggiornaSchermo()
        GlobalHWVar.canaleSoundCanzone.set_volume(0)
        GlobalHWVar.canaleSoundCanzone.play(canzone, -1)
        i = 0
        while i < GlobalHWVar.volumeCanzoni:
            GlobalHWVar.canaleSoundCanzone.set_volume(i)
            i += GlobalHWVar.volumeCanzoni / 10
            pygame.time.wait(30)
        GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoCasaHansLucy1"] and stanza == GlobalGameVar.dictStanze["casaHansLucy1"] and x == GlobalHWVar.gpx * 6 and y == GlobalHWVar.gpy * 8:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Tutorial", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoCasaHansLucy2"] and stanza == GlobalGameVar.dictStanze["forestaCadetta1"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Tutorial", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ingressoForestaCadetta"] and stanza == GlobalGameVar.dictStanze["forestaCadetta1"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialCampoVisivo"] and stanza == GlobalGameVar.dictStanze["forestaCadetta2"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Tutorial", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialDifesa"] and stanza == GlobalGameVar.dictStanze["forestaCadetta4"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["quartaStanzaForestaCadetta"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["legnaReportataSam"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["forestaCadetta5"]
        cambiosta = True
        carim = True
        caricaTutto = True
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "FiglioUfficiale":
                personaggio.x = GlobalHWVar.gpx * 17
                personaggio.y = GlobalHWVar.gpy * 8
                personaggio.vx = personaggio.x
                personaggio.vy = personaggio.y
                personaggio.girati("s")
                break
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioUltimoDialogoHans"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        pygame.time.wait(1000)
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "FiglioUfficiale", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["fineUltimoDialogoHans"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        percorsoNemico = ["w", "w"]
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 12, "w", "Cinghiale", stanza, percorsoNemico)
        nemico.mosseRimaste = 3
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        percorsoNemico = []
        nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 15, GlobalHWVar.gsy // 18 * 14, "w", "Cinghiale", stanza, percorsoNemico)
        nemico.mosseRimaste = -3
        listaNemiciTotali.append(nemico)
        listaNemici.append(nemico)
        npers = 4
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "OggettoCinghiale", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["attaccoCinghiale"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        nemicoArrivato = False
        for nemico in listaNemici:
            if nemico.tipo == "Cinghiale" and nemico.mosseRimaste == 0:
                nemicoArrivato = True
                break
        if nemicoArrivato:
            GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.nero)
            GlobalHWVar.canaleSoundCanzone.stop()
            GlobalHWVar.canaleSoundSottofondoAmbientale.stop()
            GlobalHWVar.aggiornaSchermo()
            i = 0
            while i < len(tutteporte):
                if tutteporte[i] == GlobalGameVar.dictStanze["casaHansLucy1"] and tutteporte[i + 1] == GlobalHWVar.gpx * 6 and tutteporte[i + 2] == GlobalHWVar.gpx * 9:
                    tutteporte[i + 3] = False
                    break
                i += 4
            # 0-9 => oggetti / 10 => frecce / 11 => guanti / 12 => monete
            oggettiRimastiAHans = [dati[31], dati[32], dati[33], dati[34], dati[35], dati[36], dati[37], dati[38], dati[39], dati[40], dati[132], dati[62], dati[131]]
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
            stanza = GlobalGameVar.dictStanze["casaHansLucy1"]
            cambiosta = True
            carim = True
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and stanza == GlobalGameVar.dictStanze["casaHansLucy1"]:
        pygame.time.wait(1000)
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["trovatoMappaDiario"] and stanza == GlobalGameVar.dictStanze["casaHansLucy1"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Tutorial", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialMappaDiario"] and stanza == GlobalGameVar.dictStanze["casaHansLucy1"] and x == GlobalHWVar.gpx * 6 and y == GlobalHWVar.gpy * 8:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["armaturaNonno4"] and stanza == GlobalGameVar.dictStanze["casaHansLucy1"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["armaturaNonnoCompletata"] and stanza == GlobalGameVar.dictStanze["forestaCadetta1"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ingressoForestaCadettaLucy"] and stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["accampamentoForestaAnalizzato2"] and stanza == GlobalGameVar.dictStanze["forestaCadetta7"] and x == GlobalHWVar.gpx * 13 and y == GlobalHWVar.gpy * 6:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["incontratoBrancoLupiNeri"] and stanza == GlobalGameVar.dictStanze["forestaCadetta7"] and x == GlobalHWVar.gpx * 13 and y == GlobalHWVar.gpy * 10:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["incontratoCinghiale"] and stanza == GlobalGameVar.dictStanze["forestaCadetta7"]:
        campoRipulito = True
        for nemico in listaNemici:
            if nemico.vita > 0 and nemico.inCasellaVista:
                campoRipulito = False
                break
        if campoRipulito:
            avanzamentoStoria += 1
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["cinghialeUcciso"] and stanza == GlobalGameVar.dictStanze["forestaCadetta7"]:
        campoRipulito = True
        for nemico in listaNemici:
            if nemico.vita > 0 and nemico.inCasellaVista:
                campoRipulito = False
                break
        if not campoRipulito:
            avanzamentoStoria -= 1
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["cadavereSamDepredato"] and stanza == GlobalGameVar.dictStanze["forestaCadetta7"]:
        # oggettiRimastiAHans: 0-9 => oggetti / 10 => frecce / 11 => guanti / 12 => monete
        if oggettiRimastiAHans[0] > 0:
            dati[31] += oggettiRimastiAHans[0]
        if oggettiRimastiAHans[1] > 0:
            dati[32] += oggettiRimastiAHans[1]
        if oggettiRimastiAHans[2] > 0:
            dati[33] += oggettiRimastiAHans[2]
        if oggettiRimastiAHans[3] > 0:
            dati[34] += oggettiRimastiAHans[3]
        if oggettiRimastiAHans[4] > 0:
            dati[35] += oggettiRimastiAHans[4]
        if oggettiRimastiAHans[5] > 0:
            dati[36] += oggettiRimastiAHans[5]
        if oggettiRimastiAHans[6] > 0:
            dati[37] += oggettiRimastiAHans[6]
        if oggettiRimastiAHans[7] > 0:
            dati[38] += oggettiRimastiAHans[7]
        if oggettiRimastiAHans[8] > 0:
            dati[39] += oggettiRimastiAHans[8]
        if oggettiRimastiAHans[9] > 0:
            dati[40] += oggettiRimastiAHans[9]
        if oggettiRimastiAHans[10] > 0:
            dati[132] += oggettiRimastiAHans[10]
        if dati[132] > 1:
            dati[132] = 1
        if dati[62] <= 0 and oggettiRimastiAHans[11] > 0:
            dati[62] = oggettiRimastiAHans[11]
        if oggettiRimastiAHans[12] > 0:
            dati[131] += oggettiRimastiAHans[12]
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
            if listaPersonaggiTotali[i].stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta7"]:
                del listaPersonaggiTotali[i]
            else:
                i += 1
        i = 0
        while i < len(listaNemiciTotali):
            if listaNemiciTotali[i].stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta7"]:
                del listaNemiciTotali[i]
            else:
                i += 1
        stanza = GlobalGameVar.dictStanze["forestaCadetta7"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sotterratoSam"] and stanza == GlobalGameVar.dictStanze["forestaCadetta7"]:
        pygame.time.wait(1000)
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoDopoTombaSam"] and stanza == GlobalGameVar.dictStanze["forestaCadetta8"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["penultimaStanzaForesta"] and stanza == GlobalGameVar.dictStanze["forestaCadetta9"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ultimaStanzaForesta"] and stanza == GlobalGameVar.dictStanze["stradaPerCittà1"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivatoAllaPortaDellaCittà"] and stanza == GlobalGameVar.dictStanze["stradaPerCittà3"]:
        screen = GlobalHWVar.schermo.copy().convert()
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreBussareCitta)
        i = 0
        while i < 1:
            pygame.time.wait(1000)
            pygame.event.pump()
            i += 1
        pygame.time.wait(500)
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "PadreUfficialeServizio", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        i = 0
        while i < len(stanzeGiaVisitate):
            if stanzeGiaVisitate[i] == stanza:
                del stanzeGiaVisitate[i]
            i += 1
        i = 0
        while i < len(listaPersonaggiTotali):
            if listaPersonaggiTotali[i].stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta7"]:
                del listaPersonaggiTotali[i]
            else:
                i += 1
        stanza = GlobalGameVar.dictStanze["stradaPerCittà3"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["apertoPortaCittà"] and stanza == GlobalGameVar.dictStanze["stradaPerCittà3"]:
        pygame.time.wait(1000)
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "PadreUfficialeServizio", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        stanza = GlobalGameVar.dictStanze["casaDavid1"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoCasaUfficiale"] and stanza == GlobalGameVar.dictStanze["casaDavid1"]:
        screen = GlobalHWVar.schermo.copy().convert()

        pygame.time.wait(1000)
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "PadreUfficialeServizio", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)

        GlobalHWVar.disegnaImmagineSuSchermo(screen, (0, 0))
        GlobalHWVar.aggiornaSchermo()
        GlobalHWVar.canaleSoundCanzone.set_volume(0)
        GlobalHWVar.canaleSoundCanzone.play(canzone, -1)
        i = 0
        while i < GlobalHWVar.volumeCanzoni:
            GlobalHWVar.canaleSoundCanzone.set_volume(i)
            i += GlobalHWVar.volumeCanzoni / 10
            pygame.time.wait(30)
        GlobalHWVar.canaleSoundCanzone.set_volume(GlobalHWVar.volumeCanzoni)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["primoDialogoConDavid"] and stanza == GlobalGameVar.dictStanze["casaDavid1"]:
        padreArrivato = False
        for personaggio in listaPersonaggi:
            if personaggio.tipo == "PadreUfficialeServizio":
                if personaggio.x == GlobalHWVar.gpx * 28 and personaggio.y == GlobalHWVar.gpy * 11:
                    padreArrivato = True
                break

        if padreArrivato:
            for personaggio in listaPersonaggi:
                if personaggio.tipo == "PadreUfficialeServizio":
                    listaPersonaggi.remove(personaggio)
                    break
            for personaggio in listaPersonaggiTotali:
                if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"] and personaggio.tipo == "PadreUfficialeServizio":
                    listaPersonaggiTotali.remove(personaggio)
                    break
            avanzamentoStoria += 1
            caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioBagnoCasaDavid"] and stanza == GlobalGameVar.dictStanze["casaDavid3"]:
        dati[6] = 0
        dati[7] = 0
        dati[8] = 0
        dati[128] = 0
        dati[129] = 0
        dati[130] = 0
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["casaDavid3"]
        cambiosta = True
        carim = True
        aggiornaImgEquip = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["fattoBagnoCasaDavid"] and stanza == GlobalGameVar.dictStanze["casaDavid3"]:
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPreCambioPerCenaDavid"] and stanza == GlobalGameVar.dictStanze["casaDavid3"]:
        avanzamentoStoria += 1
        stanza = GlobalGameVar.dictStanze["casaDavid3"]
        cambiosta = True
        carim = True
        caricaTutto = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"] and stanza == GlobalGameVar.dictStanze["casaDavid3"]:
        for personaggio in listaPersonaggiTotali:
            if personaggio.stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"] and personaggio.tipo == "PadreUfficialeServizio":
                listaPersonaggiTotali.remove(personaggio)
                break
        personaggio = PersonaggioObj.PersonaggioObj(x, y, False, "Nessuno", stanza, avanzamentoStoria, False)
        avanzamentoStoria, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi = GenericFunc.dialoga(avanzamentoStoria, personaggio, listaAvanzamentoDialoghi)
        caricaTutto = True

    if caricaTutto:
        bottoneDown = False
    return avanzamentoStoria, cambiosta, stanza, npers, carim, caricaTutto, bottoneDown, movimentoPerMouse, listaPersonaggi, listaNemici, listaPersonaggiTotali, listaNemiciTotali, dati, oggettiRimastiAHans, tutteporte, oggettoRicevuto, visualizzaMenuMercante, listaAvanzamentoDialoghi, aggiornaImgEquip
