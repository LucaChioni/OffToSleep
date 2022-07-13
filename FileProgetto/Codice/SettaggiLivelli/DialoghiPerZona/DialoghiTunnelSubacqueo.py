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

    if stanzaDiAppartenenza == GlobalGameVar.dictStanze["tunnelSubacqueo1"]:
        if tipo == "OggettoPortaSfondata":
            partiDialogo = []
            nome = "OggettoPortaSfondata"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(Qualcuno ha sfondato la porta per entrare...)")
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(u"(È la porta del laboratorio... credo che l'unico che possa averla sfondata sia il Costruttore...)")
                partiDialogo.append(dialogo)
        elif tipo == "Bibliotecario":
            partiDialogo = []
            nome = u"René"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo2PostSecondaSparizioneDiNeilDalLaboratorio"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(u"... Neil!")
                partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo
