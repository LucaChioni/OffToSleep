# -*- coding: utf-8 -*-

import GlobalHWVar
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
    if tipo == "PadreUfficialeServizio":
        partiDialogo = []
        nome = LI.SOLDATO
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["entratoInCittà"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0069_01_Soldato_CHI_SEI_E_COS_VUO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0069_02_Tu_SON_UHM_MI_CHI_SAR_E_STO_CER_MIO_FRA_SI_CHI_HAN_HA_PI_O_MEN_LA_MIA_ET_DOV_ESS_PAS_DI_QUI_NON_MOL_TEM_FA_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0069_03_Soldato_SEI_DA_SOL_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0069_04_Tu_S_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0069_05_Soldato_MMH_AL_MOM_GLI_ALL_PRO_SON_TUT_OCC_TUO_FRA_POT_AVE_PRE_UNO_DEG_ULT_POS_DIS_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0069_06_Tu_AH_POS_DIV_LA_STA_CON_LUI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0069_07_Soldato_TSK_S_LA_STA_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0069_08_Tu__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0069_09_Soldato__OGN_STA_HA_CIR_UNA_VEN_DI_LET_E_OGN_LET_OSP_DAL_TRE_ALL_SEI_PER_NON_C_PI_SPA_L_DEN_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0069_10_Tu_OH_E_COM_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0069_11_Soldato_LA_TUA_ARM_DAC_DOV_LHA_PRE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0069_12_Tu_ERA_LHO_TRO_SU_UN_CAD_DI_UN_SOL_NEL_FOR_E_HO_PEN_CHE_MI_POT_ESS_UTI_PER_ARR_IN_CIT_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0069_13_Soldato_E_IL_SOL_CHE_LA_IND_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0069_14_Tu_LHO_SEP_PER_NON_VEN_DIV_DA_QUE_BES_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0069_15_Soldato__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0069_16_Tu__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0069_17_Soldato__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0069_18_Tu__SAI_I_LUP_I_CIN_E_QUE_TAR_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0069_19_Soldato__SEN_PER_STA_POT_ESS_MIA_OSP_TI_FAR_PRE_UNA_STA_MA_DA_DOM_DOV_TOG_IL_DIS_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0069_20_Tu_VVA_BEN_GRA_MA_TU_CHI_SEI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0069_21_Soldato_DAV_EX_UFF_DEL_CIT_ORA_A_COM_DEL_GUA_NOT_VAD_A_PRE_LA_GUA_PER_LA_MIA_ASS_E_AND_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0069_22_Tu_OK_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["primoDialogoDavid"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["città1"]:
            nome = "David"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0628_01_David_SEG_CAS_MIA__DA_QUE_PAR_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCittà2"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["città2"]:
            nome = "David"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0629_01_David_DA_QUE_PAR_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCittà3"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["città3"]:
            nome = "David"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0630_01_David_NON_MAN_MOL_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCittà4"] and stanzaDiAppartenenza == GlobalGameVar.dictStanze["città4"]:
            nome = "David"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0631_01_David_SIAMO_ARRIVATI_)
            partiDialogo.append(dialogo)
    elif tipo == "Mercante":
        partiDialogo = []
        nome = "Rod"
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoCasaDavid"]:
            nome = LI.SCONOSCIUTO
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0070_01_Tu_CHI_SCU_SIG_STO_CER_GLI_ALL_PRO_SAI_DIR_DOV_SI_TRO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0070_02_Sconosciuto_EH_IO_STA_EHM_EHM_GLI_ALL_SON_IN_UN_EDI_CHE_SI_AFF_SU_QUE_STR_CHE_VA_VER_OVE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0070_03_Tu_VERSO_OVEST_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0070_04_Sconosciuto_S_OVE_A_SIN_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0070_05_Tu__OK_CER_SIN_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0070_06_Sconosciuto_SIN_SAI_DIS_DES_E_SIN_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0070_07_Tu_S_S_CER_LO_SO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0070_08_Sconosciuto_DIO_SAN_NON_CI_POS_CRE_OK_ALL_LA_SIN_LA_SIN__LA_PAR_DEL_PET_IN_CUI_SEN_BAT_IL_CUO_OK_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0070_09_Tu_UHM_OK_QUI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0070_10_Sconosciuto__MET_ENT_LE_MAN_SUL_PET_PER_FAV_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0070_11_Tu_OK_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0070_12_Sconosciuto_ECC_LA_MAN_SIN__QUE_CON_CUI_SEN_IL_BAT_DEL_CUO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0070_13_Tu_OH_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0070_14_Sconosciuto_BEN_ADE_DEV_SEG_QUE_DIR_RAG_SEG_IL_TUO_CUO_E_TRO_LA_TUA_STR_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0070_15_Tu_VA_BEN_VA_BEN_HO_CAP_ADE_LO_SO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0070_16_Sconosciuto_PERFETTO_ARRIVEDERCI_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cercatoHansInAlloggiProfughi"]:
            nome = LI.SCONOSCIUTO
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0632_01_Tu_SCU_SE_TI_DIS_DI_NUO_POT_RIP_DOV_SI_TRO_GLI_ALL_PRO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0632_02_Sconosciuto_A_SIN_SIN_DOV_TI_BAT_IL_CUO_SE_FAI_FAT_A_RIC_PUO_TEN_LE_MAN_SUL_PET_DUR_IL_TRA_E_CIO_NO_QUE_FOR__MEG_DI_NO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0632_03_Tu_VA_BEN_VA_BEN_ME_LO_RIC_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["resettatoAvanzamentoDialoghiCittadiniACuiChiediInfo"]:
            nome = LI.SCONOSCIUTO
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0071_01_Tu_SCU_NUO_IL_DIS_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0071_02_Sconosciuto_ANC_TU_SE_MI_CHI_DI_NUO_DA_CHE_PAR__LA_SIN_IMP_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0071_03_Tu_S_VA_BEN_HO_CAP_SEN_VOL_CHI_SE_MA_PER_CON_A_GUA_ATT_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0071_04_Sconosciuto_PER_NO_STO_SOL_OSS_IN_GIR_COM_PRO_LA_VIT_CIT_NES_IN_PAR_SOL_IL_MOV_DEL_PER_IN_GEN_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0071_05_Tu_S_DI_SIC_NON_STA_FIS_QUE_RAG_LAG_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0071_06_Sconosciuto_COS_NES_IN_PAR_HO_DET_POI_NON_POS_FIS_QUA_SE_CON_A_GIR_NO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0071_07_Tu_CER_CER_COM_TU_CHE_OSS_COS_TAN_IL_MOV_DEL_PER_IN_GEN_HAI_PER_CAS_VIS_PAS_DA_QUE_PAR_UN_RAG_PI_O_MEN_DEL_MIA_ET_UN_PO_PI_ALT_DI_ME_CON_I_CAP_NER_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0071_08_Sconosciuto__NON_RIV_INF_DI_QUE_TIP_SEN_NES_TIP_DI_COM_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0071_09_Tu_MA_STO_SOL_CER_MIO_FRA_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append({lingua: testo % GlobalGameVar.monetePerEntrareNellaConfraternita for lingua, testo in LDP._0071_10_Sconosciuto_NON_PAR_SEN_COM_SON___STR__U_MON_.items()})
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append({lingua: testo % GlobalGameVar.monetePerEntrareNellaConfraternita for lingua, testo in LDP._0071_11_Tu_COS___STR__U_MON_PER_RIS_A_UNA_DOM_.items()})
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0071_12_Sconosciuto_S_DIC_CHE_IN_REA_QUE__UNA_PIC_QUO_NEC_PER_PER_ENT_NEL_CON_UNA_VOL_DEN_TI_VER_CON_TUT_LE_INF_CHE_RIC_PER_NON_PAR_DI_TUT_LE_ALT_RIS_A_CUI_POT_AVE_ACC_CON_DEI_PIC_SOS_ECO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0071_13_Tu__NEL_CO_SUO_PRO_COM_UNA_TRU_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0071_14_Sconosciuto_NOO_NON_LO__GIU_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0071_15_Tu__SEN_NON_MI_INT_DEL_CON_POS_PAG_DI_MEN_SOL_PER_QUE_DOM_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0071_16_Sconosciuto_MI_DIS_NON_POS_RIV_INF_A_CHI_NON__NEL_COF__UNA_DEL_REG_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append({lingua: testo % GlobalGameVar.monetePerEntrareNellaConfraternita for lingua, testo in LDP._0071_17_Tu_CER_DI_SIC_NON_TE_LO_SEI_APP_INV___STR__U_MON_PER_AVE_UNA_RIS_E_LOP_DI_SPE_ALT_MON_PER_DEL_RI_NON_MI_SEN_PER_NIE_TRU_ANZ_SEM_PRO_UNO_DA_PRE_AL_VOL_.items()})
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0071_18_Sconosciuto_LO__NON_MI_CAP_SPE_DI_OFF_QUE_SEI_STA_FOR_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0071_19_Tu_CERTO_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["richiesteMonetePerEntrareInConfraternita"]:
            if monetePossedute < GlobalGameVar.monetePerEntrareNellaConfraternita:
                nome = LI.SCONOSCIUTO
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0633_01_Tu_SEN_MI_POT_DIR_DOV_HAI_VIS_MIO_FRA_COM_FAV_POI_VAL_MOL_PI_SER_DI_ENT_NEL_CON_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append({lingua: testo % GlobalGameVar.monetePerEntrareNellaConfraternita for lingua, testo in LDS._0633_02_Sconosciuto_CER_SON___STR__U_MON_.items()})
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0633_03_Tu__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append({lingua: testo % GlobalGameVar.monetePerEntrareNellaConfraternita for lingua, testo in LDP._0072_01_Tu_TIE_LE___STR__U_MON_UHM_NON_SO_ANC_IL_TUO_NOM_.items()})
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0072_02_Sconosciuto_PER_BEN_NEL_CON_IO_SON_ROD_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0072_03_Tu_ROD_PIA_SAR_QUI_DOV_HAI_VIS_MIO_FRA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0072_04_Sconosciuto_ALL_HAI_CHI_DI_UN_RAG_DEL_TUA_ET_UN_PO_PI_ALT_DI_TE_E_CON_I_CAP_NER_SE_DEV_ESS_SIN_NON_HO_VIS_NES_IN_CIT_CHE_COR_A_QUE_DES_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0072_05_Tu_COS_CON_CHE_FAC_HAI_AVU_IL_COR_DI_CHI_DEL_MON_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0072_06_Sconosciuto_BEH_TI_STO_COM_DAN_DEL_INF_E_HAI_TUT_I_VAN_DI_ESS_NEL_CON_TRA_LAL_ORA_CHE_CI_PEN_NON_HO_MAI_VIS_NEA_TE_DA_QUE_PAR_SIE_ARR_OGG_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0072_07_Tu__UFF_ASS_S_SIA_ARR_DUR_LA_NOT_MIO_FRA__ARR_PRI_DI_ME_E_GLI__STA_ASS_UN_ALL_CHE_A_QUA_PAR_ERA_LUL_RIM_PER_IO_SON_STA_OSP_DI_DAV_IL_CO_DEL_GUA_NOT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0072_08_Sconosciuto_ADD_VA_BEH_QUI_NON_SIE_ARR_INS_E_NON_LHA_NEA_MAI_VIS_IN_CIT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0072_09_Tu_S_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0072_10_Sconosciuto__BEH_BUO_FOR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0072_11_Tu_ASP_COS_DOV_FAR_ALL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0072_12_Sconosciuto_E_CHE_NE_SO_IO_TOR_A_CAS_E_ASP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0072_13_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0072_14_Sconosciuto_SEN_NON_LO_SO_LA_BIB__FRE_DA_MOL_RAG_DEL_VOS_ET_MAG_IL_GES_SAP_DIR_QUA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0072_15_Tu_OK_BIB_CHE_SI_TRO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0072_16_Sconosciuto_NEL_STR_CHE_POR_A_EST_CHE__IL_CON_DI_OVE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0072_17_Tu_S_S_OK_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0072_18_Sconosciuto_AH_ASP_UHM_SAR_ORA_CHE_SEI_NEL_CON_HAI_DIR_AD_ACC_AL_CAT_DI_RIS_DIS_QUA_TI_SER_QUA_TI_FAR_DAR_UNO_)
                partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["rifiutatoDallaBiblioteca"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = True
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0634_01_Tu_EHI_ROD_COS_DIC_RIG_ALL_RI_DEL_CON_POS_PRE_QUA_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0634_02_Sconosciuto_CER_DAI_PUR_UNO_)
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["rifiutatoDallaBiblioteca"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoDopoArrivoInBiblioteca"]:
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0635_01_Tu_EHI_ROD_TRA_LE_TUE_RIS_HAI_PER_CAS_UN_DOC_O_QUA_DEL_GEN_CHE_POS_FAR_ENT_IN_BIB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0635_02_Sconosciuto_NON_SON_LE_MIE_RIS_COM_NON_C_BIS_DI_SCO_LA_CON_PER_QUE_COS_PER_AVE_UN_DOC_DI_RES_BAS_RIC_A_CHI_TI_HA_OSP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0635_03_Tu_MH_UN_PO_DEL_LE_POS_DI_QUE_CON_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0635_04_Sconosciuto_GUA_CHE_ANC_TU_NE_FAI_PAR_POT_CON_AL_POS_DI_LAM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0635_05_Tu_SON_APP_ARR_PIU_POT_VAL_DI_AND_IN_UNA_NO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append({lingua: testo % GlobalGameVar.monetePerLasciareLaConfraternita for lingua, testo in LDS._0635_06_Sconosciuto_COM_VUO_SON___STR__U_MON_PER_LAS_LA_CON_.items()})
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0635_07_Tu_AH_AH_CER_)
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = True
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0636_01_Tu_EHI_ROD_CHE_RIS_OFF_OGG_LA_CON_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0636_02_Sconosciuto_DAI_UNO_E_PRE_QUE_CHE_TI_SER_)
                partiDialogo.append(dialogo)
    elif (tipo == "GuardiaCitta" or tipo.startswith("Ragazz")) and avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
        partiDialogo = []
        if tipo.startswith("Ragazzo"):
            nome = LI.SCONOSCIUTO
        elif tipo.startswith("Ragazza"):
            nome = LI.SCONOSCIUTA
        else:
            nome = LI.SOLDATO
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDS._0637_01_Soldato__)
        partiDialogo.append(dialogo)
    elif tipo == "GuardiaCitta" and avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
        partiDialogo = []
        nome = LI.SOLDATO
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["città4"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0638_01_Soldato_NON_CI_PRO_RAG_LAC__VIE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0638_02_Tu_EHM_OK_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0639_01_Tu_NON_VOG_PAR_COI_SOL_POT_INS_PER_IMP_)
            partiDialogo.append(dialogo)
    elif tipo == "GuardiaCitta" and avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"]:
        partiDialogo = []
        nome = LI.SOLDATO
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(LDS._0640_01_Tu_MEG_RIS_LE_CON_COI_SOL_NON_HO_VOG_DI_POT_CHI_QUA_SUL_)
        partiDialogo.append(dialogo)
    elif tipo.startswith("Ragazz") and avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["presiStrumentiPerStudiareImpo"]:
        if tipo.startswith("Ragazzo"):
            partiDialogo = []
            nome = LI.SCONOSCIUTO
        elif tipo.startswith("Ragazza"):
            partiDialogo = []
            nome = LI.SCONOSCIUTA
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(LDS._0641_01_Tu_NON_HO_NIE_DA_CHI_)
        partiDialogo.append(dialogo)
    elif tipo.startswith("OggettoDict"):
        partiDialogo = []
        nome = LI.CADAVERE
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDS._0642_01_Cadavere__)
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("tu")
        dialogo.append(LDS._0642_02_Tu__)
        partiDialogo.append(dialogo)

    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città1"]:
        if tipo == "GuardiaCitta":
            partiDialogo = []
            nome = LI.SOLDATO
            if y == GlobalHWVar.gpy * 2:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0643_01_Soldato_VAI_CON_IL_COM_QUA_CI_PEN_NOI_)
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0644_01_Tu_CHI_SCU_DOV_PAS_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0644_02_Soldato_QUE_ZON__ACC_SOL_AI_MER_TU_NON_SEI_UN_MER_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0644_03_Tu_S_CHE_SON_UN_MER_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0644_04_Soldato_BEN_MOS_LA_LIC_ALL_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0644_05_Tu_LA_LIC_NON_CE_LHO_ADE_LHO_DIM_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0644_06_Soldato_MMH_LEV_DI_TOR_)
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0645_01_Soldato_QUE_ZON__ACC_SOL_AI_MER_)
                    partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 15:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0646_01_Soldato_CHE_CI_FA_QUI_UNA_RAG_TUT_SOL_NEL_BEL_MEZ_DEL_NOT_NON_LO_SAI_CHE__PER_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0646_02_Tu_S_SO_BAD_A_ME_STE_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0646_03_Soldato_TSK_CERTO_)
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0647_01_Soldato_NON_VIA_MAI_DA_SOL_RAG_)
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0648_01_Soldato_NON_PUO_PAS_DI_QUA_RAG_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0648_02_Tu_PERCH_NO_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0648_03_Soldato_PER_IO_TI_HO_DET_CHE_NON_PUO_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0648_04_Tu_E_CHI_SEI_TU_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0648_05_Tu_NO_ASP_ASP_HO_ESA_VA_BEN_NON_PAS_DI_QUA_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0648_06_Soldato_SAR_MEGLIO_)
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0649_01_Soldato_SMAMMA_RAGAZZINA_)
                    partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 5:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0650_01_Soldato_NON_TI_CON_DI_PRO_PER_QUE_DIR_RAG_LA_FUO__PER_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0650_02_Tu_C_UNA_GUE_IN_COR_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0650_03_Soldato_NO_PAR_DEL_FOR__POP_DA_BES_MOL_AGG_)
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0651_01_Soldato_LA_FOR__POP_DA_BES_MOL_AGG_)
                    partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 12:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0652_01_Soldato_SE_FOS_IN_TE_NON_USC_DAL_CIT_ADE_LA_FOR__UN_POS_PER_PER_UNA_RAG_COM_TE_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0652_02_Tu_QUE_STR_POR_SOL_ALL_FOR_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0652_03_Soldato_S_NON__PER_SPI_OLT_)
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0653_01_Soldato_LA_FOR__UN_POS_PER_PER_UNA_RAG_COM_TE_)
                    partiDialogo.append(dialogo)
        elif tipo == "Ragazzo2":
            partiDialogo = []
            nome = LI.SCONOSCIUTO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0654_01_Tu_SCUSA_SIGNORE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0654_02_Sconosciuto_NO_GRA_NON_MIN_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0655_01_Sconosciuto_QUE_TIZ_NON_VUO_PAR_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0656_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo3":
            partiDialogo = []
            nome = LI.SCONOSCIUTO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0657_01_Sconosciuto_SI_SPO_SIG_NON_VED_CHE_STO_SCE_LE_ARA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0657_02_Tu_S_VOL_CHI_UNI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0657_03_Sconosciuto_SI_SPO_PER_COR_NON_MIN_LE_VOS_INI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0658_01_Tu_A_QUA_PAR_QUE_TIZ__TRO_IMP_A_SCE_LE_ARA_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0659_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza1":
            partiDialogo = []
            nome = LI.SCONOSCIUTA
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0660_01_Tu_SCUSA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0660_02_Sconosciuta_MA_GUA_TE_COM_SON_BRU_QUE_POM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0660_03_Tu_POS_CHI_UNI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0660_04_Sconosciuta_MAR_TUT_MAR_DOV_COS_LA_MET_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0660_05_Tu_E_NON_LI_PRE_CI_SON_ALT_BAN_CON_DEI_POM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0660_06_Sconosciuta__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0660_07_Tu_MI_STA_IGN_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0661_01_Sconosciuta_QUE_POM_SON_TUT_MAR_DOV_COS_LA_MET_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0661_02_Tu_CON_A_LAM_DI_QUE_POM_PER_NON_VA_IN_UNA_BAN_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0662_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza3":
            partiDialogo = []
            nome = LI.SCONOSCIUTA
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0663_01_Sconosciuta_ARA_E_POM_ARA_E_POM_COS_C_DI_MEG_DI_UN_BUO_PRA_CON_ARA_E_POM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0663_02_Tu_CON_ARA_E_POM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0663_03_Sconosciuta_CON_ARA_E_POM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0663_04_Tu_NON_SO_NON_LI_HO_MAI_MAN_INS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0663_05_Sconosciuta_NEA_MI_STA_GIU_CHI_SE_FOS_IL_CAS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0663_06_Tu_NON_MI_SEM_UNA_BEL_ACC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0663_07_Sconosciuta_NON_PUO_SAP_FIN_NON_LO_PRO_RAG_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0664_01_Sconosciuta_ARA_E_POM_COS_PU_ESS_DI_MEG_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0665_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0666_01_Tu_SCU_HAI_PER_CAS_VIS_UN_MER_DI_NOM_ROD_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0666_02_Sconosciuta_UN_MER_QUA__PIE_DI_MER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0666_03_Tu_S_MA_QUE__GIR_INC_IN_UN_ABI_GRI_SCU_E_HA_UNA_UN_PO_INQ_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0666_04_Sconosciuta_AHH_QUE_MER_S_LO_VED_PAS_SPE_DI_QUA_FOR__DA_QUA_PAR_IN_CIT_DI_SOL_STA_SOT_LA_TOR_DEL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0666_05_Tu_OK_GRAZIE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0667_01_Sconosciuta_QUE_MER_LO_VED_SPE_PAS_DI_QUA_FOR__DA_QUA_PAR_IN_CIT_DI_SOL_STA_SOT_LA_TOR_DEL_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città2"]:
        if tipo == "Ragazzo1":
            partiDialogo = []
            nome = LI.SCONOSCIUTO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0668_01_Sconosciuto_QUA_MAN_DEI_CAV_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0668_02_Tu_EHI_TU_LAV_QUI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0668_03_Sconosciuto_S_MI_DIC_HA_BIS_DI_QUA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0668_04_Tu_COM_MAI_C_COS_TAN_MER_OGG_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0668_05_Sconosciuto_NON__PI_DEL_NOR_RAG_SE_VIE_QUI_TRO_SEM_FRU_E_VER_IN_ABB_E_A_PRE_SCO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0668_06_Tu_SEM__RIC_COS_TAN_ROB_TUT_I_GIO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0668_07_Sconosciuto_NON__RIC_MA_PI_NE_MET_PI_NE_COM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0668_08_Tu_E_COS_FAT_CON_TUT_QUE_CHE_RIM_NON_MAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0668_09_Sconosciuto_S_LA_BUT_SUL_BAN_TRO_SEM_ROB_FRE_TUT_IL_GIO_TUT_I_GIO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0668_10_Tu_OK_MA_COM_FAT_A_GUA_SE_GET_TUT_QUE_IN_ECC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0668_11_Sconosciuto_NON_TI_PRE_NON_LO_FAR_SE_NON_FOS_VAN_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0669_01_Sconosciuto_L_MAN_DEI_CAV_E_L_DEL_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0670_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0671_01_Tu_EHI_CIA_COM_MAI_CI_SON_COS_POC_PER_IN_GIR_OGG_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0671_02_Sconosciuto_BUO_RAG_S_NON_SO_OGG_POC_PER_ARR_PI_TAR_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0672_01_Sconosciuto_OGG_CI_SON_POC_PER_IN_GIR_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo2":
            partiDialogo = []
            nome = LI.SCONOSCIUTO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0673_01_Sconosciuto_QUE__STR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0673_02_Tu_UVA_QUE_SON_MEL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0673_03_Sconosciuto_MA_CHE_VAI_DIC_LE_MEL_SON_GIA_QUE__CHI_UVA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0673_04_Tu__NON__UVA_POI_I_MEL_SON_GIA_NON_LE_MEL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0673_05_Sconosciuto_MA_SEI_COM_IMP_HO_TRE_VUO_VEN_A_INS_TE_I_COL_DEL_FRU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0673_06_Tu_CER_QUE_NON__VA_BEH_NON_IMP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0673_07_Sconosciuto_AH_SAR_MEG_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0674_01_Sconosciuto_DA_QUA_LE_CAR_SON_COS_STO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0675_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza1":
            partiDialogo = []
            nome = LI.SCONOSCIUTA
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0676_01_Sconosciuta_SPO_SPO_FAI_LAR_DEV_PAS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0676_02_Tu_VA_BEN_VA_BEN_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0677_01_Tu_NON_LE_PAR_DI_NUO_QUA_LE_PER_SEM_MOL_SCO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0678_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0679_01_Sconosciuta_SPO_SPO_FAI_LAR_DEV_PAS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0679_02_Tu_OK_CAL_NON_C_NES_PUO_FAR_ANC_CON_CAL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0679_03_Sconosciuta_SPOSTATI_SPOSTATI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0680_01_Sconosciuta_SPO_SPO_FAI_LAR_DEV_PAS_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza3":
            partiDialogo = []
            nome = LI.SCONOSCIUTA
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0681_01_Sconosciuta_NO_NON_HO_TEM_ADE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0681_02_Tu_PER_SIE_TUT_COS_DI_FRE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0681_03_Sconosciuta_LEV_HO_DET_DEV_TOR_A_CAS_MIO_FIG_MI_STA_ASP_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0682_01_Tu_NON_VOG_PRE_ALT_URL_DA_QUE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0683_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città3"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoNemiciBloccatiSelvaArida"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0073_01_Tu_SEM_TUT_IMM_ANC_QUA_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo1":
            partiDialogo = []
            nome = LI.SCONOSCIUTO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0684_01_Sconosciuto_ODD_HO_LAS_I_DOC_IN_CAS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0684_02_Tu_SCUSA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0684_03_Sconosciuto_AH_NO_CE_LI_HO_QUI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0684_04_Tu__SIGNORE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0684_05_Sconosciuto_ASP_LE_CHI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0684_06_Tu__PER_CAS_SAI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0684_07_Sconosciuto_AH_NO_SON_IN_TAS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0684_08_Tu_NON_MI_ASC_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                avanzaColDialogo = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0685_01_Sconosciuto_CAV_DOV_TOR_IN_CAS_E_CON_SE_HO_PRE_TUT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0685_02_Tu_SCUSA_SIGNORE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0685_03_Sconosciuto_HO_CHI_I_RUB_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0686_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo2":
            partiDialogo = []
            nome = LI.SCONOSCIUTO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cercatoHansInAlloggiProfughi"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0687_01_Sconosciuto_SAL_BEL_VAG_HAI_BIS_DI_QUA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0687_02_Tu_UHM_S_STO_CER_GLI_ALL_PRO_SAI_DIR_DOV_SON_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0687_03_Sconosciuto_GLI_ALL_PEV_UNA_BEL_VAG_COM_TE_DOV_AND_IN_UN_POS_SIM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0687_04_Tu_STO_CER_UNA_PER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0687_05_Sconosciuto_CHI_SIA_SE_VIV_IN_QUE_POS_NON_MEV_DI_AVE_IO_POS_POV_A_VIV_NEL_MIG_VIL_CIT_QUA_DES_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0687_06_Tu__NO_GRA_DEV_AND_AGL_ALL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0687_07_Sconosciuto_BEH_COM_TI_PAV_IO_NON_TI_ACC_IN_QUE_MIS_ABI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cercatoHansInAlloggiProfughi"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0688_01_Sconosciuto_IO_NON_TI_ACC_IN_QUE_MIS_ABI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0689_01_Tu_SCU_SIG_HAI_PER_CAS_VIS_DA_QUE_PAR_UN_RAG_DI_NOM_HAN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0689_02_Sconosciuto_SPI_LA_MIA_ATT__SOL_PEV_LE_VAG_SE__UN_COM_QUE_CHE_CEV_SAP_CHE_IO_NON_TI_LAS_SOL_NEA_UN_MOM_NON_COM_QUE_HON_CHE_VAI_CEV_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0689_03_Tu__SI_CHI_HAN_ED__MIO_FRA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0689_04_Sconosciuto_TUO_FVA_CHE_BIS_C_DI_UN_FVA_QUA_PUO_AVE_ME_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0689_05_Tu_NON_SEN_NON_IMP_LO_CER_DA_SOL_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0690_01_Sconosciuto_NON_HO_VIS_NES_HOU_PAS_DI_QUA_MA_CI_SON_IO_SE_LO_DES_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0691_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0692_01_Sconosciuto_SAL_BEL_VAG_HAI_BIS_DI_QUA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0692_02_Tu_UHM_S_STO_CER_UN_CER_ROD_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0692_03_Sconosciuto_CHI_SIA_VOU_DI_SIC_NON_MEV_DI_AVE_IO_INV_SON_VIC_SON_BEL_E_POS_SOD_OGN_TUO_DES_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0692_04_Tu__OK_ORA_HO_DA_FAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0692_05_Sconosciuto_CEV_NON_ESI_A_TOV_DA_ME_QUA_SEN_LA_MIA_MAN_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0693_01_Sconosciuto_VAI_FAI_LE_TUE_COS_MA_NON_ESI_A_TOV_DA_ME_QUA_SEN_LA_MIA_MAN_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo3":
            partiDialogo = []
            nome = LI.SCONOSCIUTO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cercatoHansInAlloggiProfughi"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0694_01_Sconosciuto_CCI_SER_QUA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0694_02_Tu_STO_CER_GLI_ALL_PRO_SAI_DA_CHE_PAR_DEV_AND_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0694_03_Sconosciuto_GLI_ALL_MI_SEM_A_NOR_DI_QUI_NO_FOR_ERA_NOR_NON_MI_RIC_BEN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0694_04_Tu_OK_INT_VAD_VER_NOR_POI_CHI_IN_GIR_GRA_MIL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0694_05_Sconosciuto_DDI_NIENTE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cercatoHansInAlloggiProfughi"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0695_01_Sconosciuto_NON_MI_RIC_BEN_DOV_SIA_GLI_ALL_FOR_NOR_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0696_01_Tu_SCU_HAI_VIS_UN_RAG_DI_NOM_HAN_DA_QUE_PAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0696_02_Sconosciuto_NO_NON_CON_NES_HAN_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0697_01_Sconosciuto_NON_CON_NES_HAN_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0698_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza1":
            partiDialogo = []
            nome = LI.SCONOSCIUTA
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0699_01_Tu_CIA_SIG_SAI_DIR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0699_02_Sconosciuta_SIG_MA_CHI_TI_CRE_DI_ESS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0699_03_Tu__SCU_NON_VOL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0699_04_Sconosciuta_MA_VAI_A_CHI_SCU_A_QUA_ALT_MAL_SIG_MA_COM_SI_PER_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0700_01_Sconosciuta_SME_DI_DIS_ALT_CHI_LE_GUA_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0701_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città4"]:
        if tipo == "OggettoFinestraCasaDavid":
            partiDialogo = []
            nome = "OggettoFinestraCasaDavid"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0702_01_Tu_DA_QUE_FIN_SI_VED_LIN_DEL_CAS_SEM_ENO_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo1":
            partiDialogo = []
            nome = LI.SCONOSCIUTO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cercatoHansInAlloggiProfughi"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0703_01_Tu_SCU_SAI_DIR_DOV_POS_TRO_GLI_ALL_PRO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0703_02_Sconosciuto_CER_BEL_CON_ANC_DEI_POS_MIG_IN_CUI_POT_ALL_E_DIV_PER_BEN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0703_03_Tu_NO_NON_IO_HO_SOL_BIS_DI_AND_AGL_ALL_PRO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0703_04_Sconosciuto_EDD_TI_OFF_LA_BIR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0703_05_Tu_SEN_NON_IMP_FAC_DA_SOL_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["uscitoCasaDavidDopoSuicidio"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0704_01_Tu_SCU_PER_CAS_HAI_VIS_UNA_PER_DI_NOM_HAN_DA_QUE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0704_02_Sconosciuto_NO_HO_VIS_TE_BAM_E_QUE_MI_BAS_TI_VA_DI_UNI_A_NOI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0704_03_Tu_NO_NON_VOL_SOL_SAP_SE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0704_04_Sconosciuto_EDD_TI_OFF_LA_BIR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0704_05_Tu_SEN_NON_IMP_FAC_DA_SOL_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["uscitoCasaDavidDopoSuicidio"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0705_01_Tu_QUE_DUE_SON_PAR_UBR_MEG_EVI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoCasaDavidDopoSuicidio"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0074_01_Sconosciuto_EHI_BEL_DOV_VAI_COS_DI_FRE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0074_02_Tu_EH__STO_AND_HAI_BIS_DI_QUA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0074_03_Sconosciuto_PER_GIR_TUT_SOL_INT_ALL_VIL_DEL_COM_SEI_LA_NUO_PUT_PER_CAS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0074_04_Tu_COS_NO_MI_HA_OSP_PER_CIO_SON_ARR_IER_NOT_IN_CIT_E_GLI_ALL_PRO_ERA_PIE_QUI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0074_05_Sconosciuto_QUE_MAI_LE_PRE_SEM_PI_PIC_EH_HAH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0074_06_Tu_NO_NON_ORA_DEV_AND_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0074_07_Sconosciuto_DOV_VUO_AND_HAI_AVU_TUT_LA_NOT_PER_DAV_ORA_NON_HAI_UN_PO_DI_TEM_PER_ME_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0074_08_Tu_NO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0074_09_Sconosciuto_EHI_DAT_UNA_CAL_IO_E_IL_MIO_AMI_VOL_SOL_PAR_UN_PO_CON_TE_NON_POS_NON_SIA_ABB_ALT_PER_ESS_DEG_DI_UNA_CON_PUT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0074_10_Sconosciuto_DOV_CRE_DI_AND_VIE_QUI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["incontratoIDueAggressori"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0706_01_Sconosciuto_VIE_QUI_TRO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uccisoPrimoAggressore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0075_01_Sconosciuto_BRU_TRO_SCH_LHA_UCC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0075_02_Tu__SST_LON_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0075_03_Sconosciuto_VIE_QUI_SCH_PUT_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo3":
            partiDialogo = []
            nome = LI.SCONOSCIUTO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cercatoHansInAlloggiProfughi"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0707_01_Tu_SAL_SIG_PER_CAS_SAI_DIR_DOV_DEV_AND_PER_GLI_ALL_PRO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0707_02_Sconosciuto_MA_SAL_BEL_VUO_VEN_A_DIV_CON_NOI_LA_PRI_BIR_TE_LA_OFF_IO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0707_03_Tu_NO_NON_VOG_BIR_GLI_ALL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0707_04_Sconosciuto_TIE_BEV_UN_PO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0707_05_Tu_SCU_ORA_DEV_AND_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["uscitoCasaDavidDopoSuicidio"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0708_01_Tu_SAL_SIG_SAP_DIR_SE_UN_CER_HAN__PAS_DI_QUI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0708_02_Sconosciuto_MA_SAL_BEL_VUO_VEN_A_DIV_CON_NOI_LA_PRI_BIR_TE_LA_OFF_IO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0708_03_Tu_NO_NON_VOG_BIR_STO_CER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0708_04_Sconosciuto_TIE_BEV_UN_PO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0708_05_Tu_SCU_ORA_DEV_AND_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["uscitoCasaDavidDopoSuicidio"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0709_01_Tu_QUE_NON_MI_SEN_NEA_COM_FA_A_ESS_UBR_GI_A_QUE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoCasaDavidDopoSuicidio"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0710_01_Tu__EHI_VA_TUT_BEN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0710_02_Sconosciuto_CER_BAM_E_TU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0710_03_Tu_SS_TUT_BEN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0710_04_Sconosciuto_OTTIMO_HAHAHA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0710_05_Tu__)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città5"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoInCitta9CercandoRod"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0076_01_Tu_OH_NO_NON__NEA_QUI_C_SOL_QUE_PAP_INC_ADD_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoCittàPostTempoBloccato"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0077_01_Tu_CON_QUE_SIL_SEM_QUA_UN_ALT_POS_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo1":
            partiDialogo = []
            nome = LI.SCONOSCIUTO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0711_01_Tu_SCUSATE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0711_02_Sconosciuto_SMACK_MWAH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0711_03_Tu__EHI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0711_04_Tu_NON_MI_SEN_NEA_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0712_01_Tu_POS_ASP_QUA_VOG_QUE_DUE_NON_FIN_MAI_DI_BAC_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0713_01_Tu_COM_POS_CHE_SIA_ANC_QUI_A_BAC_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo2":
            partiDialogo = []
            nome = LI.SCONOSCIUTO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0714_01_Tu_SCUSATE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0714_02_Sconosciuto_NON_ADE_SIA_MOL_OCC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0714_03_Tu_OK_OK_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0715_01_Sconosciuto_NON_ADE_SIA_MOL_OCC_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0716_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo3":
            partiDialogo = []
            nome = LI.SCONOSCIUTO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0717_01_Tu_CHIEDO_SCUSA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0717_02_Sconosciuto_NO_LEV_DAI_PIE_VOI_CON_LE_VOS_OP_IMP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0717_03_Tu_MA_NON_VOG_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0717_04_Sconosciuto_BAS_TOG_DI_TOR_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0718_01_Sconosciuto_QUE_TIZ_NON_VUO_PAR_SEM_ANC_MOL_ARR_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0719_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0720_01_Tu_SALVE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0720_02_Sconosciuto__HAI_VIS_QUE_PAP_QUA_MI_AVV_MI_URL_AC_NEG_MA_CHE_SIG_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0720_03_Tu_AH_NON_LO_SO__UNO_STR_PAP_COM_HAI_VIS_PAS_DI_QUA_UN_CER_ROD_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0720_04_Sconosciuto_NO_NON_CON_NES_ROD_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0720_05_Tu_OK_GRA_LO_STE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0721_01_Sconosciuto_QUA_MI_AVV_QUE_PAP_MI_URL_SEM_AC_NEG_MA_CHE_SIG_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza1":
            partiDialogo = []
            nome = LI.SCONOSCIUTA
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0722_01_Tu_POS_INT_UN_ATT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0722_02_Sconosciuta_SMACK_MWAH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0722_03_Tu__EHI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0722_04_Tu_NON_MI_SEN_NEA_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0723_01_Tu_POS_ASP_QUA_VOG_QUE_DUE_NON_FIN_MAI_DI_BAC_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0724_01_Tu_COM_POS_CHE_SIA_ANC_QUI_A_BAC_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza2":
            partiDialogo = []
            nome = LI.SCONOSCIUTA
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cercatoHansInAlloggiProfughi"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0725_01_Tu_SCU_MI_HAN_DET_CHE_IN_CIT_CI_SON_DEG_ALL_PER_I_PRO_SAI_DIR_DA_CHE_PAR_SON_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0725_02_Sconosciuta_NO_NON_SAP_VIV_QUI_DA_POC_SCU_POT_PRO_A_CHI_A_QUE_RAG_LAG_CI_HO_PAR_UNA_VOL_SEM_SAP_TUT_DI_QUE_CIT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0725_03_Tu_QUE_TIP_LOS_COL_CAP_CHE_CI_STA_FIS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0725_04_Sconosciuta_S_DIC_CHE_CI_STA_GUA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0725_05_Tu_OGN_TAN_SI_GIR_DA_UNA_PAR_MA_POI_GUA_NUO_IN_QUE_DIR_FOR__SOL_UNA_MIA_IMP_MA__STR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0725_06_Sconosciuta_MA_NO_LHO_CON__STA_MOL_GEN_CON_ME_DI_SIC_SAP_AIU_ANC_TE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0725_07_Tu_MMH_VA_BEN_TAN_VAL_PRO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0726_01_Tu_SCU_STO_CER_UN_RAG_DI_NOM_HAN_LHA_PER_CAS_VIS_PAS_DA_QUE_PAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0726_02_Sconosciuta_NO_NON_HO_CON_NES_HAN_VIV_QUI_DA_POC_SCU_POT_PRO_A_CHI_A_QUE_RAG_LAG_CI_HO_PAR_UNA_VOL_SEM_SAP_TUT_DI_QUE_CIT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0726_03_Tu_QUE_TIP_LOS_COL_CAP_CHE_CI_STA_FIS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0726_04_Sconosciuta_S_DIC_CHE_CI_STA_GUA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0726_05_Tu_OGN_TAN_SI_GIR_DA_UNA_PAR_MA_POI_GUA_NUO_IN_QUE_DIR_FOR__SOL_UNA_MIA_IMP_MA__STR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0726_06_Sconosciuta_MA_NO_LHO_CON__STA_MOL_GEN_CON_ME_DI_SIC_SAP_AIU_ANC_TE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0726_07_Tu_MMH_VA_BEN_TAN_VAL_PRO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0727_01_Sconosciuta_PRO_A_CHI_A_QUE_TIZ_LAG_LHO_CON__STA_MOL_GEN_CON_ME_DI_SIC_SAP_AIU_ANC_TE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0728_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza3":
            partiDialogo = []
            nome = LI.SCONOSCIUTA
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0729_01_Tu_CHIEDO_SCUSA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0729_02_Sconosciuta_NO_PER_FAV_STI_AFF_UNA_CON_IMP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0729_03_Tu_OK_OK_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0730_01_Sconosciuta_STI_AFF_UNA_CON_IMP_NON_INT_PER_FAV_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0731_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
        elif tipo.startswith("OggettoCassaMercante"):
            partiDialogo = []
            nome = "OggettoCassaMercante"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0732_01_Tu_QUE_CAS_SEM_MOL_INV_MA_HO_LA_SEN_CHE_QUE_PAP_INI_A_URL_SE_PRO_AD_APR_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0733_01_Tu_C_UN_SAC_DI_ROB_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoPappaLibroSonoroMercante":
            partiDialogo = []
            nome = LI.PAPPAGALLO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = True
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0734_01_Pappagallo_NOME_UTENTE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0734_02_Tu_COSA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0734_03_Pappagallo_SAR_ACC_CON_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0734_04_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0734_05_Pappagallo_COMPRA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0734_06_Tu__FAI_PAR_DEL_CON_DI_ROD_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0734_07_Pappagallo_COMPRA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0734_08_Tu__OK_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = True
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0735_01_Pappagallo_NOM_UTE_SAR_COM_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = True
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0736_01_Tu_IO_PRE_UN_ATT_DEL_COS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0736_02_Pappagallo__)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città6"]:
        if tipo == "GuardiaCitta":
            partiDialogo = []
            nome = LI.SOLDATO
            if x == GlobalHWVar.gpx * 16:
                if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["trovatoAlloggiProfughi"]:
                    oggettoDato = False
                    avanzaStoria = True
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0078_01_Tu_CHI_SCU_SOL__POS_ENT_NEG_ALL_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDP._0078_02_Soldato_NON__CON_LAC_A_QUE_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0078_03_Tu_VA_BEN_STO_CER_UN_RAG_CHE_HA_PI_O_MEN_LA_MIA_ET_E_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDP._0078_04_Soldato_GLI_ALL_SON_VUO_AL_MOM_VEN_SGO_TUT_LE_MAT_SE_HAI_BIS_RIP_STA_E_TE_NE_VER_ASS_UNO_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0078_05_Tu_NO_NON_HO_BIS_DI_UN_ALL_STO_CER_UN_RAG_DI_NOM_HAN__MI_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDP._0078_06_Soldato__VIE_FOR_INF_SUI_RES_I_REG_SON_GI_STA_PRE_E_NON__PER_CON_PER_SCO_DI_INT_PRI_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0078_07_Tu_OK_MA_IO_VOL_SOL_SAP_SE_MIO_FRA_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDP._0078_08_Soldato_I_REG_SON_GI_STA_PRE_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0078_09_Tu_OK_OK_)
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0737_01_Tu__INU_PAR_CON_QUE_SOL_CON_A_DIR_I_REG_SON_STA_PRE_)
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0738_01_Tu_QUE_SOL_NON_HA_INT_DI_DIR_NIE_)
                    partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 19:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0739_01_Tu_SAL_MI_STA_CHI_SE_FOS_POS_ENT_NEG_ALL_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0739_02_Soldato_ENT_NEG_ALL_A_QUE_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0739_03_Tu_S_NON_LO_SO_TE_LO_STO_CHI_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0739_04_Soldato_ME_LO_STA_CHI_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0739_05_Tu__S_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0739_06_Soldato_S_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0739_07_Tu__S_TI_STO_CHI_SE_POS_ENT_NEG_ALL_ADE_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0739_08_Soldato_ADESSO_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0739_09_Tu__S_ADE__POS_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0739_10_Soldato_EHMM_S_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0739_11_Tu_S_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0739_12_Soldato_S_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0739_13_Tu__OK_OK_S_PER_NON_RIE_AD_APR_CRE_CHE_SIA_CHI_A_CHI_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0739_14_Soldato_CRE_CHE_SIA_CHI_A_CHI_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0739_15_Tu_S_POT_APR_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0739_16_Soldato_POTREI_APRIRTI_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0739_17_Tu__POT_APR_LA_POR_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0739_18_Soldato_LA_PORTA_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0739_19_Tu__HAI_LA_CHI_PER_APR_QUE_POR_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0739_20_Soldato_EHMM_S_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0739_21_Tu_PER_ALL_PUO_APR_LA_POR_PER_FAV_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0739_22_Soldato_EHM_NON_CE_LHO_LA_CHI_IO_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0739_23_Tu_COS_VA_BEN_VA_BEN_CHI_AL_TUO_COL_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0739_24_Soldato_CHI_AL_MIO_COL_)
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0740_01_Tu_NON_HO_INT_DI_RIA_UNA_CON_CON_QUE_)
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0741_01_Tu_QUE_SOL_NON_MI_SAR_DAI_)
                    partiDialogo.append(dialogo)
        elif tipo == "Pazzo1":
            partiDialogo = []
            nome = "Rallo"
            if avanzamentoDialogo == 0:
                nome = LI.SCONOSCIUTO
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0742_01_Sconosciuto_TU_SAI_PER_SON_QUI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0742_02_Tu__NO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0742_03_Sconosciuto_PER_SON_PAZ_IL_MIO_NOM__RAL_E_SON_IL_CAP_DI_QUE_PER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0742_04_Tu_OK_RAL_HAI_PER_CAS_VIS_UN_RAG_DI_NOM_HAN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0742_05_Sconosciuto_NO_IO_SON_RAL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0742_06_Tu_OK_)
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = -1
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0743_01_Tu_CIAO_RALLO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0743_02_Sconosciuto_RAL_SAI_CHI_SON_IO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0743_03_Tu__SEI_RAL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0743_04_Sconosciuto_SON_RIL_VUO_PAR_AL_TES_SO_PAZ_O_SON_RAL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0743_05_Tu_UHM_VA_BEN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0743_06_Sconosciuto_DOMANDA_)
                dialogo.append(LDS._0743_07_Sconosciuto_PRI_DOM_SEI_PAZ_O_SEI_RAL_)
                dialogo.append(LDS._0743_08_Sconosciuto_SONO_PAZZO_)
                dialogo.append(LDS._0743_09_Sconosciuto_SONO_RALLO_)
                dialogo.append(LDS._0743_10_Sconosciuto_SONO_SARA_)
                dialogo.append(LDS._0743_11_Sconosciuto_NON_LO_SO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0743_12_Sconosciuto_RISPOSTA_)
                dialogo.append(LDS._0743_13_Sconosciuto_UUULULULU_)
                dialogo.append(LDS._0743_14_Sconosciuto_SEI_RALAU_)
                dialogo.append(LDS._0743_15_Sconosciuto_E_IO_SON_TRR_)
                dialogo.append(LDS._0743_16_Sconosciuto_MMH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0743_17_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0743_18_Sconosciuto__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0743_19_Tu___FIN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0743_20_Sconosciuto_NO_IL_TES_TOR_TOR_TOR_QUA_MEN_TE_LO_ASP_)
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 2:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0744_01_Sconosciuto_IL_TES_TOR_TOR_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo1":
            partiDialogo = []
            nome = LI.SCONOSCIUTO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0745_01_Tu_CIA_HAI_PER_CAS_INC_UN_RAG_DI_NOM_HAN_NEG_ALL_IER_NOT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0745_02_Sconosciuto_SPI_NON_CON_NES_CON_QUE_NOM_A_MEN_CHE_NON_FOS_NUO_E_NON_LAB_VIS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0745_03_Tu_S__NUO_DOV_ESS_ARR_IER_NOT_SUL_TAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0745_04_Sconosciuto_BEH_MI_ADD_ABB_VEL_CI_STA_CHE_NON_LAB_VIS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0745_05_Tu_MMH_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0746_01_Sconosciuto_MI_SON_ADD_ABB_PRE_IER_NOT_CI_STA_CHE_IL_TUO_HAN_SIA_ARR_PI_TAR_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0747_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0748_01_Tu_EHI_CIA_SCU_IL_DIS_HAI_PER_CAS_VIS_UN_CER_ROD_QUA_INT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0748_02_Sconosciuto_ROD_LHO_VIS_IER_OGG_NON_SI__ANC_PRE_IN_CIT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0748_03_Tu_MMH_E_SAI_DOV_POT_ESS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0748_04_Sconosciuto_BEH__SEM_IN_GIR_LO_VED_SPE_AND_VER_LA_SEL_ARI_E_RAR_ANC_VER_IL_PAS_MON_MA_NON_TI_CON_DI_CER_IN_QUE_POS_FOS_IN_TE_LO_ASP_QUI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0748_05_Tu_MMH_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0749_01_Sconosciuto_VED_SPE_ROD_AND_VER_LA_SEL_ARI_E_RAR_ANC_VER_IL_PAS_MON_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo2":
            partiDialogo = []
            nome = LI.SCONOSCIUTO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0750_01_Tu_CIA_RAG_VIV_NEG_ALL_PRO_VOI_DUE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0750_02_Sconosciuto_S_QUA_C_POS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0750_03_Tu_AVE_PER_CAS_INC_UN_RAG_DI_NOM_HAN_IER_NOT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0750_04_Sconosciuto_HAN_NO_NON_CER_NES_DI_NUO_IER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0750_05_Tu_SICURO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0750_06_Sconosciuto_BEH_NON_AL_CEN_PER_CEN_MA_IO_NON_HO_INC_NES_CON_QUE_NOM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0750_07_Tu_OK_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0751_01_Sconosciuto_NON_C_NES_NEG_ALL_CHE_SI_CHI_HAN_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0752_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0753_01_Tu_SAL_SIG_HAI_PER_CAS_VIS_UN_MER_INC_UN_PO_LOS_PAS_DI_QUA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0753_02_Sconosciuto_INT_ROD_PAS_RAR_IN_QUE_PAR_DEL_CIT_MA_OGN_TAN_LO_VED_ARR_DAL_PAS_MON_IND_VER_IL_CEN_CIT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0753_03_Tu_DAL_PAS_MON_OK_GRA_MIL_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0754_01_Sconosciuto_ROD_PAS_RAR_IN_QUE_PAR_DEL_CIT_MA_OGN_TAN_LO_VED_ARR_DAL_PAS_MON_IND_VER_IL_CEN_CIT_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza1":
            partiDialogo = []
            nome = LI.SCONOSCIUTA
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0755_01_Tu_SCU_PER_CON_A_FAR_AVA_E_IND_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0755_02_Sconosciuta_COS_BEH_PER_GUA_QUE_SOL_NON__IRR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0755_03_Tu__NO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0755_04_Sconosciuta__COS_BEL_E_SEN_DEV_AND_A_PAR_MA_NON_SO_COS_DIR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0755_05_Tu_NON_ANDARCI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0755_06_Sconosciuta__VA_BEN_VAD_NO_ASP_DEV_PRI_PEN_A_QUA_DA_DIR_SEN_SEM_UNA_PAZ_SFI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0755_07_Tu_MA_NON_VA_BEH_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0756_01_Sconosciuta_CI_SON_VAD__NO_NO_DEV_PRE_QUA_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0757_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza3":
            partiDialogo = []
            nome = LI.SCONOSCIUTA
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0758_01_Sconosciuta_COS_CRE_DI_FAR_QUE_TRO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0758_02_Tu_DI_CHE_STA_PAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0758_03_Sconosciuta_DI_QUE_TRO_BIO_LAG_PEN_DI_POT_PRO_COL_MIO_RAG_LUI__MIO_LE_TRO_COM_LEI_NON_SI_DEV_NEA_AZZ_A_GUA_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0759_01_Sconosciuta_COS_CRE_DI_FAR_QUE_TRO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0760_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città7"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0079_01_Tu_OK_PER_AND_DA_NEI_DEV_PRO_VER_SUD_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0079_02_Tu__TU_CON_A_SEG_VER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0079_03_Impo__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0079_04_Tu__MH_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo3":
            partiDialogo = []
            nome = LI.SCONOSCIUTO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0761_01_Sconosciuto_SE_VUO_POS_AIU_PER_S_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0761_02_Tu__CIA_SIE_DEG_STU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0761_03_Sconosciuto_S_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0761_04_Tu_OK_E_COS_STA_STU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0761_05_Sconosciuto_HAI_BIS_DI_QUA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0761_06_Tu_NO__CHE_NON_SON_MAI_STA_UNA_STU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0761_07_Sconosciuto_AH_BEA_TE_ALM_TI_SEI_EVI_TUT_QUE_INU_STR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0761_08_Tu_STR_STU_NON__UNA_COS_TRA_CIO_TE_NE_STA_L_COL_TUO_LIB_SEN_CHE_NES_TI_DIC_NIE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0761_09_Sconosciuto_S_SAR_BEL_SE_NES_TI_DIC_NIE_PUR_AND_A_SCU_NON_SIG_SEM_STU_SIG_APP_PI_COS_POS_IN_MEN_TEM_POS_UNA_SPE_DI_COR_CON_IL_TEM_PER_QUA_ARG_TI_VEN_ASS_CHE_TI_PIA_O_NO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0761_10_Tu_OH_CI_SON_DEI_LIM_DI_TEM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0761_11_Sconosciuto_CI_SON_DEI_PRO_DA_RIS_E_PRO_CHE_SI_VOG_VAN_CON_ALT_PRO_CRE_LA_SCU_NON__UN_BEL_POS_IN_CUI_ST_PUR_PER__ANC_LUN_PER_I_RAG_DEL_MIA_ET_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0761_12_Tu_BEH_HA_SEN_CHE_CI_SIA_DEI_PRO_PER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0761_13_Sconosciuto_NON_QUA_SI_RIC_DI_COM_TUT_IL_SAP_DI_PLA_O_ARI_IN_QUA_GIO_A_QUE_PUN_PER_POT_TEN_IL_PAS_TI_LIM_A_LEG_E_RIP_LEG_E_RIP_FIN_NON_SEI_PRO_PER_LIN_NON_TI_RIM_TEM_PER_RIF_O_PER_APP_GLI_ARG_DEV_SEG_QUE_CHE_TI_DIC_NEI_TEM_CHE_TI_DIC_COM_PU_ESS_PIA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0761_14_Tu_OH_QUI_A_NES_PIA_STU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0761_15_Sconosciuto_STU__UNA_COS_BEN_DIV_DA_QUE_CHE_SI_FA_A_SCU_LEG_E_RIP_NON_VUO_DIR_STU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0761_16_Tu_OK_ALL_A_NES_PIA_LA_SCU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0761_17_Sconosciuto_ESA_CIO_ALL_MAG_PAR_ALM_C_CHI_IGN_TUT_QUE_E_VA_AVA_SEN_PEN_E_CHI_INV__ADD_FEL_DI_ESE_GLI_ORD_E_SOD_I_PRO_MA_NON_LI_BIA_CRE_CHE_SIA_QUE_IL_MOD_GIU_DI_CRE_CHI_SON_IO_PER_DIR_CHE_SBA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0761_18_Tu_E_PER_TU_CON_AD_AND_ALL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0761_19_Sconosciuto_PER_ALT_MIO_PAD_MI_CAC_DI_CAS_E_NON_SON_ANC_PRO_PER_AVE_UNA_MIA_IND_UN_GIO_MAG_LO_SAR_NON_VED_LOR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0761_20_Tu_OK_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0762_01_Sconosciuto_BEA_TE_CHE_NON_DEV_AND_A_SCU_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0763_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza1":
            partiDialogo = []
            nome = LI.SCONOSCIUTA
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0764_01_Sconosciuta__DOM_HO_DUE_INT_CIA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0764_02_Tu_CIA_COS_FAT_QUI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0764_03_Sconosciuta_STI_AND_A_STU_NEL_NOS_GRU_NON_C_SPA_PER_ALT_PER_E_ORA_NON_ABB_TEM_DA_PER_DOB_CON_PER_LO_STU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0764_04_Tu_AVE_UN_GRU_PER_STU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0764_05_Sconosciuta_S_SIA_SOL_NOI_DUE_MA__GI_ABB_COS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0764_06_Tu_OK_HO_CAP_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0765_01_Sconosciuta_NEL_NOS_GRU_NON_C_SPA_PER_ALT_PER_E_ORA_NON_ABB_TEM_DA_PER_DOB_CON_PER_LO_STU_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0766_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città8"]:
        if tipo == "GuardiaCitta":
            partiDialogo = []
            nome = LI.SOLDATO
            if x == GlobalHWVar.gpx * 9:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0767_01_Tu_SAL_SOL_DA_QUA_TEM_SEI_QUI_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0767_02_Soldato__DA_STA_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0767_03_Soldato_OK_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0767_04_Soldato__NON_DIS_I_SOL_IN_SER_RAG_)
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0768_01_Soldato_SE_NON_SER_EVI_DI_DIS_I_SOL_IN_SER_)
                    partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 12:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0769_01_Tu_CHI_SCU_SOL_DEV_ATT_QUE_POR_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0769_02_Soldato_CHI_SEI_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0769_03_Tu_SONO_SARA_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0769_04_Soldato__)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0769_05_Tu__)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0769_06_Soldato__E_PER_DOV_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0769_07_Tu_BEH_PER_NON_LO_SO_VOL_VED_COS_C_DIE_QUE_POR_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0769_08_Soldato__)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0769_09_Tu__VOL_VED_IL_CAS_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0769_10_Soldato_NON__PER_LAC_AI_CIV_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0769_11_Tu_OK_)
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0770_01_Soldato_NON__PER_LAC_AI_CIV_)
                    partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 19:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0771_01_Tu_PER_SOR_QUE_POR_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0771_02_Soldato__LA_POR_DEL_CAS_DOB_ASS_CHE_NON_CI_SIA_ACC_IND_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0771_03_Tu__IL_TUO_CAS_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0771_04_Soldato___IL_CAS_DEL_RE_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0771_05_Tu_E_PER_SEI_TU_A_SOR_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0771_06_Soldato__IL_RE_HA_ALT_A_CUI_PEN_NON_PU_CER_MET_DI_GUA_AL_SUO_CAS_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0771_07_Tu_E_A_COS_DEV_PEN_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0771_08_Soldato_COS_CHI_CRE_CHE_GES_LA_CIT_TUT_I_SER_IL_CON_DEI_TER_LE_GUA_CHE_GAR_LA_SIC_IN_CIT_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0771_09_Tu_IL_RE_GES_TUT_QUE_E_HA_ABB_SOL_PER_MAN_TUT_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0771_10_Soldato_CER__SUP_DA_TUT_IL_POP_CHE_LO_SEG_E_LO_ADO_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0771_11_Tu__PER_IL_POP_DOV_SU_DEI_SOL_CHE_HAN_IL_COM_DI_NON_FAR_ENT_NEL_CAS_IL_POP_STE_VOG_DIR__GRA_AL_POP_SE_IL_RE_PU_PER_DI_MAN_UN_CAS_QUI_PER_NON_DOV_ESS_ACC_A_TUT_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0771_12_Soldato_PER_QUE_NON__IL_CAS_DI_TUT__IL_SUO_CAS_E_SUA_MAE_SA_COS_MEG_PER_IL_SUO_CAS_E_PER_IL_SUO_POP_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0771_13_Tu_BEH_IO_SO_CHE_SAR_FEL_DI_ENT_NEL_CAS_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0771_14_Soldato_VUO_MET_IN_DIS_LE_DEC_DEL_RE_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0771_15_Tu_NO_NO_HO_CHI_SOL_PER_CER_DI_AVV_AL_SUO_SAP_IL_MIO_INT_ERA_QUE_DI_COM_NON_DI_OFF_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0771_16_Soldato_BENE_)
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0772_01_Soldato_NON_TI__PER_ENT_NEL_CAS_SE__QUE_CHE_VUO_SAP_)
                    partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 22:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0773_01_Soldato__COS_DA_GUA_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0773_02_Tu_NIE_POT_AVE_ANC_UNA_COM_LA_TUA_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0773_03_Soldato_EH_SON_ARM_FAB_PER_LA_GUA_CIT__VIE_POR_SE_NON_NE_FAI_PAR_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0773_04_Tu_OK_)
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0774_01_Soldato_QUE_ARM_VEN_FAB_ESC_PER_LA_GUA_CIT__VIE_POR_SE_NON_NE_FAI_PAR_)
                    partiDialogo.append(dialogo)
        elif tipo == "Ragazzo1":
            partiDialogo = []
            nome = LI.SCONOSCIUTO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0775_01_Tu_SAL_SIG_SAI_PER_CAS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0775_02_Sconosciuto_ASP_SOL_UN_SEC_DEV_RIU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0775_03_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0775_04_Sconosciuto_FOR_DA_QUE_ANG_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0775_05_Tu_CHE_STA_FAC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0775_06_Sconosciuto_MMH_NO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0775_07_Tu_STA_GUA_LA_TOR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0775_08_Sconosciuto_UN_PO_PI_A_DES_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0775_09_Tu__EH_S__PRO_UNA_BEL_TOR_SAR_UN_PEC_PER_LA_SUA_MAG_ANC_SOL_PER_UN_ATT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0775_10_Sconosciuto_EH_LO_CRE_ANC_TU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0775_11_Tu_CER_SOP_LA_PUN__QUA_DI_INC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0775_12_Sconosciuto_VER_GLI_ARC_HAN_PEN_A_QUA_DI_VER_GEN_PER_LA_PAR_PI_ALT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0775_13_Tu_SAR_PRO_UN_PEC_SE_QUA_NON_POT_VED_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0775_14_Sconosciuto_GI_PRO_PER_QUE_LHA_MES_IN_ALT_COS_TUT_POS_VED_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0775_15_Tu_HAN_PEN_PRO_A_TUT_E_A_TUT_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0776_01_Sconosciuto_GLI_ARC_HAN_PEN_A_QUA_DI_VER_GEN_PER_LA_PAR_PI_ALT_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0777_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo2":
            partiDialogo = []
            nome = LI.SCONOSCIUTO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0778_01_Tu_CHE_STA_CER_DI_FAR_CON_QUE_SCA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0778_02_Sconosciuto_PRO_UN_BEL_NIE_DEI_CAL_HAN_FAT_IL_NID_SUL_TET_E_LA_SCA__TRO_BAS_PER_ARR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0778_03_Tu_E_NON_POT_LAS_STA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0778_04_Sconosciuto_CER_CHE_NO_OGN_VOL_CHE_APR_LA_FIN_ME_LI_RIT_IN_CAS_CHE_SVO_FAC_UN_RUM_TER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0778_05_Tu_TIE_LE_FIN_CHI_ALL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0778_06_Sconosciuto_AH_CER_ECC_LA_SOL_COM_AVE_FAT_A_NON_PEN_TI_RIN_DAV_MOL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0778_07_Tu_VA_BEN_SCU_VOL_ESS_DAI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0778_08_Sconosciuto_CERTO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0779_01_Sconosciuto_OGN_VOL_CHE_APR_LA_FIN_MI_RIT_IN_CAS_QUE_CAL_CHE_SVO_IN_GIR_FAC_UN_RUM_TER_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0780_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo3":
            partiDialogo = []
            nome = LI.SCONOSCIUTO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0781_01_Tu_SER_UNA_MAN_CON_QUE_SCA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0781_02_Sconosciuto_NO_CRE_CHE_LAS_PER__TRO_COR_PER_ARR_AL_TET_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0781_03_Tu_SIC_SEC_ME_CON_UN_PIC_SAL_ALL_FIN_CIO_NON_MAN_MOL_PER_ARR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0781_04_Sconosciuto_UN_PIC_SAL_VUO_PRO_TE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0781_05_Tu_NO_NO_ERA_SOL_UNI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0782_01_Sconosciuto_QUE_MAL_SCA__TRO_COR_PER_ARR_AL_TET_POT_PRO_A_RIA_MA_CON_COS_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0783_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza3":
            partiDialogo = []
            nome = LI.SCONOSCIUTA
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0784_01_Sconosciuta_QUE_DUE_SON_LE_PER_PI_IMP_CHE_ABB_MAI_VIS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0784_02_Tu_PER_LI_STA_GUA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0784_03_Sconosciuta_MI_GOD_LO_SPE_PRI_O_POI_PRO_QUA_DI_FOL_PER_SAL_SUL_TET_HAH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0784_04_Tu_PER_NON_VAI_AD_AIU_ANZ_STA_QUI_A_DER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0784_05_Sconosciuta_EHI_NON__MIC_IL_TET_DI_CAS_MIA_QUE_POI_QUE_TIP_CON_I_CAP_BIO_SEM_SUL_PUN_DI_ESP_DA_UN_MOM_ALL_NON_ME_LO_VOG_PER_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0785_01_Sconosciuta_QUE_TIP_SEM_SUL_PUN_DI_ESP_DA_UN_MOM_ALL_NON_ME_LO_VOG_PER_PER_NIE_AL_MON_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0786_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città9"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoUscitaSelvaAridaCercandoRod"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0080_01_Tu_OK_SPE_CHE_SIA_QUI_DA_QUA_PAR_)
                partiDialogo.append(dialogo)
        elif tipo == "GuardiaCitta":
            partiDialogo = []
            nome = LI.SOLDATO
            if x == GlobalHWVar.gpx * 16:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0787_01_Tu_QUE_USC_DOV_POR_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0787_02_Soldato_PRO_VER_SUD_ARR_ALL_SEL_ARI_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0787_03_Tu_LA_SEL_ARI__UN_BEL_POS_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0787_04_Soldato__NO__ORR_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0787_05_Tu_OH_OK_)
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0788_01_Soldato_PRO_VER_SUD_ARR_ALL_SEL_ARI_)
                    partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 20:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0789_01_Tu_QUE__LUS_SUD_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0789_02_Soldato_S_LA_SEL_ARI_BLO_IL_PAS_VER_IL_LAG__SCO_PRO_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0789_03_Tu_NON_SI_PU_ATT_LA_SEL_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0789_04_Soldato_NON_SE_SEI_DA_SOL_E_NON_ADD_CI_SON_DEL_CRE_MOL_PER_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0789_05_Tu_TIPO_CINGHIALI_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0789_06_Soldato_I_CIN_HAN_GI_LAS_DA_UN_PEZ_QUE_ZON_ADE__PIE_DI_CRE_VEL_HO_VIS_MOL_PER_TOR_IN_CON_CHE_NON_MI_VA_NEA_DI_RIC_PER_NON_PAR_DI_TUT_I_DI_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0789_07_Tu_OH_GRA_DEL_)
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0790_01_Soldato_HO_VIS_MOL_PER_TOR_DAL_SEL_IN_CON_CHE_NON_MI_VA_NEA_DI_RIC_FAR_MEG_A_NON_AVV_IN_QUE_)
                    partiDialogo.append(dialogo)
        elif tipo == "Ragazza3":
            partiDialogo = []
            nome = LI.SCONOSCIUTA
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0791_01_Sconosciuta_EHI_RAG_SEI_VEN_A_FRE_LA_FRU_MIG_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0791_02_Tu_COS_NO_STA_SOL_PAS_DI_QUI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0791_03_Sconosciuta_HAH_NON_PRE_STA_SCH_IN_POC_LO_SAN_MA_QUA_C_LA_FRU_MIG_DI_TUT_IL_MER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0791_04_Tu_OH_E_TU_COM_FAI_A_SAP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0791_05_Sconosciuta_HO_GUA_GLI_ALT_VAN_SEM_DAL_PAR_E_PEN_DI_DOV_ARR_PRI_PER_AVE_LE_COS_MIG_IN_REA_BAS_VEN_QUI_E_HAI_TUT_LA_ROB_MIG_IN_QUA_MOM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0791_06_Tu_E_IN_COS_QUE_FRU__MEG_DEL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0791_07_Sconosciuta_QUA_LE_PER_SCE_LE_COS_SUC_CHE_LE_TOC_LE_STR_E_LE_RIM_SUL_BAN_IN_QUE_MOD_LA_FRU_SI_ROV_MA_NON_QUI_QUI_NON_VIE_MAI_NES_A_ROV_QUE_BEL_MEL__UN_BEL_VAN_EH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0791_08_Tu_CERTO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0792_01_Sconosciuta_QUA_NON_VIE_NES_A_ROV_QUE_BEL_MEL__UN_BEL_VAN_EH_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0793_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["città10"]:
        if tipo == "GuardiaCitta":
            partiDialogo = []
            nome = LI.SOLDATO
            if y == GlobalHWVar.gpy * 7:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0794_01_Tu_DOV_POR_QUE_STR_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0794_02_Soldato_AL_PAS_MON_NON_TRO_NIE_DI_BUO_L_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0794_03_Tu__DIS_DA_QUI_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0794_04_Soldato_NON_DOV_AVV_DA_QUE_PAR__PIE_DI_BES_ALA_CHE_TI_PIO_ADD_A_VEL_EST_ELE_PER_ATT_COI_LOR_AFF_ART_SEN_UNA_DOV_PRE__MOR_CER_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0794_05_Tu__ANC_PI_PER_DEL_FOR_CAD_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0794_06_Soldato_TSK_LA_FOR__UNO_SCH_A_CON__IL_POS_PEG_IN_CUI_QUA_POS_AND_)
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0795_01_Soldato_IL_PAS_MON__IL_POS_PI_PER_IN_CUI_UN_ESS_UMA_POS_AND_)
                    partiDialogo.append(dialogo)
            elif y == GlobalHWVar.gpy * 11:
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0796_01_Soldato_RAG_TI_SCO_VIV_DI_PRO_PER_QUE_STR_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0796_02_Tu_PER_COS_C_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0796_03_Soldato_NON__SIC_NON_SIA_STA_FAT_DIV_SPE_IL_TER__ANC_LAR_INE_E_QUE_POC_CHE__CON__ABB_PER_CON_DI_NON_IND_OLT_)
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0797_01_Soldato_NON_AVV_NEL_PAS_MON_QUE_TER_NON__SIC_)
                    partiDialogo.append(dialogo)
        elif tipo == "Ragazzo3":
            partiDialogo = []
            nome = LI.SCONOSCIUTO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0798_01_Tu_STA_CER_QUA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0798_02_Sconosciuto_NO_SON_RIM_CHI_FUO_DI_CAS_DEV_ASP_CHE_MIA_MAD_TOR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0798_03_Tu_TUA_MADRE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0798_04_Sconosciuto_S_HA_PRE_LEI_LE_CHI_AVE_DET_CHE_SAR_RIM_A_CAS_INV_HA_PEN_BEN_DI_USC_SEN_DIR_NIE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0798_05_Tu_MAG__IN_CAS_HAI_PRO_A_BUS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0798_06_Sconosciuto_CER_CHE_HO_PRO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0799_01_Sconosciuto_MA_QUA_ARR_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0800_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza1":
            partiDialogo = []
            nome = LI.SCONOSCIUTA
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0801_01_Sconosciuta_MMH_QUE_CAS_HAN_QUA_CHE_NON_VA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0801_02_Tu_PAR_DEI_MUR_STO_CHE_CON_VER_LAL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0801_03_Sconosciuta_DEI_MUR_CHE_SEM_STO_CRE_SI_TRA_DEL_PRO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0801_04_Tu_DIC_A_ME_SEM_UGU_STO_DA_QUA_PRO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0801_05_Sconosciuta_MMH_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0802_01_Sconosciuta_QUE_CAS_HAN_QUA_CHE_NON_VA_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0803_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo


