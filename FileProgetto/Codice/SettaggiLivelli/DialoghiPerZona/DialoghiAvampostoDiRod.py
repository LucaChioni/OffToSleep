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
            dialogo.append(LDS._0394_01_Tu_MA_SI__PRE_LA_MIA_ROB_)
            partiDialogo.append(dialogo)
        elif tipo == "OggettoDictCofanettoChiuso":
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0395_01_Tu_ADE_NON_MI_SER_QUE_ROB_)
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["avampostoDiRod1"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoUscitaSelva"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0001_01_Tu_OK_DOP_LA_SEL_DOB_COS_IL_LAG_CHE_NON__QUI_PER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0001_02_Impo__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0001_03_Tu__NON_GUA_COS_LE_IST_ERA_CHI_CER_ANC_TU_QUA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0001_04_Tu_EHI_MA_QUE__ROD_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["eliminatoPersonaggioOggettoPerEnigmaMappaLabirinto"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0002_01_Tu_FAT_ADE_DOV_POT_ORI_BEN_L_DEN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0002_02_Impo__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0002_03_Tu__LO_SO_LO_SO_ROD_NON_ISP_MOL_FID_MA_CI_POS_FID_DI_LUI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["trovatoChiaveAvampostoDiRod"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0003_01_Tu__NON_C_FOR__TOR_IN_CIT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0003_02_Tu_MI_SA_CHE_DOB_RIA_LA_SEL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0003_03_Impo__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0003_04_Tu__MMH_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostEsplosioneDelVulcano2"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0004_01_Tu__STA_USC_UN_SAC_DI_FUM_DA_QUE_MON_)
                partiDialogo.append(dialogo)
        elif tipo == "Mercante":
            partiDialogo = []
            nome = "Rod"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoAvampostoDiRod"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0005_01_Tu_ROD_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0005_02_Rod_OH_CAZZO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0005_03_Tu_EHI_CAL_SON_IO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0005_04_Rod_CHE_CI_FAI_TU_QUI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0005_05_Tu_STO_CER_DI_MA_TU_VIV_QUI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0005_06_Rod_NO_QUE__IL_MIO_AVA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0005_07_Tu_UN_AVA_CER_COM_HO_FAT_A_NON_CAP_HA_PRO_LAS_DI_UN_CLA_AVA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0005_08_Rod_NON__UN_CL_AVA__MOL_DI_PI_COM_CRE_CHE_POS_SOS_LIN_ECO_DI_QUE_REG_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0005_09_Tu_MA_SIC_GRA_A_QUE_BAR_OVV_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0005_10_Rod_AVA_GRA_A_QUE_AVA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0005_11_Tu_CERTO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0005_12_Rod_CHE_NON__UN_POS_PER_RAG_COM_TE_PER_SEI_QUI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0005_13_Tu__STO_CER_DI_AND_DA_UN_CER_NEI_MI_HAN_DET_CHE_SAR_ARR_AL_SUO_CAS_ATT_LA_SEL_ARI_E_POI_COS_IL_LAG_MA_SON_ACC_CAP_IN_QUE_INC_AVA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0005_14_Rod_DA_NEI_PER_QUA_MOT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0005_15_Tu_A_QUA_PAR_LUI_CON_GLI_SPO_NEL_TER_MI_HAN_DET_DI_PRO_A_CHI_A_LUI_PER_MIO_FRA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0005_16_Rod_AH_TUO_FRA_HAI_DEC_DI_CON_A_TOR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0005_17_Tu_NON_VOG_TOR_VOG_SOL_SAP_SE_STA_BEN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0005_18_Rod_MH_E_POI_NON_TI_OFF_MA_TRA_TUT_LE_COS_DI_CUI_SI_DEV_OCC_NEI_NON_CRE_CHE_AVR_VOG_DI_STA_A_SEN_UNA_RAG_QUA_CHE_BUS_AL_SUO_CAS_IN_CER_DI_AIU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0005_19_Tu_S_PU_DAR_MA_IO_POT_ATT_LA_SUA_ATT_CON_QUE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0005_20_Rod_UN_IMP_NE_AVR_A_DEC_DI_QUE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0005_21_Tu__DAV_MI_AVE_DET_CHE_NON_SE_NE_TRO_PI_IN_GIR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0005_22_Rod_BEH_DOP_CHE_SON_MOR_NEI_LI_HA_RAC_TUT_PER_STU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0005_23_Tu_OH_MA_LUI_NON__MOR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0005_24_Rod__MH_S_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0005_25_Tu_NON_GUA_COS_NON_PUO_AVE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0005_26_Rod_NO_NO_FIG_MA_SAP_CHE_SE_TI_PRE_A_NOM_DEL_CON_AVR_UN_POT_CON_MOL_MAG_POT_SPI_UN_BEL_PO_DI_MON_AL_VEC_TRO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0005_27_Tu__VEC_TRO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0005_28_Rod_NEIL_INTENDO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0005_29_Tu_S_AVE_NON_IMP_NON_MIN_ROD_SAI_DA_CHE_PAR__IL_LAG_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0005_30_Rod__NON_DEV_AND_VER_IL_LAG_QUE__UNA_VEC_STR_NON_PI_PER_AL_GIO_DOG_PER_AND_DA_NEI_DEV_PER_FOR_ATT_IL_LAB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0005_31_Tu_MA_DAI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0005_32_Rod_MA_NON_PRE_HO_QUI_UNA_MAP_CHE_PU_AIU_TE_LA_POS_PRE_PER_SOL___STR__U_MON_ % GlobalGameVar.monetePerLaMappaDelLabirinto)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0005_33_Tu_NO_NON_CI_POS_CRE_E_POI_COS_VUO_DIR_CHE_ME_LA_PRE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0005_34_Rod_CHE_DOV_MEM_E_POI_RID_NON_PUO_DI_CER_PAR_CON_LA_MIA_MAP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0005_35_Tu_MA_SEI_COM_IMP_COM_FAC_A_MEM_TUT_LE_STR_DI_UN_LAB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0005_36_Rod_NON_DEV_MEM_TUT_E_POI_NON_SEI_OBB_AD_ACC__SOL_UNO_CHE_TI_OFF_PUO_ANC_RIF_SE_CRE_CHE_NON_TI_SER_MA_SAP_CHE_CI_SON_MOR_MOL_PER_L_DEN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0005_37_Tu__E_TU_MI_LAS_MOR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0005_38_Rod_NO_NON_TI_AVR_OFF_LA_MAP_ALT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0005_39_Tu_S__PRO_UNO_LA_TUA_CRE_CHE_AND_A_CER_LA_STR_NO_PI_PER_AL_GIO_DOG_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0005_40_Rod_NON_C_PI_NES_STR_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["richiesteMonetePerMappaLabirinto"]:
                if monetePossedute < GlobalGameVar.monetePerLaMappaDelLabirinto:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0396_01_Tu_SEN_NON_HO_QUE_MON_PUO_FAR_SEM_VED_LA_MAP_PUO_TEN_TU_MEN_LA_GUA_NON_LA_TOC_NEM_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0396_02_Rod_SON_IMP_AL_MOM_CON___STR__U_MON_POT_STU_PER_BEN_ % GlobalGameVar.monetePerLaMappaDelLabirinto)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0396_03_Tu__)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = True
                    menuMercante = False
                    scelta = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0006_01_Tu_ECC_LE___STR__U_MON_ROD_ % GlobalGameVar.monetePerLaMappaDelLabirinto)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDP._0006_02_Rod_OHH_NON__STA_COS_DIF_EH_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0006_03_Tu_CER_ROD_CER_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDP._0006_04_Rod_COM_HO_DEL_MER_CHE_POT_TOR_UTI_PER_QUE_SE_TI_PU_INT_DAI_PUR_UNO_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0006_05_Tu_INTENDI_IMPOFRUTTI_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDP._0006_06_Rod_ESATTAMENTE_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0006_07_Tu_E_DOV_LI_HAI_TRO_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDP._0006_08_Rod_UHM_CON_REN_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0006_09_Tu_S_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDP._0006_10_Rod_GLI_HO_RUB_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0006_11_Tu__OH_E_ME_LO_DIC_COS_SEN_FAR_PRO_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDP._0006_12_Rod_TSK_NON_C_BIS_DI_SCA_HO_VIS_FAR_COS_PEG_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0006_13_Tu__)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDP._0006_14_Rod_LAS_QUI_LA_MAP_CER_DI_FAR_IN_FRE_)
                    partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = True
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0397_01_Tu_EHI_ROD_AVR_BIS_DI_UN_PAI_DI_COS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0397_02_Rod_PRE_PUR_QUE_CHE_TI_SER_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoTavoloMappaLabirinto":
            partiDialogo = []
            nome = "OggettoTavoloMappaLabirinto"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["messaMappaLabirintoSulTavolo"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0398_01_Tu_ROD_STA_SCR_DEL_COS_SU_QUE_FOG_HA_UNA_PES_CAL_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["copiataMappaLabirinto"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0007_01_Tu_ODD_SEM_UN_VER_CAS_ALL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0007_02_Tu_OK_LHO_COP_NEL_MIA_MAP_ADE_DEV_SOL_SEG_IL_PER_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0399_01_Tu_NON_MI_SER_PI_QUE_MAP_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presiStrumentiPerStudiareImpo"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0400_01_Tu_NON_CI_POS_CRE_NON_LHA_NEA_RIP_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0401_01_Tu_E_IO_CHE_HO_PUR_PAG_PER_VED_)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0402_01_Tu_OH_LA_MIA_MAP_DAV_NON_LHA_PRE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0403_01_Tu_LA_MAP_DEL_LAB_DIS_DA_ROD_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0404_01_Tu_LA_MAP_DI_ROD_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAttrezziRod":
            partiDialogo = []
            nome = "OggettoAttrezziRod"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0405_01_Tu_SON_I_MIE_ATT_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0406_01_Tu_CI_SON_DEG_ATT_DA_LAV_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0407_01_Tu_ATT_DI_ROD_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoFogliProgettiRod":
            partiDialogo = []
            nome = "OggettoFogliProgettiRod"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0408_01_Tu_NON_HO_VOG_DI_SCR_ADE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0409_01_Tu_CRE_SIA_DEG_APP_SON_VER_INC_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0410_01_Tu_APP_DI_ROD_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoScatoloniRod":
            partiDialogo = []
            nome = "OggettoScatoloniRod"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0411_01_Tu_COS_HO_MES_QUA_DEN_AH_ALT_ATT_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0412_01_Tu_SCA_CON_DEG_ATT_ALL_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0413_01_Tu_ATT_DI_ROD_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["avampostoDiRod2"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoMetaScorciatoiaLabirinto"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0008_01_Tu_OH__LAV_DI_ROD_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostEsplosioneDelVulcano2"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0009_01_Tu__STA_USC_UN_SAC_DI_FUM_DA_QUE_MON_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoTuboRod":
            partiDialogo = []
            nome = "OggettoTuboRod"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sbloccatoTunnelDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0414_01_Tu_CHE_CAV__QUE_COS_UN_SER_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0415_01_Tu_QUE_TUB_VA_VER_LA_SEL_)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0416_01_Tu_IL_TUB__A_POS_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0417_01_Tu__UN_TUB_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["avampostoDiRod3"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoRetroAvampostoRod"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0010_01_Tu_C_NESSUNO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0010_02_Tu__ROD_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAttrezziRod":
            partiDialogo = []
            nome = "OggettoAttrezziRod"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0418_01_Tu_SON_I_MIE_ATT_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0419_01_Tu_CI_SON_DEG_ATT_DA_LAV_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0420_01_Tu_ATT_DI_ROD_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoFinestraAvampostoDiRod":
            partiDialogo = []
            nome = "OggettoFinestraAvampostoDiRod"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0421_01_Tu_COM_ILL_UN_INT_AVA_CON_UNA_SOL_FIN_SAR_UNA_SFI_IMP_PER_CHI_ALT_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0422_01_Tu_DA_QUI_SI_VED_SOL_LA_SIE_DEL_LAB_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0423_01_Tu__)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoPappaLibroSonoroMercante":
            partiDialogo = []
            nome = LI.PAPPAGALLO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = True
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0424_01_Pappagallo_NOME_UTENTE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0424_02_Tu_COSA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0424_03_Pappagallo_SAR_ACC_CON_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0424_04_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0424_05_Pappagallo_COMPRA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0424_06_Tu__FAI_PAR_DEL_CON_DI_ROD_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0424_07_Pappagallo_COMPRA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0424_08_Tu__OK_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = True
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0425_01_Pappagallo_NOM_UTE_SAR_COM_)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0426_01_Pappagallo_COS_DES_OH_MIO_SIG_SUP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0426_02_Tu_MMH_NIE_PER_IL_MOM_TOR_A_RIP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0426_03_Pappagallo_S_MIO_SIG_SUP_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = True
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0427_01_Tu_IO_PRE_UN_ATT_DEL_COS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0427_02_Pappagallo__)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAppuntiLabirintoRod":
            partiDialogo = []
            nome = "OggettoAppuntiLabirintoRod"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0428_01_Tu_CI_SON_DEG_APP_INC_E_DEI_DIS_DI_NON_SO_SEM_SEZ_DI_LAB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0428_02_Tu__CRE_CHE_SIA_DEL_ANN_PER_RIC_LA_MAP_DEL_LAB_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0429_01_Tu_SON_DEG_ABB_FAT_DUR_LES_DEL_LAB_CRE_)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0430_01_Tu_I_MIE_VEC_APP_SUL_LAB_CI_SON_STA_TRE_GIO_L_DEN_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0431_01_Tu_APP_DI_ROD_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoLibriInquinamentoRod":
            partiDialogo = []
            nome = "OggettoLibriInquinamentoRod"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoEntratoAvampostoRod"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0011_01_Tu_CI_SON_DIV_LIB_SUL_FLO_LOC_LA_SUA_EVO_E_SUL_DI_ALC_PIA_PAR_NON_CI_SIA_RIF_ALL_DEL_SEL_PER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0011_02_Tu__OH_QUE_PAR_DI_AG_DEG_E_SOS_INQ__PIE_DI_APP_IND_DI_ROD_CI_SON_SCA_E_GRA_OVU_SI__INT_MOL_ALL_QUE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0011_03_Tu__MI_DOM_SE_SIA_RIU_A_CAP_COS_SUC_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["lettoAppuntiInquinamentoAvampostoRod"]:
                oggettoDato = LI.CHI_AVA_DI_ROD
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0012_01_Tu_CI_SON_UN_SAC_DI_LIB_SUL_CRE_DI_SO_E_LET_VER_UN_CER_ROD_OH_ROD_ROD_HA_HA_CHE_NOM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0012_02_Tu__OH_C_ANC_UNA_CHI_QUA_IN_MEZ_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0432_01_Tu_SON_DEI_LIB_DI_ROD_SUL_FLO_LOC_CRE_CHE_SAP_QUA_DI_CI_CHE__SUC_ALL_SEL_)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0433_01_Tu_DEV_AVE_FRU_QUA_IN_MEZ_DOV_LA_MIA_CHI_PER_NON_LA_RIM_A_POS_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0434_01_Tu_APP_DI_ROD_)
                partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo


