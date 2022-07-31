# -*- coding: utf-8 -*-

import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.Localizzazione.LocalizDialoghiSecondari as LDS
import Codice.Localizzazione.LocalizDialoghiPrincipali as LDP


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
                dialogo.append(LDS._1310_01_Tu_QUA_HA_SFO_LA_POR_PER_ENT_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1311_01_Tu__LA_POR_DEL_LAB_CRE_CHE_LUN_CHE_POS_AVE_SFO_SIA_IL_COS_)
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
                dialogo.append(LDP._0375_01_Ren__NEIL_)
                partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo


