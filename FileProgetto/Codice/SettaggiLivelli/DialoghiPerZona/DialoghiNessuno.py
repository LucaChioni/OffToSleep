# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.Localizzazione.LocalizInterfaccia as LI
import Codice.Localizzazione.LocalizDialoghiSecondari as LDS
import Codice.Localizzazione.LocalizDialoghiPrincipali as LDP


def setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute):
    tipo = tipoId.split("-")[0]

    if GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
        frasePortaChiusa = LDS._1322_01_Tu_POT_ENT_MA_NON_MI_PAR_IL_CAS_DI_RIC_AL_CAL_DI_FAR_DEL_LAV_SUP_AI_FIN_DEL_STO_PRI
    else:
        frasePortaChiusa = LDS._1323_01_Tu__CHI_A_CHI

    partiDialogo = []
    nome = LI.NESSUNO
    oggettoDato = False
    avanzaStoria = False
    menuMercante = False
    scelta = False
    avanzaColDialogo = False
    if GlobalGameVar.dictStanze["sognoSara1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["sognoSara4"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizio"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0180_01_Tu_OH_CAV_DOV_SON_ADE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0180_02_Tu_MI_SON_PER_LO_SAP_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialMovimento"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1069_01_Tu_DOV_APR_QUE_BAU_PRI_DI_AND_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialOggettiBattaglia"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0181_01_Tu_OK_HAN_DOV_ESS_PAS_DI_QUA_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoSognoSara2"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0182_01_Tu_PER_SON_VEN_QUI_)
            partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["casaHansSara1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["casaHansSara4"]:
        if (GlobalGameVar.dictAvanzamentoStoria["inizioSognoCasaDavid"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCasaDavid"] or GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"]) and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara1"] and ((x == GlobalHWVar.gpx * 24 and y == GlobalHWVar.gpy * 3) or (x == GlobalHWVar.gpx * 7 and y == GlobalHWVar.gpy * 7)):
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1070_01_Tu_NON_SI_APR_)
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara2"] and (y == GlobalHWVar.gpy * 1 or y == GlobalHWVar.gpy * 3):
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1071_01_Tu_DEV_SEG_HAN_)
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara4"] and y == GlobalHWVar.gpy * 1:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1072_01_Tu_NON_VOG_TOR_IND_)
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara4"] and y == GlobalHWVar.gpy * 16:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1073_01_Tu_DEV_PAR_CON_HAN_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and x == GlobalHWVar.gpx * 24 and y == GlobalHWVar.gpy * 3 and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara1"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1074_01_Tu_NON_VOG_FAR_SCO_E_SE_ENT_I_MIE_GEN_SI_SVE_O_FOR_SON_ANC_SVE_NON_IMP_BAS_CHE_NON_MI_FAC_VED_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoCasaHansSara2"] and (x == GlobalHWVar.gpx * 16 or x == GlobalHWVar.gpx * 17) and y == GlobalHWVar.gpy * 16 and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara1"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1075_01_Tu_PRI_DEV_POR_LAC_A_SAR_COS_SI_RIA_E_NON_SI_ACC_CHE_SON_USC_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara1"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0183_01_Tu__MI_HA_POR_LAC_MA_NON__TOR_A_LET_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0183_02_Tu_PRO_A_VED_SE__ANC_QUA_FUO_DA_QUA_PAR_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRisveglioSara"] and x == GlobalHWVar.gpx * 6 and y == GlobalHWVar.gpy * 10 and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara1"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1076_01_Tu_ASP_PRI_DI_AND_DEV_PRE_LA_MIA_MAP_E_IL_DIA_DOV_POT_DOC_QUA_DI_INT_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialMappaDiario"] and x == GlobalHWVar.gpx * 6 and y == GlobalHWVar.gpy * 8 and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara1"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0184_01_Tu_FUO__TRO_PER_DI_NOT_DEV_PRE_PRI_DI_USC_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0184_02_Tu_NEL_RIP_DI_MIO_PAD_CI_DOV_ESS_QUA_DI_UTI_)
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["armaturaNonnoCompletata"] and (x == GlobalHWVar.gpx * 16 or x == GlobalHWVar.gpx * 17) and y == GlobalHWVar.gpy * 16 and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara1"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1077_01_Tu_FUO__PER_DEV_PRE_MEG_PRI_DI_USC_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1077_02_Tu_NEL_RIP_DI_MIO_PAD_CI_DOV_ESS_QUA_DI_UTI_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoIndicazioniArmaturaNonno"] and x == GlobalHWVar.gpx * 26 and y == GlobalHWVar.gpy * 10 and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara1"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0185_01_Tu_NO_MER_NON_SI_APR_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0185_02_Tu_LA_CHI_DEV_ESS_QUI_DA_QUA_PAR_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"] and x == GlobalHWVar.gpx * 26 and y == GlobalHWVar.gpy * 10 and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara1"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1078_01_Tu_DEV_TRO_LA_CHI_PER_ENT_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["armaturaNonno4"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0186_01_Tu_BEN_QUE_MI_ENT_PER_SON_PRO_PER_AND_ADE_)
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"] and y == GlobalHWVar.gpy * 1 and (x == GlobalHWVar.gpx * 14 or x == GlobalHWVar.gpx * 15 or x == GlobalHWVar.gpx * 16 or x == GlobalHWVar.gpx * 17) and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara4"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1079_01_Tu_I_MIE_GEN_NON_SE_LA_STA_PAS_BEN_MA_NON_POS_TOR_FIN_NON_SCO_DOV_AND_HAN_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 1 and (x == GlobalHWVar.gpx * 14 or x == GlobalHWVar.gpx * 15 or x == GlobalHWVar.gpx * 16 or x == GlobalHWVar.gpx * 17) and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara4"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1080_01_Tu_NON_MI_VA_DI_TOR_ADE_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["missileNucleareScoppiatoSecondaVolta"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0187_01_Tu_STOOOP_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoNelCalcolatoreACasaTua"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0188_01_Tu__TOR_IND_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroNelTempoAllaSeraDellInizioDelGioco"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0189_01_Tu_AVVIA_SEQUENZA_)
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and ((stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara2"] and (y == GlobalHWVar.gpy * 1 or y == GlobalHWVar.gpy * 3)) or (stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara4"] and y == GlobalHWVar.gpy * 1)):
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1081_01_Tu_DEV_SEG_HAN_)
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["monologoUscitaLaboratorioPostPassatiMoltiAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fine"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaHansSara4"] and y == GlobalHWVar.gpy * 16:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(u"...")
            partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["forestaCadetta1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["forestaCadetta9"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ingressoForestaCadetta"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0190_01_Tu_BEN_DAL_PAR_DEL_FOR_C_LA_CIT_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialDifesa"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0191_01_Tu_PAN_PAN_DOV_ESS_QUA_DAL_PAR_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["quartaStanzaForestaCadetta"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0192_01_Tu_POR_MIS_QUE_LUP_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0192_02_Tu_UN_MOM_C_UN_SOL_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontroFiglioUfficiale"] and ((x == GlobalHWVar.gpx * 15 and y == GlobalHWVar.gpy * 16) or (x == GlobalHWVar.gpx * 30 and y == GlobalHWVar.gpy * 8)) and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta5"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1082_01_Tu_PRI_DI_PRO_POT_CHI_A_QUE_SOL_QUA_DI_QUE_STR_POR_ALL_CIT_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and x == GlobalHWVar.gpx * 15 and y == GlobalHWVar.gpy * 16 and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta5"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1083_01_Tu_MEG_PRE_LA_LEG_E_ACC_QUI_PER_LA_NOT_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialSeppellireCadaveri"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0193_01_Tu_HANS_HAAANS_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0193_02_Tu__CAVOLO_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ingressoForestaCadettaSara"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0194_01_Tu_EHI_C_UN_ACC_QUI_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["accampamentoForestaAnalizzato2"] and ((x == GlobalHWVar.gpx * 15 and y == GlobalHWVar.gpy * 16) or (x == GlobalHWVar.gpx * 30 and y == GlobalHWVar.gpy * 8)) and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta5"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1084_01_Tu_DOV_GUA_BEN_LAC_PER_CAP_SE_HAN__STA_QUI_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["accampamentoForestaAnalizzato2"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta7"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0195_01_Tu_NON_SAR_FAC_PAS_QUA_IN_MEZ_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["incontratoBrancoLupiNeri"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta7"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0196_01_Tu_C_UN_UOM_A_TER_E_OK_PRI_DI_TUT_MI_DEV_OCC_DI_QUE_BES_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sotterratoSam"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta7"]:
            oggettoDato = LI.EQUIPAGGIAMENTO_SOLDATO
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0197_01_Tu_ECCO_FATTO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0197_02_Tu_FOR_NON_AVR_DOV_PRE_LE_SUE_COS_MA_NON_CRE_CHE_GLI_SER_ANC_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["rimessaMusicaDopoTombaSam"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta9"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0198_01_Tu_FINALMENTE_LUSCITA_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoHansFuoriCasaSognoCastello"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta5"] and y == GlobalHWVar.gpy * 8:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0199_01_Tu_EHI_IN_QUE_CES_)
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta5"] and y == GlobalHWVar.gpy * 1:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1085_01_Tu_NON_VOG_TOR_IND_)
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta5"] and (y == GlobalHWVar.gpy * 16 or x == GlobalHWVar.gpx * 30):
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1086_01_Tu_C_QUA_INC_IN_QUE_CES_)
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and ((stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta1"] and y == GlobalHWVar.gpy * 1) or (stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta2"] and x == GlobalHWVar.gpx * 30) or (stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta3"] and y == GlobalHWVar.gpy * 1) or (stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta4"] and y == GlobalHWVar.gpy * 1) or (stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta5"] and y == GlobalHWVar.gpy * 1)):
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1087_01_Tu_DEV_SEG_HAN_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["SaraUscitaDaForestaCadetta5Calcolatore"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["forestaCadetta5"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0200_01_Tu__)
            partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["stradaPerCittà1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["stradaPerCittà3"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ultimaStanzaForesta"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["stradaPerCittà1"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0201_01_Tu_PER_ADE_MI_BAS_SEG_LA_STR_E_ARR_IN_CIT_HAN_SAR_SIC_L_DA_QUA_PAR_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivatoAllaPortaDellaCittà"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["stradaPerCittà3"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0202_01_Tu__)
            partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["città1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["città10"]:
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["città1"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCittà2"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1088_01_Tu_NON_SO_DOV_AND_DEV_SEG_DAV_)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città2"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1089_01_Tu_MEG_SEG_DAV_)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città3"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 13 and (x == GlobalHWVar.gpx * 14 or x == GlobalHWVar.gpx * 15):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1090_01_Tu_NON_CRE_DI_POT_ENT_IN_QUE_ABI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 13 and (x == GlobalHWVar.gpx * 14 or x == GlobalHWVar.gpx * 15):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1091_01_Tu_MEG_SEG_DAV_)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 1:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1092_01_Tu_NON_HO_VOG_DI_TOR_L_POI__PIE_DI_GUA_MEG_EVI_)
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1093_01_Tu_NON_HO_VOG_DI_TOR_L_)
                    partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città4"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1094_01_Tu_MEG_SEG_DAV_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoDopoAlzatoDalLetto"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0203_01_Tu_OK_DEV_CER_HAN_NEG_ALL_PRO_CHE_NON_HO_IDE_DI_DOV_SIA_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ricevutoCertificatoDalServo"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0204_01_Tu_UFF__DIF_PEN_AD_ALT_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and y == GlobalHWVar.gpy * 4 and (x == GlobalHWVar.gpx * 11 or x == GlobalHWVar.gpx * 12):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1095_01_Tu_NON_ENT_ADE_I_SOL_MI_ACC_DEL_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uccisoSecondoAggressore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0205_01_Tu__ODDIO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0205_02_Tu_DEV_AND_DA_QUI_)
                partiDialogo.append(dialogo)
            elif (x == GlobalHWVar.gpx * 11 or x == GlobalHWVar.gpx * 12) and y == GlobalHWVar.gpy * 5:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città5"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and x == GlobalHWVar.gpx * 1 and (y == GlobalHWVar.gpy * 12 or y == GlobalHWVar.gpy * 13):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1096_01_Tu_NON_CRE_DI_POT_ENT_IN_QUE_ABI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and x == GlobalHWVar.gpx * 1 and (y == GlobalHWVar.gpy * 12 or y == GlobalHWVar.gpy * 13):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["chiestoDegliAlloggiAlMercante"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1097_01_Tu_POT_CHI_A_QUA_QUI_INT_PER_GLI_ALL_PRO_SE_INI_AD_AND_A_CAS_POT_IMP_MOL_TEM_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cercatoHansInAlloggiProfughi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1098_01_Tu_IL_CUO_MI_DIC_CHE_STO_SBA_STR_LA_SIN__DAL_PAR_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["rimosseMonetePerEntrareInConfraternita"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1099_01_Tu_QUA_CI_SON_TAN_PER_CHE_POT_AVE_VIS_HAN_DEV_PAR_CON_TUT_PRI_DI_CON_A_ESP_LA_CIT_)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città6"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cercatoHansInAlloggiProfughi"] and y == GlobalHWVar.gpy * 4 and (x == GlobalHWVar.gpx * 17 or x == GlobalHWVar.gpx * 18):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1100_01_Tu__CHI_FOR_QUE_SOL_POS_AIU_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["cercatoHansInAlloggiProfughi"] and y == GlobalHWVar.gpy * 4 and (x == GlobalHWVar.gpx * 17 or x == GlobalHWVar.gpx * 18):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1101_01_Tu__CHIUSO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["chiestoDegliAlloggiAlMercante"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0206_01_Tu_QUE_DOV_ESS_LO_STA_CHE_OSP_GLI_ALL_PRO_)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città7"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 15 and (x == GlobalHWVar.gpx * 9 or x == GlobalHWVar.gpx * 10):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1102_01_Tu_NON_CRE_DI_POT_ENT_IN_QUE_ABI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 15 and (x == GlobalHWVar.gpx * 9 or x == GlobalHWVar.gpx * 10):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["fuggitoVersoCittà7"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0207_01_Tu__PAN_PAN_CAZ_CHE_COS_FAT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0207_02_Tu__PAN_PAN_CCH_FAC_ORA_)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1103_01_Tu_NON_VOG_TOR_IND_)
                partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 5 and (x == GlobalHWVar.gpx * 18 or x == GlobalHWVar.gpx * 19):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1104_01_Tu_IL_SAN_SUL_MIE_ARM_NON_DOV_TEN_ADD_)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città8"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1105_01_Tu_NON_CRE_CHE_LAS_ENT_PER_COM_ME_O_HAN_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1106_01_Tu__CHIUSO_)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città9"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and x == GlobalHWVar.gpx * 28 and (y == GlobalHWVar.gpy * 9 or y == GlobalHWVar.gpy * 10):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1107_01_Tu_NON_CRE_DI_POT_ENT_IN_QUE_ABI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and x == GlobalHWVar.gpx * 28 and (y == GlobalHWVar.gpy * 9 or y == GlobalHWVar.gpy * 10):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1108_01_Tu_DEV_CER_MEG_IN_CIT_PRI_DI_AND_)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città10"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 2 and (x == GlobalHWVar.gpx * 8 or x == GlobalHWVar.gpx * 9):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1109_01_Tu_NON_CRE_DI_POT_ENT_IN_QUE_ABI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and y == GlobalHWVar.gpy * 2 and (x == GlobalHWVar.gpx * 8 or x == GlobalHWVar.gpx * 9):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 1 and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1110_01_Tu_DEV_CER_MEG_IN_CIT_PRI_DI_AND_)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 1 and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1111_01_Tu_LA_SEL_ARI_NON__DA_QUE_PAR_)
                partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["casaDavid1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["casaDavid3"]:
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineDialogoCenaDavid"] and y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1112_01_Tu_NON_HA_SEN_AND_IN_GIR_PER_LA_CIT_ADE_AVR_TUT_IL_TEM_PER_CER_HAN_DOM_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1113_01_Tu_NON_SEG_DAV_MEG_AND_A_LET_MI_RES_POC_TEM_PER_RIP_)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 1 or y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["padreUfficialeUscitoDallaCena"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0208_01_Tu__)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["dialogoServoCasaDavidDopoSuicidio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ricevutoCertificatoDalServo"] and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1114_01_Tu_MI_HA_DET_DI_ASP_QUI_)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["dialogoServoCasaDavidDopoSuicidio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ricevutoCertificatoDalServo"] and (x == GlobalHWVar.gpx * 1 or y == GlobalHWVar.gpy * 5):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1115_01_Tu_NON_POS_AND_DEV_PRE_IL_CER_PRI_)
                partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1116_01_Tu_C_UN_TER_ENO_CON_UNA_BEL_VIS_)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid3"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["fattoBagnoCasaDavid"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0209_01_Tu_CAV_QUE_RIS_VOR_RIM_L_DEN_PER_SEM_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0210_01_Tu_PER_QUE_AND_BEN_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["alzatoDalLettoSecondoGiorno"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0211_01_Tu_YAA_CHE_SON_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presaChiaveStanzaDaLettoDavid"] and x == GlobalHWVar.gpx * 12 and y == GlobalHWVar.gpy * 9:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoDopoBagnoDavid"] and x == GlobalHWVar.gpx * 30:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1117_01_Tu_MI_DEV_ANC_CAM_I_VES_CRE_CHE_ME_LI_ABB_LAS_NEL_MIA_CAM_)
                partiDialogo.append(dialogo)
            elif (x == GlobalHWVar.gpx * 14 and y == GlobalHWVar.gpy * 14) or (x == GlobalHWVar.gpx * 20 and y == GlobalHWVar.gpy * 8) or (x == GlobalHWVar.gpx * 22 and y == GlobalHWVar.gpy * 14) or (x == GlobalHWVar.gpx * 28 and y == GlobalHWVar.gpy * 8):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["biblioteca1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["biblioteca3"]:
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca2"]:
            if x == GlobalHWVar.gpx * 21 and y == GlobalHWVar.gpy * 11:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoBibliotecarioPreVomito2"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0212_01_Tu_PUAH_)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 21 and y == GlobalHWVar.gpy * 9:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["risoltoEnigmaBibliotecario"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1118_01_Tu_IL_BIB_MI_STA_ASP_)
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoBibliotecarioControlloRegistri"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1119_01_Tu_DEV_CON_I_REG_PRI_DI_AND_)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1120_01_Tu_REN_MI_STA_ASP_DEV_PRE_LA_MAR_DA_CON_A_NEI_PRI_DI_AND_)
                    partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["avampostoDiRod1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["avampostoDiRod3"]:
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["avampostoDiRod1"]:
            if x == GlobalHWVar.gpx * 3 and y == GlobalHWVar.gpy * 6:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 21 and y == GlobalHWVar.gpy * 16:
                if avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["arrivoAvampostoDiRod"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1121_01_Tu_NON_CRE_CHE_QUE_SIA_LA_DIR_GIU_FOR_ROD_PU_AIU_)
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["richiesteMonetePerMappaLabirinto"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1122_01_Tu_SEN_UNA_MAP_MI_PER_DI_SIC_)
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["copiataMappaLabirinto"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1123_01_Tu_MEG_DAR_UNO_ALL_MAP_PRI_)
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["risoltoEnigmaMappaLabirinto"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1124_01_Tu_SE_MI_SEG_IL_PER_DA_SEG_SAR_MOL_PI_FAC_ATT_IL_LAB_)
                    partiDialogo.append(dialogo)
                elif GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1125_01_Tu_FAC_PRI_USA_LA_SCO_)
                    partiDialogo.append(dialogo)
            elif (x == GlobalHWVar.gpx * 19 or x == GlobalHWVar.gpx * 20 or x == GlobalHWVar.gpx * 21 or x == GlobalHWVar.gpx * 22 or x == GlobalHWVar.gpx * 23 or x == GlobalHWVar.gpx * 24) and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1126_01_Tu_NON_VOG_PER_TEM_DEV_PAR_CON_SAR_ADE_)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["avampostoDiRod2"]:
            if (x == GlobalHWVar.gpx * 6 or x == GlobalHWVar.gpx * 7 or x == GlobalHWVar.gpx * 8 or x == GlobalHWVar.gpx * 9 or x == GlobalHWVar.gpx * 10) and y == GlobalHWVar.gpy * 3:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1127_01_Tu__UNA_GRO_BLO_DA_DEL_SBA_COS_CI_SAR_L_DEN_)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1128_01_Tu_ROD_DEV_AVE_RIC_)
                    partiDialogo.append(dialogo)
            elif (x == GlobalHWVar.gpx * 28 and y == GlobalHWVar.gpy * 10) or y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1129_01_Tu_DEV_SEG_REN_)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["avampostoDiRod3"]:
            if x == GlobalHWVar.gpx * 26 and y == GlobalHWVar.gpy * 6:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1130_01_Tu_NON_SI_APR_FOR_LA_CHI__QUI_DA_QUA_PAR_)
                partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["esternoCastello1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["esternoCastello5"]:
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["esternoCastello1"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoUscitaCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0213_01_Tu_ECC_IL_PAS_PER_LA_SCO_ADE_IL_CAN__APE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRodDecisoDiParlareConSara"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0214_01_Tu_NON_CI_SON_SOL_)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 1 and y == GlobalHWVar.gpy * 9:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 13 and y == GlobalHWVar.gpy * 13:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 13 and y == GlobalHWVar.gpy * 1:
                if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1131_01_Tu_NON_VOG_PER_TEM_DEV_PAR_CON_SAR_ADE_)
                    partiDialogo.append(dialogo)
                elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1132_01_Tu_DEV_SEG_REN_)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1133_01_Tu_POS_PAS_PER_LA_SCO_ADE_)
                    partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 30:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1134_01_Tu_DEV_SEG_REN_)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["esternoCastello2"]:
            if y == GlobalHWVar.gpy * 16 or x == GlobalHWVar.gpx * 30:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1135_01_Tu_DEV_SEG_REN_)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["esternoCastello4"]:
            if y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1136_01_Tu_DEV_SEG_REN_)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["esternoCastello5"]:
            if y == GlobalHWVar.gpy * 15:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1137_01_Tu_DEV_SEG_REN_)
                partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["internoCastello1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["internoCastello21"]:
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello1"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRodArrivoAlCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0215_01_Tu_QUE__SAN_CHE__SUC_QUI_)
                partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 1:
                if GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1138_01_Tu_SE_HO_CAP_BEN_DOV_ESS_NEL_DI_NEI_ADE_)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1139_01_Tu_QUE_SOL_SI__MES_PRO_DAV_ALL_POR_E_NON_MI_FA_PAS_)
                    partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello2"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRodNotatoSangueNelCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0216_01_Tu_OH_IL_PIA_ASC__APE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoImpossibilitaRaggiungereInFrettaUfficioDiNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0217_01_Tu_AH_ASPETTA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0217_02_Tu_EHM_EHM_MOV_SPA_IN_IN_STA_IN_CUI_NEI_IN_CUI_NEI_FA_)
                partiDialogo.append(dialogo)
            elif (x == GlobalHWVar.gpx * 13 or x == GlobalHWVar.gpx * 14) and y == GlobalHWVar.gpy * 15:
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostAttraversamentoPortachiusaLaboratorio2"]:
                    oggettoDato = False
                    avanzaStoria = True
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0218_01_Tu_CAV_NON_POS_AZI_IL_PIA_ASC_ADE_)
                    partiDialogo.append(dialogo)
                elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1140_01_Tu_VOG_VED_COS_FA_NEI_ADE_)
                    partiDialogo.append(dialogo)
                elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1141_01_Tu_DEV_SEG_REN_)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1142_01_Tu_NON_SI_APR_)
                    partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 1 or y == GlobalHWVar.gpy * 1 or y == GlobalHWVar.gpy * 16:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1143_01_Tu_VOG_VED_COS_FA_NEI_ADE_)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1144_01_Tu_DEV_SEG_REN_)
                    partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello3"]:
            if x == GlobalHWVar.gpx * 29 and y == GlobalHWVar.gpy * 12:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif (x == GlobalHWVar.gpx * 25 and y == GlobalHWVar.gpy * 5) or (x == GlobalHWVar.gpx * 25 and y == GlobalHWVar.gpy * 7):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello4"]:
            if x == GlobalHWVar.gpx * 19 and y == GlobalHWVar.gpy * 2:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello5"]:
            if x == GlobalHWVar.gpx * 5 and y == GlobalHWVar.gpy * 4:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 23 and y == GlobalHWVar.gpy * 2:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 23 and y == GlobalHWVar.gpy * 14:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 28 and y == GlobalHWVar.gpy * 14:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif (x == GlobalHWVar.gpx * 24 and y == GlobalHWVar.gpy * 4) or (x == GlobalHWVar.gpx * 26 and y == GlobalHWVar.gpy * 4):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello7"]:
            if x == GlobalHWVar.gpx * 27 and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["guardiaCastelloChiusoPortaLibreriaInternoCastello18"] and x == GlobalHWVar.gpx * 25:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0219_01_Tu__QUI_CHE_CIO__PER_ME_QUE_POS_A_TAV_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSalaDaPranzoCastello"] and ((x == GlobalHWVar.gpx * 1) or (x == GlobalHWVar.gpx * 30) or (y == GlobalHWVar.gpy * 1) or (y == GlobalHWVar.gpy * 16)):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1145_01_Tu_MI_STA_VEN_MAL_DI_TES_PER_LA_FAM_POI_QUE_SOL_HA_DET_CHE_LA_CEN__SER_AL_PRI_PIA_E_QUE__IL_PRI_PIA_QUI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioCenaAlCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0220_01_Tu__OK_MAN_QUA_E_VAD_A_LET_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0220_02_Tu__ANC_SE_NON_HO_VIS_LET_IN_GIR_POT_DOR_SU_UNO_DI_QUE_DIV_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0220_03_Tu__CHI_AI_SOL_NON_CRE_SER_A_QUA_STA_FER_IMM_TUT_IL_TEM_SEN_EME_UN_FIA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0220_04_Tu__QUE_L_SEM_SEM_FIS_QUA_NON_LO_GUA_A_COS_STA_PEN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0220_05_Tu__A_QUA_STA_SIC_PEN_IL_PEN__FON_PER_LA_VIT_NO_SE_UN_ESS_NON_PEN_NON_LO_SI_PU_DEF_VIV_GIU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0220_06_Tu__ODD_FOR_NON_SON_VIV_MA_LI_HO_VIS_MUO_PER_FAR_DEI_MOV_DEV_PRI_PEN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0220_07_Tu__NO_ASP_NON_TUT_I_MOV_CHE_FAC_LI_PEN_PRI_ALC_LI_FAC_SEN_PEN_QUI_ANC_NON_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0220_08_Tu__OK_NON_IMP_DEV_MAN_QUE_BRO_ADE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoCenaAlCastello1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0221_01_Tu__QUE_BRO_NON_SA_DI_NIE_NON_ODO_DI_NIE_SEM_ARI__FRE_SA_DI_ARI_FRE_FRE_COM_QUE_CAS_COM_QUE_PER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0221_02_Tu__NON_C_NUT_IN_QUE_BRO_COM_NON_C_VIT_IN_QUE_PER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0221_03_Tu__CON_A_FIS_QUA_NON_LI_GUA_DOV_PRO_A_PRE_DI_SOR_DOV_PRO_A_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoCenaAlCastello2"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0222_01_Tu_WAAA_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["urloDuranteCenaAlCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0223_01_Tu_ODD_LHO_FAT_DAV_NON_SI_SON_MOS_COM_SE_NON_FOS_SUC_NUL_RIM_IMM_NON_REA_AGL_STI_EST_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0223_02_Tu__NON_SEM_NEA_PRE_DEL_MIO_URL_FOL_SEM_CHE_SE_LO_ASP_NON_SON_SOR_NEA_UN_PO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0223_03_Tu__CAV_MI_SEN_GI_SAZ_NE_HO_MAN_SOL_UN_CUC_COS_PEN_SE_NON_FIN_DI_MAN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0223_04_Tu__NIE_NON_PEN_NIE_NON_MI_CON_NEA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0223_05_Tu__ODD_MI_STA_APP_UN_SAC_MEG_SME_QUI_OH_CAV_MI_STA_VEN_SON_MI_SI_CHI_GLI_OCC_HAN_MES_QUA_IN_QUE_BRO_LO_SAP_CHE_NON_DOV_FID_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0223_06_Tu__OK_CAL_CAL_NON_AVR_SEN_DRO__SOL_UN_PAS_PES_E_MI_STO_ABB_UN_PAS_DAR_FRE_INA_PES_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0223_07_Tu__CAZ_NON_RIE_A_TEN_GLI_OCC_APE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0223_08_Tu__DEV_DEV_FAR_DUE_PAS_)
                partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 1 or x == GlobalHWVar.gpx * 1 or y == GlobalHWVar.gpy * 16 or x == GlobalHWVar.gpx * 30:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1146_01_Tu_VOG_VED_COS_FA_NEI_ADE_)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1147_01_Tu_DEV_SEG_REN_)
                    partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello8"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRiconosciutoIngressoVulcano3"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0224_01_Tu_OH_QUE_POR_NON_ERA_APE_PRI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["giratoPostIndecisoSuComeAttraversarePortaLaboratorio"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0225_01_Tu_OH_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostAttraversamentoPortachiusaLaboratorio1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0226_01_Tu__OK_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoNotatoDiPoterCapireGliAppuntiDiNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0227_01_Tu__)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 6 and y == GlobalHWVar.gpy * 15:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 7 and y == GlobalHWVar.gpy * 8:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 22 and y == GlobalHWVar.gpy * 4:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1148_01_Tu_NON_SI_APR_DEV_QUA_QUA_SOT_)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1149_01_Tu_DEV_SEG_REN_)
                    partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1150_01_Tu_VOG_VED_COS_FA_NEI_ADE_)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 16 and (y == GlobalHWVar.gpy * 13 or y == GlobalHWVar.gpy * 14 or y == GlobalHWVar.gpy * 15):
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1151_01_Tu_VOG_VED_COS_FA_NEI_ADE_)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1152_01_Tu_DEV_SEG_REN_)
                    partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello9"]:
            if x == GlobalHWVar.gpx * 7 and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"]:
                    dialogo.append(LDS._1153_01_Tu_LA_CHI_NON_GIR_DEV_PRO_UNA_POR_)
                else:
                    dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 18 and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"]:
                    dialogo.append(LDS._1154_01_Tu_LA_CHI_NON_GIR_DEV_PRO_UNA_POR_)
                else:
                    dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 23 and y == GlobalHWVar.gpy * 13:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"]:
                    dialogo.append(LDS._1155_01_Tu_LA_CHI_NON_GIR_DEV_PRO_UNA_POR_)
                else:
                    dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif (x == GlobalHWVar.gpx * 30) or (x == GlobalHWVar.gpx * 7 and (y == GlobalHWVar.gpy * 12 or y == GlobalHWVar.gpy * 13 or y == GlobalHWVar.gpy * 14)):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dormitoNelCastello"]:
                    dialogo.append(LDS._1156_01_Tu_NON_MI_REG_IN_PIE_LA_MIA_STA_DOV_ESS_SU_QUE_PIA_)
                else:
                    dialogo.append(LDS._1156_02_Tu_PEN_CHE_NEI_SIA_DI_SOP_DOV_MI_HAN_FER_IER_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["servoLanciaUscitoDaSalaPranzoCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0228_01_Tu_QUE__IL_SEC_PIA_MA_NON_SO_QUA_SIA_LA_STA_DEV_TRO_PRI_DI_CRO_DAL_SON_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostAttraversamentoPortachiusaLaboratorio2"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0229_01_Tu_OH_NO_TUT_QUE_SCA_DI_NUO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoImpossibilitaRaggiungereInFrettaUfficioDiNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0230_01_Tu_AH_ASPETTA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0230_02_Tu_EHM_EHM_MOV_SPA_IN_IN_STA_IN_CUI_NEI_IN_CUI_NEI_FA_)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello10"]:
            if x == GlobalHWVar.gpx * 12 and y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"]:
                    dialogo.append(LDS._1157_01_Tu_LA_CHI_NON_GIR_DEV_PRO_UNA_POR_)
                else:
                    dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 14 and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"]:
                    dialogo.append(LDS._1158_01_Tu_LA_CHI_NON_GIR_DEV_PRO_UNA_POR_)
                else:
                    dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 20 and y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"]:
                    dialogo.append(LDS._1159_01_Tu_LA_CHI_NON_GIR_DEV_PRO_UNA_POR_)
                else:
                    dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 26 and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"]:
                    dialogo.append(LDS._1160_01_Tu_LA_CHI_NON_GIR_DEV_PRO_UNA_POR_)
                else:
                    dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0231_01_Tu_TROVATA_)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 9 and y == GlobalHWVar.gpy * 5:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dormitoNelCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0232_01_Tu__UH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0232_02_Tu__MA_QUA_HO_DOR_CHE_ORE_SON_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["alzatoDalLettoNelCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0233_01_Tu__NON_CAP_SE__GIO_O_SE__ANC_NOT_IN_QUE_POS_CI_SON_POC_FIN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0233_02_Tu__ORA_CHE_CI_PEN_COM_ARR_LA_LUC_IN_QUE_STA_I_CAN_SON_SEM_SPE_E_NON_CI_SON_OMB_)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello11"]:
            if x == GlobalHWVar.gpx * 1 and y == GlobalHWVar.gpy * 3:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"]:
                    dialogo.append(LDS._1161_01_Tu_LA_CHI_NON_GIR_DEV_PRO_UNA_POR_)
                else:
                    dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 9 and y == GlobalHWVar.gpy * 10:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"]:
                    dialogo.append(LDS._1162_01_Tu_LA_CHI_NON_GIR_DEV_PRO_UNA_POR_)
                else:
                    dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 22 and y == GlobalHWVar.gpy * 10:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"]:
                    dialogo.append(LDS._1163_01_Tu_LA_CHI_NON_GIR_DEV_PRO_UNA_POR_)
                else:
                    dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 30 and y == GlobalHWVar.gpy * 3:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"]:
                    dialogo.append(LDS._1164_01_Tu_LA_CHI_NON_GIR_DEV_PRO_UNA_POR_)
                else:
                    dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello12"]:
            if x == GlobalHWVar.gpx * 4 and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 13 and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 22 and y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 30 and y == GlobalHWVar.gpy * 3:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 30 and y == GlobalHWVar.gpy * 11:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello13"]:
            if x == GlobalHWVar.gpx * 5 and y == GlobalHWVar.gpy * 8:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 13 and y == GlobalHWVar.gpy * 15:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 20 and y == GlobalHWVar.gpy * 2:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 30 and y == GlobalHWVar.gpy * 5:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello14"]:
            if x == GlobalHWVar.gpx * 6 and y == GlobalHWVar.gpy * 14:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 16 and y == GlobalHWVar.gpy * 6:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 22 and y == GlobalHWVar.gpy * 13:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello15"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoAlzatoDalLettoNelCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0234_01_Tu__NON_CE_LA_FAC_PI_CON_TUT_QUE_SCA_CHE_SEN_HA_ABI_IN_UN_POS_COS_GRA_)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 2 and y == GlobalHWVar.gpy * 4:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 7 and y == GlobalHWVar.gpy * 12:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 9 and y == GlobalHWVar.gpy * 2:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 18 and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 18 and y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 27 and y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 30 and y == GlobalHWVar.gpy * 12:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello16"]:
            if x == GlobalHWVar.gpx * 5 and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 7 and y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 18 and y == GlobalHWVar.gpy * 9:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 20 and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif (x == GlobalHWVar.gpx * 16 and y == GlobalHWVar.gpy * 4) or (x == GlobalHWVar.gpx * 16 and y == GlobalHWVar.gpy * 6):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif (x == GlobalHWVar.gpx * 8 and y == GlobalHWVar.gpy * 5) or (x == GlobalHWVar.gpx * 8 and y == GlobalHWVar.gpy * 7):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello17"]:
            if x == GlobalHWVar.gpx * 1 and y == GlobalHWVar.gpy * 10:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 4 and y == GlobalHWVar.gpy * 3:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 12 and y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 15 and y == GlobalHWVar.gpy * 14:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 16 and y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif (x == GlobalHWVar.gpx * 9 and y == GlobalHWVar.gpy * 3) or (x == GlobalHWVar.gpx * 7 and y == GlobalHWVar.gpy * 3):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello18"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoStanza15CastelloSecondaVolta"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0235_01_Tu__APE_ADE_)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 18 and y == GlobalHWVar.gpy * 12:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1165_01_Tu_NON_SI_APR_QUE_SOL_HA_PRE_IMP_E_SI__CHI_LA_POR_ALL_SPA_HA_DET_CHE_LA_CEN__SER_AL_PRI_PIA_)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 30 and y == GlobalHWVar.gpy * 11:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["riletturaLibroNeilSulTempo"] and x == GlobalHWVar.gpx * 26 and (y == GlobalHWVar.gpy * 6 or y == GlobalHWVar.gpy * 7 or y == GlobalHWVar.gpy * 8):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1166_01_Tu_DEV_RIL_UN_ATT_QUE_LIB_DI_NEI_SUL_TEM_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoApprofondimentoParadossiTempoBloccato"] and x == GlobalHWVar.gpx * 26 and (y == GlobalHWVar.gpy * 6 or y == GlobalHWVar.gpy * 7 or y == GlobalHWVar.gpy * 8):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1167_01_Tu_PRE_IL_PIA_ASC_)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello19"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRipresoImpoDaNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0236_01_Tu_OK_NEI__CRE_CHE_ABB_FAT_TUT_LE_OPE_DES_IN_QUE_LIB_DIR_SU_SE_STE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoUscitaStudioDiNeil"] and y == GlobalHWVar.gpy * 8:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0237_01_Tu_OH__QUE_IL_PIA_ASC_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoDaInternoCastello21ConRod"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0238_01_Tu__)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoPostLetturaAppuntiNeilSuRatti"] and (y == GlobalHWVar.gpy * 1 or ((x == GlobalHWVar.gpx * 10 or x == GlobalHWVar.gpx * 11) and y == GlobalHWVar.gpy * 3)):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1168_01_Tu_FOR_NEL_STA_IN_CUI_MI_SON_RIS_POS_TRO_QUA_CHE_MI_AIU_A_CAP_COS_SUC_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["NeilUscitoDaUfficioPostAvvioSequenzaNelCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0239_01_Tu_ASP_ASP_STO_FER_FER_SEQ_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoStopTempoPreAscensoreDiNeilMentreSeiNelCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0240_01_Tu_OK_OK_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0240_02_Tu__POS_PRE_IL_PIA_ASC_CON_LUI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostStopTempoPreAscensoreDiNeilMentreSeiNelCalcolatore"] and x == GlobalHWVar.gpx * 10 and y == GlobalHWVar.gpy * 4:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0241_01_Tu_VA_BEN_UHM_AVV_SEQ_)
                partiDialogo.append(dialogo)
            elif (x == GlobalHWVar.gpx * 10 or x == GlobalHWVar.gpx * 11) and y == GlobalHWVar.gpy * 3:
                if GlobalGameVar.dictAvanzamentoStoria["lettoAppuntiNeilSuRatti"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["riletturaLibroNeilSulTempo"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1169_01_Tu_DEV_RIL_UN_ATT_QUE_LIB_DI_NEI_SUL_TEM_)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1170_01_Tu_NON_SI_APR_)
                    partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 15 and y == GlobalHWVar.gpy * 16:
                if GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1171_01_Tu_VOG_VED_COS_FA_NEI_ADE_)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(frasePortaChiusa)
                    partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 25 and y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 30 and y == GlobalHWVar.gpy * 13:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1172_01_Tu_DEV_ASP_CHE_MI_CHI_POT_LEG_QUA_NEL_FRA_)
                    partiDialogo.append(dialogo)
                elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1173_01_Tu_VOG_VED_COS_FA_NEI_ADE_)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1174_01_Tu_NON_VOG_TOR_IND_)
                    partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1175_01_Tu_VOG_VED_COS_FA_NEI_ADE_)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello20"]:
            if x == GlobalHWVar.gpx * 1 and y == GlobalHWVar.gpy * 4:
                if GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["avviatoSequenzaDiEventiCalcolatore"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1176_01_Tu_DOV_ESS_SU_UN_TAV_IN_QUE_STA_)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1177_01_Tu_DEV_PAR_CON_NEI_ADE_)
                    partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["apertoPortaStanza19CastelloVerso20"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0242_01_Tu__UN_COR_NON_SO_PER_MA_CRE_SIA_CHI_QUA_SIA_LA_POR_DA_APR_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoInternoCastello20"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0243_01_Tu_OH_FOR_AVR_DOV_BUS_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["primoDialogoNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0244_01_Tu_ODD_LA_SUA_FAC_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["voltatoBibliotecarioDopoIlDialogoPostRianimazione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0245_01_Tu__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0246_01_Tu__UH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0246_02_Tu__MA_CHE_CAV_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0246_03_Tu_OH_POS_POS_MUO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPrimoComandoViaggioRapidoCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0247_01_Tu_MA_NON_AVE_ANC_FIN_DI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["viaggioRapidoCalcolatore1UfficioNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0248_01_Tu_OH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0248_02_Tu__QUI_VA_BEN_QUI_VA_BEN_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["interagitoConTeNelCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0249_01_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0249_02_Tu_MA_RIM_QUI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPreAvvioSequenzaEventiCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0250_01_Tu_AH_FOR_DEV_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0250_02_Tu_UHM_AVVIA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0250_03_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0250_04_Tu__AVV_EVE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0250_05_Tu__PRO_PRO_EVE_PRO_SEQ_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["avviatoSequenzaDiEventiCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0251_01_Tu_OH_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["RenéUscitoDallUfficioDiNeilPostAvvioSequenzaDiEventiCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0252_01_Tu__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostUscitaDiRenéPostAvvioSequenzaDiEventiCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0253_01_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0253_02_Tu_UHM_RREGREDISCI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0253_03_Tu_REG_DIE_MIN_)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 20 and y == GlobalHWVar.gpy * 2:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 26 and y == GlobalHWVar.gpy * 4:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 16 and y == GlobalHWVar.gpy * 9:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 10 and y == GlobalHWVar.gpy * 5:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1178_01_Tu_NON_VOG_TOR_IND_)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello21"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["risveglioSaraResuscitata"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0254_01_Tu_UH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0254_02_Tu_ODD_MA_CHE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["alzataDalTavoloLaboratorioCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0255_01_Tu_AHI_GLI_OCC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0255_02_Tu_LE_MIE_MAN_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoSpecchioPostRianimazione3"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0259_01_Tu__OK_OK_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0259_02_Tu__CALMA_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoConSoldatoPostRianimazione1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0261_01_Tu__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["lettoAppuntiNeilSuRatti"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0262_01_Tu__)
                partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["scorciatoiaLabirinto1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["scorciatoiaLabirinto2"]:
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["scorciatoiaLabirinto1"]:
            if x == GlobalHWVar.gpx * 30:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1179_01_Tu_DEV_SEG_REN_)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["scorciatoiaLabirinto2"]:
            if y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1180_01_Tu_DEV_SEG_REN_)
                partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["palazzoDiRod1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["palazzoDiRod5"]:
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["palazzoDiRod1"]:
            if y == GlobalHWVar.gpy * 4:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1181_01_Tu_UNA_GRO_BLO_DA_DEL_SBA_)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1182_01_Tu_FOR_DA_QUI_SI_RAG_LIN_DEL_MON_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1182_02_Tu_QUE_SBA_LE_HA_MES_SIC_ROD_DEV_UNA_LEV_DA_QUA_PAR_)
                    partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["palazzoDiRod2"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0263_01_Tu__NON_HAN_UN_CER_COM_POS_PEN_FOR_NON_NE_HAN_BIS_USA_GLI_IMP_PER_QUE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0263_02_Tu__GLI_IMP_SON_DEI_PEN_GI_COM_MA_COM_DA_CHI_NES_SPE_ANI_LI_USA_O_LI_PRO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0263_03_Tu__NES_SPE_ANI_HA_QUA_IN_COM_CON_GLI_IMP_NES_SPE_CON_QUA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0263_04_Tu__MAG_NON_SON_GLI_UNI_A_VIV_NEL_CAV_CHI_PRO_GLI_IMP_MAG_VIV_CON_LOR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0263_05_Tu__VI_POS_DIR_PER_CER_CHE_SON_VIV_CHI_GLI_MAT_I_PEN_PRO_LO__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0263_06_Tu__QUA_ABB_INT_PER_FAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0263_07_Tu__UN_UMA_CHE_SIA_OPE_DEL_NEM_VOR_DIR_CHE_STA_COS_DEI_TUN_PER_ATT_LA_CAT_MON_E_ATT_DA_OVE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0263_08_Tu__MA_SON_ANN_CHE_ESI_QUE_CAV_PER_AVR_DOV_ASP_COS_TAN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0263_09_Tu__FOR_STO_AND_FUO_STR_OGN_VOL_CHE_CI_PEN_FIN_PER_PER_UN_SAC_DI_TEM_DEV_FIN_LAR_E_AND_L_DEN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0263_10_Tu__IL_TEM_NON__CER_DAL_MIA_PAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0263_11_Tu__LA_NUO_REC__RIU_AD_AVE_UN_IMP_ANC_VIV_MA_HA_DEC_BEN_DI_COL_CON_NEI_E_NEI_GIU_PRE_ALL_MIE_STE_SCO_TUT_I_MIE_PRO_E_I_MIE_STU_DIV_IMM_OBS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0263_12_Tu__E_COS_RIS_ENT_IN_QUE_MAL_GRO_PER_STO_FAC_TUT_QUE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0263_13_Tu__SME_NON__CER_IL_MOM_DI_DUB_QUE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0263_14_Tu__DEV_REC_QUA_CHE_POS_AIU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0263_15_Tu__COM_SE_FOS_FAC_TRO_QUA_TAN_INC_CHE_VOG_ANC_SOL_ATT_IL_PAS_MON_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0263_16_Tu__LUL_VOL_CHE_QUA__VEN_QUA_SU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0263_17_Tu__ASPETTA_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRodSuImpoNonVivi"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0264_01_Tu_SARA_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRodCercandoSaraAlPalazzo1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0265_01_Tu__SARA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0265_02_Tu_SE_N_GI_AND_)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 13 and y == GlobalHWVar.gpy * 8:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 16:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presiStrumentiPerStudiareImpo"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1183_01_Tu_DEV_PRE_GLI_STR_PRI_DI_AND_)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1184_01_Tu__BLO_DEV_CHI_A_ROD_DI_APR_)
                    partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 1:
                if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1185_01_Tu_FAC_PRI_PAS_DAL_TUN_)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1186_01_Tu_POS_USA_IL_TUN_DI_ROD_PER_TOR_)
                    partiDialogo.append(dialogo)
            elif (x == GlobalHWVar.gpx * 7 and (y == GlobalHWVar.gpy * 3 or y == GlobalHWVar.gpy * 4)) or ((x == GlobalHWVar.gpx * 4 or x == GlobalHWVar.gpx * 5) and y == GlobalHWVar.gpy * 11):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1187_01_Tu_NON_VOG_PER_TEM_DEV_PAR_CON_SAR_ADE_)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["palazzoDiRod3"]:
            if (x == GlobalHWVar.gpx * 12 and y == GlobalHWVar.gpy * 5) or (x == GlobalHWVar.gpx * 21 and y == GlobalHWVar.gpy * 12):
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["palazzoDiRod4"]:
            if x == GlobalHWVar.gpx * 16 and y == GlobalHWVar.gpy * 4:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(frasePortaChiusa)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["palazzoDiRod5"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRodCercandoSaraAlPalazzo2"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0266_01_Tu_FOR_RIE_A_RAG_PRI_CHE_ARR_DA_NEI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRenéRod2PreLancioMissile"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0267_01_Tu__VA_BEN_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRenéRod3PreLancioMissile"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0268_01_Tu__IMMAGINAVO_)
                partiDialogo.append(dialogo)
            elif (x == GlobalHWVar.gpx * 14 and y == GlobalHWVar.gpy * 4) or y == GlobalHWVar.gpy * 13:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1188_01_Tu_DEV_SEG_REN_)
                partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["tunnelDiRod1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["tunnelDiRod3"]:
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["tunnelDiRod1"]:
            if y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1189_01_Tu_DEV_SEG_REN_)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["tunnelDiRod2"]:
            if y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1190_01_Tu_DEV_SEG_REN_)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["tunnelDiRod3"]:
            if y == GlobalHWVar.gpy * 16:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1191_01_Tu_C_LAV_DI_ROD_DAL_PAR_DEV_CAP_COM_ABB_QUE_SBA_)
                    partiDialogo.append(dialogo)
                elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1192_01_Tu_DEV_SEG_REN_)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1193_01_Tu_DEV_TIR_LA_LEV_SE_VOG_PAS_)
                    partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["caverna1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["caverna18"]:
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["caverna18"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoVistoImpoNonOstili2"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0269_01_Tu_MA_QUESTO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRiconosciutoIngressoVulcano1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0270_01_Tu__DA_QUI_CI_SIA_VEN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0270_02_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0270_03_Tu__QUI_CHE_FAC_ADE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0270_04_Tu__CHE_SON_VEN_A_FAR_QUA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0270_05_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0270_06_Tu__UFF_PER_NON_CAP_NIE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRiconosciutoIngressoVulcano2"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0271_01_Tu__NEIL_)
                partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["vulcano1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["vulcano3"]:
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["vulcano1"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["interagitoConComputerVulcano"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0272_01_Tu_NON_NON_CI_ATT_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoVistoImpoNonOstili1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0273_01_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0273_02_Tu_CI_STA_IGN_)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["vulcano2"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["interazioneCellaCostruttore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0274_01_Tu_OH_WOW_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0274_02_Tu___UN_MAR_INC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0274_03_Tu_E_SUL_QUE_MAS_)
                partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 16:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1194_01_Tu_C_SCR_QUA_SUL_QUE_MAS_)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["vulcano3"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["risvegliatoNelVulcano"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0275_01_Tu_UH_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoImpoPostRisveglioVulcano"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0276_01_Tu__SON_VIV_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo1PostRisveglioNelVulcano"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0277_01_Tu__COS_QUE_POS_)
                partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["tunnelSubacqueo1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["tunnelSubacqueo2"]:
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["tunnelSubacqueo1"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoVistoIngressoTunnelSubaqueoAperto"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0278_01_Tu__QUE__IL_LAG_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0278_02_Tu__SIA_SUL_FON_DEL_LAG_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostApparizioneStanzaNelCalcolatore3"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0279_01_Tu_LA_PORTA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0279_02_Tu___CHI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoVistoPortaLaboratorioAggiustata"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0280_01_Tu__E_ADE_COM_)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 1:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["arrivatoRenéNelTunnelSubacqueo1"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1195_01_Tu_VOG_VED_COS_FA_NEI_ADE_)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1196_01_Tu__DOV_VA_REN_)
                    partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 30:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1197_01_Tu_DEV_SEG_REN_)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["tunnelSubacqueo2"]:
            if x == GlobalHWVar.gpx * 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1198_01_Tu_VOG_VED_COS_FA_NEI_ADE_)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 30:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1199_01_Tu_DEV_SEG_REN_)
                partiDialogo.append(dialogo)
    elif GlobalGameVar.dictStanze["laboratorioSegretoNeil1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoTunnelSubacqueo"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0281_01_Tu_OH_UN_LAB_SEG_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoLaboratorioNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0282_01_Tu__NEIL_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sedutaSulCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0283_01_Tu__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["messoCascoCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0284_01_Tu_QUE__LO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0284_02_Tu__CER_SCR_OCC_PAR_E_CHI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["chiusoGliOcchiSulCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0285_01_Tu_E_UHM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0285_02_Tu__NAVIGAZIONE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["apparizioneNelCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0286_01_Tu__UHM_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["apparizioneStanzaNelCalcolatore"]:
                nome = LI.VOCE_SCONOSCIUTA
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0287_01_VoceSconosciuta_MOM_SER_DI_EVE_ATT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0287_02_Tu_OH_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sentitoVoceCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0288_01_Tu_SON_NEL_LAB_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostApparizioneStanzaNelCalcolatore1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0289_01_Tu_MA_MO_SER_DI_EVE_ATT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0289_02_Tu_FOR_SI_RIF_AGL_EVE_NOR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0289_03_Tu__SE__COS_DOV_ESS_NEL_DI_NEI_ERO_L_PRI_CHE_IL_TEM_SI_BLO_SDR_SU_UN_TAV_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostApparizioneStanzaNelCalcolatore2"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0290_01_Tu_MA_NON_FAC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0290_02_Tu_ODD_SON_TRA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0290_03_Tu_NON_FAC_NES_RUM_QUI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["NeilUscitoDaTunnelSubaqueo2PostAvvioSequenzaNelCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0291_01_Tu__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoLaboratorioDiNeilDelPassato1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0292_01_Tu__NON_ERA_COS_PRI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["riavviatoSottofondoAmbientalePostTrasformazioneLaboratorio"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0293_01_Tu_OH_CAVOLO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoCellaNeilPostTrasformazioneLaboratorio1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0294_01_Tu__LHA_COS_MEN_ERA_BLO_NEL_TEM_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoCellaNeilPostTrasformazioneLaboratorio2"]:
                nome = LI.VOCE_SCONOSCIUTA
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0295_01_Tu__CHE_SUC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0295_02_VoceSconosciuta_MOM_ATT_RAG_PRO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0295_03_Tu__UHM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0295_04_VoceSconosciuta__MOM_ATT_RAG_PRO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0295_05_Tu_SS_S_PRO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sparitoNeilDallaCellaDelLaboratorio"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0296_01_Tu__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo1PostScomparsaNeilDallaCella"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0297_01_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0297_02_Tu__OK_UHM_REG_DIE_SEC_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroNelTempo10SecInLaboratorio"]:
                nome = LI.VOCE_SCONOSCIUTA
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0298_01_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0298_02_VoceSconosciuta_MOM_ATT_RAG_PRO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0298_03_Tu__S_PRO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostTornatoIndietroNelTempo10SecInLaboratorio"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0299_01_Tu__SPARITO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sparitoNeilDallaCellaDelLaboratorioSecondaVolta"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0300_01_Tu__SPA_COM_ME_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0300_02_Tu__E_NEL_STE_MOM_IL_MOM_ATT_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo1PostSecondaSparizioneDiNeilDalLaboratorio"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0301_01_Tu__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sedutoSulCalcolatoreRenéNelLaboratorioDiNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0302_01_Tu__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoAttesaRenéSulCalcolatore2"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0303_01_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0303_02_Tu__PRO_DIE_MIN_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoDieciMinAspettandoRenéSulCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0304_01_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0304_02_Tu__PRO_UNO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoUnOraAspettandoRenéSulCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0305_01_Tu_PRO_DUE_ORE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoDueOreAspettandoRenéSulCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0306_01_Tu_PRO_CIN_ORE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoCinqueOreAspettandoRenéSulCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0307_01_Tu__PRO_UN_GIO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoUnGiornoAspettandoRenéSulCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0308_01_Tu_PRO_TRE_GIO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoTreGiorniAspettandoRenéSulCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0309_01_Tu_PRO_UN_MES_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoUnMeseAspettandoRenéSulCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0310_01_Tu_PRO_CIN_MES_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoCinqueMesiAspettandoRenéSulCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0311_01_Tu_PRO_UN_ANN_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoUnAnnoAspettandoRenéSulCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0312_01_Tu_PRO_CIN_ANN_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoCinqueAnniAspettandoRenéSulCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0313_01_Tu_PRO_DIE_ANN_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroDieciAnniAspettandoRenéSulCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0314_01_Tu__OOK_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0314_02_Tu__PRO_UN_ANN_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoUnAnno1AspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0315_01_Tu__PRO_UN_ANN_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroSeiMesiAspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0316_01_Tu__OK_ADE_AVA_DI_UN_MES_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoUnMese1AspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0317_01_Tu_AVA_UN_MES_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroDieciGiorniAspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0318_01_Tu_AVA_UN_GIO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoUnGiornoAspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0319_01_Tu_OH_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoNotatoRenéScomparsoDalCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0320_01_Tu_OK_UHM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0320_02_Tu__IND_CIN_ORE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroCinqueOreAspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0321_01_Tu_OK_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0321_02_Tu__AVA_DUE_ORE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoDueOreAspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0322_01_Tu_AVANTI_UNORA_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoUnOra1AspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0323_01_Tu_AVANTI_UNORA_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoUnOra2AspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0324_01_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0324_02_Tu__AVA_UNO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoUnOra3AspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0325_01_Tu_AV_OH_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoNotatoAssenzaRenéCalcolatore2"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0326_01_Tu__IND_DIE_MIN_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroDieciMinutiAspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0327_01_Tu_AVA_UN_MIN_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["rialzataDalCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0328_01_Tu__HO_BIS_DI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0328_02_Tu__DORMIRE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostPassatiMoltiAnniSulCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0329_01_Tu_QUE_ROB_NON__INC_ADE_)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 1:
                if GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1200_01_Tu_NON_VOG_AND_PRI_VOG_CAP_COS_SUC_A_QUE_POS_)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1201_01_Tu_CRE_CI_SIA_ALT_COS_INT_QUA_)
                    partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["stanzaEsplosa"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoDieciAnniAspettandoRenéSulCalcolatore"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0330_01_Tu__)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo1NotatoTuttoDistruttoDopoDieciAnniDiAttesaPerRené"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0331_01_Tu__INI_TOR_IND_DIE_ANN_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["aggiornatoStanzaPerDistruzioneDelMondo2"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0332_01_Tu__TOR_IND_IND_DI_SEI_MES_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["aggiornatoStanzaPerDistruzioneDelMondo3"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0333_01_Tu__IND_QUI_GIO_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroQuindiciGiorniAspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0334_01_Tu__IND_DIE_GIO_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["conclusioneAnimazioneDistruzionePostScoppioMissile"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0335_01_Tu__)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostFineDelMondo1"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0336_01_Tu_VVA_A_CAS_MIA_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["andatoACasaPerVedereLoScoppioDelMissile"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0337_01_Tu_TORNA_INDIETRO_)
            partiDialogo.append(dialogo)
    else:
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(LDS._1202_01_Tu__)
        partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo


