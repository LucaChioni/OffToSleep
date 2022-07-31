# -*- coding: utf-8 -*-

import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.Localizzazione.LocalizInterfaccia as LI
import Codice.Localizzazione.LocalizDialoghiPrincipali as LDP


def setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute):
    tipo = tipoId.split("-")[0]

    partiDialogo = []
    nome = LI.TUTORIAL
    oggettoDato = False
    avanzaStoria = False
    menuMercante = False
    scelta = False
    avanzaColDialogo = False
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoSognoSara1"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDP._0376_01_Tutorial_PER_MUO_USA_I_TAS_W_A_S_E_D_DEL_TAS_LA_CRO_DIR_DEL_CON_OPP_UTI_IL_MOU_CLI_CON_IL_TAS_SIN_SUL_CAS_VER_CUI_VUO_SPO_)
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDP._0376_02_Tutorial_MUO_VER_IL_BAU_DAV_A_TE_E_PRO_AD_APR_UTI_IL_TAS_SPA_DEL_TAS_A_DEL_CON_OPP_CLI_SOP_CON_IL_TAS_SIN_DEL_MOU_)
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["aperturaPrimoCofanetto"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDP._0377_01_Tutorial_HAI_TRO_UNA_POZ_PUO_USA_DAL_MEN_A_CUI_PUO_ACC_PRE_ESC_SUL_TAS_MEN_DEL_CON_O_IL_TAS_CEN_DEL_MOU_)
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDP._0377_02_Tutorial_DAL_MEN_POT_ACC_ANC_A_EQ_DOV_POT_SEL_ARM_PRO_E_ACC_DA_EQU_)
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialUtilizzoOggetti"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDP._0378_01_Tutorial_DAV_A_TE_C_UN_NEM_PER_VED_LE_SUE_INF_PAS_ALL_MOD_INT_PRE_IL_TAS_E_DEL_TAS_X_DEL_CON_O_IL_TAS_DES_DEL_MOU_E_INQ_SPO_IL_PUN_SUL_SUA_CAS_)
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDP._0378_02_Tutorial_UNA_VOL_INQ_PUO_SEL_E_ATT_PRE_SPA_SUL_TAS_A_DEL_CON_O_IL_TAS_SIN_DEL_MOU_DAT_CHE_AL_MOM_NON_HAI_FRE_PUO_ATT_SOL_DA_VIC_BR_PER_DES_LOB_PRE_Q_SUL_TAS_B_DEL_CON_O_IL_TAS_DES_DEL_MOU_SUL_SUO_STA_IN_ALT_A_SIN_DEL_SCH_)
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDP._0378_03_Tutorial_ATT_SE_CI_SON_DEI_NEM_PRE_NEL_STA_PRE_ESC_DEL_TAS_MEN_DEL_CON_O_IL_TAS_CEN_DEL_MOU_VER_APE_UN_MEN_RAP_CHE_PER_DI_COM_MEN_OPE_RIP_AL_MEN_NOR_)
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialBattaglia"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDP._0379_01_Tutorial_FAI_ATT_A_QUE_PIP__VEL_E_ATT_A_DIS_)
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDP._0379_02_Tutorial_SE_VUO_ING_ASS_DI_POT_ATT_A_DIS_PRI_CHE_TI_POS_VED_IN_QUE_BAU_POT_ESS_QUA_CHE_FA_AL_CAS_TUO_)
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDP._0379_03_Tutorial_OPP_PUO_SEM_EVI_ASP_IL_MOM_GIU_PER_PAS_PER_SAL_UN_TUR_PRE_IL_TAS_0_DEL_TAS_VIE_DEL_CON_OPP_CLI_CON_IL_TAS_SIN_DEL_MOU_SUL_REL_ICO_IN_ALT_A_DES_DEL_SCH_)
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoCasaHansSara1"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDP._0380_01_Tutorial__POS_RIC_LE_POR_UTI_LA_MOD_INT_)
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["messoBicchiereConAcquaSulComodino"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDP._0381_01_Tutorial_IN_MOD_INT_LE_CAS_FUO_DAL_TUO_CAM_VIS_VEN_OSC_)
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDP._0381_02_Tutorial_INQ_UN_NEM_INO_VER_OSC_IN_ROS_LE_CAS_CHE_LUI_NON_RIE_A_VED_QUA_UN_NEM_TI_VED_LOC_IN_ALT_A_DES_DEL_SCH_SI_APR_VIC_QUA_SEI_FUO_DAL_CAM_VIS_DI_TUT_I_NEM_LOC_SAR_CHI_)
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDP._0381_03_Tutorial_DAT_CHE_AL_MOM_SEI_DIS_NON_TI_CON_AFF_I_NEM_A_VIS_APE_PRO_A_PAS_SEN_FAR_VED_)
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialCampoVisivo"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDP._0382_01_Tutorial_IN_MOD_INT_CLI_SU_TE_STE_ASS_UNA_POS_DIF_CHE_TI_PER_DI_SUB_MEN_DAN_FAC_IN_UN_LUO_SIC_INV_TI_PER_DI_RIP_E_REC_TUT_I_PV_)
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["quintaStanzaForestaCadetta"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDP._0383_01_Tutorial_ASS_LA_POS_DIF_IN_LUO_SIC_REC_TUT_I_PV_)
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["trovatoMappaDiario"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDP._0384_01_Tutorial_LA_MAP_E_IL_DIA_SI_POS_APR_DAL_MEN_CLI_SUL_REL_VOC_)
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["armaturaNonnoCompletata"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDP._0385_01_Tutorial_QUA_UCC_UN_NEM__POS_INT_COL_SUO_CAD_PER_SOT_E_DEP_)
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["introduzioneImpoDalBibliotecario"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDP._0386_01_Tutorial_PER_ATT_E_DIS_LIM_USA_IL_TAS_SHI_DEL_TAS_Y_DEL_CON_OPP_CLI_SUL_SUA_ICO_IN_ALT_A_DES_DEL_SCH_CON_IL_TAS_SIN_DEL_MOU_)
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDP._0386_02_Tutorial_NEL_MEN__APP_LA_VOC_SE_IMP_SEL_PER_GES_GLI_EQU_DI_IMP_BR_ATT__POS_ACC_SOL_SE_IMP_SI_TRO_IN_UNA_CAS_RAG_DA_SAR_)
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoUscitaBibliotecaDirettoVersoNeil"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDP._0387_01_Tutorial_CLI_SU_IMP_IN_MOD_INT_POT_VED_LA_SUA_PRO_MOS_BR_MA_FAI_ATT_IL_MOV_DI_SAR_PU_INT_E_ANN_LE_CON_PRE_IN_CON_NEL_PRE_)
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoSelvaArida"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDP._0388_01_Tutorial_DUR_LA_BAT_PUO_USA_GLI_IMP_SOL_SE_IMP__IN_UNA_CAS_ADI_A_QUE_DI_SAR_PER_USA_FUO_DAL_COM_INV__SUF_CHE_IMP_SIA_IN_UNA_CAS_RAG_)
        partiDialogo.append(dialogo)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostRisoluzioneEnigma"]:
        oggettoDato = False
        avanzaStoria = True
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDP._0389_01_Tutorial_FIN_SEI_NEL_LAB_PRE_IL_TAS_ESC_DEL_TAS_MEN_DEL_CON_O_IL_TAS_CEN_DEL_MOU_AND_DIR_ALL_MAP_DA_L_POT_SPO_NOR_NEL_MEN_)
        partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo


