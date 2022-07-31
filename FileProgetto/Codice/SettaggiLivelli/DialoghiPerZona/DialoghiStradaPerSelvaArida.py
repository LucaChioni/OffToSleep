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
    if stanzaDiAppartenenza == GlobalGameVar.dictStanze["stradaPerSelvaArida1"]:
        if tipo == "GuardiaCitta":
            partiDialogo = []
            nome = LI.SOLDATO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1295_01_Tu_NON_VOG_PAR_COI_SOL_POT_INS_PER_IMP_)
                    partiDialogo.append(dialogo)
                elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"]:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1296_01_Tu_MEG_RIS_LE_CON_COI_SOL_NON_HO_VOG_DI_POT_CHI_QUA_SUL_)
                    partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1297_01_Soldato__)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["stradaPerSelvaArida2"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoNotatoAssenzaRodFuoriDallAvamposto"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0372_01_Tu___STA_PI_FAC_DEL_PRI_VOL_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoCartelloSelva":
            partiDialogo = []
            nome = "OggettoCartelloSelva"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1298_01_Tu_C_SCR___SEL_ARI__ATT_ALL_FAU_VEL_)
            partiDialogo.append(dialogo)
        elif tipo == "AssistBiblioteca":
            if avanzamentoDialogo == 0:
                partiDialogo = []
                nome = LI.SCONOSCIUTO
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1299_01_Sconosciuto_EHI_TU_DOV_HAI_TRO_QUE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1299_02_Tu__SCU_NON_HO_TEM_ADE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1299_03_Sconosciuto_NO_ASP_SON_SER_INT_STO_CON_DEL_RIC_SUL_DEL_SEL_E_TRA_GLI_ARG_COR_C_ANC_LA_SCO_DEG_IMP_DAL_CIR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1299_04_Tu_CON_REN_IL_BIB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1299_05_Sconosciuto_GLIELHAI_RUBATO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1299_06_Tu_MI_HA_NO_MI_HA_CHI_DI_CON_A_UNA_PER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1299_07_Sconosciuto__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1299_08_Tu__DEV_CON_A_UN_CER_NEI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1299_09_Sconosciuto_CERTO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1299_10_Tu_SEN_SE_LAV_RUB_CHE_SEN_AVR_DIR_DA_CHI_LHO_PRE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1299_11_Sconosciuto_MMH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1299_12_Tu__UNI_FAC_DA_VER_NEL_CAS_MI_SAR_INV_QUA_CER_DI_RIM_SUL_VAG_NO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1299_13_Sconosciuto_OK_OK_FOR_HAI_RAG_VA_BEH_QUI_NON_NE_SAI_NUL_DI_QUE_CRE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1299_14_Tu_NO_QUA_NIE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1299_15_Sconosciuto_VA_BENE_)
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 1:
                partiDialogo = []
                nome = LI.SCONOSCIUTO
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1300_01_Tu_QUI_SEI_RIU_A_CAP_COS_SUC_A_QUE_POS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1300_02_Sconosciuto_BEH__DIF_DA_DIR_MA_UNA_COS__CER_QUE_NON__UNE_NAT_DEL_FLO_SON_STA_GET_DEL_SOS_INQ_IN_TUT_LAR_SOS_CHE_TUT_NON_SON_ANC_STA_ASS_E_SMA_DAL_TER_E_PUR_UNA_GRA_QUA_SI__POI_RIV_NEL_LAG_QUA_ACC_CRE_GRA_DAN_ANC_A_TUT_LA_FAU_ACQ_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1300_03_Tu_DA_QUA_TEM_C_QUE_SIT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1300_04_Sconosciuto_DA_MOL_TEM_ERO_PIC_QUA__SUC_NON_HO_RIC_AL_RIG_DIC_CHE_SIA_MUT_REP_NEL_GIR_DI_UNA_SET_NES_SA_PER_CER_COM_SUC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1300_05_Tu_PER_QUA_DOV_FAR_UNA_COS_DEL_GEN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1300_06_Sconosciuto_E_CHI_LO_SA_NES_SEM_AVE_TRA_BEN_FOR_SI__TRA_DI_UN_INC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1300_07_Tu_MMH_HO_SEN_CHE_C_UNA_GUE_IN_COR_NE_SAI_QUA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1300_08_Sconosciuto_NON_INI_CON_QUE_COS_ANC_LI_HO_SEN_SON_SOL_COM_CHE_SIN_DEL_TEO_PER_FAR_ASC_DA_QUA_NON_FID_DI_QUE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1300_09_Tu_DIC_SAR_UNA_SPI_VAL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1300_10_Sconosciuto_CERTO_)
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 2:
                partiDialogo = []
                nome = LI.SCONOSCIUTO
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1301_01_Sconosciuto_SE_INI_A_CRE_A_TUT_LE_DIC_CIT_PEN_CHE_TRA_QUA_GIO_FIN_IL_MON_E_MOR_TUT_)
                partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo


