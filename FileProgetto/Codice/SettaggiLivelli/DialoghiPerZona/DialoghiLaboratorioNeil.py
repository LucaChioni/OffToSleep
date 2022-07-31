# -*- coding: utf-8 -*-

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

    if stanzaDiAppartenenza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        if tipo == "OggettoCellaNeil":
            partiDialogo = []
            nome = "Neil"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoNotatoCellaDiNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0166_01_Tu__NEIL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0166_02_Neil__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0166_03_Tu__NEIL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0166_04_Neil__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["interazioneConCellaDiNeil1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0167_01_Tu__NEIL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0167_02_Neil__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo1PostTrasformazioneLaboratorio"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0168_01_Neil__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0168_02_Tu__HA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0168_03_Tu_COME_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo2PostTrasformazioneLaboratorio"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0169_01_Tu__PRI_CHE_IO_MI_RIS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0169_02_Neil__)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sparitoNeilDallaCellaDelLaboratorioSecondaVolta"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1046_01_Tu_NEI__SEM_QUA_DEN_)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["sparitoNeilDallaCellaDelLaboratorioSecondaVolta"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1047_01_Tu__SCO_NEL_STE_MOM_IN_CUI_SON_SCO_ANC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1047_02_Tu__MA_NEL_REA__ANC_QUI_DEN_)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1048_01_Tu_NEI_NON_C_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1049_01_Tu_C_NEI_QUA_DEN_MA_NON_RIS_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1050_01_Neil__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1050_02_Tu__FOR_TOR_PRI_O_POI_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoLetteraInvitoReneLaboratorio":
            partiDialogo = []
            nome = LI.LET_DI_NEI
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["interazioneConCellaDiNeil2"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0170_01_Tu__UNA_LET_DI_NEI_PER_REN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0170_02_LetteraDiNeil_REN_TI_MAN_I_MIE_RIN_PER_LE_RIS_SPE_LE_RIC_SUL_SI_SON_AVV_NON_APP__STA_POS_E_SON_FEL_DI_COM_CHE_STA_GI_DAN_OTT_RIS_TAN_CHE_MI_HAN_PER_DI_SBL_UN_FRO_DI_RIC_CHE_AVE_ORM_ABB_DA_ANN_OSS_LIN_DI_FRE_DI_CAM_PER_E_COG_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0170_03_LetteraDiNeil__DA_QUE_CHE_HO_POT_OSS_FIN_GLI_IMP_POS_TEC_CHE_PER_LOR_DI_ELA_INF_A_UNA_FRE_TAL_ELE_DA_SUP_ADD_LA_FRE_CON_CUI_GLI_EVE_REA_SI_SUS_CI_VUO_DIR_CHE_SE_LA_TEC_VEN_RIA_PER_NOI_ESS_UMA_SAR_POS_RIM_COS_O_ADD_MUO_IN_QUE_FRA_DI_TEM_IN_CUI_IL_TEM_STE_NON_SCO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0170_04_Tu_LAPPARECCHIO_CEREBRALE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0170_05_LetteraDiNeil_POT_ESS_VIC_A_SCO_INI_E_DI_QUE_TI_RIN_INF_TI_CON_DI_NON_AVE_BEN_COM_QUA_SIA_LE_TUE_PRE_IN_CAM_IL_MES__STA_UN_PO_VAG_HA_RIC_INF_SUL_SIT_GEO_COR_E_LAC_ILL_A_TUT_I_MIE_STU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0170_06_LetteraDiNeil__NON_HO_ESI_AD_ACC_SAP_ENT_CHE_LIN_DEL_COS__IMM_E_NON_POS_PER_PER_DI_TEM_SOP_SE_QUE__IL_SUO_LIV_TEC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0170_07_Tu__IL_CO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0170_08_LetteraDiNeil__PER_QUE_COL_LOC_NON_SOL_PER_DAR_ACC_ALL_MIE_RIC_MA_ANC_PER_INV_A_FAR_ALT_IN_UNO_COL_E_DI_CON_DEI_NOS_RIS_PER_PRE_AL_MEG_ALL_PRO_INT_DEL_COS_TI_INV_DUN_A_UN_PER_DI_RIC_COO_NEI_LAB_DEL_MIO_CAS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0170_09_LetteraDiNeil_SE_DEC_DI_ACC_PRE_IL_PRI_POS_AL_MIO_CAS_CON_QUE_LET_ALL_GUA_E_TI_LAS_ENT_NEI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0170_10_Tu__ERA_QUI_PER_QUE_REN_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1051_01_Tu__UN_INV_AL_CAS_PER_REN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1051_02_LetteraDiNeil_REN_TI_MAN_I_MIE_RIN_PER_LE_RIS_SPE_LE_RIC_SUL_SI_SON_AVV_NON_APP__STA_POS_E_SON_FEL_DI_COM_CHE_STA_GI_DAN_OTT_RIS_TAN_CHE_MI_HAN_PER_DI_SBL_UN_FRO_DI_RIC_CHE_AVE_ORM_ABB_DA_ANN_OSS_LIN_DI_FRE_DI_CAM_PER_E_COG_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1051_03_LetteraDiNeil__DA_QUE_CHE_HO_POT_OSS_FIN_GLI_IMP_POS_TEC_CHE_PER_LOR_DI_ELA_INF_A_UNA_FRE_TAL_ELE_DA_SUP_ADD_LA_FRE_CON_CUI_GLI_EVE_REA_SI_SUS_CI_VUO_DIR_CHE_SE_LA_TEC_VEN_RIA_PER_NOI_ESS_UMA_SAR_POS_RIM_COS_O_ADD_MUO_IN_QUE_FRA_DI_TEM_IN_CUI_IL_TEM_STE_NON_SCO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1051_04_LetteraDiNeil_POT_ESS_VIC_A_SCO_INI_E_DI_QUE_TI_RIN_INF_TI_CON_DI_NON_AVE_BEN_COM_QUA_SIA_LE_TUE_PRE_IN_CAM_IL_MES__STA_UN_PO_VAG_HA_RIC_INF_SUL_SIT_GEO_COR_E_LAC_ILL_A_TUT_I_MIE_STU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1051_05_LetteraDiNeil__NON_HO_ESI_AD_ACC_SAP_ENT_CHE_LIN_DEL_COS__IMM_E_NON_POS_PER_PER_DI_TEM_SOP_SE_QUE__IL_SUO_LIV_TEC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1051_06_LetteraDiNeil__PER_QUE_COL_LOC_NON_SOL_PER_DAR_ACC_ALL_MIE_RIC_MA_ANC_PER_INV_A_FAR_ALT_IN_UN_OTT_COL_E_DI_CON_DEI_NOS_RIS_PER_PRE_AL_MEG_ALL_PRO_INT_DEL_COS_TI_INV_DUN_A_UN_PER_DI_RIC_COO_NEI_LAB_DEL_MIO_CAS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1051_07_LetteraDiNeil_SE_DEC_DI_ACC_PRE_IL_PRI_POS_AL_MIO_CAS_CON_QUE_LET_ALL_GUA_E_TI_LAS_ENT_NEI_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1052_01_Tu__LIN_PER_REN_NEI_HA_COL_LOC_PER_VEL_LE_SUE_RIC_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiIstruzioniCalcolatoreLaboratorio":
            partiDialogo = []
            nome = LI.IST_PER_IL_CAL_DI_EVE
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["creatoPersonaggioOggettoIstruzioniCalcolatoreLaboratorio"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0171_01_Tu__UNA_LIS_DI_COM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0171_02_IstruzioniPerIlCalcolatoreDiEventi_COM_CER_DEL_CAL_DI_EVE_POS_IL_CAS_OCC_CHI_E_PAR_ALL_BR_COM_DI_ACC_NAV_BR_COM_DAV_SEQ_DI_EVE_AVV_SEQ_BR_COM_DAR_SEQ_DI_EVE_STO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0171_03_IstruzioniPerIlCalcolatoreDiEventi_COM_PRO_TEM_PRO_X_ANN_X_MES_X_GIO_X_ORE_X_MIN_X_SEC_BR_COM_REG_TEM_REG_X_ANN_X_MES_X_GIO_X_ORE_X_MIN_X_SEC_BR_COM_MOV_MOV_SPA_IN_INS_LUO_BR_IL_SIS_PRO_GLI_EVE_NEL_MEN_DEL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0171_04_IstruzioniPerIlCalcolatoreDiEventi_ECC_A_TE_TUT_LA_MIA_CON_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0171_05_Tu_ASPETTA_POSSO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0171_06_Tu_CA_DI_EVE_NON_DIR_CHE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1053_01_Tu_CRE_CHE_SIA_DEI_COM_PER_QUE_CAS_QUA_ACC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1053_02_IstruzioniPerIlCalcolatoreDiEventi_COM_CER_DEL_CAL_DI_EVE_POS_IL_CAS_OCC_CHI_E_PAR_ALL_BR_COM_DI_ACC_NAV_BR_COM_DAV_SEQ_DI_EVE_AVV_SEQ_BR_COM_DAR_SEQ_DI_EVE_STO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1053_03_IstruzioniPerIlCalcolatoreDiEventi_COM_PRO_TEM_PRO_X_ANN_X_MES_X_GIO_X_ORE_X_MIN_X_SEC_BR_COM_REG_TEM_REG_X_ANN_X_MES_X_GIO_X_ORE_X_MIN_X_SEC_BR_COM_MOV_MOV_SPA_IN_INS_LUO_BR_IL_SIS_PRO_GLI_EVE_NEL_MEN_DEL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1053_04_IstruzioniPerIlCalcolatoreDiEventi_ECC_A_TE_TUT_LA_MIA_CON_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1054_01_Tu_SON_I_COM_PER_UTI_IL_CAL_DI_EVE_ME_LI_HA_LAS_NEI_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiGenerici0Laboratorio":
            partiDialogo = []
            nome = LI.APP_DI_NEI
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1055_01_Tu_CI_SON_DEG_APP_NON_SI_CAP_GRA__PIE_DI_FOR_E_CAL_INC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1055_02_Tu__NON_C_TRA_DI_ALC_SPI_NEA_DUE_RIG_COM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1055_03_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1055_04_Tu__OH_DEL_PAR_LEG_SI_ON_SE_CER_PR_CER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1055_05_Tu__BOH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1055_06_Tu__FOR__MEG_INI_DA_COS_PI_FAC_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1056_01_Tu_CI_SON_POC_PAR_COM_SI_ON_SE_CER_PR_CER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1056_02_Tu__IL_RES_SON_FOR_E_CAL_CRE_SAR_MEG_INI_DA_COS_PI_LEG_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoCalcolatoreEventi":
            partiDialogo = []
            nome = LI.MACCHINARIO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["lettoAppuntiIstruzioniCalcolatoreLaboratorio"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1057_01_Tu__UNA_SED_CON_UNA_SPE_DI_CAS_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["lettoAppuntiIstruzioniCalcolatoreLaboratorio"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0172_01_Tu_QUI_MI_SIE_QUI_)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sparitoNeilDallaCellaDelLaboratorioSecondaVolta"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1058_01_Tu_SON_SED_QUA_IN_QUE_MOM_NEL_REA_)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["sparitoNeilDallaCellaDelLaboratorioSecondaVolta"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1059_01_Tu_NEI_DEV_AVE_COS_MEN_ERA_BLO_TRA_DUE_MOM_)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1060_01_Tu__RIM_QUI_PER_PI_DI_SET_ANN_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1061_01_Tu_NON_HO_VOG_ADE_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiGenerici1Laboratorio":
            partiDialogo = []
            nome = LI.APP_DI_NEI
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1062_01_Tu_APP_DI_NEI_QUA_SPI_NEL_DET_IL_FUN_DEL_SIS_USA_DAL_COS_PER_CRE_LA_REA_QUE_RO_IN_MEZ_ALL_LAV_DEL_VUL__UN_CAL_MEN_GLI_IMP_SON_OPE_IN_PAT_DA_QUE_CHE_HO_CAP_IL_CAL_ELA_GLI_EVE_IN_MAN_SIM_AL_CAL_DI_NEI_E_GLI_IMP_PRO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1062_02_Tu__HO_CON_MIL_VOL_MA_DAL_CAL_DI_NEI_NON_SI_VED_COM__STA_COS_ALL_DI_TUT_NEG_EVE_PI_LON_NEL_PAS_A_CUI__POS_ACC_IL_SIS__SEM_GI_PRE_INS_AL_COS_E_A_QUA_IMP_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1063_01_Tu_APP_DI_NEI_IN_CUI_DES_IL_FUN_DEL_SIS_USA_DAL_COS_PER_CRE_GLI_EVE_REA_DAL_CAL_DI_NEI_NON_SI_VED_COM__STA_COS__SEM_SEM_ESI_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiGenerici2Laboratorio":
            partiDialogo = []
            nome = LI.APP_DI_NEI
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1064_01_Tu_APP_DI_NEI_QUA_CI_SON_TUT_LE_SPI_DI_COM_HA_FAT_A_REN_IL_SUO_CAL_INF_PI_VEL_ED_EFF_DI_QUE_DEL_COS_NEL_VUL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1064_02_Tu__PRI_PER_DUE_RAG_LA_PRI_LOU__PI_IMM_E_SFR_LE_CAP_CER_DEL_CHE_LO_UTI_LA_SEC_NON_CON_LES_DI_AGE_EST_TUT_COL_CHE_SON_STA_FUO_DAL_SER_DI_EVE_VEN_CAN_DAL_SIS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1064_03_Tu__QUE_VUO_DIR_CHE_IL_FUT_CHE_HO_VIS_NON_SAR_IDE_A_QUE_CHE_AVV_REA_IO_SAR_DA_QUA_PAR_A_FAR_QUA_POI_ROD_POT_VED_IL_COS_MOR_NEL_VUL_E_MAG_FAR_QUA_DI_DIV_POT_LEG_IL_MIO_MES_POT_VEN_QUI_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1065_01_Tu__APP_DI_NEI_IN_CUI_DES_IL_FUN_DEL_CAL_DI_EVE_IO_NON_SON_CON_NEL_PRE_QUI_POT_ANC_CAM_QUA_POI_FAR_DEL_PRO_DOV_SOL_ASP_QUA_MIL_DI_ANN_PER_CON_I_RIS_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiGenerici3Laboratorio":
            partiDialogo = []
            nome = LI.APP_DI_NEI
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1066_01_Tu_APP_DI_NEI_IN_CUI_SPI_DEL_SIS_DEL_COS_PER_EV_DA_QUE_DIM_SI_RIF_ALL_CEL_NEL_VUL_DOV_HO_TRO_IL_SUO_CAD_NON_HO_ANC_CAP_COM_FUN_MA_A_QUA_PAR_PER_DI_AND_IN_UN_POS_IN_CUI_SA_FIN_POS_COM_LA_REA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1066_02_Tu__NEI_GLI_COP_E_NE_HA_RIC_UNA_QUI_NEL_SUO_LAB_MA_DOP_DIV_TES_HA_SCO_CHE_NON__POS_UTI_FIN_ALM_UNA_PER__GI_FU_SI_PU_USC_SOL_UNO_ALL_VOL_IL_MOT_NON_LO_SPI_NON_LO_SA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1066_03_Tu__COM_SAR_BAS_FAR_TOR_IL_COS_E_PRE_IL_SUO_POS_COM_SEM_MAN_NEL_VUL_UNA_RAG_CHE_NON_HA_NIE_DA_FAR_E_FAI_SCA_QUA_ALL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1066_04_Tu__IL_COS_CRE_CHE_ALL_FIN_CI_ABB_VOL_PRO_COM_AD_USA_LA_SUA_CEL_MA_NON_POT_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1067_01_Tu_APP_DI_NEI_IN_CUI_SPI_IL_FUN_DEL_MAC_CHE_PER_DI_EV_DA_QUE_DIM_)
                partiDialogo.append(dialogo)
        elif tipo == "Bibliotecario" or tipo == "OggettoBibliotecarioCalcolatore" or tipo == "BibliotecarioOperato":
            partiDialogo = []
            nome = u"René"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivatoRenéNelLaboratorioDiNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0173_01_Ren__CHE_DIA_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo1RenéNelLaboratorioDiNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0174_01_Ren__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0174_02_Ren__CCOME_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo2RenéNelLaboratorioDiNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0175_01_Ren__PER_DIO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo3RenéNelLaboratorioDiNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0176_01_Ren__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo4RenéNelLaboratorioDiNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0177_01_Ren__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoAttesaRenéSulCalcolatore1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0178_01_Ren__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0179_01_Ren__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0179_02_Tu__SI__)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoImpoFermo":
            partiDialogo = []
            nome = "Impo"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._1068_01_Impo__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1068_02_Tu_NON_MI_SER_ADE_)
            partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo


