# -*- coding: utf-8 -*-

import Codice.Localizzazione.LocalizInterfaccia as LI
import Codice.Localizzazione.LocalizDialoghiSecondari as LDS


def setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute):
    tipo = tipoId.split("-")[0]

    partiDialogo = []
    nome = "---"
    oggettoDato = False
    avanzaStoria = False
    menuMercante = False
    scelta = False
    avanzaColDialogo = False
    if tipo.startswith("OggettoDict"):
        partiDialogo = []
        if tipo.startswith("OggettoDictCadavereOrco"):
            nome = LI.ORCO
        elif tipo.startswith("OggettoDictCadaverePipistrello"):
            nome = LI.PIPISTRELLO
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = True
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDS._1272_01_Pipistrello__)
        partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo


