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
        if tipo == "SerpeVerde":
            nome = LI.SERPENTE_VERDE
        elif tipo == "SerpeArancio":
            nome = LI.SERPENTE_ARANCIONE
        elif tipo == "RagnoNero":
            nome = LI.RAGNO_NERO
        elif tipo == "RagnoRosso":
            nome = LI.RAGNO_ROSSO
        elif tipo == "Scorpione":
            nome = LI.SCORPIONE
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoAvampostoPostEsplosioneVulcano"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0364_01_Tu_SONO_IMMOBILI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0364_02_Scorpione__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0364_03_Tu__STR_POT_OSS_COS_DA_VIC_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._1270_01_Scorpione__)
            partiDialogo.append(dialogo)
    elif tipo.startswith("OggettoDict"):
        partiDialogo = []
        if tipo.startswith("OggettoDictCadavereSerpeVerde"):
            nome = LI.SERPENTE_VERDE
        elif tipo.startswith("OggettoDictCadavereSerpeArancio"):
            nome = LI.SERPENTE_ARANCIONE
        elif tipo.startswith("OggettoDictCadavereRagnoNero"):
            nome = LI.RAGNO_NERO
        elif tipo.startswith("OggettoDictCadavereRagnoRosso"):
            nome = LI.RAGNO_ROSSO
        elif tipo.startswith("OggettoDictCadavereScorpione"):
            nome = LI.SCORPIONE
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = True
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDS._1271_01_Scorpione__)
        partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["selvaArida1"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialMenuPrevisioniImpo"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0365_01_Tu_OH_CHE_SCH_IL_TER__TUT_APP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0365_02_Tu__TUT_A_POS_TU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0365_03_Impo__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0365_04_Tu__DIR_DI_S_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["selvaArida2"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialUsoImpoFrutti"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0366_01_Tu_QUE_POS__UN_CAS_PER_CI_SON_QUE_TRA_PER_TER_DOV_SEG_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0366_02_Impo__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0366_03_Tu__MMH_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["selvaArida4"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSelva2"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0367_01_Tu_PAN_PAN_CAV_PAN_PAN_DEV_DIR_CHE_NON_ME_LA_SAR_CAV_DA_SOL_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["selvaArida6"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSelva4"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0368_01_Tu_OTT_SCO_MI_SA_CHE_CI_SAR_BIS_DI_UN_BEL_LAV_DI_SQU_QUI_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["selvaArida16"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSelva6"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0369_01_Tu_OHH_LUS_CE_LAB_FAT_)
                partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo


