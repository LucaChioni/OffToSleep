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
        if tipo == "TartarugaVerde":
            nome = LI.TARTARUGA_VERDE
        elif tipo == "TartarugaMarrone":
            nome = LI.TARTARUGA_MARRONE
        elif tipo == "LupoGrigio":
            nome = LI.LUPO_GRIGIO
        elif tipo == "LupoBianco":
            nome = LI.LUPO_BIANCO
        elif tipo == "LupoNero":
            nome = LI.LUPO_NERO
        elif tipo == "Cinghiale":
            nome = LI.CINGHIALE
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDS._0820_01_Cinghiale__)
        partiDialogo.append(dialogo)
    elif tipo.startswith("OggettoDict"):
        partiDialogo = []
        if tipo.startswith("OggettoDictCadavereTartarugaVerde"):
            nome = LI.TARTARUGA_VERDE
        elif tipo.startswith("OggettoDictCadavereTartarugaMarrone"):
            nome = LI.TARTARUGA_MARRONE
        elif tipo.startswith("OggettoDictCadavereLupoGrigio"):
            nome = LI.LUPO_GRIGIO
        elif tipo.startswith("OggettoDictCadavereLupoBianco"):
            nome = LI.LUPO_BIANCO
        elif tipo.startswith("OggettoDictCadavereLupoNero"):
            nome = LI.LUPO_NERO
        elif tipo.startswith("OggettoDictCadavereCinghiale"):
            nome = LI.CINGHIALE
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = True
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDS._0821_01_Cinghiale__)
        partiDialogo.append(dialogo)
    elif tipo == "OggettoSiepe":
        partiDialogo = []
        nome = "OggettoSiepe"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and avanzamentoDialogo == 0:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0092_01_Tu__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0092_02_Tu_QUE_CIN_STA_FAC_DEG_STR_LAM_E_STA_PER_MOL_SAN_MA_CRE_CHE_MI_ATT_SE_LO_LIB_QUI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0092_03_Tu__MAG_RIU_A_CAV_IN_QUA_MOD_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and avanzamentoDialogo == 1:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0822_01_Tu__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0822_02_Tu_MI_ATT_SE_LO_LIB_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoForestaSognoCastello"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0093_01_Tu_IMPO_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0823_01_Tu__)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0824_01_Tu_QUE_CIN_NON__RIU_A_LIB_ALM_HA_SME_DI_FAR_QUE_STR_LAM_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0825_01_Tu_UN_CIN_MEZ_MAN_DA_ALT_ANI_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0826_01_Tu_IL_COR__GI_IN_DEC_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoFuoco":
        partiDialogo = []
        nome = "OggettoFuoco"
        if avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["tutorialRecuperoPvDifesa"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0827_01_Tu_SEM_ALL_PER_FAR_UN_PIC_FAL_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0828_01_Tu_QUI__DOV_SAM_HA_INT_DI_ACC_IL_FUO_PER_LA_NOT_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0829_01_Tu_QUE_FAL__STA_USA_DI_REC_)
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0830_01_Tu__)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0831_01_Tu_PRO_QUE_ACC__STA_ALL_DA_QUE_SOL_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0832_01_Tu_UN_FAL_SPE_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoCibo":
        partiDialogo = []
        nome = "OggettoCibo"
        if avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["tutorialRecuperoPvDifesa"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0833_01_Tu__UNA_TAV_DI_LEG_CON_UNA_TOV_SOP_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["trovatoLegna3"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0834_01_Tu_PRE_CHE_SAM_VOG_MET_QUA_IL_CIB_CHE_RAC_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0835_01_Tu_SAM_HA_RAC_UN_BEL_PO_DI_CAR_MI_DOM_COS_ABB_CAC_LE_OSS_SEM_PIC_MA_MOL_ROB_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cadavereSamDepredato"] and avanzamentoDialogo == 0:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0094_01_Tu_QUA_SOP_C_DEL_CAR_FRE_DEL_GOC_DI_SAN_STA_ANC_COL_PER_TER_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0094_02_Tu__MA_HAN_NON_SA_CAC_CHE_CI_SIA_QUA_ALT_NEL_BOS_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0094_03_Tu_OK_OK_CAL_STA_SIC_BEN_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cadavereSamDepredato"] and avanzamentoDialogo == 1:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0836_01_Tu_C_DEL_CAR_SU_QUE_TAV_E_NON_PU_ESS_STA_HAN_A_CAC_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0837_01_Tu_CRE_CHE_SIA_STA_QUE_SOL_A_ESS_PRO_QUE_CAR_)
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0838_01_Tu__)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0839_01_Tu_QUA_ANI_DEV_DIV_TUT_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0840_01_Tu_NON_C_PI_NIE_QUA_SOP_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0841_01_Tu_UNA_TAV_DI_LEG_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoMucchioLegna":
        partiDialogo = []
        nome = "OggettoMucchioLegna"
        if avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["tutorialRecuperoPvDifesa"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0842_01_Tu__UN_MUC_DI_LEG_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["trovatoLegna2"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0843_01_Tu_NON_C_ANC_ABB_LEG_PER_LA_NOT_DEV_RAC_ALT_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["trovatoLegna3"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0095_01_Tu_OK_HO_RAC_ABB_LEG_ADE_)
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0844_01_Tu__)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0845_01_Tu__UN_MUC_DI_LEG_DA_BRU_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0846_01_Tu_UN_MUC_DI_LEG_)
            partiDialogo.append(dialogo)
    elif tipo == "FiglioUfficiale":
        partiDialogo = []
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontroFiglioUfficiale"]:
            nome = LI.SOLDATO
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0096_01_Tu_EHM_EHM_SAL_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0096_02_Soldato_UH_STA_LON_RAG_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0096_03_Tu_OK_OK_CAL_NON_VOG_CAU_PRO_SEI_UN_SOL_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0096_04_Soldato_NON_TI_CON_PRO_A_DER_RAG_SON_ARM_E_BEN_ADD_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0096_05_Tu_NO_NO_IO_CER_SOL_UN_POS_PER_ACC_CER_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0096_06_Soldato__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0096_07_Tu_MI_CHI_HAN_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0096_08_Soldato__SEI_DIS_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0096_09_Tu_S_IO_STA_STA_SOL_CER_DI_ATT_LA_FOR_PER_ARR_IN_CIT_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0096_10_Soldato__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0096_11_Tu__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0096_12_Soldato_LAC_NON__ANC_PRO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0096_13_Tu_OK_POS_POS_AIU_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0096_14_Soldato__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0096_15_Tu_UHM_POSSO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0096_16_Soldato__HO_TAG_DEL_LEG_A_EST_DI_QUI_VAI_A_RAC_E_MET_ACC_AL_FAL_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0096_17_Tu_OK_MA_TU_CHE_STA_FAC_QUI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0096_18_Soldato_IL_MIO_NOM__SAM_STO_AFF_LUL_PRO_PER_DIV_UFF_DEL_CIT_MUO_CON_LA_LEG_TRA_POC_SAR_MOL_PI_PER_IO_MI_OCC_DEL_CIB_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0096_19_Tu_OK_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["legnaDepositata"]:
            nome = "Sam"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0847_01_Tu_DOV_HAI_DET_CHE_POS_TRO_DEL_LEG_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0847_02_Sam_HO_GI_TAG_LA_LEG_A_EST_DI_QUI_DEV_SOL_PRE_E_MET_ACC_AL_FAL_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["legnaDepositata"]:
            nome = "Sam"
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0097_01_Tu_HO_POR_TUT_LA_LEG_CHE_HO_TRO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0097_02_Sam__S_DOV_BAS_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioUltimoDialogoHans"]:
            nome = "Sam"
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0098_01_Tu___BUO_QUE_CAR_CHE_COS_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0098_02_Sam__CINGHIALE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0098_03_Tu_CIN_HAN_LE_OSS_COS_PIC_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0098_04_Sam__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0098_05_Tu__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0098_06_Sam__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0098_07_Tu_EHM_EHM_DA_QUA_SEI_IN_QUE_FOR_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0098_08_Sam__CIN_GIO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0098_09_Tu_E_QUA_GIO_CI_DEV_RIM_ANC_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0098_10_Sam__NOVE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0098_11_Tu_NOV_E_COS_SUC_SE_TOR_PRI_O_SE_NON_TOR_AFF_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0098_12_Sam__NON_SUP_LA_PRO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0098_13_Tu_AH_BEH_CER_MA_SCU_SE_TE_LO_CHI_IN_QUE_GEN_DI_PRO_NON_DOV_ESS_VIE_LAI_DI_ALT_PER_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0098_14_Sam_MI__CON_SFR_TUT_CI_CHE_MI_VIE_MES_A_DIS_DAL_NAT_TU_NON_NE_FAI_PAR_RAG_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0098_15_Tu_MAH_SEN_RAG_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0098_16_Sam__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0098_17_Tu_MA_QUI_TU_VIV_IN_CIT_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0098_18_Sam_MH_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0098_19_Tu_QUI_SEI_TIP_RIC_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0098_20_Sam_TSK_VAI_IN_CER_DI_RIC_RAG_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0098_21_Tu_NO_CIO_NON_SO_MI_PIA_DIC_CHE_VOR_USA_IL_MIO_TEM_PER_COS_PI_INT_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0098_22_Sam_OH_CAZ_ATT_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivataInForestaCadetta5Calcolatore"]:
            nome = "Sam"
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0099_01_Tu__CIN_HAN_LE_OSS_COS_PIC_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0099_02_Sam__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0099_03_Tu__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0099_04_Sam__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0099_05_Tu_EHM_EHM_DA_QUA_SEI_IN_QUE_FOR_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0099_06_Sam__CIN_GIO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0099_07_Tu_E_QUA_GIO_CI_DEV_RIM_ANC_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0099_08_Sam__NOVE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0099_09_Tu_NOV_E_COS_SUC_SE_TOR_PRI_O_SE_NON_TOR_AFF_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0099_10_Sam__NON_SUP_LA_PRO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0099_11_Tu_AH_BEH_CER_MA_SCU_SE_TE_LO_CHI_IN_QUE_GEN_DI_PRO_NON_DOV_ESS_VIE_LAI_DI_ALT_PER_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0099_12_Sam_MI__CON_SFR_TUT_CI_CHE_MI_VIE_MES_A_DIS_DAL_NAT_TU_NON_NE_FAI_PAR_RAG_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0099_13_Tu_MAH_SEN_RAG_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0099_14_Sam__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0099_15_Tu_MA_QUI_TU_VIV_IN_CIT_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0099_16_Sam_MH_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0099_17_Tu_QUI_SEI_TIP_RIC_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0099_18_Sam_TSK_VAI_IN_CER_DI_RIC_RAG_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0099_19_Tu_NO_CIO_NON_SO_MI_PIA_DIC_CHE_VOR_USA_IL_MIO_TEM_PER_COS_PI_INT_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0099_20_Sam_OH_CAZ_ATT_)
            partiDialogo.append(dialogo)
    elif tipo.startswith("OggettoLegna"):
        partiDialogo = []
        nome = "OggettoLegna"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["trovatoLegna1"] and avanzamentoDialogo == 0:
            oggettoDato = LI.LEGNA
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0100_01_Tu_CRE_CHE_SIA_QUE_LA_LEG_TAG_DA_SAM_DI_SIC_NON_BAS_PER_LA_NOT_QUI_INT_CE_NE_DOV_ESS_DEL_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["trovatoLegna2"] and avanzamentoDialogo == 0:
            oggettoDato = LI.LEGNA
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0101_01_Tu_ECC_DEL_LEG_ANC_UN_PO_E_POS_TOR_IND_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["trovatoLegna3"] and avanzamentoDialogo == 0:
            oggettoDato = LI.LEGNA
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0102_01_Tu_OK_HO_PRE_ABB_LEG_ADE_DEV_POR_ALL_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0848_01_Tu_NON_C_PI_LEG_DA_PRE_QUI_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0849_01_Tu_CI_SON_DEI_BAS_DI_LEG_PER_TER_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0850_01_Tu_DEI_RAMETTI_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoCinghiale":
        partiDialogo = []
        nome = LI.CINGHIALE
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDP._0103_01_Cinghiale_GRUNT_GRUNT_)
        partiDialogo.append(dialogo)
    elif tipo == "OggettoPersonaCadavereSam":
        partiDialogo = []
        nome = LI.SOLDATO
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cinghialeUcciso"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0851_01_Tu_DEV_LIB_LA_ZON_PRI_DI_OCC_DI_LUI_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["cinghialeUcciso"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0104_01_Tu_SOLDAT_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0104_02_Soldato__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0104_03_Tu_OH_CAZZO_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoTombaSam":
        partiDialogo = []
        nome = "OggettoTombaSam"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0852_01_Tu_CRE_CHE_STE_CER_DI_SCA_DA_QUE_CIN_E_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0852_02_Tu__FOR_STA_CAC_CHE_SIA_STA_LUI_AD_ALL_QUE_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0853_01_Tu_HAN_MES_UNA_LAP_C_SCR_SA_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0853_02_Tu__IL_FIG_DI_DAV_E_OLI_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0854_01_Tu_LA_TOM_DI_SA_)
            partiDialogo.append(dialogo)
    elif tipo == "Ragazzo1":
        partiDialogo = []
        nome = LI.SCONOSCIUTO
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["apparsiAggressoriForestaSognoCastello"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0105_01_Tu_UH_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0105_02_Sconosciuto__VIE_QUI_TRO_)
            partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo


