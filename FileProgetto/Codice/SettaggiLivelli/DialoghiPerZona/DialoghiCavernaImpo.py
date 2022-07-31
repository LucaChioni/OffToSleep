# -*- coding: utf-8 -*-

import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.Localizzazione.LocalizInterfaccia as LI
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
    if tipo in GlobalImgVar.vettoreNomiNemici:
        partiDialogo = []
        if tipo == "RoboLeggero":
            nome = LI.IMPO_LEGGERO
        elif tipo == "RoboVolante":
            nome = LI.IMPO_VOLANTE
        elif tipo == "RoboPesante":
            nome = LI.IMPO_PESANTE
        elif tipo == "RoboPesanteVolante":
            nome = LI.IMP_VOL_PES
        elif tipo == "RoboTorre":
            nome = LI.IMPO_TORRE
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0624_01_Tu_MI_IGNORANO_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0625_01_ImpoTorre__)
            partiDialogo.append(dialogo)
    elif tipo.startswith("OggettoDict"):
        partiDialogo = []
        if tipo.startswith("OggettoDictCadavereRoboLeggero"):
            nome = LI.IMPO_LEGGERO
        elif tipo.startswith("OggettoDictCadavereRoboVolante"):
            nome = LI.IMPO_VOLANTE
        elif tipo.startswith("OggettoDictCadavereRoboPesante"):
            nome = LI.IMPO_PESANTE
        elif tipo.startswith("OggettoDictCadavereRoboPesanteVolante"):
            nome = LI.IMP_VOL_PES
        elif tipo.startswith("OggettoDictCadavereRoboTorre"):
            nome = LI.IMPO_TORRE
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = True
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDS._0626_01_ImpoTorre__)
        partiDialogo.append(dialogo)
    elif tipo == "OggettoCumuloImpo":
        partiDialogo = []
        nome = LI.CUMULO_IMPO
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["risvegliatoNelVulcano"]:
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0627_01_Tu__UN_CUM_DI_IMP_MA_SON_SEN_QUE_TUB_PER_ALI_IMP_)
            partiDialogo.append(dialogo)
        else:
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0627_02_Tu__UN_CUM_DI_IMP_)
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["caverna1"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostSbloccoCaverna"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0062_01_Tu_C_COR_QUA_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoCaverna1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0063_01_Tu__UN_IMP_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["attaccatoDaImpoInCaverna1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0064_01_Tu_CAZZO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostAttaccoDiImpoOstile"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0065_01_Tu__MA_CHE_CAV_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["caverna2"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostAttaccoDiImpoOstile"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0066_01_Tu__MA_CHE_CAV_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["caverna9"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostAttaccoDiImpoOstile"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0067_01_Tu__MA_CHE_CAV_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["caverna18"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostUccisioneImpoOstile"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0068_01_Tu_UFF_FOR_SON_FIN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0068_02_Tu__MAM_MIA_QUE_CAL_DA_DOV_PRO_)
                partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo


