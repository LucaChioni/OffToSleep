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
    if tipo == "OggettoLettoSara":
        partiDialogo = []
        nome = "Sara"
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0037_01_Sara__UH_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0037_02_Tu_EHI_HAI_FAT_UN_BRU_SOG_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0037_03_Sara_NO_IO_STA_STA_CER_NON_LO_SO_NON_IMP_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0037_04_Sara_PER_SEI_SVE_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0037_05_Tu_STA_AND_IN_BAG_VA_TUT_BEN_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0037_06_Sara_S_S_MI_POR_UN_BIC_DAC_QUA_TOR_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0037_07_Tu_OK_)
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["dialogoCasaHansSara1"] <= avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["tutorialChiusuraPorte"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0487_01_Sara_YAA_STO_ANC_ASP_LA_MIA_ACQ_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ottenutoBicchiere"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0488_01_Sara_DAI_HAN_MI_HAI_POR_UN_BIC_VUO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0488_02_Tu_AH_LO_VOL_CON_LAC_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0488_03_Sara_MMH_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ottenutoBicchiereAcqua"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0038_01_Tu_SARA_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0038_02_Sara_ZZZ_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0038_03_Tu_SI__GI_RIA_POS_PAR_ADE_ALL_PRI_CHE_QUA_ALT_SI_SVE_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0489_01_Sara_ZZZ_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0490_01_Tu_NON_MI_RIM_A_DOR_)
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["monologoPerTornareIndietroNelTempoAllaSeraDellInizioDelGioco"] <= avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["HansUscitoDaCasa2NellaSeraDellInizioDelGioco"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0491_01_Sara_ZZZ_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoUscitaLaboratorioPostPassatiMoltiAnni"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0492_01_Tu_PER_EVI_LIN_ALL_FIN_DEL_GIO_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0493_01_Tu__IL_MIO_LET_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoLavandinoCucina" or tipo == "OggettoLavandinoBagno":
        partiDialogo = []
        nome = "OggettoLavandino"
        if avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["tutorialChiusuraPorte"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0494_01_Tu_DEV_PRE_UN_BIC_PRI_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ottenutoBicchiere"]:
            oggettoDato = LI.BIC_CON_ACQ
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0039_01_Tu_OK_HO_RIE_IL_BIC_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0495_01_Tu_NON_HO_PI_BIS_DAC_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0496_01_Tu_NON_HO_BIS_DAC_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0497_01_Tu__IL_LAV_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoScaffaleBicchieri":
        partiDialogo = []
        nome = "OggettoScaffaleBicchieri"
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialChiusuraPorte"]:
            oggettoDato = LI.BICCHIERE
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0040_01_Tu_ECC_UN_BIC_ORA_DEV_RIE_DAC_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0498_01_Tu_NON_MI_SER_ALT_BIC_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0499_01_Tu_NON_HO_BIS_DI_QUE_COS_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0500_01_Tu__LO_SCA_DOV_TEN_I_PIA_E_I_BIC_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoComodinoSara":
        partiDialogo = []
        nome = "OggettoComodinoSara"
        if avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["ottenutoBicchiereAcqua"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0501_01_Tu_QUE__LA_ROB_DI_SAR_C_IL_SUO_DIA_E_UN_FOG_ARR_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0501_02_Tu_NON_IMP_NON_PRE_QUE_COS_)
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["dialogoCasaHansSara2"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0502_01_Tu_HO_MES_QUA_IL_BIC_CON_LAC_)
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["trovatoMappaDiario"]:
            oggettoDato = LI.MAP_E_DIA
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0041_01_Tu_OK_MAP_E_DIA_PRE_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0503_01_Tu_NON_C_NIE_DI_IMP_DA_PRE_QUI_)
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["monologoPerTornareIndietroNelTempoAllaSeraDellInizioDelGioco"] <= avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["HansUscitoDaCasa2NellaSeraDellInizioDelGioco"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0504_01_Tu_HA_APP_MES_QUA_IL_BIC_DAC_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0505_01_Tu__IL_MIO_COM_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoComodinoHans":
        partiDialogo = []
        nome = "OggettoComodinoHans"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0506_01_Tu_NON_TEN_NIE_DI_UTI_QUI_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0507_01_Tu__IL_COM_DI_HAN_NON_C_NIE_DI_INT_SOL_UNA_PIC_LAN_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0508_01_Tu__IL_COM_DI_HAN_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoFinestra":
        partiDialogo = []
        nome = "OggettoFinestra"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0509_01_Tu__NOT_FON_DEV_PAR_ADE_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0510_01_Tu_HAN_STA_GUA_FUO_DAL_FIN_QUA_MI_SON_SVE_SPE_CHE_SIA_ANC_QUA_FUO_E_CHE_CI_STI_RIP_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0511_01_Tu__)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoLettoHans":
        partiDialogo = []
        nome = "OggettoLettoHans"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0512_01_Tu_NON_POS_RIM_A_DOR_NON_VOG_RIM_ANC_SON_PRO_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0513_01_Tu__IL_LET_DI_HAN_E_LUI_NON_C_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0514_01_Tu__IL_LET_DI_HAN_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoVasca":
        partiDialogo = []
        nome = "OggettoVasca"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0515_01_Tu__UNA_VAS_DA_BAG_LAB_FAT_IO_E_MIO_PAD_PER_POT_LAV_SEN_DOV_USC_DI_CAS_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0515_02_Tu_LA_PAR_PI_DIF_E_FAT__STA_SEN_DUB_COS_IL_CAN_PER_LAC_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0516_01_Tu__LA_VAS_CHE_USI_PER_LAV__MOL_COM_AVE_UNA_IN_CAS_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0517_01_Tu__LA_NOS_VAS_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoGabinetto":
        partiDialogo = []
        nome = "OggettoGabinetto"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0518_01_Tu_NON_HO_BIS_DI_USA_IL_GAB_ADE_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0519_01_Tu_NON_MI_SCA_LA_PIP_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0520_01_Tu__IL_GAB_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoCamino":
        partiDialogo = []
        nome = "OggettoCamino"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0521_01_Tu__UN_CAM_LO_USI_PER_RIS_LA_CAS_E_CUC_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0522_01_Tu__IL_CAM_CHE_USI_SEM_IO_E_LA_MAM_PER_CUC_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0523_01_Tu__IL_NOS_CAM_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoScaffaleCucina":
        partiDialogo = []
        nome = "OggettoScaffaleCucina"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ottenutoBicchiere"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0524_01_Tu__LO_SCA_DOV_CON_GLI_ALI_NIE_BIC_QUI_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0525_01_Tu__LO_SCA_DOV_CON_GLI_ALI_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0526_01_Tu_NON_HO_BIS_DI_CIB_NON_HO_FAM_ADE_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0527_01_Tu__LO_SCA_DOV_CON_GLI_ALI_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoTavolinoFiori":
        partiDialogo = []
        nome = "OggettoTavolinoFiori"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0528_01_Tu__UN_TAV_CON_DEI_FIO_LHA_VOL_MET_PER_SEM_UNO_SPA_TRO_VUO_)
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0529_01_Tu_CI_SON_DEI_BEL_FIO_CHE_SAR_GI_MOR_SE_NON_CI_FOS_IO_A_INN_)
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["trovataChiaveRipostiglio"]:
            oggettoDato = LI.CHI_DEL_RIP
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0042_01_Tu_SON_I_MIE_BEL_FIO_MA_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0042_02_Tu_EHI_SOT_IL_VAS_C_UNA_CHI_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0530_01_Tu_SOT_QUE_VAS_CER_LA_CHI_DEL_RIP_COM_HO_FAT_A_NON_ACC_PER_TUT_QUE_TEM_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0531_01_Tu_DEI_FIORI_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoComodinoMamma":
        partiDialogo = []
        nome = "OggettoComodinoMamma"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0532_01_Tu__IL_COM_DI_MIA_MAD_NIE_DI_INT_)
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["trovataChiaveRipostiglio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0533_01_Tu_NIE_LA_CHI_NON__QUI_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0534_01_Tu_NON_C_NIE_DI_UTI_PER_ME_QUI_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0535_01_Tu__IL_COM_DI_MAM_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoComodinoBabbo":
        partiDialogo = []
        nome = "OggettoComodinoBabbo"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0536_01_Tu__IL_COM_DI_MIO_PAD_NIE_DI_INT_QUI_SOL_UN_PO_DI_ROB_PUZ_)
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["trovataChiaveRipostiglio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0537_01_Tu_AVR_GIU_CHE_LA_CHI_FOS_QUI_DEV_CER_IN_UN_POS_PI_INS_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0538_01_Tu_NON_C_NIE_DI_UTI_PER_ME_QUI_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0539_01_Tu__IL_COM_DI_MIO_PAD_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoLettoGenitori":
        partiDialogo = []
        nome = "OggettoLettoGenitori"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0540_01_Tu_DEV_FAR_PIA_NON_VOG_SVE_)
            partiDialogo.append(dialogo)
        elif GlobalGameVar.dictAvanzamentoStoria["inizioRicercaChiaveRipostiglio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["trovataChiaveRipostiglio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0541_01_Tu_NON_CRE_CHE_TEN_LA_CHI_DEL_RIP_NEL_LET_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0542_01_Tu_STA_DOR_PRO_NON_DEV_FAR_RUM_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0543_01_Tu__IL_LET_DEI_MIE_GEN_)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoCancellettoCasa":
        partiDialogo = []
        nome = "OggettoCancellettoCasa"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0544_01_Tu_NON_VOG_AND_NEI_CAM_ADE_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0545_01_Tu_NON_CRE_CHE_HAN_SIA_AND_NEI_CAM_ADE_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0546_01_Tu__)
            partiDialogo.append(dialogo)
    elif tipo == "CaneCasa":
        partiDialogo = []
        nome = "Lino"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0547_01_Tu_EHI_LIN_COS_STA_CER_IN_QUE_CES_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0547_02_Tu_DEV_AVE_FIU_QUA_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0548_01_Tu_LIN_HAI_VIS_HAN_AND_DA_QUE_PAR_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0549_01_Tu_LINOOO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0549_02_Lino__)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0550_01_Lino__)
            partiDialogo.append(dialogo)
    elif tipo == "OggettoCanaleCasa":
        partiDialogo = []
        nome = "OggettoCanaleCasa"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0551_01_Tu__IL_CAN_CHE_ABB_COS_PER_POR_LAC_DEL_FIU_NEI_RUB_DI_CAS_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0552_01_Tu_QUA_DEN_SCO_LAC_DEL_FIU_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0552_02_Tu__STA_UNI_GEN_COS_QUE_TUN_ADE_POS_UTI_LAC_DIR_IN_CAS_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0553_01_Tu__IL_CON_PER_LAC_)
            partiDialogo.append(dialogo)
    elif tipo == "FratelloMaggiore":
        partiDialogo = []
        nome = "Hans"
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["hansUscitoCamerettaSognoCasaDavid"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0043_01_Tu__HANS_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["hansUscitoCamerettaSognoCastello"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0044_01_Tu__HANS_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["hansAndatoInCasa4SognoCastello"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0045_01_Tu_HAN_PER_SEI_QUI_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0045_02_Hans__LIN_SE_N_AND_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0045_03_Tu_OH_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0045_04_Hans_TOR_IN_CAS_VAD_A_CER_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0045_05_Tu_PER_DEV_TOR_IN_CAS_TOR_TU_IN_CAS_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0045_06_Hans_SME_NON_PUO_AND_NEL_FOR_DA_SOL_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0045_07_Tu_ANDIAMO_INSIEME_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0045_08_Hans__SAR_NON_FAR_LA_BAM_NON_SEI_CAP_DI_DIF_DA_QUE_BES_SAR_SOL_UN_PES_PER_ME_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0045_09_Tu_BEN_CI_VAD_DA_SOL_ALL_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0045_10_Hans_SAR_SME_PER_FAV_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0045_11_Tu_NO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0045_12_Hans__COM_VUO_POT_PIA_QUA_VOR_IO_NON_VER_A_SAL_STA_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoHansFuoriCasaSognoCastello"]:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0554_01_Hans_SAR_SME_IO_NON_VER_A_SAL_STA_)
            partiDialogo.append(dialogo)
    elif tipo == "Madre":
        partiDialogo = []
        nome = "Teresa"
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroAPrimaDelloScoppioDelMissileACasa"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0046_01_Teresa_JOH_JOE__PRO_A_TAV_)
            partiDialogo.append(dialogo)
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoMadre1PreScoppioMissileSecondaVolta"]:
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0047_01_Teresa_JOHN_JOEY_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0555_01_Teresa__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0555_02_Tu__)
            partiDialogo.append(dialogo)
    elif tipo == "Padre":
        partiDialogo = []
        nome = "Norm"
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDS._0556_01_Norm__)
        partiDialogo.append(dialogo)
        dialogo = []
        dialogo.append("tu")
        dialogo.append(LDS._0556_02_Tu__)
        partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo


