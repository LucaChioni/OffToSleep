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
    if tipo == "PadreUfficialeServizio":
        partiDialogo = []
        nome = "David"
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["arrivoCasaUfficiale"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0048_01_David_ECCOCI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0048_02_Tu__ENORME_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0048_03_David_AVV_CHE_ABB_OSP_PER_CEN_SEG_LA_SAL_DA_PRA__AL_PIA_DI_SOP_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["giratoDavidVersoIlBasso"]:
            oggettoDato = LI.CHIAVE_STANZA
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0049_01_David_LA_TUA_STA__GI_STA_PRE__LUL_POR_A_DES_DI_QUE_COR_VAI_PUR_A_CAM_QUE__LA_CHI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0049_02_Tu_OK_A_DES_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0049_03_David_E_NEL_POR_IN_FON_AL_COR_C_IL_BAG_SE_HAI_BIS_DI_DAR_UNA_RIP_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0049_04_Tu_OOK_GRA_VAD_A_DAR_UNA_RIP_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0049_05_David_TI_ASP_PER_LA_CEN_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0557_01_David_VAI_PUR_A_CAM_AL_TUO_RIT_LA_CEN_SAR_SER_)
            partiDialogo.append(dialogo)
    elif tipo == "ServoDavid":
        partiDialogo = []
        nome = LI.SERVO
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"] and avanzamentoDialogo == 0:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0558_01_Tu_UHM_SALVE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0558_02_Servo_SAL_POS_ESS_DAI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0558_03_Tu_NO_CIO_TU_LAV_QUI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0558_04_Servo_S_AL_MOM_SON_IN_SER_SE_HA_BIS_DI_QUA_PU_CHI_A_ME_O_AGL_ALT_SER_RES_QUI_PER_LA_NOT_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0558_05_Tu_S_SOL_PER_STA_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0558_06_Servo_PER_ALL_PU_CAM_IN_UNA_DEL_STA_PER_GLI_OSP_AL_PIA_DI_SOP_IL_PAD_NE_STA_GI_FAC_PRE_UNA_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0558_07_Tu_VA_BEN_GRA_)
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"] and avanzamentoDialogo == 1:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0559_01_Servo_PU_CAM_IN_UNA_DEL_STA_PER_GLI_OSP_AL_PIA_DI_SOP_IL_PAD_NE_STA_GI_FAC_PRE_UNA_)
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sedutoACenaDavid"] and avanzamentoDialogo == 1:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0560_01_Servo_LA_CEN__SER_LA_PRE_DI_PRE_POS_)
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and avanzamentoDialogo == 1:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0561_01_Tu_SCU_PER_CAS_HAI_VIS_SE_DAV__PAS_DI_QUI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0561_02_Servo_S__APP_USC_MA_NON_SO_DOV_FOS_DIR_)
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and avanzamentoDialogo == 2:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0562_01_Servo_LA_PRE_DI_AND_A_RIP_TRA_POC_SAR_GIO_)
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0563_01_Servo_SAL_SIG_LA_SUA_STA__STA_PRE_PU_AND_A_CAM_)
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sedutoACenaDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0564_01_Servo_LA_PRE_DI_PRE_POS_LA_CEN__SER_)
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0565_01_Servo_LA_SUA_STA__IN_FON_AL_COR_PU_AND_A_RIP_QUA_VUO_)
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["vistoDalServo"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0566_01_Servo_SAL_AL_MOM_IL_PAD_NON__IN_CAS_POS_ESS_DAI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0566_02_Tu_NO_GRAZIE_)
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["vistoDalServo"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0050_01_Servo_SIG_SAR_COS_CI_FA_DI_NUO_QUI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0050_02_Tu_CIA_SON_VEN_PER_RIC_IL_CER_DI_PER_IN_CIT_MI_SER_PER_AND_IN_BIB_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0050_03_Servo_AH_IL_CER_DAV_LAV_PRE_DEV_DIM_DI_DAR_VAD_SUB_A_PRE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0050_04_Tu_OK_MA_COM_MAI_CI_SON_DEI_SOL_QUI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0050_05_Servo_OLI_SI__FAT_MAL_POC_FA_NON_SO_BEN_COS_SIA_SUC_DEV_STA_UN_INC_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0050_06_Tu_MA_STA_BEN_ADE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0050_07_Servo_NON_SO_ERA_PRI_DI_SEN_QUA_LHO_TRO_E_HA_PER_MOL_SAN_MA_NON_TI_DEV_PRE_CI_SON_I_MIG_MED_DEL_CIT_AD_ASS_ADE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0050_08_Servo_ORA_RIM_UN_ATT_QUI_TOR_SUB_CON_IL_CER_)
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["servoArrivaConCertificazione"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0567_01_Servo_RIM_UN_ATT_QUI_TOR_SUB_CON_IL_CER_)
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["servoArrivaConCertificazione"]:
            oggettoDato = LI.CER_DI_RES
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0051_01_Servo_SIG_ECC_IL_CER_ERA_GI_PRO_COM_PEN_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0051_02_Tu_GGRAZIE_MILLE_)
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"] and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0568_01_Servo_NON_MI_HAN_ANC_DET_NIE_DEL_SIT_DI_OLI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0568_02_Tu__)
            partiDialogo.append(dialogo)
        elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid3"] and avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0052_01_Servo__BUO_SIG__MAT_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0052_02_Tu_UH_OHH_BUO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0052_03_Servo_COS_DES_PER_COL_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0052_04_Tu_NO_NON_IMP_NON_SON_SOL_FAR_COL_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0052_05_Servo_COM_PRE_SE_CAM_IDE_NON_SI_FAC_PRO_A_FAR_PRE_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0569_01_Servo_SAL_AL_MOM_IL_PAD_NON__IN_CAS_POS_ESS_DAI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0569_02_Tu_NO_GRAZIE_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0570_01_Servo__)
            partiDialogo.append(dialogo)
    elif tipo == "MadreUfficiale":
        partiDialogo = []
        nome = "Olivia"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sedutoACenaDavid"] and avanzamentoDialogo == 0:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0571_01_Tu_SAL_MI_CHI_SAR_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0571_02_Olivia__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0571_03_Tu_UHM_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0571_04_Olivia__OLI_SON_LA_MOG_DI_DAV_E_LA_MAD_DI_SAM_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0571_05_Tu_OK_PIACERE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0571_06_Olivia__)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sedutoACenaDavid"] and avanzamentoDialogo == 1:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0572_01_Tu_NON_CRE_VOG_PAR_SEM_DIS_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoCenaDavid1"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0053_01_Olivia__)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoLettoCasaDavid":
        partiDialogo = []
        nome = "OggettoLettoCasaDavid"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sedutoACenaDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0573_01_Tu_QUE_SAR_IL_MIO_LET_PER_STA_NON_VED_LOR_DI_DOR_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["fineDialogoCenaDavid"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0054_01_Tu_STO_MOR_DI_SON_PEN_A_TUT_DOM_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["uscitoCasaDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0574_01_Tu_NON_POS_RIM_A_DOR_ADE_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0575_01_Tu__UN_LET_MOL_COM_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0576_01_Tu_UN_LETTO_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0577_01_Tu_NON__IL_MIO_LET_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoArmadioCasaDavid":
        partiDialogo = []
        nome = "OggettoArmadioCasaDavid"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fattoBagnoCasaDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0578_01_Tu_QUA_CI_SON_UN_PO_DI_VES_MA_CRE_CHE_DOV_DAR_UNA_RI_PRI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0578_02_Tu_HA_DET_CHE_IL_BAG__IN_FON_AL_COR_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoDopoBagnoDavid"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0055_01_Tu_OK_CI_SON_UN_BEL_PO_DI_VES_QUI_VED_QUE_SEM_OK_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sedutoACenaDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0579_01_Tu_CI_SON_ALT_VES_TRA_CUI_SCE_MA_QUE_VAN_PI_CHE_BEN_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0580_01_Tu_NON_HO_BIS_DI_ALT_VES_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0581_01_Tu_CI_SON_I_MIE_VEC_VES_NON_MI_ENT_PI_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoVascaCasaDavid":
        partiDialogo = []
        nome = "OggettoVascaCasaDavid"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presaChiaveStanzaDaLettoDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0582_01_Tu_SEM_UNA_VAS_COM_QUE_CHE_USI_A_CAS_PER_LAV_CHI_SE_MIO_PAD_HA_PRE_SPU_DA_UNA_COM_QUE_PER_FAR_LA_NOS_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["cambiatoPercorsoDavid"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0056_01_Tu_OK_CRE_CHE_QUE_VAS_FUN_PI_O_MEN_COM_QUE_CHA_ABB_A_CAS_VED_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sedutoACenaDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0583_01_Tu_VOR_RIE_IN_QUE_PIC_PAR_MA_MI_STA_ASP_PER_LA_CEN_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0584_01_Tu_NON_HO_BIS_DI_LAV_ADE_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0585_01_Tu_UNA_VASCA_)
            partiDialogo.append(dialogo)
    elif tipo == "PadreUfficialeCasa":
        partiDialogo = []
        nome = "David"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sedutoACenaDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0586_01_David_SIE_PUR_LA_CEN__SER_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["cenaConDavidIniziata"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0057_01_Tu___BUO_COS_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0057_02_David__CIN_IN_UMI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0057_03_Tu_CAV__DAV_GNA_GNA_MI_PIA_UN_SAC_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0057_04_David_VEDO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0057_05_Tu_OH_SCU_UHM_SCU_NON_VOL_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0057_06_David_UMPF_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0057_07_Tu___CHE_AVE_MOL_FAM_NON_MI_ERO_ACC_DI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0057_08_David__)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoCenaDavid2"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0058_01_Tu__EHM_NON_SON_ABI_A_MAN_COS_COS_BUO__UN_PIA_COM_QUI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0058_02_David__LO_ERA_PAR_CHE_I_CIN_SI_STI_EST_ADE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0058_03_Tu_OH_NE_AVE_SEN_PAR_COM_MAI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0058_04_David__CAM_CLI_CAC_TRO_FRE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0058_05_Tu_AH_DEV_UNA_PRE_DES_E_CAC_DA_CHI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0058_06_David__DA_CHI_SIA_CAP_DI_CAC_QUA_NON_DI_CER_DAI_DEB_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["mammaUfficialeUscitaDallaCena"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0059_01_David__IN_REA_LA_RAG__UNA_MOL_LHA_SOT_MA_LA_PUT_DEL_LAG_AVR_MOL_CON_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0059_02_Tu__COSA_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0059_03_David__UNA_VEN_DI_ANN_FA_IL_LAG__STA_AVV_NON_SOL_PER_LE_PER_MA_ANC_PER_LE_IMB_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0059_04_Tu__DAV_COS_OLI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0059_05_David__IL_LEG_VIE_COR_QUA_ENT_IN_CON_CON_QUE_POL_PUT_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0059_06_Tu_DAV_OLI_NON_CRE_STI_BEN_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0059_07_David_S__MOR_SUO_FIG_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0059_08_Tu__COSA_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0059_09_David_ABB_BIS_DI_UOM_PI_FOR_SAR_LUI_ERA_UN_DEB_LO__SEM_STA_NON_POS_PER_DEI_DEB_A_CAP_DEL_NOS_SQU_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0059_10_Tu__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0059_11_David_MA_NON_IMP_NON_AVR_FAT_ALC_DIF_NES_SAR_MAI_IN_GRA_DI_FRO_QUE_CHE_CI_ACC_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0059_12_Tu__COS_COS_CI_ACC_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0059_13_David_NON_TI_PRE_SAR_SAR_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0059_14_Tu_C_UNA_GUE_IN_COR_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0059_15_David__SAR__UN_BEL_NOM_SAR_MI_RIC_QUE_RAG_AL_PRI_ANN_DI_ADD_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0059_16_Tu_DAV_C_UNA_GUE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0059_17_David_ERA_COS_BEL_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0059_18_Tu__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0059_19_David__E_SIM_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0059_20_Tu__SEI_UBR_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0059_21_David_TSK_SAR_TOR_NEL_TUA_STA_E_DOR_DOM_DOV_SVE_PRE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0059_22_Tu__C_UNA_GUE_CHE_STI_PER_DAV_E_NES_LO_SA_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0059_23_David_BAS_COS_SME_DI_PAR_DI_QUE_COS_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0059_24_David_ANZ_SME_PRO_DI_PAR_NON_HO_PI_VOG_DI_CON_A_SEN_PER_CHE_MI_FAN_SEM_PI_PRO_E_QUE_E_PRO_OGN_VOL_CHE_PAR_DI_PRO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0059_25_Tu__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0059_26_David_OHHH_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0059_27_Tu__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0059_28_Tu__E_PER_MI_HAI_OSP_PER_CEN_ALL_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0059_29_David__UMPF_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0059_30_Tu__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0059_31_David__IL_SOL_DA_CUI_HAI_PRE_QUE_DAC_DOV_LHA_SEP_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0059_32_Tu_CHE_CEN_ADE_QUE_OH_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0059_33_Tu_ERA_ERA_IN_MEZ_ALL_FOR_POC_DIS_DA_UN_ACC_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0059_34_David__)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0587_01_David__)
            partiDialogo.append(dialogo)
    elif tipo == "Ragazza2":
        partiDialogo = []
        nome = LI.SCONOSCIUTA
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDS._0588_01_Sconosciuta__)
        partiDialogo.append(dialogo)
    elif tipo == "OggettoSediaCasaUfficiale":
        partiDialogo = []
        nome = "OggettoSediaCasaUfficiale"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sedutoACenaDavid"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0060_01_Tu_MI_SIE_QUI_)
            partiDialogo.append(dialogo)
    elif tipo == "GuardiaCitta":
        partiDialogo = []
        nome = LI.SOLDATO
        if stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"]:
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["servoAndatoPrendereCertificazione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0061_01_Soldato_NON_PUO_AND_DI_L_AL_MOM_CI_SON_DEL_IND_IN_COR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0061_02_Tu_CHE_COS_SUC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0061_03_Soldato_STI_IND_SEM_TRA_DI_SUI_MA_MAC_ANC_DEI_PRE_VAL_POT_ESS_STA_SEM_UN_INC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0061_04_Tu__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0589_01_Soldato_NON_PUO_PAS_CI_SON_DEL_IND_IN_COR_)
                partiDialogo.append(dialogo)

    elif tipo == "OggettoQuadroA":
        partiDialogo = []
        nome = "OggettoQuadro"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0590_01_Tu_UNA_STR_NEL_FOR_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0591_01_Tu_UN_QUADRO_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoQuadroB":
        partiDialogo = []
        nome = "OggettoQuadro"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0592_01_Tu_DEL_MON_NEL_BUI_DEL_NOT_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0593_01_Tu_UN_QUADRO_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoQuadroC":
        partiDialogo = []
        nome = "OggettoQuadro"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0594_01_Tu_UNA_SPI_ILL_DAL_CIE_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0595_01_Tu_UN_QUADRO_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoVaso":
        partiDialogo = []
        nome = "OggettoVaso"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0596_01_Tu__UN_VAS_CON_DEG_STR_DIS_SOP_SEM_MOL_ANT_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0597_01_Tu_UN_VASO_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoLibreria":
        partiDialogo = []
        nome = "OggettoLibreria"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            if stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid1"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0598_01_Tu_QUA_CI_SON_DEI_LIB_NON_NE_CON_NEA_UNO_)
                partiDialogo.append(dialogo)
            elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["casaDavid2"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0599_01_Tu_CI_SON_UN_SAC_DI_LIB_COM_SI_FA_AD_AVE_VOG_DI_LEG_TUT_QUE_ROB_)
                partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0600_01_Tu_DEI_LIBRI_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoMappamondo":
        partiDialogo = []
        nome = "OggettoMappamondo"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0601_01_Tu_SU_QUE_TAV__STA_INC_UNA_MAP_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0602_01_Tu_UNA_MAPPA_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoTavoloVaso":
        partiDialogo = []
        nome = "OggettoTavoloVaso"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0603_01_Tu_UN_ALT_TAV_CON_DEL_COS_SOP_PER_ARR_A_CHE_SER__SOL_TEM_BUT_PER_LE_PUL_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0604_01_Tu_UN_TAV_CON_DEL_COS_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoCamino":
        partiDialogo = []
        nome = "OggettoCamino"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0605_01_Tu_SEM_CHE_QUE_CAM_NON_SIA_MAI_STA_USA_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0606_01_Tu_UN_CAMINO_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoTavoloMappamondo":
        partiDialogo = []
        nome = "OggettoTavoloMappamondo"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0607_01_Tu_C_UNA_MAP_COM_QUE_AL_PIA_DI_SOT_E_UN_MOD_MOL_ACC_DI_UNA_BAR_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0608_01_Tu_UN_TAV_CON_DEL_COS_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoTavoloBusto":
        partiDialogo = []
        nome = "OggettoTavoloBusto"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0609_01_Tu_SU_QUE_TAV_C_UN_ALT_VAS_UNA_BAR_E_UN_BUS_DI_DA_VI_CHE_SIA_UN_ANT_DI_DAV_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0610_01_Tu_UN_TAV_CON_DEL_COS_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoComodinoCasaDavid":
        partiDialogo = []
        nome = "OggettoComodinoCasaDavid"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0611_01_Tu_NON_C_NIE_IN_QUE_CAS_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0612_01_Tu_UN_COMODINO_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoGabinetto":
        partiDialogo = []
        nome = "OggettoGabinetto"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0613_01_Tu_MA__UN_GAB_INC_HA_ANC_DEL_PLA_IN_ORO_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0614_01_Tu_UN_GABINETTO_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoLavandinoCasaDavid":
        partiDialogo = []
        nome = LI.SPECCHIO
        if avanzamentoDialogo == 0 and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presaChiaveStanzaDaLettoDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0615_01_Tu_PRO_IL_LAV_PI_COS_DEL_MON_)
            partiDialogo.append(dialogo)
        elif avanzamentoDialogo == 0 and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0616_01_Tu_PRO_IL_LAV_PI_COS_DEL_MON_CI_SON_ANC_UN_SAC_DI_SAP_PRO_E_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0616_02_Tu_OOO_QUE__UNO_SPE__ENO_NOI_A_CAS_NE_ABB_UNO_MOL_PI_PIC_CHE_USA_SOL_MIA_MAD_LO_CUS_GEL_IN_UN_COF_)
            partiDialogo.append(dialogo)
        elif avanzamentoDialogo == 1 and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fattoBagnoCasaDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0617_01_Specchio_EHI_MA_CHE_CAR_QUE_RAG_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0617_02_Tu_OH_MA_SAL_IL_MIO_NOM__SAR_PIA_DI_CON_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0617_03_Specchio_PIA_SAR_HAI_PRO_UN_BEL_VIS_SAI_SAR_PER_SE_NON_FOS_PER_QUE_OCC_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0617_04_Tu_COS_QUE_NON_SON_OCC_SON_SOL_LE_LUC_CHE_FAN_DEI_RIF_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0617_05_Specchio_ED_EMA_ANC_UNO_SGR_ODO_SAR_PRO_IL_CAS_CHE_TI_DES_UNA_RI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0617_06_Tu__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0617_07_Tu_UFF_MI_DEV_LAV_)
            partiDialogo.append(dialogo)
        elif avanzamentoDialogo == 1 and GlobalGameVar.dictAvanzamentoStoria["fattoBagnoCasaDavid"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0618_01_Tu_MI_SEN_RIG_DOP_QUE_BAG_NON_HO_NEA_PI_QUE_FAS_OCC_)
            partiDialogo.append(dialogo)
        elif avanzamentoDialogo == 2 and avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fattoBagnoCasaDavid"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0619_01_Tu_MEG_CHE_MI_DIA_UNA_RI_PRI_DI_AND_A_TAV_)
            partiDialogo.append(dialogo)
        elif avanzamentoDialogo == 2 and GlobalGameVar.dictAvanzamentoStoria["fattoBagnoCasaDavid"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = True
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0620_01_Tu_EHI_SPE_CHI__CHE_HA_LE_OCC_ADE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0620_02_Specchio_TU_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0620_03_Tu_CAV_PER_NON_VAN_VIA_)
            partiDialogo.append(dialogo)
        elif avanzamentoDialogo == 3 and GlobalGameVar.dictAvanzamentoStoria["fattoBagnoCasaDavid"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0621_01_Tu_ALM_NON_PUZ_PI_DI_SUD_COM_PRI_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0622_01_Tu_PRO_IL_LAV_PI_COS_DEL_MON_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0623_01_Tu_UN_LAVANDINO_)
            partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo


