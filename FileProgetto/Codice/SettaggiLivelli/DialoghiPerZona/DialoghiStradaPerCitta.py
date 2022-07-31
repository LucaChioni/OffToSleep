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
    if tipo == "OggettoCartelloForesta":
        partiDialogo = []
        nome = "OggettoCartelloForesta"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(LDS._1273_01_Tu_C_SCR___FOR_CAD__ATT_ALL_FAU_NOT_)
        partiDialogo.append(dialogo)
    elif tipo == "OggettoCartelloStaccionata":
        partiDialogo = []
        nome = "OggettoCartelloStaccionata"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1274_01_Tu_SU_QUE_STA_C_UN_CAR_CHE_DIC__VIE_LAC__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1274_02_Tu_DA_QUE_CHE_SO_TUT_I_PAS_VER_ORI_SON_BLO_DA_ANN_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1275_01_Tu_C_SCR__VIE_LAC__)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoCartelloBloccoStrada":
        partiDialogo = []
        nome = "OggettoCartelloBloccoStrada"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1276_01_Tu_C_UN_CAR_CON_LA_SCR__VIE_LAC___OLT_QUE_CAR_VER_DIC_NEM_DEL_REG_CIT_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1276_02_Tu_NON_CRE_CHE_HAN_SIA_AND_DI_QUA_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1277_01_Tu_C_SCR__VIE_LAC___OLT_QUE_CAR_VER_DIC_NEM_DEL_REG_CIT_)
            partiDialogo.append(dialogo)
    elif tipo == "GuardiaCitta":
        partiDialogo = []
        nome = LI.SOLDATO
        if GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1278_01_Tu_MEG_RIS_LE_CON_COI_SOL_NON_HO_VOG_DI_POT_CHI_QUA_SUL_)
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1279_01_Tu_NON_VOG_PAR_COI_SOL_POT_INS_PER_IMP_)
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["stradaPerCittà1"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                if avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1280_01_Tu_CHI_SCU_SOL_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1280_02_Soldato_STA_LON_LAC_VER_ORI__VIE_A_TUT_I_CIV_PER_ORD_DEL_RE_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1280_03_Tu_MA_IO_VOL_PER__VIE_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1280_04_Soldato_NON_MI__CON_DIV_INF_A_RIG_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1280_05_Tu__ESI_QUA_A_CUI__CON_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1280_06_Soldato__MIO_COM_ARR_CHI_COM_QUE_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1280_07_Tu_MMH_)
                    partiDialogo.append(dialogo)
                elif avanzamentoDialogo == 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1281_01_Tu__MA_SE__COS_IMP_CHE_NES_PAS_DI_QUA_PER_SEI_DA_SOL_A_FAR_LA_GUA_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1281_02_Soldato_LA_STR__GI_BLO_DA_QUE_CAR_E_LUN_PUN_LIB__QUE_IN_CUI_SON_IO_ADE__PRA_IMP_PAS_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1281_03_Tu__COSA_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1281_04_Soldato_SEN_HO_STU_PER_QUE_SIS_DI_BLO_SE_TRO_UN_MOD_PER_PAS_PRO_PUR_MA_SAP_CHE_NE_SUB_LE_CON_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1281_05_Tu_OK_MA_UNO_POT_FAR_STR_NEL_BOS_SEN_TRO_PRO_NO_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1281_06_Soldato_DI_QUE_NON_DEV_PRE_TUT_GLI_ACC_VER_ORI_SON_BLO_E_BEN_PRO_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1281_07_Tu_OK_)
                    partiDialogo.append(dialogo)
                elif avanzamentoDialogo == 2:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1282_01_Tu_EHM_EHM_DOV_PAS_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1282_02_Soldato_PRO_A_FAR_UN_ALT_PAS_E_TI_TAG_LE_GAM_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1282_03_Tu_OK_OK_ME_NE_VAD_)
                    partiDialogo.append(dialogo)
                elif avanzamentoDialogo == 3:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1283_01_Tu_DEV_DIR_CHE_HAI_ORG_PRO_UN_BEL_SIS_PER_BLO_LA_STR_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1283_02_Soldato_SON_GI_ABB_FID_NEI_MIE_MEZ_NON_HO_BIS_DEL_GIU_ALT_ADE_VAT_HO_DEL_LAV_DA_FAR_QUI_)
                    partiDialogo.append(dialogo)
                elif avanzamentoDialogo == 4 and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1284_01_Tu_MEG_LAS_AL_SUO_LAV_)
                    partiDialogo.append(dialogo)
                elif avanzamentoDialogo == 4:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1285_01_Tu_NON_LO_DIS_ANC_)
                    partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                if avanzamentoDialogo > 1:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1286_01_Soldato__)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1286_02_Tu_SE_SOL_NON_AVE_ESC_UN_SIS_COS_IMP_)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1287_01_Soldato__)
                    partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1288_01_Soldato__)
                partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["stradaPerCittà3"]:
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                if y == GlobalHWVar.gpy * 5:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1289_01_Soldato_BEN_IN_CIT_SE_SEI_IN_CER_DI_UN_POS_SIC_PER_RIP_RIV_AGL_ALL_PRO_)
                    partiDialogo.append(dialogo)
                elif y == GlobalHWVar.gpy * 12:
                    if avanzamentoDialogo == 0:
                        oggettoDato = False
                        avanzaStoria = False
                        menuMercante = False
                        scelta = False
                        avanzaColDialogo = True
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(LDS._1290_01_Tu_SALVE_SOLDATO_)
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("personaggio")
                        dialogo.append(LDS._1290_02_Soldato_SAL_SI_PRE_DI_NON_ING_IL_PON_TRO_A_LUN__NEC_CHE_SIA_SEM_IL_PI_FRU_POS_)
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(LDS._1290_03_Tu_OH_MI_STA_GIU_CHI_PER_NON_CI_FOS_NES_QUI_)
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("personaggio")
                        dialogo.append(LDS._1290_04_Soldato_PER__UN_PON_SER_PER_ATT_IL_FIU_NON_PER_OST_IL_PAS_)
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(LDS._1290_05_Tu_OK_MA_TU_INV_NON_LO_STA_OST_)
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("personaggio")
                        dialogo.append(LDS._1290_06_Soldato_NO_DEV_QUA_CHE_LO_MAN_LIB_ALT_SAR_PIE_DI_PER_CHE_COM_TE_BLO_UN_TRA_DI_PER_CHE_LO_VUO_ATT_SOL_PER_STA_SOP_)
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(LDS._1290_07_Tu_A_ME_SEM_CHE_LUN_TRA_QUI_SIA_COM_DA_DUE_GUA_CHE_STA_SUL_PON_SEN_NEA_ATT_)
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("personaggio")
                        dialogo.append(LDS._1290_08_Soldato_DUE_GUA_CHE_MAN_IL_PON_LIB_DAL_TRA_)
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(LDS._1290_09_Tu_CER_DIC_SOL_CHE_SEN_TUT_QUE_GUA_IL_PON_SAR_SIC_PI_LIB_E_FRU_TUT_QUI_)
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("personaggio")
                        dialogo.append(LDS._1290_10_Soldato_SEN_RAG_NON_HO_ALT_TEM_DA_PER_VAI_DOV_DEV_AND_SEN_OST_IL_PAS_)
                        partiDialogo.append(dialogo)
                    elif avanzamentoDialogo == 1:
                        oggettoDato = False
                        avanzaStoria = False
                        menuMercante = False
                        scelta = False
                        avanzaColDialogo = False
                        dialogo = []
                        dialogo.append("personaggio")
                        dialogo.append(LDS._1291_01_Soldato_VAI_DOV_DEV_AND_SEN_OST_IL_PAS_)
                        partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1292_01_Soldato__)
                partiDialogo.append(dialogo)
    elif tipo == "OggettoBucoPorta":
        partiDialogo = []
        nome = "OggettoBucoPorta"
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(LDP._0370_01_Tu__CHIUSO_)
        partiDialogo.append(dialogo)
    elif tipo == "PadreUfficialeServizio":
        partiDialogo = []
        nome = LI.SOLDATO
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["bussatoAllaPortaCittà"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0371_01_Soldato_CHI_VA_L_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0371_02_Tu_SCU_SON_DI_PAS_STO_CER_UN_RAG_CHE_DOV_ESS_PAS_DI_QUA_POC_FA_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0371_03_Soldato_UNA_RAG_APR_)
            partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo


