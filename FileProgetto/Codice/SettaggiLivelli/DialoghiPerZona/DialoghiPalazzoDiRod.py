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

    if tipo.startswith("OggettoDictCofanetto"):
        nome = LI.COFANETTO
        if tipo == "OggettoDictCofanettoAperto":
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1203_01_Tu_MA_SI__PRE_LA_MIA_ROB_)
            partiDialogo.append(dialogo)
        elif tipo == "OggettoDictCofanettoChiuso":
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1204_01_Tu_ADE_NON_MI_SER_QUE_ROB_)
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["palazzoDiRod1"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["rodEntratoNelPalazzo"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0338_01_Tu_ROD_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0338_02_Tu___CAS_SUA_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoFreddoNonPercepitoPassoMontanoPostTempoBloccato"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0339_01_Tu_SIA_ABB_VIC_ADE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0339_02_Tu__CHE_SIA_STA_ROD_A_FAR_QUE_CAS_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostAttaccoDiImpoOstile"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0340_01_Tu__MA_CHE_CAV_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoPortaPalazzoDiRod":
            partiDialogo = []
            nome = "OggettoPortaPalazzoDiRod"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoVistoRodEntrareNelPalazzo"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0341_01_Tu_ROD_)
                partiDialogo.append(dialogo)
        elif tipo == "Mercante":
            partiDialogo = []
            nome = "Rod"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPreBussataPalazzo"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0342_01_Tu__ROD_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0342_02_Rod__CHI__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0342_03_Tu_ROD_SON_IO_SAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0342_04_Rod_SAR_MA_CHE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0342_05_Tu_POSSO_ENTRARE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0342_06_Rod_UHM_NO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0342_07_Tu_DAI_ROD_SI_CON_QUA_FUO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0342_08_Rod__PER_SEI_VEN_FIN_QUI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0342_09_Tu_DEV_PAR_DI_UNA_COS_MI_MAN_NEI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0342_10_Rod__)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["palazzoDiRod2"]:
        if tipo == "Mercante":
            partiDialogo = []
            nome = "Rod"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["entratoInPalazzoDiRod"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0343_01_Rod__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0343_02_Tu_CAV_C_UN_CAS_INC_QUA_DEN_E_UN_SAC_DI_POL_OVU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0343_03_Rod__HAI_INC_NEI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0343_04_Tu__S_ERA_DAV_INT_A_IMP_MA_GLI_MAN_DEG_STR_PER_STU_MI_HA_MAN_DA_TE_PER_CHI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0343_05_Rod_CHE_LAV_PER_LUI_ADE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0343_06_Tu_NO_NOI_STI_COL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0343_07_Rod_AHH_STA_COL_CER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0343_08_Tu_S_COLLABORIAMO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0343_09_Rod_S_S_E_COL_FIN_LA_PER_DI_TUO_FRA_NON_SAR_CON_IMM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0343_10_Tu_NON__UNA_VA_BEH_NON_GLI_HO_DET_DI_HAN_ALL_FIN_HO_PEN_CHE_FOS_MEG_LAS_AND_DOV_VUO_COM_DIC_TE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0343_11_Rod_OH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0343_12_Tu_COM_TI_DIC_DEG_STR_CHE_SER_A_NEI_QUE__LA_LIS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0343_13_Rod_OK_VEDIAMO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0343_14_Rod_PER_PEN_CHE_IO_ABB_QUE_ROB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0343_15_Tu__NON_CE_LI_HAI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0343_16_Rod__GLI_HAI_DET_CHE_FAI_PAR_DEL_CON_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0343_17_Tu_S_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0343_18_Rod_MMH_OK_CE_LI_HO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["rodArrivatoAlTavoloDegliStrumenti"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0344_01_Tu__SON_QUE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append({lingua: testo % GlobalGameVar.monetePerGliStumentiPerNeil for lingua, testo in LDP._0344_02_Rod_ESA_FAN___STR__U_MON_.items()})
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0344_03_Tu_COS_MA_DAI_NE_HAI_UN_SAC_DI_QUE_AFF_COM_FAN_A_COS_COS_TAN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0344_04_Rod__IL_LOR_VAL_TU_NON_TI_PRE_LAS_CHE_IL_VEC_TRO_SGA_LE_SUE_MON_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0344_05_Tu_MA_NON_UFF_NON_MI_HA_LAS_MON_SIC_SAP_CHE_SAR_SER_E_NE_AVR_A_PAL_LUI_PER_NON_ME_LE_HA_DAT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0344_06_Rod_BEH_SE_NE_HA_COS_TAN_UN_MOT_CI_SAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0344_07_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0344_08_Rod_MA_ORM_PUO_OCC_TU_NO_SON_SIC_CHE_SE_TU_FAR_BEN_LA_TUA_PAR_DI_COL_LUI_RIC_CON_ALT_IMP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0344_09_Tu_MA_PER_MI_VOL_FRE_CHE_VI_HO_FAT_STA_COL_VOI_DUE_PER_PRE_PI_MON_POS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0344_10_Rod_TSK_CO_FAC_SOL_I_MIE_INT_COM_TUT_COM_TE_CHE_SE_POT_AVE_QUE_STR_ALL_MET_DEL_PRE_LI_PRE_SUB_SEN_FAR_DOM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0344_11_Tu_MA_CHE_CEN_NON_TI_STA_FRE_IN_QUE_CAS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0344_12_Rod_NO_MI_STA_SOL_CON_A_PAG_DI_MEN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0344_13_Tu_NON__LA_STE_COS_SE_CI_FOS_UNA_SCO_PER_EVI_UN_LAB_IO_NON_TI_FAR_PAG_UNA_MAP_PER_ATT_DIC_CHE_NON_CI_SON_STR_ALT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0344_14_Rod_BEH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0344_15_Tu_VER_ROD_O_DOV_DIR_ROD_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0344_16_Rod_NO_NON_NON_DOV_E_PER_QUA_RIG_LA_SCO_NON_POT_DIR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0344_17_Tu_CER_ROD_NON_POT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0344_18_Rod__QUE__UNA_STR_DI_NEI_E_VUO_CHE_RIM_SEG_TI_AVR_UCC_SE_TI_AVE_VIS_PAS_DI_L_E_PRO_SAR_VEN_A_CER_ANC_ME_DOP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0344_19_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0344_20_Rod_POI_SEI_LIB_DI_RIF_LE_MIE_OFF_SE_NON_TI_VAN_BEN_TE_LHO_GI_DET_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0344_21_Tu__MH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0344_22_Rod__E_LA_PRO_VOL_CHE_DOV_PAS_PER_IL_MIO_AVA_EVI_ALM_DI_ROV_TRA_LE_MIE_COS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0344_23_Tu_MI_SER_LA_CHI_PER_USC_NON_ME_NE_FRE_NIE_DEL_TUA_ROB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0344_24_Rod_OK_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["chiesteMonetePerGliStrumenti"]:
                if monetePossedute < GlobalGameVar.monetePerGliStumentiPerNeil:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1205_01_Tu_NON_HO_ABB_MON_E_QUE_CAP_NON_ABB_IL_PRE_PER_ME_)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = LI.STR_DI_ROD
                    avanzaStoria = True
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0345_01_Tu_ECC_LE_TUE_SCH_MON_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDP._0345_02_Rod_OH_OTTIMO_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0345_03_Tu__)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDP._0345_04_Rod__RIM_ARR_PER_SEM_ADE_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0345_05_Tu_NO_SOL_FIN_NE_HO_VOG_ROD_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDP._0345_06_Rod__BENE_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0345_07_Tu_COS_C_TI_D_FAS_IL_TUO_NOM_COM_OLF_TI_POS_CHI_SOL_OL_SE_VUO_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDP._0345_08_Rod_OH_SAN_CIE_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0345_09_Tu__)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDP._0345_10_Rod__)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0345_11_Tu__)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDP._0345_12_Rod__GI_FIN_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0345_13_Tu__UFF_CHE_STU_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDP._0345_14_Rod__)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0345_15_Tu__)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDP._0345_16_Rod__ALM_SU_QUE_SIA_DAC_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0345_17_Tu_SEN_OLF_NON_ROM_NON_SO_PER_MI_SON_INN_PER__SIC_COL_TUA_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDP._0345_18_Rod_CER_OVV_PRE_GLI_STR_COL_E_TOR_DAL_TUO_COL_CHE_SIC_NON_VED_LOR_DI_RIP_LA_VOS_COL_)
                    partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dateMonetePerStrumentiPerStudiareImpo"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0346_01_Tu_VA_BEN_E_TU_TOR_DAI_TUO_CON_CON_CHE_SIC_NON_VED_LOR_DI_RIP_LA_VOS_CON_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0346_02_Rod_CONFRATERNITA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0346_03_Tu_S_QUE_CHE__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0346_04_Rod_E_NON__UNA_COS_DA_RI_ESI_SEM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0346_05_Tu_CER_ROD_CER_AH_A_PRO_QUE_PAP_CHE_VEN_LA_TUA_MER_SON_TUO_CON_ANC_LOR_O_TI_STA_SOL_FRE_LA_ROB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0346_06_Rod_QUE_NON_SON_SEM_PAP_SON_PAP_SON_SI_USA_PER_REG_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0346_07_Tu_OH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0346_08_Rod_PUO_CHI_A_LOR_LA_MER_QUA_NON_CI_SON_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0346_09_Tu__OK_MA_COM_CIO_COM_FAN_A_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0346_10_Rod__PAR_IN_BAS_A_QUE_CHE_GLI_PAS_PER_LA_TES_IN_PRA_BAS_SUS_I_RIC_GIU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0346_11_Tu_OH_E_TU_TI_SEI_MES_AD_ADD_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0346_12_Rod__HO_RUB_LID_A_UN_COR_PER_PIR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0346_13_Tu__UN_COR_PER_PIR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0346_14_Rod_UN_COR_PER_PIR_S_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0346_15_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0346_16_Rod_COM_SE_VUO_FAR_PI_IN_FRE_PER_TOR_PUO_USA_IL_MIO_TUN_POR_DIR_ALL_LO_TRO_SUL_RET_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0346_17_Tu__OK_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRodDopoAverPresoStrumenti"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0347_01_Rod_CHE_CI_FAI_ANC_QUI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0347_02_Tu_ROD_VOL_CHI_TU_SAI_QUA_SUL_RIC_DI_NEI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0347_03_Rod__HO_LET_QUA_S_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0347_04_Tu_OH_CHE_COS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0347_05_Rod_COS_SU_LA_VIT_LA_REA_ROB_STR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0347_06_Tu_E_COS_NE_PEN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0347_07_Rod_COS_NE_DEV_PEN_SON_TEO_SEN_MA_SOL_TEO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0347_08_Tu_TU_COS_PEN_CHE_SIA_LA_VIT_CIO_FIS_INT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0347_09_Rod__NON_CRE_CHE_NES_SIA_MAI_RIU_A_DAR_UNA_DEF_ESA_SE_DOV_DEF_IN_BAS_A_COM_SIA_FAT_DIR_TIP_IL_PEZ_DI_CER_DOV_C_LA_COS_MA_LE_PIA_NON_CE_LHA_NEA_UN_CER_QUI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0347_10_Tu_MMH_FOR_LE_PIA_NON_SON_VIV_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0347_11_Rod_E_COM_CRE_CON_LA_MAG_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0347_12_Tu_DIR_CHE_CRE_GRA_ALL_VI_NON__MEN_ASS_FOR_SI_MUO_E_BAS_COM_FA_IL_VEN_IL_MAR_E_TUT_CI_CHE_NON_HA_UN_CER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0347_13_Rod_NON_CRE_SIA_PRO_LA_STE_COS_E_POI_NEA_GLI_IMP_HAN_UN_CER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0347_14_Tu_DAV_IMP_NON_HA_IL_CER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0347_15_Rod__NO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0347_16_Tu_COM_POSSIBILE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0347_17_Rod_NON_LO_SO_ADE_DEV_TOR_A_LAV_SAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0347_18_Tu_ASP_LA_POR_SUL_RET__BLO_NON_SI_APR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0347_19_Rod_AH_GI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRodAperturaRetroPalazzo"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = True
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0348_01_Rod_FAT_ADE_LAS_ALL_MIE_QUE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0348_02_Tu_OH_COM_ASP_POS_PRE_DEL_COS_DAL_CAT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0348_03_Rod_S_SBRIGATI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = True
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1206_01_Rod_SON_MOL_OCC_ADE_SE_TI_SER_QUA_PRE_E_LAS_ALL_MIE_QUE_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoPalazzo1PostEsplosioneVulcano"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0349_01_Tu__ROD_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoPappaLibroSonoroMercante":
            partiDialogo = []
            nome = LI.PAPPAGALLO
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1207_01_Pappagallo_COS_DES_OH_MIO_SIG_SUP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1207_02_Tu_MMH_NIE_PER_IL_MOM_TOR_A_RIP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1207_03_Pappagallo_S_MIO_SIG_SUP_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = True
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1208_01_Tu_IO_PRE_UN_ATT_DEL_COS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1208_02_Pappagallo__)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoScatoloniPalazzoRodA":
            partiDialogo = []
            nome = "OggettoScatoloniPalazzoRodA"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1209_01_Tu_NON_MI_SER_NIE_DI_QUE_ROB_ADE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1210_01_Tu_CI_SON_UN_SAC_DI_SCA_IMP_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1211_01_Tu_DEGLI_SCATOLONI_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoScatoloniPalazzoRodB":
            partiDialogo = []
            nome = "OggettoScatoloniPalazzoRodB"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1212_01_Tu_NON_MI_SER_NIE_DI_QUE_ROB_ADE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1213_01_Tu_ALT_SCA_IMP_QUA_ROB_HA_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1214_01_Tu_DEGLI_SCATOLONI_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiInElaborazioneRod":
            partiDialogo = []
            nome = "OggettoAppuntiInElaborazioneRod"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoRodAperturaRetroPalazzo"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1215_01_Tu_SON_APP_SU_NON_SO_FOR__UNA_SPE_DI_MAP_O_DEG_SCH_INC_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1216_01_Tu_STA_SCR_CON_UNA_FOG_ASS__IMP_CAP_QUA_LE_FRA_SON_TUT_STO_E_SI_INC_TRA_LOR_COM_FAR_A_RIL_)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1217_01_Tu_SON_I_MIE_APP_POI_LI_MET_DA_QUA_PAR_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1218_01_Tu_APP_DI_ROD_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiArmaInquinanteFaseA":
            partiDialogo = []
            nome = "OggettoAppuntiArmaInquinanteFaseA"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1219_01_Tu_OH_I_MIE_VEC_APP_SUL_DEL_DI_IMP_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1220_01_Tu_SON_APP_SU_UN_PRO_DI_ROD_SEM_DEI_MET_PER_EST_QUA_DAG_IMP_TIP_UN_LIQ_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1220_02_Tu_CI_SON_DEI_DIS_CHE_MOS_LIN_DEG_IMP_SON_PAR_STR_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1221_01_Tu_APP_DI_ROD_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiArmaInquinanteFaseB":
            partiDialogo = []
            nome = "OggettoAppuntiArmaInquinanteFaseB"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1222_01_Tu_I_MIE_APP_SUL_MAX_POM_IDR_LA_PRO_VOL_NON_CI_SAR_INT_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1223_01_Tu_SON_APP_SU_UN_PRO_DI_ROD_NON_CAP_BEN_COS_SIA_SEM_UNA_SPE_DI_RUB_GIG_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1223_02_Tu_CI_SON_ALC_FOR_CHE_SIM_LA_TRA_DI_UN_GET_DAC_SPR_A_VAR_VEL_E_ANG_RIS_AL_TER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1223_03_Tu_A_COS_DOV_SER_UNA_ROB_DEL_GEN_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1224_01_Tu_APP_DI_ROD_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["palazzoDiRod3"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoEntrataPalazzoDiRodConTempoBloccato"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0350_01_Tu__OK_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiApprendimentoPappagalli":
            partiDialogo = []
            nome = LI.APP_DI_ROD
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoVistoStanzaPappagalliPalazzoDiRod"]:
                oggettoDato = LI.CHIAVE_SEMINTERRATO
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0351_01_Tu_SON_DEG_APP_DI_ROD_INC_COM_AL_SOL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0351_02_AppuntiDiRod__PRO_DI_APP_CON_LA_NUO_MAN_CI_MAN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0351_03_AppuntiDiRod__IL_PAP_N22_NON_FA_CHE_RIP_NA_NAL_MA_CHE_SIG_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0351_04_AppuntiDiRod__AVE_DET_SE_NUO_FOR_CI_SON_STA_PRO_DUR_LA_SPE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0351_05_AppuntiDiRod___ASS_NON_RIE_PI_AD_ASS_I_VOL_ALL_FRA_PRO_CON_RIT_PI_REA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0351_06_Tu_OH_QUI__A_QUE_CHE_SER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0351_07_Tu_OH_C_ANC_UNA_CHI_QUA_IN_MEZ_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1225_01_Tu_SON_APP_DI_ROD_IN_CUI_SI_LAM_DEL_DI_ALC_PAP_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1226_01_Tu_APP_DI_ROD_)
                partiDialogo.append(dialogo)
        elif tipo == "Mercante":
            partiDialogo = []
            nome = "Rod"
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1227_01_Tu_ROD_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1227_02_Rod__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1227_03_Tu__ROD_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1227_04_Rod__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1227_05_Tu__BLOCCATO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1227_06_Tu_STA_DIP_ME_COM_SON_ADE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1227_07_Tu_QUI_HA_GI_VIS_COM_SON_DIV_)
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1228_01_Tu_STA_MET_MOL_DET_NEL_VOL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1228_02_Tu_CER_DI_REN_IN_QUA_MOD_RIC_RIS_A_A_CHI_SIA_STA_OPE_IN_QUE_MOD_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1229_01_Tu_STA_DIP_ME_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoScatoloni":
            partiDialogo = []
            nome = "OggettoScatoloni"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1230_01_Tu_SCATOLONI_)
            partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiArmaturaDiRod":
            partiDialogo = []
            nome = LI.APP_DI_ROD
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                if avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1231_01_Tu_SON_DEI_PRO_DI_UNA_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1231_02_AppuntiDiRod__I_MAT_SON_FIN_SUF_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1231_03_AppuntiDiRod__LAR__QUA_COM_E_PRE_POT_TES_DIR_SUL_CAM_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1231_04_AppuntiDiRod__LA_RAC_DI_IMP_VER_NOT_INC_IL_VEC_TRO_LA_SME_DI_LAM_DEL_SCA_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1231_05_Tu_CHE_CEN_LAR_CON_GLI_IMP_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1231_06_Tu__E_POI_HA_UN_TRA_DI_IMP_CON_NEI_)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1232_01_Tu_SON_DEI_PRO_DI_ROD_PER_UNA_)
                    partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1233_01_Tu_APP_DI_ROD_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoLetteraStopTrattamentiEstetici":
            partiDialogo = []
            nome = LI.LET_DI_NEI
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                if avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1234_01_Tu_C_UNA_LET_DI_NEI_QUA_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1234_02_LetteraDiNeil_ROD_TI_INF_CHE_I_TRA_EST_SU_SAR_DA_TE_SUG_SON_STA_SOS_IN_CON_A_DEL_ANO_COM_DEL_SOG_IN_FAS_DI_RIC_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1234_03_LetteraDiNeil__TI_INV_A_RIV_E_COR_LA_TER_E_DI_TES_SU_SOG_NON_CRU_RIM_IN_ATT_DI_NOV_NEI_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1234_04_Tu__)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1235_01_Tu__UNA_LET_DI_NEI_IN_CUI_COM_A_ROD_DI_AVE_SOS_I_SUO_TR_EST_DUR_LA_MIA_RIA_)
                    partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1236_01_Tu__LA_LET_DI_NEI_IN_CUI_COM_A_ROD_DI_AVE_SOS_I_SUO_TR_EST_DUR_LA_MIA_RIA_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoQuadroSara":
            partiDialogo = []
            nome = "OggettoQuadroSara"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1237_01_Tu_SON_IO_COM_PRI_)
            partiDialogo.append(dialogo)
        elif tipo == "OggettoQuadroSaraRianimata":
            partiDialogo = []
            nome = "OggettoQuadroSaraRianimata"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1238_01_Tu_SON_IO_COM_SON_ADE_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1239_01_Tu_GLI_HO_LAS_UN_BIG_IN_CUI_GLI_SPI_COS_MI__SUC_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoPappaLibroSonoroApprendista":
            partiDialogo = []
            nome = "OggettoPappaLibroSonoroApprendista"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1240_01_Tu_CI_SON_UN_SAC_DI_PAP_QUI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1240_02_Tu__QUI_CHE_LI_ADD_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1241_01_Tu_SON_I_PAP_DI_ROD_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["palazzoDiRod4"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["presoChiavePianoInterratoPalazzoRod"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0352_01_Tu_UNA_LEVA_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sbloccatoCaverna"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0353_01_Tu_OK_CRE_DI_POT_ENT_NEL_CAV_QUA_FUO_ADE_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoMucchioImpo":
            partiDialogo = []
            nome = LI.MUC_DI_IMP
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                if avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1242_01_Tu_MA_)
                    partiDialogo.append(dialogo)
                elif avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1243_01_Tu_MA_CHE_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1243_02_Tu_LI_HA_LI_HA_PRE_LUI_NON_NEI_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1243_03_Tu_E_LI_HA_UCC_)
                    partiDialogo.append(dialogo)
                elif avanzamentoDialogo == 2:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1244_01_Tu_SON_TUT_MOR_HAN_UN_BUC_ENO_IN_TES_)
                    partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1245_01_Tu_SON_GLI_IMP_DI_ROD_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoLevaPalazzo":
            partiDialogo = []
            nome = "OggettoLevaPalazzo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoVistoLevaNelPalazzoDiRod"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0354_01_Tu_VED_SE_FUN_)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1246_01_Tu_NON_POS_TIR_ADE_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1247_01_Tu__UNA_LEV_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoSbarreCaverna":
            partiDialogo = []
            nome = "OggettoSbarreCaverna"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1248_01_Tu_SON_DEL_SBA_)
            partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiPazzoNellaCaverna":
            partiDialogo = []
            nome = LI.APP_DI_ROD
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                if avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1249_01_Tu_APP_DI_ROD_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1249_02_AppuntiDiRod__DEV_LUI_QUE_PAZ_MON_CHE_CON_AD_AGG_INT_ALL_DEL_CAV_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1249_03_AppuntiDiRod__ADE_ERA_PRO_QUA_SOP_SPE_NON_SIA_RIU_A_ENT_PRI_CHE_CHI_LE_SBA_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1249_04_AppuntiDiRod__NON_LHO_PI_VIS_N_SEN_IN_GIR_SPE_DI_NON_TRO_MOR_IN_UN_CUN_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1249_05_Tu_IL_PA_MON_)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1250_01_Tu_APP_DI_ROD_IN_CUI_PAR_DI_UN_PA_MON_CHE_SI_AGG_INT_ALL_DEL_CAV_)
                    partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1251_01_Tu_APP_DI_ROD_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiRaccoltaImpo":
            partiDialogo = []
            nome = LI.APP_DI_ROD
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                if avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1252_01_Tu_APP_DI_ROD_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1252_02_AppuntiDiRod__IL_TRO_HA_INI_A_INT_AGL_IMP_POT_GUA_QUA_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1252_03_AppuntiDiRod__LI_HO_PRE_TUT_NON_CE_NE_SON_PI_ALL_ADE_HO_TUT_IL_TEM_PER_CAP_COM_SFR_LA_SIT_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1252_04_AppuntiDiRod__HO_DAT_UNO_A_COM_SON_FAT_HAN_UN_BEL_PO_DI_LIQ_ENE_NEL_TES_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1252_05_AppuntiDiRod__HO_INI_IL_PRE_STO_RIC_UNA_QUA_INC_DI_LIQ_OGN_IMP_VAL_PI_DI_TRE_IMP_CON_QUE_QUA_POS_TES_SER_LA_MIA_NUO_POM_IDR_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1252_06_Tu_DIO_SAN_MA__PAZ_)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1253_01_Tu_SON_GLI_APP_DI_ROD_IN_CUI_SPI_COM_HA_QUA_STE_GLI_IMP_)
                    partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1254_01_Tu_APP_DI_ROD_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiMacchinarioIdraulico":
            partiDialogo = []
            nome = LI.APP_DI_ROD
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                if avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1255_01_Tu_APP_DI_ROD_SU_UNA_PO_IDR_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1255_02_AppuntiDiRod__COS_TER_LA_POM_IDR_HA_PAS_TUT_I_TES_SEN_INT_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1255_03_AppuntiDiRod__FIN_HO_ABB_LIQ_PER_MOS_SER_COS__IN_GRA_DI_FAR_LA_POM_NEI_NE_VOR_SAP_DI_PI_QUA_VED_IL_GET_PRO_DIR_SUL_LIN_NEM_ORI_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1255_04_AppuntiDiRod__DIM_CON_LA_GIU_N19_NON_HA_RET_IL_SIS_HA_CON_A_POM_E_LER__ESP_NEL_SEL_STA_SUC_UN_MAC_NEL_GIR_DI_QUA_GIO_SAR_TUT_DIS_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1255_05_AppuntiDiRod__MER_DOV_RIF_TUT_I_TES_COL_LIQ_ENE_COM_HO_FAT_A_NON_PEN_BR_RIC_ROD_ACQ__LIQ_ENE_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1255_06_Tu_MA_QUI__STA_ROD_)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1256_01_Tu_SON_GLI_APP_DI_ROD_IN_CUI_SPI_COM_HA_INQ_LA_SEL_ARI_)
                    partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1257_01_Tu_APP_DI_ROD_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoVascaMacchinario":
            partiDialogo = []
            nome = "OggettoVascaMacchinario"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1258_01_Tu_C_UNO_STR_LIQ_QUA_DEN_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1259_01_Tu__UNA_VAS_PIE_DI_LIQ_ENE_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoMacchinario":
            partiDialogo = []
            nome = "OggettoMacchinario"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1260_01_Tu_NON_SO_COS_SIA_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1261_01_Tu__LA_POM_IDR_DI_ROD_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["palazzoDiRod5"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoConclusivoRodAlPalazzo"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0355_01_Tu_ECC_IL_TUN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0355_02_Tu_ODD_QUE_COS_ARR_FIN_QUI_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoTuboPalazzoRod":
            partiDialogo = []
            nome = "OggettoTuboPalazzoRod"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1262_01_Tu_IL_TUB__A_POS_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1263_01_Tu__UNA_SPE_DI_TUB_MOL_SEM_FAT_CON_PEL_DI_SER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1263_02_Tu_DEV_OPE_DI_ROD_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1264_01_Tu__UN_TUB_)
                partiDialogo.append(dialogo)
        elif tipo == "BibliotecarioOperato":
            partiDialogo = []
            nome = u"René"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoRodDalPalazzoPreLancioMissile"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0356_01_Tu__NEIL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0356_02_Ren_NEI_SE_N_AND_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0356_03_Tu_REN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0356_04_Ren__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0356_05_Tu_SCU_NON_NON_TI_AVE_RIC_SEN_BAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0356_06_Ren__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0356_07_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0356_08_Ren__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0356_09_Tu__CHE_SEI_VEN_A_FAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0356_10_Ren_PER_VED_DI_PER_NON_VOG_FER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0356_11_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0356_12_Ren__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0356_13_Tu__DOV_SEI_STA_PER_TUT_QUE_TEM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0356_14_Ren__DA_NEI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0356_15_Tu__DOV_NEI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0356_16_Ren_SE_N_AND_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0356_17_Tu_ANDATO_DOVE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0356_18_Ren_NON_LO_SO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0356_19_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0356_20_Ren__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0356_21_Tu_QUE_MAL_SCH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0356_22_Ren__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0356_23_Tu__E_SAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0356_24_Ren_ANDATA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0356_25_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0356_26_Ren__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0356_27_Tu__VA_BEN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0356_28_Ren__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0356_29_Tu__NON_CRE_CHE_TRO_UN_LUO_DOV_POS_SAL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0356_30_Ren_NES_LUO_PRE_LA_VIT_DOP_OGG_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0356_31_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0356_32_Ren__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0356_33_Tu__HO_TRO_DA_NEI_QUE_PRO_COS_SI_ASP_CHE_FAC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0356_34_Ren__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0356_35_Tu__SIE_TUT_SPA_DA_UN_MOM_ALL_NON_CER_PI_NES_SOL_QUE_CAP_DEL_RE_CHE_QUA_HA_CAP_CHE_QUE_SUL_CO_ERA_TUT_CAZ_HA_PEN_BEN_DI_RIV_A_ME_PER_CON_LAV_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0356_36_Ren__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0356_37_Tu__E_POI_TU_CHE_HAI_FAT_PER_TUT_QUE_TEM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0356_38_Ren__NIENTE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0356_39_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0356_40_Ren_NON_CER_NIE_DA_FAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0356_41_Tu__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRenéRod1PreLancioMissile"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0357_01_Tu__NO_CER_NIE_DA_FAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0357_02_Ren__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0357_03_Tu__TRA_QUA_MIN_SAR_ALL_POR_DEL_CIT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0357_04_Ren__ABB_PER_PRE_UN_PUL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0357_05_Tu_S_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRod1PreLancioMissile"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0358_01_Tu_AH_TI_HO_FRE_DEG_IMP_UNA_VOL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0358_02_Ren_LO_SO_ROD_)
                partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo


