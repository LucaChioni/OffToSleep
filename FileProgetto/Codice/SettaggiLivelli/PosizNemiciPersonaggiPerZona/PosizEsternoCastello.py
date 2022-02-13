# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj
import Codice.GestioneNemiciPersonaggi.NemicoObj as NemicoObj


def setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria):
    if stanza == GlobalGameVar.dictStanze["esternoCastello1"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 2, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 3, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 5, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 6, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 7, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 9, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 10, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 11, "d", "ServoArco", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 19, GlobalHWVar.gsy // 18 * 6, "d", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 2, "d", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 3, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 5, "d", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 7, "d", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 9, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 10, "d", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 11, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 5, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 21, GlobalHWVar.gsy // 18 * 7, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 2, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 10, "d", "ServoSpada", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 3, "d", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 9, "d", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)
            percorsoNemico = []
            nemico = NemicoObj.NemicoObj(GlobalHWVar.gsx // 32 * 23, GlobalHWVar.gsy // 18 * 11, "d", "ServoLancia", stanza, percorsoNemico)
            listaNemiciTotali.append(nemico)
            listaNemici.append(nemico)

    return listaNemiciTotali, listaNemici


def setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi):
    if stanza == GlobalGameVar.dictStanze["esternoCastello1"]:
        if not (GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]):
            percorsoPersonaggio = ["sGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 3, GlobalHWVar.gsy // 18 * 8, "s", "ServoLancia-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["dGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 6, "d", "ServoLancia-1", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoUscitaInternoCastello20Fuggendo"]:
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 22, GlobalHWVar.gsy // 18 * 6, "d", "Neil-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["esternoCastello2"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["apertoCancelloPrincipaleCastello"]:
            percorsoPersonaggio = ["wGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 13, "w", "ServoLancia-2", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["wGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13, "w", "ServoLancia-3", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = []
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 14, "s", "OggettoCancelloCastello-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["apertoCancelloPrincipaleCastello"]:
            percorsoPersonaggio = ["wGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 13, "d", "ServoLancia-2", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["wGira", "s", "s"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 18, GlobalHWVar.gsy // 18 * 13, "s", "ServoLancia-3", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["servoLanciaTornatoAlCancello"]:
            percorsoPersonaggio = ["wGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 13, "w", "ServoLancia-2", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
        elif not (GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]):
            percorsoPersonaggio = ["wGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 13, "w", "ServoLancia-2", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
            percorsoPersonaggio = ["wGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 20, GlobalHWVar.gsy // 18 * 13, "w", "ServoLancia-3", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["esternoCastello4"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["servoLanciaAndatoInEsternoCastello4"]:
            percorsoPersonaggio = ["s"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 16, GlobalHWVar.gsy // 18 * 4, "w", "ServoLancia-3", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)
    elif stanza == GlobalGameVar.dictStanze["esternoCastello5"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["servoLanciaAndatoInEsternoCastello5"]:
            percorsoPersonaggio = ["a", "s", "a", "a", "s", "s", "s", "s", "s", "a", "s", "dGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 12, GlobalHWVar.gsy // 18 * 6, "w", "ServoLancia-3", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)

    return listaPersonaggiTotali, listaPersonaggi
