# -*- coding: utf-8 -*-

import random
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
    if tipo == "Bibliotecario":
        partiDialogo = []
        nome = u"René"
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["mostratoCertificatoPerIngressoBiblioteca"]:
            nome = LI.BIBLIOTECARIO
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0013_01_Tu__SEI_TU_IL_BIB_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0013_02_Bibliotecario_S_ADE_SON_MOL_OCC_QUI_PER_COR_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0013_03_Tu_VOL_SAP_SE_MIO_FRA_FOS_PAS_DI_QUI_OGG_ERA_UN_PO_PI_ALT_DI_ME_E_AV_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0013_04_Bibliotecario_FER_FER_NON_HO_TEM_PER_QUE_COS_ADE_PRE_UN_APP_E_RIP_PI_TAR_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0013_05_Tu__AVE_I_CAP_NER_E_SI_CHI_SI_CHI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0013_06_Bibliotecario__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0013_07_Tu__HANS_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0013_08_Bibliotecario__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0013_09_Tu__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0013_10_Bibliotecario__SME_DI_FIS_TI_HO_DET_DI_RIP_PI_TAR_HO_DA_FAR_ADE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0013_11_Tu__IO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0013_12_Bibliotecario__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0013_13_Tu__IO_HO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0013_14_Bibliotecario__COS_COS_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0013_15_Tu__IIO_HO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0013_16_Bibliotecario_POR_E_VA_BEN_SEG_TI_FAC_CON_I_REG_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["andatoNelloStudioDelBibliotecario"]:
            nome = LI.BIBLIOTECARIO
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0014_01_Bibliotecario__QUE__IL_MIO_STU_NON_TOC_NIE_PER_FAV_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0014_02_Tu__)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoBibliotecarioArrivoNelloStudio"]:
            nome = LI.BIBLIOTECARIO
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0015_01_Bibliotecario_ALL_IL_REG_DI_STA_ECC_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0015_02_Tu__IO_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["messoRegistroBibliotecaSullaScrivania"]:
            nome = LI.BIBLIOTECARIO
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0016_01_Bibliotecario_OK_VED_CHI_STA_CER_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0016_02_Tu__IO_HO_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoBibliotecarioPreVomito1"]:
            nome = LI.BIBLIOTECARIO
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0017_01_Bibliotecario__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0017_02_Tu__IIO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0017_03_Bibliotecario__CHE_HAI_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["vomitatoInBiblioteca"]:
            nome = LI.BIBLIOTECARIO
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0018_01_Bibliotecario__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0018_02_Tu_ODDIO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0018_03_Bibliotecario__OK_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0018_04_Tu__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0018_05_Bibliotecario__NON_NON_PRE_CI_PEN_IO_A_PUL_TU_SIE_UN_ATT_E_RIP_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0018_06_Tu_OOK_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sedutaInBiblioteca"]:
            nome = LI.BIBLIOTECARIO
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0019_01_Bibliotecario__PER_NON_VIE_VIA_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ripulitoVomito"]:
            nome = LI.BIBLIOTECARIO
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0020_01_Bibliotecario_VA_BEH_NON_IMP_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["bibliotecarioVenutoVersoDiTe"]:
            nome = LI.BIBLIOTECARIO
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0021_01_Tu_SCU_NON_VOL_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0021_02_Bibliotecario_NON_PRE_TI_SEN_MEG_ORA_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0021_03_Tu_S_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0021_04_Bibliotecario_PER_SEI_COS_SCO_CHE_TI__SUC_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0021_05_Tu__NO_NIE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0021_06_Bibliotecario__VA_BEN_COM_TI_CHI_RAG_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0021_07_Tu__SARA_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0021_08_Bibliotecario_SAR_SEI_IN_PER_PER_QUA_HAI_PRO_FAM_ECO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0021_09_Tu__NO_NON_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0021_10_Bibliotecario__OK_SEG_SEG_TI_FAC_FAR_UN_PIC_ESP_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0021_11_Tu_COSA_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["riavviatoMusicaPostDialogoBibliotecario"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0022_01_Tu_ECC_UHM_BIB_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0022_02_Bibliotecario_S_CHI_REN_PER_FAV_VED_AH_ECC_FAT_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0022_03_Bibliotecario_ALL_CON_E_CER_DI_SEG_QUE_PIC_RAG_SE_UN_EVE_CHE_CHI_E2__AVV_IN_PAS_A_CAU_DEL_E1__IMP_CHE_DAL_E1_FOS_CAU_EVE_DIV_DA_E2_IN_ALT_PAR_UN_EVE_ACC_NEL_PAS__DET_E_INV_MA_SE_LEV_E1_SI_DOV_RIP_IN_FUT_IO_SAP_CHE_SUC_AVV_E2_MI_SEG_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0022_04_Tu__PI_O_MEN_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0022_05_Bibliotecario_FAC_QUE_PIC_ESP_SU_QUE_TAV_INC__INC_UNA_MOL_CHE_PER_DI_SPI_UNA_PAL_LUN_QUE_CAN_QUE_LIN_DIS_SUL_TAV_SER_PER_SEG_LA_DIS_DAL_MOL_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0022_06_Bibliotecario_SE_IO_ADE_SPI_LA_PAL_CAR_UN_PO_LA_MOL_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["eseguitoEsperimentoDiProva1"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0023_01_Bibliotecario_LA_PAL__ARR_FIN_ALL_LIN_CHE_SEG_UN_MET_MET_CHE_IL_MOM_IN_CUI_ABB_CAR_LA_MOL__IL_NOS_EVE_E1_MEN_IL_MOM_IN_CUI_LA_PAL_SI_FER_PRI_DI_TOR_IND__LEV_E2_SE_ADE_RIP_LES_ALL_STE_MOD_FIN_A_DOV_PEN_CHE_ARR_LA_PAL_PRI_DI_FER_E_TOR_IND_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0023_02_Tu_SEM_A_UN_MET_DIR_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0023_03_Bibliotecario_ESA_IN_ALT_PAR_MI_STA_DIC_CHE_DAL_E1_SCA_INE_E2_EBB_SEI_APP_RIU_A_PRE_LEV_CHE_STA_PER_ACC_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["eseguitoEsperimentoDiProva2"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0024_01_Bibliotecario_PAR_DA_QUE_PRE_SON_STA_FAT_DIV_STU_CHE_PER_DI_PRE_MOL_TIP_DI_EVE_TRA_DEL_FOR_MAT_QUE__UNA_SIT_MOL_FAC_DA_PRE_E_DA_CAL_SEM_MOS_I_PAS_POT_CAL_ANC_TU_ADE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0024_02_Tu_MH_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0024_03_Bibliotecario_NON_STO_SCH_TI_SCR_QUA_I_PAS_E_I_DAT_DI_PAR_TU_PRO_A_CAL_QUA_SPA_PER_LA_PAL_PRI_DI_TOR_IND_SE_PAR_CON_UNA_VEL_DI_3_MS_PER_I_CAL_UTI_PUR_I_FOG_SU_QUE_TAV_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["scrittiDatiEnigmaBibliotecario"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0025_01_Bibliotecario_SE_HAI_DIF_A_COM_QUA_PUO_CON_I_LIB_SU_QUE_LIB_TRO_DEL_SEM_SPI_NEL_SEZ_MO_RET_UNI_ACC_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["spiegazioneEnigmaBibliotecario4"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = random.randint(1, 4)
            velPalla = GlobalGameVar.datiEnigmaBibliotecario["velocità"]
            if GlobalGameVar.datiEnigmaBibliotecario["velocità"] < 5:
                velProssimaPalla = GlobalGameVar.datiEnigmaBibliotecario["velocità"] + 1
            else:
                velProssimaPalla = 1
            soluzione = GlobalGameVar.datiEnigmaBibliotecario["soluzione"]
            vettoreRisposteFalse = [GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa1"], GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa2"], GlobalGameVar.datiEnigmaBibliotecario["rispostaFalsa3"]]

            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0026_01_Bibliotecario_DOMANDA_)
            dialogo.append({lingua: testo % str(velPalla) for lingua, testo in LDP._0026_02_Bibliotecario_DIM_QUA_SPA_PER_LA_PAL_PRI_DI_FER_SE_LA_FAC_PAR_CON_UNA_VEL_DI___STR__U_MS_.items()})
            i = 1
            while i <= 4:
                if i == scelta:
                    dialogo.append(str(soluzione) + " m.")
                else:
                    dialogo.append(str(vettoreRisposteFalse.pop(0)) + " m.")
                i += 1
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0026_03_Bibliotecario_RISPOSTA_)
            i = 1
            while i <= 4:
                if i == scelta:
                    dialogo.append({lingua: testo % str(soluzione) for lingua, testo in LDP._0026_04_Bibliotecario_SEG_I_CAL_ESA___STR___M_E_QUE_RIS_COR_A_UN_EVE_NON_ANC_AVV_.items()})
                else:
                    dialogo.append({lingua: testo % (str(velProssimaPalla), str(soluzione)) for lingua, testo in LDP._0026_05_Bibliotecario_MMH_NO_DEV_AVE_SBA_DEI_CAL_RIP_CON_UNA_VEL_DI___STR___MS_LA_RIS_GIU_ERA___STR___M_TI_FAC_VED_.items()})
                i += 1
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["eseguitaVerificaRisultatoEnigma"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0027_01_Bibliotecario_QUE_CHE_ABB_APP_FAT_DIM_UNA_COS_MOL_IMP_LA_MAT_CHE_COM_LA_REA_SEG_DEL_REG_BEN_PRE_ORA_SE_CON_MA_INT_TUT_CI_CHE__PER_ESI_UNA_RAG_PER_CUI_GLI_ESS_VIV_ESS_ANC_PER_E_FAT_DI_MAT_NON_DOV_SEG_LE_STE_REG_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0027_02_Tu_BEH_UN_ESS_VIV_HA_QUA_IN_PI_RIS_ALL_MAT_NOR_PU_FAR_QUA_PU_PEN_PRE_DEC_HA_QUA_CHE_LO_REN_VI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0027_03_Bibliotecario_TIPO_UNANIMA_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0027_04_Tu_S_TIP_UNA_COS_DEL_GEN_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0027_05_Bibliotecario_CER_PU_AVE_SEN_MA_IL_RAG_NON_CAM__POS_CHE_ESI_UN_NON_MAT_ANC_SE_MOL_IMP_PER_IL_MOD_IN_CUI_QUE_SI_EVO_E_INT_CON_LA_REA__DET_DA_SPE_REG_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0027_06_Bibliotecario_NON_NON_SIA_POS_DIM_CI_CHE_LO_FA_SEM_OVV__CHE_GLI_UMA_SON_IN_GRA_DI_SPI_IL_MOT_DEL_LOR_AZI_E_SE_CI_SON_DEI_MOT_VUO_DIR_CHE_ANC_POT_TOR_IND_NEL_TEM_LE_AZI_COM_SAR_SEM_LE_STE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0027_07_Tu_MMH_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0027_08_Bibliotecario_FAC_FIN_CHE_SIA_POS_TOR_IND_NEL_TEM_TOR_A_UNA_SIT_IN_CUI_HAI_PRE_UNA_SCE_UNA_SCE_QUA_PER_FAC_PER_ANC_I_RIC_CHE_HAI_ACC_NEL_TEM_CHE_STA_RIA_DAC_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0027_09_Tu_OK_MA_DEV_IMM_UNA_SIT_SPE_O_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0027_10_Bibliotecario_NO_NON_IMP_VA_BEH_FAC_CHE_TOR_A_UNA_SIT_CHE_VOR_CAM_UN_EPI_DOV_HAI_COM_UNA_SCE_SB_ADE_HAI_LOC_DI_TOR_IND_E_SIS_LE_COS_PER_FAC_SCO_TUT_QUE_CHE__SUC_DOP_AVE_PRE_QUE_SCE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0027_11_Tu_VA_BEN_TOR_IND_ANC_CON_I_RIC_QUI_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["chiestoDiPensareASceltaPassataNelDialogoBibliotecario"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0028_01_Tu_MMMH_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0028_02_Bibliotecario__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0028_03_Tu__ALLORA_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0028_04_Bibliotecario__UNA_COS_QUA_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0028_05_Tu_S_STO_PEN_NON_POS_SPR_QUE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0028_06_Bibliotecario__NON_SUC_VER_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0028_07_Tu_ASP_CI_SON_QUA_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0028_08_Bibliotecario_MA_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0028_09_Tu__VA_BEN_CI_SON_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0028_10_Bibliotecario_OK_MI_RAC_HAI_PER_I_RIC_CHE_HAI_ACC_DA_QUE_MOM_FIN_AD_ADE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0028_11_Tu_S_S_CI_SON_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0028_12_Bibliotecario_PER_SEI_IN_QUE_SIT_NEL_MOM_IMM_PRI_A_QUE_IN_CUI_PRE_LA_TUA_DEC_OGN_COS__IDE_A_COM_TU_STA_PEN_ESA_A_QUE_CHE_PEN_IN_QUE_MOM_E_NON_SAI_COS_SUC_DIM__POS_CHE_TU_FAC_QUA_DI_DIV_CHE_TU_AGI_IN_MAN_INC_RIS_A_QUE_PRO_MEN_CHE_TI_HAN_POR_AD_AGI_COM_HAI_AGI_LA_PRI_VOL_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0028_13_Tu__AVR_POT_AVR_POT_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0028_14_Bibliotecario__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0028_15_Tu_BEH_SE_PEN_ALL_STE_COS_NON_SO_TUT_QUE_CHE_HO_FAT_E_PEN_SON_LA_CAU_DEL_MIA_DEC_QUI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0028_16_Bibliotecario_ESA_SON_LA_CAU_E_SAR_ASS_PEN_CHE_DAL_MED_CON_DI_PAR_POS_ESS_SCA_EFF_DIV_TRA_LOR_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0028_17_Tu_SON_LA_CAU_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0028_18_Bibliotecario_NON_HAI_MER_O_COL_DI_QUA_COS_TU_ABB_FAT_DET_O_PEN_NEL_TUA_VIT_SEM_SUC_DEG_EVE_CHE_TI_IMP_DEL_REA_PUN_PER_COS_CHE_HAI_FAT_O_CHE_TI_SON_SUC_SAR_COM_PUN_QUE_PAL_PER_QUA_PEN_CHE_SI_FER_TRO_PRE_O_TRO_TAR_PRI_DI_TOR_IND_SE_LE_CON_DI_PAR_SON_LE_STE_I_RIS_NON_CAM_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["pensatoASceltaPassataNelDialogoBibliotecario"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0029_01_Tu_MA_ASP_COS_PER_NES_SAR_RES_DEL_PRO_AZI_SE_OGN_SCE_DIP_DA_QUE_CHE_CI_SUC_NON_SON_VER_SCE_PER_DOV_IMP_A_CIO_NON_CI_SAR_MOT_DI_CIO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0029_02_Bibliotecario_S_INF_PER_QUE__COM_CHE_LE_PER_PEN_DI_AVE_LIB_ARB_LE_POR_A_IMP_PER_DEG_OBI_A_DAR_IMP_ALL_LOR_AZI_A_RES_A_SEG_LE_REG_LE_REN_PUN_QUA_SB_COS_SI_PEN_E_SI_EVO_SEC_LA_VIS_CHE_GLI_SI_VUO_IMP_LE_POR_A_OBB_SE_COS_NON_FOS_SAR_UN_PRO_ORG_DEL_SOC_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0029_03_Tu__BEH_E_TU_PUR_SAP_QUE_COS_NON_SEI_UN_PRO_PER_LA_SOC_NO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0029_04_Bibliotecario_IO_ACC_LE_CON_FIN_MI_POR_VAN_PER_QUA_MI_RIG__MOL_MEG_CON_CON_LAV_STA_CHE_CON_ORG_IST_E_BES_LI_DAL_LOR_ARB_MI_MET_COM_CON_I_MIE_STU_E_OSS_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0029_05_Tu_OK_MA_QUI_TU_TI_CON_UN_OR_IST_E_BES_LIB_DAL_TUO_ARB_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0029_06_Bibliotecario__BEH_QUA_CI_PEN_MA_FIN_NON_PEN_O_PEN_GLI_ALT_SON_UN_IND_RES_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0029_07_Tu__OK_MA_NON_MI_SEM_MOL_IS_O_BE_ORA_CHE_CI_STA_PEN_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0029_08_Bibliotecario_SAR_LO_SON_IO_E_LO_SEI_TU_TAN_QUA_LO_SON_LE_API_LE_FOR_E_I_CAS_QUA_COS_ALV_FOR_E_DIG_IO_POS_COS_EDI_DIS_IMM_E_SCR_LIB_QUE_DOV_REN_NO_IST_SIA_UNA_SPE_ANI_TRA_TAN_ALT_LA_DIF_TRA_NAT_E_ART_SER_SOL_A_NOI_PER_INN_IL_NOS_LAV_PER_REN_PI_NOB_PI_IMP_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0029_09_Tu_MH_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0029_10_Bibliotecario_COM_A_PRO_DI_LAV_DOV_TOR_AL_MIO_ADE_DIC_DI_ESS_VEN_PER_SAP_DI_TUO_FRA_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0029_11_Tu__S_S_MIO_FRA_VOL_SAP_SE_FOS_PAS_DI_QUI__SCA_DI_CAS_IER_NOT_DA_UN_PO_DI_TEM_DIC_DI_VOL_VEN_IN_CIT_QUI_LHO_SEG_HO_CHI_IN_GIR_E_MI__STA_DET_DI_CON_IN_BIB_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0029_12_Bibliotecario_SE_TUO_FRA__PAS_DI_QUI_LO_VED_SUB_DAI_REG_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ripartitaMusicaDopoPensatoASceltaPassataNelDialogoBibliotecario"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0435_01_Bibliotecario_IL_REG_DI_STA__SUL_MIA_SCR_SE_MI_FAI_PAS_VAD_A_CON_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["bibliotecarioArrivatoAlRegistro"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0030_01_Bibliotecario_IL_NOME_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0030_02_Tu_HANS_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0030_03_Bibliotecario_HAN_NO_NON_C_NES_HAN_QUI_POT_ESS_PRE_CON_UN_NOM_DIV_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0030_04_Tu_NON_CRE_PER_AVR_DOV_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0030_05_Bibliotecario_SE_N_AND_SEN_DIR_NIE_NON_CRE_CHE_VOL_ESS_SEG_NON_MI_OST_TRO_FOS_IN_TE_MAG_UN_GIO_VI_RIN_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0030_06_Tu_S_SAI_A_CHI_ALT_POT_CHI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0030_07_Bibliotecario_COM_VUO_IN_EFF_QUA_C_E_MI_FAR_ANC_UN_BEL_FAV_SE_CI_AND_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0030_08_Bibliotecario_DEV_FAR_UNA_CON_A_UN_MIO_VEC_AMI_VIV_A_SUD_OLT_LA_SEL_ARI_SI_CHI_NEI__UNA_PER_MOL_POT_CHE_HA_NOT_DI_TUT_GLI_SPO_CHE_AVV_IN_QUE_TER_DA_QUE_CHE_HO_CAP__POS_CHE_TUO_FRA_NON_SIA_IN_CIT_QUI_SE_C_UNA_PER_A_CUI_DOV_CHI__SEN_DUB_NEI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0030_09_Tu_MMH_NON_PEN_SE_NE_SIA_AND_DAL_CIT_RIS_DI_PER_SOL_TEM_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0030_10_Bibliotecario_NON_SAI_NEM_SE_CI__MAI_STA_IN_CIT_MAG__ADE_CHE_STA_PER_TEM_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0030_11_Tu_UFF_E_QUE_NEI_VOR_AIU_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0030_12_Bibliotecario_CER_SAR_MOL_FEL_DI_RIC_CI_CHE_GLI_CON_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0030_13_Tu__E_COS_DOV_CON_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0030_14_Bibliotecario_TI_FAC_VED_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["andatoACercareImpo"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0031_01_Bibliotecario__LAV_MES_QUA_DA_QUA_PAR_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ricercaImpoDiBibliotecario1"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0032_01_Bibliotecario__ERA_QUI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0032_02_Bibliotecario__AH_TRO_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"]:
            oggettoDato = LI.IMPOPIETRA
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0033_01_Bibliotecario_ECCO_QUI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0033_02_Tu__COS_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0033_03_Bibliotecario_QUE__UNA_CRE_DEL_MON_OCC_APP_A_UNA_SPE_CHE_SI__EST_DA_DIV_ANN_ORM_MA_SON_RIU_A_CON_UN_ESE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0033_04_Tu_MA__VIV_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0033_05_Bibliotecario_S_CER_QUE_BES_SON_PRA_IMM_SON_IN_GRA_DI_CO_PER_MOL_ANN_FIN_NON_TRO_NUT_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0033_06_Tu_AH_E_COM_HAN_FAT_A_EST_ALL_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0033_07_Bibliotecario_QUE__UNA_BEL_DOM_SON_SPA_TUT_IN_UNA_NOT_DI_CIR_DIE_ANN_FA_DI_COL_NON_SE_NE_SON_PI_VIS_IN_GIR_UN_EPI_PIU_STR_CHE__STA_IGN_DA_MOL_PER_VIA_DEI_DIS_AVV_NEL_SEL_E_NEL_LAG_QUA_GIO_DOP_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0033_08_Bibliotecario_PER_QUE_SOL_POC_STU_SI_INT_ALL_QUE_MA_IO_ERO_TRA_QUE_SON_PAR_ALL_RIC_DI_UNA_QUA_SPI_VER_OVE_E_SON_RIU_A_TRO_QUE_PIC_IMP_INC_IN_UNA_ROC_COS_LHO_PRE_E_HO_INI_A_STU_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0033_09_Tu_IMP_SI_CHI_COS_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0033_10_Bibliotecario_IM__IL_NOM_DEL_SPE_GLI__STA_DAT_PER_POR_UNI_SUL_NUC_CHE_FOR_QUE_SCR_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0033_11_Tu_UNI_CHE_DIC_IM_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0033_12_Bibliotecario_COM_IO_LHO_OSS_ABB_E_NON_SAP_COS_RIC_NEI_STA_INI_A_INT_MA_DA_QUE_CHE_SO_NON_NE_HA_MAI_POT_OSS_UNO_DA_VIC_SE_GLI_LAS_STU_POT_DED_QUA_IN_PI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0033_13_Tu__VA_BEN_COM_LO_TRA_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0033_14_Bibliotecario_NON_DEV_TRA_TI_SEG_QUA_ATT_QUE_PIE_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ricaricatoImpoDalBibliotecario"]:
            oggettoDato = LI.IMPOFRUTTO_PICCOLO
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0034_01_Tu_SI__SVE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0034_02_Bibliotecario_LHO_APP_ALI_NON_TI_PRE_NON__AGG_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0034_03_Tu_OK_QUI_ADE_MI_SEG_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0034_04_Bibliotecario_SEG_SEM_LA_PIE_CHE_TI_HO_DAT_QUA__ATT_MA_CI_CHE_REN_VER_INT_QUE_CRE__IL_SUO_COM_QUA_LA_PIE__SPE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0034_05_Tu_ADE__SPE_E_NON_STA_FAC_NIE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0034_06_Bibliotecario_GLI_IMP_SON_MOL_RAZ_E_MET_ESE_SEM_LAZ_CHE_RIT_PRI_PER_LE_CIR_LO_FAN_FIN_NON_ESA_LE_ENE_A_QUE_PUN_SI_FER_E_ASP_IL_NUT_ADE_SEM_STR_MA_LA_PRI_DI_QUE_IMP__RIM_FER_E_CI_RES_FIN_QUA_NON_GLI_DIR_DI_FAR_QUA_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0034_07_Tu_QUA_POS_POS_DIR_COS_FAR_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0034_08_Bibliotecario_PUO_DIR_CHE_AZI_COM_A_SEC_DEL_SIT_E_LUI_LA_ESE_OGN_VOL_SEN_BAT_CIG_MA_PER_COM_QUE_INF_DEV_INS_DEG_IMP_NEL_CHE_HA_DIE_LA_TES_QUE_APE_VEN_CHI_CE_DI_MEM_E_LUI_NE_HA_SOL_UNA_AL_MOM_QUI_PUO_FAR_FAR_SOL_UNA_ALL_VOL_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0034_09_Tu_AH_E_COS_UN_IM_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0034_10_Bibliotecario_LIM__UNA_SPE_DI_FOG_NON_MOL_SPE_MA_FAT_DI_UN_MAT_MOL_PI_RIG_E_RES_DEL_CAR_NOR_TUT_GLI_IMP_SON_DIV_TRA_LOR_E_SI_DIV_IN_DUE_CAT_CO_CHE_IND_DEL_CON_E_AZ_CHE_IND_DEL_AZI_DA_COM_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0034_11_Bibliotecario_PER_DAR_UNI_A_UN_IMP_DEV_INS_UN_CON_E_UN_AZI_NEL_CEL_DI_MEM_LIM_OGN_VOL_CHE_DEV_DEC_COS_FAR_LEG_LA_CON_E_LAZ_NEL_CEL_E_SE_VAL_DI_TRO_NEL_SIT_ADA_ESE_LIS_ALT_STA_FER_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0034_12_Tu_OK_SEM_ABB_COM_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0034_13_Bibliotecario_CER_SE_VUO_DAR_UNO_IN_BIB_CI_SON_DIV_LIB_CHE_PAR_PI_DET_DEL_LOR_FUN_MA_SON_SIC_CHE_IMP_IN_FRE_FAC_QUA_PRO_AL_MOM_IO_HO_SOL_QUE_DUE_DI_IMP_QUE_CON_IND_UNA_SIT_IN_CUI_QUA_VUO_AGG_MEN_QUE_AZI_FA_ESE_UN_ATT_FOL_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0034_14_Tu_WOW_POS_FAR_FAR_ORA_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0034_15_Bibliotecario_NO_NON_IN_CIT_E_SOP_NON_NEL_MIO_STU_POI_ADE_DEV_TOR_A_LAV_LO_POT_VED_DIR_SUL_CAM_QUA_NE_AVR_BIS_TI_FAC_IL_VIA_LA_SEL_ARI__UNA_ZON_PAR_OST_PER_GLI_UMA_MA_CON_UN_IMP_NON_AVR_PRO_LUN_COS__POR_DEL_MED_E_CER_DI_EVI_GLI_SCO_NON_DOV_INC_MA_NEL_CAS_STA_ALL_LAR_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0034_16_Tu_VA_BEN_LA_SEL_ARI_SI_TRO_A_SUD_GIU_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0034_17_Bibliotecario_ESA_DOP_AVE_ATT_PRO_ANC_VER_SUD_COS_IL_LAG_E_ARR_AL_CAS_DI_NEI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0034_18_Tu_OK_SEL_EVI_GLI_SCO_E_POI_LAG_GRA_MIL_PER_LAI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0034_19_Bibliotecario_NON_C_DI_CHE_SAR_AH_DIM_PRE_QUE__UN_IMP_UN_FRU_CHE_NAS_NEL_MON_OCC_DI_CUI_SI_NUT_GLI_IMP_DAG_QUA_VED_CHE_STA_ESA_LE_ENE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0034_20_Tu_UN_IM_NON_SEM_AFF_UN_FRU_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0034_21_Bibliotecario_GI_NE_AVE_ALT_MA_NON_LI_TRO_PI_DEV_AVE_USA_IN_OGN_CAS_BUO_FOR_PER_IL_VIA_RAG_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0436_01_Tu_SCU_REN_HAI_DET_CHE_CI_SON_DEI_LIB_IN_BIB_CHE_PAR_DI_IMP_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0436_02_Bibliotecario_S_LI_PUO_TRO_NEG_SCA_AL_PIA_DI_SOP_SON_TUT_COL_DI_NER_NON_PUO_SBA_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presiStrumentiPerStudiareImpo"]:
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0437_01_Tu_EHI_REN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0437_02_Bibliotecario__SAR_CHE_CI_FAI_QUI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0437_03_Tu_HO_POR_IMP_A_NEI_E_MI_HA_DET_CHE_SER_QUE_STR_PER_STU_TU_LI_HAI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0437_04_Bibliotecario__TI_HA_DET_DI_CHI_A_ME_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0437_05_Tu_NO_IN_REA_NO_MA_SE_LI_AVE_TU_SAR_MOL_PI_SEM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0437_06_Bibliotecario_MMH_C_UN_MER_CHE_DOV_AVE_QUE_GEN_DI_ARN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0437_07_Tu_S_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0437_08_Bibliotecario_UN_CER_ROD_LO_CON_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0437_09_Tu_S_S_LO_CON_LHO_GI_INC_QUA_VOL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0437_10_Bibliotecario_DOV_RIV_A_LUI_CRE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0437_11_Tu_OK_)
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0438_01_Tu_REN_A_PRO_DI_ROD_SAI_DOV_POS_TRO_ADE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0438_02_Bibliotecario_NON_NE_HO_IDE_RAG_QUE_TIP__SEM_IN_VIA_LHO_VIS_SPE_ARR_DAL_MON_OCC_PER_NON_SO_SE_SIA_UNA_BUO_IDE_CER_L_)
                partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0439_01_Tu_EHI_REN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0439_02_Bibliotecario__SAR_CHE_CI_FAI_QUI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0439_03_Tu_PAS_PER_UN_SAL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0439_04_Bibliotecario_OH_SEI_AND_DA_NEI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0439_05_Tu_S_MI_HA_CHI_DI_PRE_DEG_STR_PER_STU_IMP_E_CI_STO_TOR_ADE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0439_06_Bibliotecario_AH_DEG_STR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0439_07_Tu_S_NON_SO_CHE_INT_ABB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0439_08_Bibliotecario__MMH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0439_09_Tu_TU_COS_PEN_CHE_VOG_FAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0439_10_Bibliotecario__BEH_PEN_CHE_VOG_STU_NON_GLI_FAR_DEL_MAL_SE__QUE_CHE_TI_PRE_GLI_IMP_SON_PRA_IMM_TE_LHO_GI_DET_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0439_11_Tu_MMH_OK_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0439_12_Bibliotecario_VA_BEN_DEV_TOR_A_LAV_ADE_)
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0440_01_Tu_REN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0440_02_Bibliotecario_SAR_SON_IMP_AL_MOM_RIP_PI_TAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0440_03_Tu_OK_)
                partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0441_01_Bibliotecario__)
            partiDialogo.append(dialogo)
    elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["presiStrumentiPerStudiareImpo"] and (tipo.startswith("Ragazz") or tipo == "OggettoAssistBiblioteca"):
        partiDialogo = []
        if tipo.startswith("Ragazzo"):
            nome = LI.SCONOSCIUTO
        elif tipo.startswith("Ragazza"):
            nome = LI.SCONOSCIUTA
        elif tipo == "OggettoAssistBiblioteca":
            nome = LI.ASSISTENTE_BIBLIOTECARIO
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0442_01_Tu_NON_HO_NIE_DA_CHI_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0443_01_AssistenteBibliotecario__)
            partiDialogo.append(dialogo)

    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca1"]:
        if tipo == "AssistBiblioteca":
            partiDialogo = []
            nome = LI.ASSISTENTE_BIBLIOTECARIO
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["rimosseMonetePerEntrareInConfraternita"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0035_01_AssistenteBibliotecario_EHI_TU_DEV_FOR_UN_DOC_PER_ENT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0035_02_Tu_EH_IO_NON_HO_NES_DOC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0035_03_AssistenteBibliotecario_MI_SER_PER_CER_LA_T_NON_PUO_NON_AVE_NE_VIE_ASS_UNO_A_TUT_QUA_ENT_IN_CIT_LHA_PER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0035_04_Tu_NO_NON_MI_HAN_DAT_NES_DOC_QUA_SON_ARR_CHI_ME_LO_AVR_DOV_DAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0035_05_AssistenteBibliotecario_SE_NON_SEI_RES_TI_VIE_ASS_UN_CER_DI_PER_QUA_ARR_AGL_ALL_PRO_ERA_IN_MEZ_AGL_ALT_FOG_CHE_HAI_RIC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0035_06_Tu_OH_PER_QUA_SON_ARR_MI__STA_DET_CHE_NON_CER_PI_POS_NEG_ALL_QUI_DAV_IL_COM_DEL_GUA_NOT_SI__OFF_DI_OSP_PER_LA_NOT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0035_07_AssistenteBibliotecario_ADD_OSP_DA_DAV_BEH_ALL_CHI_A_LUI_DI_RIL_LA_CER_ALT_NON_POS_LAS_PAS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0035_08_Tu_VA_BEN_MA_IN_REA_AVR_SOL_BIS_DI_SAP_SE_MIO_FRA__PAS_DI_QUA_OGG_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0035_09_AssistenteBibliotecario_NON_POS_DAR_QUE_GEN_DI_INF_GLI_ACC_ALL_BIB_VEN_INS_IN_DEI_REG_CHE_SOL_IL_BIB_PU_CON_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0035_10_Tu_AH_ALL_POS_CHI_AL_BIB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0035_11_AssistenteBibliotecario_S_CER_MA_NON_SAR_CER_IO_A_DIS_LUI_NON_HA_MOL_PAZ_PER_QUE_COS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0035_12_Tu_E_COM_POS_PAS_SOL_PER_PAR_CON_LUI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0035_13_AssistenteBibliotecario_MI_SPI_DEV_PER_FOR_AVE_UN_DOC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0035_14_Tu_E_VA_BEN_)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["rifiutatoDallaBiblioteca"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoDopoArrivoInBiblioteca"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0444_01_AssistenteBibliotecario_EHI_DEV_FOR_UN_DOC_PER_ENT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0444_02_Tu_VA_BEN_VA_BEN_LO_RIC_A_DAV_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoDopoArrivoInBiblioteca"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0036_01_Tu__ECC_IL_CER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0036_02_AssistenteBibliotecario_PER_TI_DO_LA_BEN_NEL_BIB_AL_PIA_TER_TRO_TUT_GLI_SCR_RIG_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0445_01_Tu__ECC_IL_CER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0445_02_AssistenteBibliotecario_PER_TI_DO_LA_BEN_NEL_BIB_AL_PIA_TER_TRO_TUT_GLI_SCR_RIG_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoAssistBiblioteca":
            partiDialogo = []
            nome = LI.ASSISTENTE_BIBLIOTECARIO
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["mostratoCertificatoPerIngressoBiblioteca"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0446_01_Tu_DOV_IL_BIB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0446_02_AssistenteBibliotecario__SEN_RAG__CON_ESP_LOR_DEI_REP_AI_NUO_ARR_PRI_DI_FAR_LE_TUE_DOM_DOV_ALM_AVE_LA_DEC_DI_RIS_E_ASC_CHI_HAI_DI_FRO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0446_03_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0446_04_AssistenteBibliotecario_MI_STA_ASC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0446_05_Tu__S_MA_IO_HO_BIS_DI_PAR_COL_BIB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0446_06_AssistenteBibliotecario__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0446_07_AssistenteBibliotecario_COM_TI_PAR__AL_PRI_PIA_MA_DI_SIC_NON_VOR_ESS_DIS_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["mostratoCertificatoPerIngressoBiblioteca"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0447_01_Tu_DOV_IL_BIB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0447_02_AssistenteBibliotecario_PRI_PIA_TI_HO_DET_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0448_01_Tu_NON_HO_NIE_DA_CHI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0449_01_Tu_NON_SON_RIM_IN_BUO_RAP_CON_LUI_NON_CRE_VOG_AIU_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo3":
            partiDialogo = []
            nome = LI.SCONOSCIUTO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoBibliotecario"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0450_01_Tu__SEI_TU_IL_BIB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0450_02_Sconosciuto_NO_LUI__DAL_PAR_DI_QUE_SCA_ADE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0450_03_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0450_04_Sconosciuto__CHE_C_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0450_05_Tu__DAL_PAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0450_06_Sconosciuto__S_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoBibliotecario"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0451_01_Tu__SEI_TU_IL_BIB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0451_02_Sconosciuto_NO_TI_HO_DET_CHE_NON_SON_IO_LUI__DAL_PAR_DI_QUE_SCA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0451_03_Tu__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0452_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo1":
            partiDialogo = []
            nome = LI.SCONOSCIUTO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoBibliotecario"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0453_01_Tu__SEI_TU_IL_BIB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0453_02_Sconosciuto_NO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0453_03_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0453_04_Sconosciuto__DOV_ESS_AL_PIA_DI_SOP_ADE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0453_05_Tu__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoBibliotecario"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0454_01_Tu__SEI_TU_IL_BIB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0454_02_Sconosciuto_NO_TUT_BEN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0454_03_Tu__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0455_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0456_01_Tu_EHI_SCU_IL_DIS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0456_02_Sconosciuto_SHH_NON_SI_PAR_IN_BIB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0456_03_Tu__S_MA_UNA_DOM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0456_04_Sconosciuto_SHHH_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza3":
            partiDialogo = []
            nome = LI.SCONOSCIUTA
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoBibliotecario"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0457_01_Tu__SEI_TU_IL_BIB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0457_02_Sconosciuta_NO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0457_03_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0457_04_Sconosciuta__PER_MI_FIS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0457_05_Tu__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoBibliotecario"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0458_01_Tu__SEI_TU_IL_BIB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0458_02_Sconosciuta_NO_NON_SON_IO_IL_BIB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0458_03_Tu__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0459_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca2"]:
        if tipo == "Ragazzo1":
            partiDialogo = []
            nome = LI.SCONOSCIUTO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoBibliotecario"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0460_01_Tu__SEI_TU_IL_BIB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0460_02_Sconosciuto_NO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0460_03_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0460_04_Sconosciuto__CHE_VUO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0460_05_Tu__NIENTE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoBibliotecario"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0461_01_Tu__SEI_TU_IL_BIB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0461_02_Sconosciuto_NO_NON_SON_IO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0461_03_Tu__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0462_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazzo2":
            partiDialogo = []
            nome = LI.SCONOSCIUTO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoBibliotecario"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0463_01_Tu__SEI_TU_IL_BIB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0463_02_Sconosciuto_NO__QUE_SIG_CON_LA_BAR_LAG_TRA_LE_DUE_COL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0463_03_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0463_04_Sconosciuto__QUE_SIG_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0463_05_Tu__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoBibliotecario"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0464_01_Tu__SEI_TU_IL_BIB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0464_02_Sconosciuto_NO__QUE_SIG_UN_PO_ANZ_LAG_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0464_03_Tu__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0465_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0466_01_Tu_SCU_IL_DIS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0466_02_Sconosciuto_SHH_SIL_IN_BIB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0466_03_Tu__UNA_DOM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0466_04_Sconosciuto_SHHH_)
                partiDialogo.append(dialogo)
        elif tipo == "Ragazza1":
            partiDialogo = []
            nome = LI.SCONOSCIUTA
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoBibliotecario"] and avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0467_01_Tu__SEI_TU_IL_BIB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0467_02_Sconosciuta_NO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0467_03_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0467_04_Sconosciuta_NON_SON_IO_IL_BIB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0467_05_Tu__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontratoBibliotecario"] and avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0468_01_Tu__SEI_TU_IL_BIB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0468_02_Sconosciuta_NO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0468_03_Tu__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0469_01_Tu_NON_MI_VA_DI_PAR_CON_LE_ALT_PER_ADE_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoLibriImpo":
            partiDialogo = []
            nome = LI.LIBRO
            if x == GlobalHWVar.gpx * 12:
                nome = LI.LIBRO_SCOPO_DEGLI_IMPO
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0470_01_Tu_QUE_LIB_SIN_SC_DEG_IMP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0470_02_LibroScopoDegliImpo__COM_GI_SPI_IN_PRE_CI_CHE_SPI_GLI_IMP_AD_AGI__DET_DAG_IMP_TUT_ESI_DUE_CAS_ECC_IN_CUI_LAZ_COM__DOV_AD_ALT_RAG_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0470_03_LibroScopoDegliImpo__IL_PRI_CAS_IN_CUI_GLI_IMP_NON_VEN_ESE_SI_PRE_QUA_LIM__ATT_A_QUE_PUN_LIM_PRO_DEL_PIE_INI_AD_AVV_A_ESS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0470_04_LibroScopoDegliImpo__IL_SEC_CAS_SI_PRE_QUA_NES_IMP_PU_ESS_ESE_MA__STA_SOD_UN_CON_IN_PRE_CHE_HA_UN_OBI_CHE_NON__PI_NEL_CAM_VIS_IN_QUE_CAS_LIM_MEM_LA_POS_IN_CUI_HA_VIS_LOB_E_SE_AVR_ABB_ENE_PER_ESE_LAZ_SI_MUO_IN_QUE_DIR_FIN_NON_ESE_LAZ_O_RAG_LA_POS_)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 18:
                nome = LI.LIBRO_SACCHE_ENERGETICHE
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0471_01_Tu_QUE_LIB_SIN_SA_ENE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0471_02_LibroSaccheEnergetiche__LEN_DEG_IMP_VIE_CON_IN_DEL_SAC_DET_SA_ENE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0471_03_LibroSaccheEnergetiche__QUE_SAC_A_SEC_DEL_DIM_POS_CON_PI_O_MEN_ENE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0471_04_LibroSaccheEnergetiche__IN_UNO_DEG_ULT_STU_SI__SCO_CHE_LE_SAC_ENE_SON_RES_ANC_DEL_DEL_SIS_DIF_ALC_SAC_PER_DI_RES_ALL_AGG_SPE_MEN_ENE_)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 22:
                nome = LI.LIBRO_GESTIONE_DELL_IMPOFORZA
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0472_01_Tu_QUE_LIB_SIN_GE_DEL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0472_02_LibroGestioneDellImpoForza__LEN_DEG_IMP_PU_ESS_GES_SOL_IN_PAR_DAG_UMA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0472_03_LibroGestioneDellImpoForza__GLI_IMP_HAN_INF_UNI_DI_SOP_CHE_PER_LOR_DI_DIF_DAG_ATT_NEM_SFR_LA_PRO_ENE_PI__VIO_LAG_PI_ENE_VER_CON_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0472_04_LibroGestioneDellImpoForza__ANC_SE_REL_POC_INF_QUE_LOR_COM_NON_PU_ESS_ALT_DA_AGE_EST_)
                partiDialogo.append(dialogo)
            elif x == GlobalHWVar.gpx * 25:
                nome = LI.LIBRO_IMPOMALUS
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0473_01_Tu_QUE_LIB_SIN_IM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0473_02_LibroImpoMalus__GLI_IMP_SOF_NEG_AMB_TRO_CAL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0473_03_LibroImpoMalus__QUA_UN_IMP_SUP_LA_PRO_TEM_MAS_INI_A_PER_ENE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0473_04_LibroImpoMalus__GLI_IMP_SON_IN_GRA_DI_TOR_AUT_ALL_LOR_TEM_IDE_MA_PER_FAR_RAL_I_PRO_MOV_PER_UN_PO_DI_TEM_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["biblioteca3"]:
        if tipo == "OggettoLibreriaStudioBibliotecario":
            partiDialogo = []
            nome = LI.LIBRO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["spiegazioneEnigmaBibliotecario4"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0474_01_Tu_CI_SON_UN_SAC_DI_LIB_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["risoltoEnigmaBibliotecario"]:
                nome = LI.LIBRO_MOT_RET_UNI_ACC
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0475_01_Tu_ALL_HA_DET_DI_VED_IL_MO_RET_UNI_ACC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0475_02_Tu__OH_TRO_VED_SE_C_UNA_SPI_COM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0475_03_LibroMotoRettilineoUniformementeAccelerato_IN_QUE_LEZ_INI_A_TRA_IL_MOD_DEL_MOT_UNI_ACC_BR_UN_MO_RET_UNI_ACC__UN_TIP_DI_MOT_IN_CUI_UN_COR_SI_MUO_LUN_UNA_LIN_RET_CON_ACC_COS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0475_04_LibroMotoRettilineoUniformementeAccelerato_LE_FOR_CHE_SI_USA_PER_CAL_GLI_ESI_DI_QUE_TIP_DI_MOT_VEN_CHI_LE_ORA_DEL_MOT_RET_UNI_ACC_E_SON_PRI_DUE_BR_VF__VI__A_BR_S__VI__12_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0475_05_LibroMotoRettilineoUniformementeAccelerato_DOV_VF__LA_VEL_DEL_COR_IN_MET_AL_SEC_NEL_FIN_VI__LA_VEL_DEL_COR_IN_MET_AL_SEC_NEL_INI_A__LAC_IN_MET_AL_SEC_QUA_CHE_IL_COR_MAN_TRA_LEV_INI_E_LEV_FIN_T__IL_TEM_CHE_PAS_IN_SEC_TRA_LEV_INI_E_LEV_FIN_S__LO_SPA_PER_DAL_COR_IN_MET_TRA_LEV_INI_E_LEV_FIN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0475_06_LibroMotoRettilineoUniformementeAccelerato_OSS_SUL_FOR_DEL_MOT_UNI_ACC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0475_07_LibroMotoRettilineoUniformementeAccelerato_LA_PRI_EQU_DET_QUA__LA_REL_TRA_VEL_ACC_E_TEM_LA_DIF_DI_VEL_TRA_LEV_INI_E_QUE_FIN_DIP_DA_QUA_LAC_E_PER_QUA_TEM_ESS_VIE_APP_LA_SEC_FOR_INV_ESP_LA_DIS_PER_DA_UN_COR_IN_UN_DET_LAS_DI_TEM_IN_CUI_VIE_IMP_UNA_COS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0475_08_LibroMotoRettilineoUniformementeAccelerato_ESE_SUL_MOT_RET_UNI_ACC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0475_09_Tu_VED_SE_CE_N_UNO_SIM_ALL_MIA_SIT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0475_10_LibroMotoRettilineoUniformementeAccelerato_UN_CAR_DI_CAV_VIA_A_6_MS_SE_IL_CAR_RAL_CON_UNA_DEC_ACC_NEG_COS_DI_2_MS_QUA_SPA_PER_PRI_DI_FER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0475_11_LibroMotoRettilineoUniformementeAccelerato_LA_VEL_INI_DEL_CAR__VI__6_MS_BR_LA_VEL_FIN_DAT_CHE_SI_DEV_FER__VF__0_MS_BR_LAC_DAT_CHE__CON_ALL_DIR_DEL_CAR__NEG_A__2_MS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0475_12_LibroMotoRettilineoUniformementeAccelerato_PRI_DI_TUT__NEC_RIC_IL_TEM_CHE_IMP_IL_CAR_PER_FER_BR_DAL_REL_VF__VI__A_SI_OTT_T__VF__VI__A_BR_SOS_CON_I_DAT_CHE_ABB_T__0__6__2__3_BR_PER_FER_IL_CAR_IMP_3_SEC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0475_13_LibroMotoRettilineoUniformementeAccelerato_ORA_CHE_SAP_QUA_TEM_SER_PER_AZZ_LA_VEL_POS_CAL_QUA_DIS_PER_IL_CAR_PRI_DI_FER_TRA_LA_REL_S__VI__12_BR_OSS_S__6__12__9_BR_IL_CAR_SI_FER_DOP_9_MET_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0475_14_Tu_MMH_NON_SO_SE_HO_CAP_TUT_MA_SOS_I_DAT_NEL_FOR_DOV_AND_CRE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0476_01_Tu_NON_MI_VA_DI_LEG_ALT_SPI_DI_FOR_CHE_NON_CAP_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0477_01_Tu_LIB_DI_REN_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoRegistroBiblioteca":
            partiDialogo = []
            nome = "OggettoRegistroBiblioteca"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoBibliotecarioControlloRegistri"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0478_01_Tu_MMM_NON_CAP_NIE_DI_COM__ORG_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0479_01_Tu_HAN_NON__STA_SEG_SU_QUE_REG_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0480_01_Tu_UN_REG_DEL_BIB_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoLibreriaRegistri":
            partiDialogo = []
            nome = "OggettoLibreriaRegistri"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0481_01_Tu_SON_I_REG_DEL_BIB_QUE_DI_OGG__SUL_SCR_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0482_01_Tu_SON_I_REG_DEL_BIB_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoTavoloEnigmaBiblioteca":
            partiDialogo = []
            nome = "OggettoTavoloEnigmaBiblioteca"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["spiegazioneEnigmaBibliotecario1"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0483_01_Tu_CI_SON_DEI_FOG_E_UNA_PEN_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0484_01_Tu_NON_MI_MET_A_FAR_ALT_CAL_ADE_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0485_01_Tu_FOG_DI_REN_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoMocio":
            partiDialogo = []
            nome = "OggettoMocio"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0486_01_Tu_NON__BAS_PER_PUL_)
            partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo


