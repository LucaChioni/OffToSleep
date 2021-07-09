# -*- coding: utf-8 -*-

import Codice.Variabili.GlobalGameVar as GlobalGameVar


def setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute):
    tipo = tipoId.split("-")[0]

    partiDialogo = []
    nome = "---"
    oggettoDato = False
    avanzaStoria = False
    menuMercante = False
    scelta = False
    avanzaColDialogo = False
    if stanzaDiAppartenenza == GlobalGameVar.dictStanze["avampostoDiRod1"]:
        if tipo == "Mercante":
            partiDialogo = []
            nome = "Rod"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoAvampostoDiRod"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"")
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"")
                partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
