# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.GestioneNemiciPersonaggi.PersonaggioObj as PersonaggioObj


def setNemici(stanza, listaNemiciTotali, listaNemici, avanzamentoStoria):
    return listaNemiciTotali, listaNemici


def setPersonaggi(stanza, listaPersonaggiTotali, listaPersonaggi, avanzamentoStoria, listaAvanzamentoDialoghi):
    if stanza == GlobalGameVar.dictStanze["labirinto10"]:
        avanzamentoDialogoPazzo = 0
        i = 0
        while i < len(listaAvanzamentoDialoghi):
            if listaAvanzamentoDialoghi[i] == "Pazzo2-0":
                avanzamentoDialogoPazzo = listaAvanzamentoDialoghi[i + 1]
                break
            elif listaAvanzamentoDialoghi[i] == "Pazzo1-0":
                avanzamentoDialogoPazzo = listaAvanzamentoDialoghi[i + 1]
            i += 2
        if avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["monologoUscitaLabirinto"] and 2 <= avanzamentoDialogoPazzo < 4:
            percorsoPersonaggio = ["dGira", "mantieniPosizione"]
            personaggio = PersonaggioObj.PersonaggioObj(GlobalHWVar.gsx // 32 * 13, GlobalHWVar.gsy // 18 * 10, "d", "Pazzo1-0", stanza, avanzamentoStoria, percorsoPersonaggio)
            listaPersonaggi.append(personaggio)
            listaPersonaggiTotali.append(personaggio)

    return listaPersonaggiTotali, listaPersonaggi
