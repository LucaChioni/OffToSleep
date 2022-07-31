# -*- coding: utf-8 -*-

import Codice.Variabili.GlobalImgVar as GlobalImgVar
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
            dialogo.append(LDS._0855_01_Tu_BAU_APE_E_SVU_ALL_NON_DER_SOL_ME_)
            partiDialogo.append(dialogo)
        elif tipo == "OggettoDictCofanettoChiuso":
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0856_01_Tu_ROB_DI_NEI_NON_MIN_)
            partiDialogo.append(dialogo)
    elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and (tipo in GlobalImgVar.vettoreNomiNemici or tipo == "ServoSpada" or tipo == "ServoArco" or tipo == "ServoLancia" or tipo.startswith("OggettoQuadro")):
        if tipo in GlobalImgVar.vettoreNomiNemici:
            partiDialogo = []
            if tipo == "ServoLancia":
                nome = LI.SOL_CON_LAN
            elif tipo == "ServoArco":
                nome = LI.SOL_CON_ARC
            elif tipo == "ServoSpada":
                nome = LI.SOL_CON_SPA
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0857_01_SoldatoConSpada__)
            partiDialogo.append(dialogo)
        elif tipo == "ServoSpada":
            partiDialogo = []
            nome = LI.SOL_CON_SPA
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0858_01_SoldatoConSpada__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0858_02_Tu__IMMOBILE_)
            partiDialogo.append(dialogo)
        elif tipo == "ServoArco":
            partiDialogo = []
            nome = LI.SOL_CON_ARC
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0859_01_SoldatoConArco__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0859_02_Tu__IMMOBILE_)
            partiDialogo.append(dialogo)
        elif tipo == "ServoLancia":
            partiDialogo = []
            nome = LI.SOL_CON_LAN
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0860_01_SoldatoConLancia__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0860_02_Tu__IMMOBILE_)
            partiDialogo.append(dialogo)
        elif tipo.startswith("OggettoQuadro"):
            partiDialogo = []
            nome = LI.QUADRO
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0861_01_Tu_UN_QUADRO_)
            partiDialogo.append(dialogo)
    elif tipoId.startswith("OggettoQuadro") and GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
        partiDialogo = []
        nome = LI.QUADRO
        if tipoId == "OggettoQuadro-7":
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0862_01_Tu_OK_QUE__UN_BEL_QUA_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0863_01_Tu_UN_QUA_DI_NEI_NON_SO_QUA_SIA_IL_SUO_SIG_E_NON_HO_VOG_DI_PEN_)
            partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-1":
        partiDialogo = []
        nome = LI.QUADRO
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(LDS._0864_01_Tu_SEM_UNA_PAR_PIE_DI_CRE_)
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-2":
        partiDialogo = []
        nome = LI.QUADRO
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(LDS._0865_01_Tu_UNA_CIT_CHE_SI_AFF_SU_UN_MAR_IN_TEM_CRE_)
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-3":
        partiDialogo = []
        nome = LI.QUADRO
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(LDS._0866_01_Tu_UN_CAS_CON_UNA_TOR_IMP_NEL_MEZ_)
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-4":
        partiDialogo = []
        nome = LI.QUADRO
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(LDS._0867_01_Tu_UNA_DON_CON_UN_VES_ENO_ACC_SU_UN_LET_)
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-5":
        partiDialogo = []
        nome = LI.QUADRO
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(LDS._0868_01_Tu_UN_PAE_A_VAL_DI_UNA_MON_)
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-6":
        partiDialogo = []
        nome = LI.QUADRO
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(LDS._0869_01_Tu_UNA_SEM_FOR_DIR_)
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-7":
        partiDialogo = []
        nome = LI.QUADRO
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(LDS._0870_01_Tu_UN_UOM_NUD_SU_UNA_CON_QUI__COS_CHE_SON_FAT_SEM_SCO_)
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-8":
        partiDialogo = []
        nome = LI.QUADRO
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(LDS._0871_01_Tu_UN_ALB_DAL_TRO_BIA_IN_MEZ_A_UN_PAE_MAC_)
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-9":
        partiDialogo = []
        nome = LI.QUADRO
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(LDS._0872_01_Tu_UN_VAS_CON_DEI_FIO_)
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-10":
        partiDialogo = []
        nome = LI.QUADRO
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(LDS._0873_01_Tu_UN_POR_CON_DIV_BAR_)
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-11":
        partiDialogo = []
        nome = LI.QUADRO
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(LDS._0874_01_Tu_UNA_NAV_DA_GUE_VOG_DIR_NON_SO_PER_MA_DAL_SEM_AGG_)
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-12":
        partiDialogo = []
        nome = LI.QUADRO
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(LDS._0875_01_Tu_UN_UOM_FAT_DI_FRU_E_VER_OK_)
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-13":
        partiDialogo = []
        nome = LI.QUADRO
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(LDS._0876_01_Tu_UNA_BAM_CHE_RAC_DEI_FIO_)
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-14":
        partiDialogo = []
        nome = LI.QUADRO
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(LDS._0877_01_Tu_PESCHE_)
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-15":
        partiDialogo = []
        nome = LI.QUADRO
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(LDS._0878_01_Tu_IL_RIF_DI_UN_CAS_NEL_)
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-16":
        partiDialogo = []
        nome = LI.QUADRO
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(LDS._0879_01_Tu_UN_ALB_IN_UN_PRA_CRE_NON_SO_LUN_COS_A_FUO__LAL_IL_RES_E_SFO_)
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-17":
        partiDialogo = []
        nome = LI.QUADRO
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(LDS._0880_01_Tu_UNA_MON_INN_)
        partiDialogo.append(dialogo)
    elif tipoId == "OggettoQuadro-18":
        partiDialogo = []
        nome = LI.QUADRO
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(LDS._0881_01_Tu_UN_LAG_ALL_)
        partiDialogo.append(dialogo)
    elif tipoId.startswith("OggettoDictCadavereSoldatoCastello"):
        partiDialogo = []
        nome = LI.CADAVERE_SOLDATO
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["comparsoCadavereSoldatoInternoCastello20"]:
            oggettoDato = LI.CHI_UFF_DI_NEI
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0106_01_Tu_OH_CAZZO_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0106_02_Tu_OK_LLA_CHI_)
            partiDialogo.append(dialogo)
        else:
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._0882_01_CadavereSoldato__)
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello1"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["saraCamminatoNelCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0107_01_Tu_MA_GUA_DOV_TI_HO_POR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0107_02_Impo__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoApprofondimentoParadossiTempoBloccato"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0108_01_Tu__E_NEI_DOV_AND_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0108_02_Tu__REN__RIM_L_NEL_SUO_UFF_E_POI_PER_REN_ERA_L_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0108_03_Impo__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0108_04_Tu__E_PER_MI_HAN_LAS_LIB_POT_AND_E_NON_TOR_PI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0108_05_Tu__DAL_LOR_PUN_DI_VIS_IO_SAR_TIP_SPA_ALL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0108_06_Impo__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0108_07_Tu_MMMH_)
                partiDialogo.append(dialogo)
        elif tipoId == "ServoLancia-3":
            partiDialogo = []
            nome = LI.SOL_CON_LAN
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["servoLanciaEntratoNelCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0109_01_SoldatoConLancia_ASPETTA_QUI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0109_02_Tu__NEI_SA_GI_CHE_LO_STI_ASP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0109_03_SoldatoConLancia__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0109_04_Tu__OK_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0883_01_Tu_SCU_DOV_USC_UN_ATT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0883_02_SoldatoConLancia__)
                partiDialogo.append(dialogo)
        elif tipoId == "ServoLancia-4":
            partiDialogo = []
            nome = LI.SOL_CON_LAN
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0884_01_SoldatoConLancia__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0884_02_Tu_EHI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0884_03_SoldatoConLancia__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0885_01_Tu__IMM_E_GUA_FIS_DAV_A_S_)
                partiDialogo.append(dialogo)
        elif tipoId == "ServoArco-0":
            partiDialogo = []
            nome = LI.SOL_CON_ARC
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0886_01_SoldatoConArco__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0886_02_Tu_SALVE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0886_03_SoldatoConArco__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0887_01_Tu_MI_STA_IGN_COM_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello2"]:
        if tipoId == "ServoSpada-0":
            partiDialogo = []
            nome = LI.SOL_CON_SPA
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0888_01_SoldatoConSpada__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0888_02_Tu_NEI__DA_QUE_PAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0888_03_SoldatoConSpada__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0889_01_Tu_NON_HAN_TAN_VOG_DI_PAR_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["riletturaLibroNeilSulTempo"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0110_01_Tu__NEI_AVE_DET_CHE_AVR_VIS_TUT_BLO_MA_PER_TU_NON_LO_SEI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0110_02_Impo__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0110_03_Tu__E_PER_LAR_SI_SPO_QUA_CAM_NON_DOV_RIM_TUT_IMM_GLI_EVE_NON_SI_STA_SUC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0110_04_Tu_E_ANC_IL_MIO_COR_E_I_RAT_DOV_RIM_TUT_IMM_SE_IO_MI_MUO_STO_TIP_PRO_UNA_SUC_DI_EVE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0110_05_Tu__SE_DEG_EVE_SCO_VUO_DIR_CHE_ANC_IL_TEM_SCO_NO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0110_06_Impo__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0110_07_Tu_MMMH_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello3"]:
        if tipoId == "ServoArco-1":
            partiDialogo = []
            nome = LI.SOL_CON_ARC
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0890_01_SoldatoConArco__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0890_02_Tu_SALVE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0890_03_SoldatoConArco__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0890_04_Tu_TI_TI_PIA_QUE_QUA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0890_05_SoldatoConArco__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0891_01_Tu_STA_FIS_QUE_QUA_DEV_AVE_COL_PAR_)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoLibreriaCastello-0":
            partiDialogo = []
            nome = "OggettoLibreriaCastello"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0892_01_Tu_LIBRI_SULLAMBIENTE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0893_01_Tu_UN_SAC_DI_LIB_SUL_LA_NAT_E_GLI_ANI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0894_01_Tu_LIB_SUL_NON_ADE_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0895_01_Tu_LIB_DI_NEI_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello4"]:
        if tipoId == "ServoLancia-5":
            partiDialogo = []
            nome = LI.SOL_CON_LAN
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0896_01_SoldatoConLancia__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0896_02_Tu__DAL_TUA_LAN_STA_COL_UNO_STR_LIQ_VIO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0896_03_SoldatoConLancia__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0897_01_Tu__IMM_SEM_CHE_NON_STI_NEA_RES_)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoSpecchioCastello-0":
            partiDialogo = []
            nome = LI.SPECCHIO
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0898_01_Tu_OH_UNO_SPE__PRO_QUE_CHE_MI_SER_NON_CRE_CHE_QUA_NOT_LA_SUA_ASS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0898_02_Tu__NON_SI_STA_ASP_CON_DEN_IL_MUR_CON_LUN_TUT_LA_PAR_PER_MET_UNO_SPE_DEN_IL_MUR_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0899_01_Tu_EHI_UNO_SPE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0899_02_Specchio__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0899_03_Tu_CAV_MI_SON_LAV_IER_E_GUA_QUA_MI_SER_UN_ALT_BAG_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0900_01_Specchio__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0900_02_Tu__)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoLavandinoCastello-0":
            partiDialogo = []
            nome = "OggettoLavandinoCastello"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0901_01_Tu_AH_UTI_ANC_IL_MIO_VEC_MOD_DI_SCH_IDR_QUA_INE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0902_01_Tu_QUE_SIS_PER_POR_LAC_IN_CAS_SON_PI_COM_DI_QUE_CHE_PEN_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0903_01_Tu_UN_LAVANDINO_)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoGabinettoCastello-0":
            partiDialogo = []
            nome = "OggettoGabinettoCastello"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0904_01_Tu_NON_DEV_AND_IN_BAG_ADE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0905_01_Tu__DA_UN_PO_CHE_NON_VAD_IN_BAG_MA_ORA_NON_HO_TEM_PER_PEN_AI_MIE_PRO_DIG_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0906_01_Tu_UN_GABINETTO_)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoVascaCastello-0":
            partiDialogo = []
            nome = "OggettoVascaCastello"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0907_01_Tu_VAS_IDR_CON_ACQ_RIS_TRO_COM_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0908_01_Tu_UNA_VAS_ENO_CHI_SE_ANC_QUI_C_LAC_RIS_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0909_01_Tu_UNA_VASCA_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello5"]:
        if tipoId == "ServoArco-2":
            partiDialogo = []
            nome = LI.SOL_CON_ARC
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0910_01_SoldatoConArco__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0910_02_Tu_COM_FAT_A_RIM_IN_PIE_IMM_PER_COS_TAN_TEM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0910_03_SoldatoConArco__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0911_01_Tu_FOR_SON_SOL_SOR_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello6"]:
        if tipoId == "ServoSpada-1":
            partiDialogo = []
            nome = LI.SOL_CON_SPA
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0912_01_SoldatoConSpada__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0912_02_Tu__COS_STA_FAC_TU_QUI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0912_03_SoldatoConSpada__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0912_04_Tu_NON_C_NIE_A_CUI_FAR_LA_GUA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0912_05_SoldatoConSpada__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0913_01_Tu_CHI_A_COS_STA_PEN_TIP_SE_MI_MUO_NON_HO_FAT_BEN_IL_MIO_LAV_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello7"]:
        if tipoId == "ServoLancia-6":
            partiDialogo = []
            nome = LI.SOL_CON_LAN
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0914_01_SoldatoConLancia__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0914_02_Tu_SE_SEI_CIT_RIM_FER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0914_03_SoldatoConLancia__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0914_04_Tu_AH_AH_FRE_)
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0915_01_Tu_CI_SI_POT_DIV_UN_SAC_CON_QUE_GUA_)
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 2:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0916_01_Tu__VOI_AVE_GI_CEN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0916_02_SoldatoConLancia__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0916_03_Tu__POT_MAN_INS_SAI_PAR_UN_PO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0916_04_SoldatoConLancia__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0917_01_Tu_NON_INS_MAG_SON_SOL_MOL_STA_E_NON_HAN_VOG_DI_STA_A_SEN_)
                partiDialogo.append(dialogo)
        elif tipoId == "ServoArco-3":
            partiDialogo = []
            nome = LI.SOL_CON_ARC
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0918_01_SoldatoConArco__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0918_02_Tu_TU_FAI_LA_GUA_AL_TAV_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0918_03_SoldatoConArco__)
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 1:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0919_01_Tu_PER_QUE_TIZ_NON_FAN_NIE_)
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 2:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0920_01_Tu___PER_ME_LA_CEN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0920_02_SoldatoConArco__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0921_01_Tu_CHI_TAC_ACC_DIR_ORA_CHE_CI_PEN_POT_CHI_UN_SAC_DI_AFF_CON_QUE_GUA_)
                partiDialogo.append(dialogo)
        elif tipoId == "ServoLancia-13":
            partiDialogo = []
            nome = LI.SOL_CON_LAN
            oggettoDato = LI.CHIAVE_STANZA
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0111_01_Tu_OH_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0111_02_SoldatoConLancia__SAR_LA_TUA_CAM_DA_LET__AL_SEC_PIA_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0111_03_Tu_AH_OK_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0111_04_SoldatoConLancia__)
            partiDialogo.append(dialogo)
        elif tipoId == "OggettoCaminoCastello-0":
            partiDialogo = []
            nome = "OggettoCaminoCastello"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0922_01_Tu_QUE_CAM__COM_INU_CON_IL_PAV_RAD_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0923_01_Tu_UN_CAM_SEM_NON_ESS_MAI_STA_UTI_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0924_01_Tu_UN_CAMINO_)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoSediaCastello-0":
            partiDialogo = []
            nome = "OggettoSediaCastello"
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0112_01_Tu_SEM_NON_ESS_NES_ALT_DOV_SED_QUI_)
            partiDialogo.append(dialogo)
        elif tipoId == "OggettoCarrelloCiboCastello-0":
            partiDialogo = []
            nome = "OggettoSediaCastello"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0925_01_Tu_CI_SON_DEI_VAS_VUO_)
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello8"]:
        if tipoId == "ServoArco-4":
            partiDialogo = []
            nome = LI.SOL_CON_ARC
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0926_01_SoldatoConArco__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0926_02_Tu_SAL_TU_PER_CAS_SAI_PAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0926_03_SoldatoConArco__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0927_01_Tu_FOR_PAR_UNA_LIN_)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoVasoCastello-0":
            partiDialogo = []
            nome = "OggettoVasoCastello"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0928_01_Tu_QUE_VAS_EMA_STR_ODO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0929_01_Tu_E_UN_ALT_VAS_MA_CHE_HAN_DI_COS_BEL_DA_DOV_ESS_PRE_OVU_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0930_01_Tu_UN_VASO_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello9"]:
        if tipoId == "ServoLancia-7":
            partiDialogo = []
            nome = LI.SOL_CON_LAN
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0931_01_SoldatoConLancia__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0931_02_Tu_EHI_TI_HO_GI_VIS_AL_PIA_DI_SOT_ERI_TU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0931_03_SoldatoConLancia__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0932_01_Tu_QUE_TIZ_SON_TUT_UGU_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello10"]:
        if tipoId == "ServoLancia-8":
            partiDialogo = []
            nome = LI.SOL_CON_LAN
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0933_01_SoldatoConLancia__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0933_02_Tu_A_COS_BIS_FAR_LA_GUA_QUI_POT_ENT_DEI_PIC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0933_03_SoldatoConLancia__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0934_01_Tu_QUE_GUA_SON_OVU_MA_NEL_CAS_NON_C_NES_SI_SOR_TRA_LOR_)
                partiDialogo.append(dialogo)
        elif tipoId == "ServoArco-5":
            partiDialogo = []
            nome = LI.SOL_CON_ARC
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0935_01_SoldatoConArco__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0935_02_Tu_TU_SOR_QUE_POR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0935_03_SoldatoConArco__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0936_01_Tu_MAG_VEN_PAG_BEN_)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoLettoCastello-0":
            partiDialogo = []
            nome = "OggettoLettoCastello"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoAperturaCameraDaLettoCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0113_01_Tu_CE_LHO_FAT_UN_ALT_PAS_E_SAR_CRO_)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0937_01_Tu_DEV_UN_LET_PER_GLI_OSP_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0938_01_Tu__UN_LET_MOR_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0939_01_Tu_UN_LETTO_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0940_01_Tu_NON__IL_MIO_LET_)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoArmadioCastello-0":
            partiDialogo = []
            nome = "OggettoArmadioCastello"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = -1
                avanzaColDialogo = False
                if not GlobalGameVar.cambiataAlCastello[0]:
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0941_01_Tu_DOMANDA_)
                    dialogo.append(LDS._0941_02_Tu_CI_SON_DEI_VES_DOV_CAM_)
                    dialogo.append(LDS._0941_03_Tu_S_)
                    dialogo.append(LDS._0941_04_Tu_FORSE_)
                    dialogo.append(LDS._0941_05_Tu_NO_)
                    dialogo.append(LDS._0941_06_Tu_NON_SO_SE_MI_STA_BEN_QUE_VIO_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0941_07_Tu_RISPOSTA_)
                    dialogo.append(LDS._0941_08_Tu_ASP_MA_CHE_STO_FAC_)
                    dialogo.append(LDS._0941_09_Tu_MMH_)
                    dialogo.append(LDS._0941_10_Tu_NON_HA_NEA_IL_CAP_)
                    dialogo.append(LDS._0941_11_Tu_ALLORA_NO_)
                    partiDialogo.append(dialogo)
                else:
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0941_12_Tu_OH_CI_SON_I_VEC_VES_DI_SAR_DEV_AVE_ALL_QUI_PRO_DI_SAP_E_UN_PO_DI_SUD_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0941_13_Tu_DOMANDA_)
                    dialogo.append(LDS._0941_14_Tu_POTREI_PROVARLI_)
                    dialogo.append(LDS._0941_15_Tu_S_)
                    dialogo.append(LDS._0941_16_Tu_FORSE_)
                    dialogo.append(LDS._0941_17_Tu_NO_)
                    dialogo.append(LDS._0941_18_Tu_NON_SO_SE_MI_ENT_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0941_19_Tu_RISPOSTA_)
                    dialogo.append(LDS._0941_20_Tu_ASP_MA_CHE_STO_FAC_)
                    dialogo.append(LDS._0941_21_Tu_MMH_)
                    dialogo.append(LDS._0941_22_Tu_MEG_DI_NO_)
                    dialogo.append(LDS._0941_23_Tu_LASCIAMO_STARE_)
                    partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = -1
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0942_01_Tu_DOMANDA_)
                if not GlobalGameVar.cambiataAlCastello[0]:
                    dialogo.append(LDS._0942_02_Tu_CI_SON_DEI_VES_DOV_CAM_)
                else:
                    dialogo.append(LDS._0942_03_Tu_CI_SON_I_MIE_VEC_VES_DOV_CAM_)
                dialogo.append(LDS._0942_04_Tu_S_)
                dialogo.append(LDS._0942_05_Tu_FORSE_)
                dialogo.append(LDS._0942_06_Tu_NO_)
                dialogo.append(LDS._0942_07_Tu_DOV_PEN_A_OPZ_DIV_DA_S_E_NO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0942_08_Tu_RISPOSTA_)
                dialogo.append(LDS._0942_09_Tu_OK_)
                dialogo.append(LDS._0942_10_Tu_MMH_)
                dialogo.append(LDS._0942_11_Tu_QUE_VES_VAN_PI_CHE_BEN_)
                dialogo.append(LDS._0942_12_Tu_DIR_DI_NO_QUI_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                if not GlobalGameVar.cambiataAlCastello[0]:
                    dialogo.append(LDS._0943_01_Tu_CI_SON_DEI_VES_NON_MI_ENT_)
                else:
                    dialogo.append(LDS._0943_02_Tu_CI_SON_I_MIE_VEC_VES_NON_MI_ENT_PI_)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoComodinoCastello-0":
            partiDialogo = []
            nome = "OggettoComodinoCastello"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0944_01_Tu_I_CAS_SON_VUO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0945_01_Tu_SU_QUE_COM_C_SOL_UNA_LAN_I_CAS_SON_VUO_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0946_01_Tu_UN_COMODINO_)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoLavandinoCastello-1":
            partiDialogo = []
            nome = "OggettoLavandinoCastello"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0947_01_Tu_AH_UTI_ANC_IL_MIO_VEC_MOD_DI_SCH_IDR_QUA_INE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0948_01_Tu_ANC_DA_QUI_USC_ACQ_RIS_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0949_01_Tu_UN_LAVANDINO_)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoVascaCastello-1":
            partiDialogo = []
            nome = "OggettoVascaCastello"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0950_01_Tu_VAS_IDR_CON_ACQ_RIS_TRO_COM_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0951_01_Tu_NON_HO_TEM_PER_FAR_UN_BAG_ADE_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0952_01_Tu_UNA_VASCA_)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoGabinettoCastello-1":
            partiDialogo = []
            nome = "OggettoGabinettoCastello"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0953_01_Tu_NON_DEV_AND_IN_BAG_ADE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0954_01_Tu_NON_SEN_IL_BIS_DI_AND_IN_BAG_FOR_DOV_SED_E_ASP_UN_PO_MA_NON_HO_TEM_DA_PER_ADE_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0955_01_Tu_UN_GABINETTO_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello11"]:
        if tipoId == "ServoSpada-2":
            partiDialogo = []
            nome = LI.SOL_CON_SPA
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0956_01_SoldatoConSpada__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0956_02_Tu_NON_CRE_CHE_QUE_PAR_COS_UNA_MIN_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0957_01_Tu_NON_SO_SE_RIU_A_FAR_QUE_LAV_)
                partiDialogo.append(dialogo)
        elif tipoId == "ServoSpada-3":
            partiDialogo = []
            nome = LI.SOL_CON_SPA
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0958_01_SoldatoConSpada__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0958_02_Tu_EHI_NON_C_BIS_DI_SOR_LA_PAR_LO_STA_GI_FAC_QUE_SOL_LAG_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0958_03_SoldatoConSpada__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0959_01_Tu_DUE_SOL_A_GUA_DI_UNA_PAR_)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoFinestraCastello-0":
            partiDialogo = []
            nome = "OggettoFinestraCastello"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0960_01_Tu__MATTINA_)
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello12"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoServoLanciaEntrataNelCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0114_01_Tu__TU_E_QUE_TIZ_AVE_DIV_COS_IN_COM_)
                partiDialogo.append(dialogo)
        elif tipoId == "ServoArco-6":
            partiDialogo = []
            nome = LI.SOL_CON_ARC
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0961_01_Tu_SAI_COS_FAC_UNO_SPU_SU_UNA_SCA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0961_02_SoldatoConArco__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0961_03_Tu_SALIVA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0961_04_SoldatoConArco__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0961_05_Tu_MMH_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0962_01_Tu_SE_NON_REA_A_QUE_DEL_SAL_NON_SO_PI_CHE_FAR_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello13"]:
        if tipoId == "ServoArco-7":
            partiDialogo = []
            nome = LI.SOL_CON_ARC
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0963_01_SoldatoConArco__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0963_02_Tu_EHI_SOL_GUA_UN_PO_COS_STO_PER_FAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0963_03_SoldatoConArco__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0963_04_Tu__STO_PER_SPU_SUL_PAV_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0963_05_SoldatoConArco__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0963_06_Tu__LO_STO_PER_FAR_PRO_SU_QUE_TAP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0963_07_SoldatoConArco__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0963_08_Tu__STO_CAR_LA_SAL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0963_09_SoldatoConArco__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0963_10_Tu__PUH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0963_11_SoldatoConArco__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0964_01_Tu_FOR_SE_GLI_SPU_IN_FAC_NO_MEG_DI_NO_)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoBarcaCastello-0":
            partiDialogo = []
            nome = "OggettoBarcaCastello"
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0965_01_Tu_PER_HA_QUE_MOD_SPA_OVU_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0966_01_Tu_E_UN_ALT_MOD_DI_UNA_BAR_NEI_DEV_ESS_PRO_APP_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0967_01_Tu_UNA_BARCA_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello14"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoInternoCastello12"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0115_01_Tu_NON_SO_BEN_DOV_STI_AND_)
                partiDialogo.append(dialogo)
        elif tipoId == "ServoSpada-4":
            partiDialogo = []
            nome = LI.SOL_CON_SPA
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0968_01_SoldatoConSpada__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0968_02_Tu_PER_STO_ANC_PRO_A_PAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0968_03_SoldatoConSpada__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0969_01_Tu_POT_ESS_STA_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello15"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoInternoCastello14"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0116_01_Tu__QUA_PIA_CI_SON_ANC_)
                partiDialogo.append(dialogo)
        elif tipoId == "ServoLancia-9":
            partiDialogo = []
            nome = LI.SOL_CON_LAN
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0970_01_SoldatoConLancia__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0970_02_Tu_EHI_MA_SON_IO_IL_PRO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0970_03_SoldatoConLancia__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0970_04_Tu_HO_FAT_QUA_DI_MAL_VI_STO_ANT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0970_05_SoldatoConLancia__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0971_01_Tu_FOR_HO_MAN_DI_RIS_IN_QUA_MOD_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello16"]:
        if tipoId == "ServoSpada-5":
            partiDialogo = []
            nome = LI.SOL_CON_SPA
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0972_01_SoldatoConSpada__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0972_02_Tu_SEI_A_GUA_DI_UNA_POR_CHE_TUT_POS_ATT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0972_03_SoldatoConSpada__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0973_01_Tu_LE_POR_SON_APE_MA_CI_SON_COM_DEI_SOL_DI_GUA_)
                partiDialogo.append(dialogo)
        elif tipoId == "ServoSpada-6":
            partiDialogo = []
            nome = LI.SOL_CON_SPA
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0974_01_SoldatoConSpada__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0974_02_Tu_EHI_CIA_MI_CHI_SAR_POS_CON_SE_TI_VA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0974_03_SoldatoConSpada__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0975_01_Tu_FOR_SON_SOL_POC_INT_)
                partiDialogo.append(dialogo)
        elif tipoId == "ServoLancia-10":
            partiDialogo = []
            nome = LI.SOL_CON_LAN
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0976_01_Tu_EHI_SEI_TU_QUE_CHE_MI_HA_APE_IL_CAN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0976_02_SoldatoConLancia__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0976_03_Tu_MH_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0977_01_Tu_QUE_SOL_SON_TUT_UGU_)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoFinestraCastello-0":
            partiDialogo = []
            nome = "OggettoFinestraCastello"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0978_01_Tu__MATTINA_)
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello17"]:
        if tipoId == "ServoSpada-7":
            partiDialogo = []
            nome = LI.SOL_CON_SPA
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0979_01_SoldatoConSpada__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0979_02_Tu_EHI_LO_CHE_VUO_SAP_COS_VUO_PER_CEN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0979_03_SoldatoConSpada__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0979_04_Tu_NIENTE_SICURO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0979_05_SoldatoConSpada__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0979_06_Tu_OK_AVE_DEL_BIS_SUC_MA_SE_NON_HAI_FAM_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0980_01_Tu_FOR_NON_HAN_BIS_NEA_DI_MAN_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello18"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoInternoCastello15"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0117_01_Tu__LE_GUA_NON_CI_STA_BLO_POS_AND_DOV_VOG_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["giratoVersoImpoPerDarloAlCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0118_01_Tu_OK_IMP_STA_CON_LOR_FIN_A_DOM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0118_02_Impo__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0118_03_Tu__NON_TI_FAR_NIE_TRA_SON_SOL_UN_PO_INQ_MA_SON_INN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0118_04_Tu__OK_FOR_SON_IO_QUE_CHE_DEV_PRE_TU_SAI_DIF_PIU_BEN_ANC_DA_SOL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0118_05_Impo__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0118_06_Tu__MA_STA_BEN_NON_PRE_PER_ME_)
                partiDialogo.append(dialogo)
        elif tipoId == "ServoLancia-12":
            partiDialogo = []
            nome = LI.SOL_CON_LAN
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoInternoCastello18"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0119_01_SoldatoConLancia__SAR_VER_RIC_DOM_LAS_QUA_LIM_LA_CEN__SER_AL_PRI_PIA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0119_02_Tu__LA_CEN_PER_DOM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0119_03_SoldatoConLancia_POT_ALL_QUI_PER_LA_NOT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0119_04_Tu_MA_CHE_ORE_SON_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0119_05_SoldatoConLancia__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0119_06_Tu__POI_NON_VOG_LAS_IL_MIO_IMP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0119_07_SoldatoConLancia__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0119_08_Tu__E_NON_HO_FAM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0119_09_SoldatoConLancia_LA_CEN__SER_AL_PRI_PIA_NON_PUO_CIR_CON_LIM_NEL_CAS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0119_10_Tu_LHO_FAT_FIN_E_POI_PER_NON_POS_PAR_CON_NEI_ADE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0119_11_SoldatoConLancia__NEI__OCC_PUO_AND_E_TOR_DOM_SE_VUO_TEN_LIM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0119_12_Tu__NO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0119_13_SoldatoConLancia__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0119_14_Tu__UFFF_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0119_15_SoldatoConLancia__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0119_16_Tu__E_VA_BEN_STA_QUI_PER_LA_NOT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0119_17_SoldatoConLancia__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0981_01_SoldatoConLancia__)
                partiDialogo.append(dialogo)
        elif tipoId == "ServoArco-8":
            partiDialogo = []
            nome = LI.SOL_CON_ARC
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0982_01_SoldatoConArco__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0982_02_Tu_NEI_HA_DET_CHE_PUO_STA_PRI_OGG_SE_SEI_STA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0982_03_SoldatoConArco__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0983_01_Tu_SE_IMP_A_IMI_LA_VOC_DI_NEI_)
                partiDialogo.append(dialogo)
        elif tipo.startswith("OggettoLibreriaCastello"):
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                if tipoId == "OggettoLibreriaCastello-1":
                    partiDialogo = []
                    nome = LI.LIB_SUL_COS_VOL1_ETI
                    if avanzamentoDialogo == 0:
                        oggettoDato = False
                        avanzaStoria = True
                        menuMercante = False
                        scelta = False
                        avanzaColDialogo = True
                    else:
                        oggettoDato = False
                        avanzaStoria = False
                        menuMercante = False
                        scelta = False
                        avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0984_01_Tu_QUE_LIB_SIN_SU_COS_VOL__ETI_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0984_02_LibroSullaCoscienzaVol1Etica__LA_CUL_DI_CUI_LET__FON_SI_CRE_E_SI_EVO_NEG_ESS_VIV_QUA_QUE_CRE_E_FAN_ESP_TAN_PI_DUE_ANI_SON_IN_CON_TAN_PI_LA_LOR_ESP_E_QUI_ANC_LA_LOR_CUL__COM_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0984_03_LibroSullaCoscienzaVol1Etica__NEL_MOM_IN_CUI_LE_CIR_IMP_UNA_CON_TRA_ANI_CON_CUL_DIV__NEC_CHE_NAS_UNA_NUO_CUL_E_TAL_UNA_NUO_ETI_COM_FRU_DEL_DEL_PRE_SPE_PER_LIM_NEL_A_UNA_CUL_CON_UNE_MOL_DIF_PU_RIC_SFO_CHE_NON_VOG_ESS_ACC_SON_QUE_I_CAS_IN_CUI_POS_NAS_SCO_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0984_04_LibroSullaCoscienzaVol1Etica__NEL_PEN_DI_ALC_NEL_MOM_IN_CUI_ESI_UNA_SOL_CUL_CON_DA_TUT_SAR_FIN_CHI_QUA_SIA_LA_GIU_ETI__SCO_DI_QUE_FAN_ESP_LE_PRO_CRE_PRE_GLI_ALT_ANC_ATT_LUS_DEL_FOR_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0984_05_LibroSullaCoscienzaVol1Etica__OSS_UNO_SCO_TRA_DUE_FAZ_CON_RIS_IRR_E_INS_DOM_QUA_DEL_DUE_ABB_TOR_OGN__IL_MAL_DEL_POI_OGN__GIU_TRA_LE_REG_ETI_DEL_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0984_06_LibroSullaCoscienzaVol1Etica__NON_PU_ESI_CON_TRA_CUL_INC_QUI_NON_PU_ESI_UNE_OGG_GIU_E_NON_ESI_NEA_NEL_MOM_IN_CUI_NE_RIM_UNA_QUE_CHE_RIS_VIN_DOV_LA_SUA_SOP_ALL_DEI_SUO_SOS_NON_ALL_SUA_OGG_)
                    partiDialogo.append(dialogo)
                    if not GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(LDS._0984_07_Tu_MMH_)
                        partiDialogo.append(dialogo)
                elif tipoId == "OggettoLibreriaCastello-2":
                    partiDialogo = []
                    nome = LI.LIB_SUL_COS_VOL2_LIB_ARB
                    if avanzamentoDialogo == 0:
                        oggettoDato = False
                        avanzaStoria = True
                        menuMercante = False
                        scelta = False
                        avanzaColDialogo = True
                    else:
                        oggettoDato = False
                        avanzaStoria = False
                        menuMercante = False
                        scelta = False
                        avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0985_01_Tu_QUE_LIB_SIN_SU_COS_VOL__LIB_ARB_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0985_02_LibroSullaCoscienzaVol2LiberoArbitrio__PER_DIS_SUL_LIB_ARB__INN_NEC_DIS_DUE_POS_LA_PRI__QUE_IN_CUI_SI_RIT_CHE_TUT_CI_CHE_ESI__COS_DA_MAT_LA_SEC_INV__QUE_IN_CUI_SI_COS_POS_LES_DI_ELE_NON_MAT_TRA_CUI_RIE_LAN_COM_MOT_DI_OGN_ESS_VIV_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0985_03_LibroSullaCoscienzaVol2LiberoArbitrio__DEC_DI_PER_LA_PRI_IPO__CHI_CHE_NON_PU_ESS_LIB_ARB_ALL_STE_MOD_IN_CUI__POS_CAL_AZ_DI_OGG_INA_SAR_POS_CAL_LE_AZI_DEG_ESS_ANI_LUN_DIF_TRA_LE_DUE_CAT_RIM_LA_PRE_NEL_SEC_RAG_DEL_COS_A_CUI_LA_PAR_VI_RID_TUT_IL_SUO_SIG_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0985_04_LibroSullaCoscienzaVol2LiberoArbitrio__PER_LA_SEC_IPO_INV__VER_CHE_LAN_NON_SAR_GOV_DAL_STE_LEG_DEL_MAT_MA_DA_QUE_LEG_COM_DIP_IL_COM_DEG_IND_COS_COM_IL_LOR_PEN_VIE_PLA_DAL_CHE_GLI_STE_COM_SUL_MON_MAT_LAN_VER_IN_QUE_MOD_INF_E_CO_DAL_MAT_RIS_QUI_NON_PI_LIB_)
                    partiDialogo.append(dialogo)
                    if not GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(LDS._0985_05_Tu_MMH_IN_SOS_LE_COS_DI_CUI_MI_HA_PAR_REN_)
                        partiDialogo.append(dialogo)
                elif tipoId == "OggettoLibreriaCastello-3":
                    partiDialogo = []
                    nome = LI.LIB_SUL_COS_VOL3_TEM
                    if avanzamentoDialogo == 0:
                        oggettoDato = False
                        avanzaStoria = True
                        menuMercante = False
                        scelta = False
                        avanzaColDialogo = True
                    else:
                        oggettoDato = False
                        avanzaStoria = False
                        menuMercante = False
                        scelta = False
                        avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0986_01_Tu_QUE_LIB_SIN_SU_COS_VOL__TEM_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0986_02_LibroSullaCoscienzaVol3Tempo__SVI_LIP_PER_CUI_LA_REA_SI_EVO_IN_MOD_DET_VIE_SPO_CHI_IN_CHE_MOD_IL_TEM_SCO_IN_AVA_POT_CON_DUE_POS_IL_TEM__COM_DA_UN_SUS_DI_EVE_DET_E_SEP_TRA_LOR_OPP_DA_UN_FL_INF_DI_EVE_IND_E_INS_TRA_LOR_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0986_03_LibroSullaCoscienzaVol3Tempo__PRE_LA_PRI_IPO_IN_CUI_GLI_EVE_SON_DIS_E_SEP_DOV_IPO_CHE_TRA_UN_EVE_E_LAL_CI_SIA_UN_MO_IN_CUI_IL_TEM_NON_SCO_MA_IN_CUI_AVV_UN_QUA_COS_CHE_PER_ALL_SUC_DI_AVV_DOV_IPO_CHE_CI_SIA_UNA_SOR_DI_MO_IMM_CHE_SEN_ESS_MOS_O_CA_DA_ALT_EVE_RIE_A_FAR_SCO_SPO_LA_SEQ_TEM_IN_AVA_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0986_04_LibroSullaCoscienzaVol3Tempo__SEG_LA_SEC_IPO_IN_CUI_GLI_EVE_SON_INS_E_IND_NON_SI_PRE_UN_FEN_DI_CAU_TRA_GLI_EVE_GLI_EVE_SON_IN_QUE_CAS_UN_UNI_BLO_CHE_ESI_SE_LA_PER_TE_DEL_TEM_RIS_QUI_PRO_DEG_ESS_VIV_UNA_PER_SIM_ALL_LET_DI_UN_LIB_CHE_PUR_ESI_PER_INT_VIE_COM_PAR_IN_DIV_MOM_DEL_TEM_)
                    partiDialogo.append(dialogo)
                    if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(LDS._0986_05_Tu_QUE__ROB_DI_ANN_FA_MI_DOM_QUA_SIA_RIU_AD_APP_)
                        partiDialogo.append(dialogo)
                    else:
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(LDS._0986_06_Tu_MMH_MI_DOM_SE_SIA_RIU_AD_APP_QUE_IPO_)
                        partiDialogo.append(dialogo)
                elif tipoId == "OggettoLibreriaCastello-4":
                    partiDialogo = []
                    nome = LI.LIB_SUL_COS_VOL4_REA
                    if avanzamentoDialogo == 0:
                        oggettoDato = False
                        avanzaStoria = True
                        menuMercante = False
                        scelta = False
                        avanzaColDialogo = True
                    else:
                        oggettoDato = False
                        avanzaStoria = False
                        menuMercante = False
                        scelta = False
                        avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0987_01_Tu_QUE_LIB_SIN_SU_COS_VOL__REA_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0987_02_LibroSullaCoscienzaVol4Realt__COS_DIS_LA_REA_DAL_LA_REA_CHE_SEN_VIE_CAT_DA_DEI_SEN_CHE_ABB_SPA_NEL_COR_E_POI_INV_AL_CER_TRA_IMP_NER_IL_CER_POI_CHE_SI_TRO_AL_BUI_DEN_UN_CRA_INT_E_IMM_CI_CHE_STA_AL_DI_FUO_DI_LUI_IS_DA_QUE_IMP_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0987_03_LibroSullaCoscienzaVol4Realt__LA_COS_TUT_NON_HA_MOD_DI_VER_LA_VER_DI_QUE_SEG_DAT_CHE_QUE_SON_LUN_FON_DI_INF_CHE_HA_A_DIS_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0987_04_LibroSullaCoscienzaVol4Realt___LEC_PEN_CHE_TUT_CI_CHE_RIS_AL_DI_FUO_DEL_COS_POT_NON_ESS_REA_IN_QUE_SEN_LE_DIF_TRA_UNA_VIT_VIS_TRA_I_FIL_DEI_SEN_E_UNA_VIS_TRA_I_FIL_DEI_SOG_SAR_QUA_NUL_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0987_05_LibroSullaCoscienzaVol4Realt__IN_ENT_I_CAS_LA_REA_VIE_IMM_MA_SE_NEL_PRI_CAS_I_SEN_IMP_DEI_PEN_E_DEL_REA_NEL_SEC_LA_COS__LI_DI_CON_SU_CI_CHE_PI_GLI_INT_SEN_DIS_IN_QUE_SEN_ALC_SOS_CHE_LA_VER_LIB_LA_SI_PU_SPE_SOL_SOG_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0987_06_LibroSullaCoscienzaVol4Realt__MA_CI_CHE_AVV_QUA_SI__LI_DI_IMM_UNA_REA_AD_ESE_SOG_NON_DIF_MOL_DA_CI_CHE_PER_ATT_I_SEN_CI_DOV_IND_A_PEN_CHE_O_LIM__CRE_E_PLA_DAL_REA_EST_OPP_CHE_IN_QUA_MOD_NEL__GI_CON_LA_REA_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0987_07_LibroSullaCoscienzaVol4Realt__CON_DEL_PRI_CAS__LIN_DEL_PEN_SE_NON_COM_PRO_DEL_REA_IN_QUE_MOD_UN_IND_PRI_DI_SEN_E_CHE_NON_HA_MAI_FAT_ESP_DEL_REA_NON_POT_PRO_ALC_PEN_LIN_ESI_SEN_ESS_COS_E_FOR_SEN_ESS_VIV_LA_COS_DUN_NAS_E_SI_EVO_SOL_NEL_MOM_IN_CUI_ENT_IN_CON_CON_CI_CHE_STA_AL_DI_FUO_DI_LEI_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0987_08_LibroSullaCoscienzaVol4Realt__SEG_LA_SEC_IPO_IN_CUI_SI_SOS_CHE_LA_REA__CON_NEL_DED_CHE__LA_COS_A_PRO_LA_REA_CI_CHE_STA_FU_DI_NOI_SAR_UNA_SOR_DI_LIS_DI_RIC_CHE_COS_ATT_LIM_E_DAT_LEV_DET_DEL_REA_DOV_PEN_CHE_LE_LEG_FIS_CHE_LA_GOV_SIA_IN_VER_I_MEC_CON_CUI_LA_COS_SVI_I_SUI_PEN_)
                    partiDialogo.append(dialogo)
                    if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(LDS._0987_09_Tu_MI_DOM_COM_FAC_AD_AVE_COS_TAN_MON_SE_NON_FA_ALT_CHE_PEN_A_QUE_ROB_COM_FA_A_CON_IN_DEN_)
                        partiDialogo.append(dialogo)
                    else:
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(LDS._0987_10_Tu_MMH_MI_SEM_PI_SEN_LA_PRI_IPO_MA_LA_SEC__MOL_AFF_)
                        partiDialogo.append(dialogo)
                elif tipoId == "OggettoLibreriaCastello-5":
                    partiDialogo = []
                    nome = LI.LIB_SUL_EVO
                    if avanzamentoDialogo == 0:
                        oggettoDato = False
                        avanzaStoria = True
                        menuMercante = False
                        scelta = False
                        avanzaColDialogo = True
                    else:
                        oggettoDato = False
                        avanzaStoria = False
                        menuMercante = False
                        scelta = False
                        avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0988_01_Tu_QUE_LIB_SIN_SU_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0988_02_LibroSullEvoluzione__LA_FRE_DI_CAM_DEL_REA_DA_PAR_DI_UN_SOG_VAR_AL_VAR_DEL_SUA_ET_LIN_DEG_ORG_CHE_INF_LE_ABI_COG_FA_S_CHE_LA_PRE_DI_COS_DEG_EVE_E_DEI_PEN_SIA_SEM_MEN_FRE_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0988_03_LibroSullEvoluzione__SE_A_QUE_AGG_CHE_GLI_EVE_ACC_COM_RIC_NEL_CER_VEN_DIM_SEM_PI_RAP_RIS_CHI_CHE_INV_VAR_ANC_LA_PER_STE_DEL_TEM_IL_TEM_PAS_SEM_PI_VEL_RIS_AL_PAS_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0988_04_LibroSullEvoluzione__PER_EVI_QUE_LEN_DEG__POS_FAR_DEL_OPE_SUG_ORG_NON_SOL_PER_MAN_GIO_MA_ANC_PER_POT_USA_MAT_CHE_SOP_CAR_DI_LAV_PI_INT_E_CHE_NON_SI_DEG_NEL_TEM_SI_POS_OTT_ORG_CHE_PER_DI_INV_QUE_TEN_NA_DI_PER_DEL_TEM_PRE_DES_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0988_05_LibroSullEvoluzione__OCC_INN_SOS_DIV_COM_DI_ALC_ORG_SEN_COM_SOS_DEL_NER_OTT_E_DEL_RET__)
                    partiDialogo.append(dialogo)
                    if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(LDS._0988_06_Tu_AH_ECC_COM_FA_QUA_COM_SI_SAR_FAT_PRI_DI_ACC_QUE_INT_SU_DI_S_)
                        partiDialogo.append(dialogo)
                    else:
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(LDS._0988_07_Tu_OK_QUA_INI_UNA_LUN_LIS_DI_ORG_DI_CUI_NON_CAP_NIE_NE_OTT_BUL_OLF_MEM_TIM_DER_TER_NER_SO_DEL_MID_SPI_CI_SON_ANC_DIV_COS_SUL_COR_CEL_E_ALT_COS_SUL_CER_POI_CON_CON_ALI_RES_E_ILL_)
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(LDS._0988_08_Tu_QUI__POS_CHE_QUE_SOL_)
                        partiDialogo.append(dialogo)
                elif tipoId == "OggettoLibreriaCastello-6":
                    partiDialogo = []
                    nome = LI.LIB_SUL_CON
                    if avanzamentoDialogo == 0:
                        oggettoDato = False
                        avanzaStoria = True
                        menuMercante = False
                        scelta = False
                        avanzaColDialogo = True
                    else:
                        oggettoDato = False
                        avanzaStoria = False
                        menuMercante = False
                        scelta = False
                        avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0989_01_Tu_QUE_LIB_SIN_SU_CON_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0989_02_LibroSulConflitto__NON_SON_NOT_LE_RAG_DEL_CON_E_I_TEN_DI_RIA_VEN_SIS_RES_IMP_STA_IL_DIA_IL_NEM_DI_CUI_CI__NOT_BEN_POC_PAR_AVE_INS_E_COL_TUT_LE_REG_CIR_LA_NOS_CI__INF_IMP_LES_A_EST_NOR_E_SUD_LE_SPE_VER_OVE_INV_SON_SEM_RIS_PRO_PER_VIA_DEL_CAT_MON_E_LA_FAU_CHE_LE_POP_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0989_03_LibroSulConflitto__CI_CHE_SAP_SUL_NEM_SON_LE_LOR_FOR_UMA_E_ALC_DEL_LOR_TEC_BEL_NON_CI__NOT_LA_LOR_ANA_ESA_LE_LOR_FOR_DI_COM_LA_LOR_CUL_E_N_TAN_I_LOR_INT_SAP_SOL_CHE_VOG_COM_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0989_04_LibroSulConflitto__NON_SI_SA_QUA_SIA_INI_IL_CON_IL_PI_VEC_REP_CHE_CE_NE_TES_LES_RIS_A_QUA_MIG_DI_ANN_FA_NEG_ULT_CEN_UNI_PER_DI_CUI_HO_ESP_DIR_ABB_PER_DIV_TER_NON_GLI_ENO_SVI_TEC_CHE_SIA_RIU_A_COM_)
                    partiDialogo.append(dialogo)
                    if not (GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]):
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(LDS._0989_05_Tu_CEN_DI_ESP_DIR_)
                        partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0989_06_LibroSulConflitto__NEG_ULT_CIN_IN_PAR_GLI_ATT_SI_SON_INT_DOP_UNA_SER_DI_SUC_DEL_NOS_DIF_HAN_INI_AD_ATT_SU_TUT_I_FRO_ORI_CON_E_IN_MAN_MAS_NEL_MOM_IN_CUI_PEN_DI_AVE_UN_VAN_CI_HAN_SOR_CON_QUA_TUT_GLI_AVA_I_POC_SOP_PAR_DI_ARM_ESP_TEC_AVA_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._0989_07_LibroSulConflitto__ANC_NES_SEG_DEL_COS_MA_IL_SUO_INT_DOV_ESS_IMM_)
                    partiDialogo.append(dialogo)
                    if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(LDS._0989_08_Tu_LIN_DEL_CO_)
                        partiDialogo.append(dialogo)
                    else:
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(LDS._0989_09_Tu_QUI_C_UNA_GUE_CHE_STI_PER_CHI_HA_SCR_QUE_LIB_HA_CEN_E_STA_PER_INT_UN_CO_)
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(LDS._0989_10_Tu_OK_)
                        partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["riletturaLibroNeilSulTempo"]:
                if tipoId == "OggettoLibreriaCastello-1":
                    partiDialogo = []
                    nome = LI.LIB_SUL_COS_VOL1_ETI
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0990_01_Tu_QUE_LIB_SIN_SU_COS_VOL__ETI_NON_ERA_QUE_)
                    partiDialogo.append(dialogo)
                elif tipoId == "OggettoLibreriaCastello-2":
                    partiDialogo = []
                    nome = LI.LIB_SUL_COS_VOL2_LIB_ARB
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0991_01_Tu_QUE_LIB_SIN_SU_COS_VOL__LIB_ARB_NON_ERA_QUE_)
                    partiDialogo.append(dialogo)
                elif tipoId == "OggettoLibreriaCastello-3":
                    partiDialogo = []
                    nome = LI.LIB_SUL_COS_VOL3_TEM
                    oggettoDato = False
                    avanzaStoria = True
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0120_01_Tu_QUE_LIB_SIN_SU_COS_VOL__TEM__QUE_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDP._0120_02_LibroSullaCoscienzaVol3Tempo__SVI_LIP_PER_CUI_LA_REA_SI_EVO_IN_MOD_DET_VIE_SPO_CHI_IN_CHE_MOD_IL_TEM_SCO_IN_AVA_POT_CON_DUE_POS_IL_TEM__COM_DA_UN_SUS_DI_EVE_DET_E_SEP_TRA_LOR_OPP_DA_UN_FL_INF_DI_EVE_IND_E_INS_TRA_LOR_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDP._0120_03_LibroSullaCoscienzaVol3Tempo__PRE_LA_PRI_IPO_IN_CUI_GLI_EVE_SON_DIS_E_SEP_DOV_IPO_CHE_TRA_UN_EVE_E_LAL_CI_SIA_UN_MO_IN_CUI_IL_TEM_NON_SCO_MA_IN_CUI_AVV_UN_QUA_COS_CHE_PER_ALL_SUC_DI_AVV_DOV_IPO_CHE_CI_SIA_UNA_SOR_DI_MO_IMM_CHE_SEN_ESS_MOS_O_CA_DA_ALT_EVE_RIE_A_FAR_SCO_SPO_LA_SEQ_TEM_IN_AVA_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0120_04_Tu_ECC_TRA_UN_EVE_E_LAL_HAN_ES_PI_DI_QUE_DUE_MIN_PER_CON_QUE_APP_CON_A_VIV_MEN_IL_TEM_ERA_BLO_840_ANN_PER_OGN_EVE_CHE_PAS_PER_UN_TOT_DI_700_MIL_DI_ANN_IN_DUE_MIN_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0120_05_Tu_E_LES__DUR_FIN_FIN_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0120_06_Tu__OK_DEV_UN_ALT_MOD_NON_MI_LAS_NON_MI_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDP._0120_07_Tu__NON_MI_)
                    partiDialogo.append(dialogo)
                elif tipoId == "OggettoLibreriaCastello-4":
                    partiDialogo = []
                    nome = LI.LIB_SUL_COS_VOL4_REA
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0992_01_Tu_QUE_LIB_SIN_SU_COS_VOL__REA_NON_ERA_QUE_)
                    partiDialogo.append(dialogo)
                elif tipoId == "OggettoLibreriaCastello-5":
                    partiDialogo = []
                    nome = LI.LIB_SUL_EVO
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0993_01_Tu_QUE_LIB_SIN_SU_NON_ERA_QUE_)
                    partiDialogo.append(dialogo)
                elif tipoId == "OggettoLibreriaCastello-6":
                    partiDialogo = []
                    nome = LI.LIB_SUL_CON
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._0994_01_Tu_QUE_LIB_SIN_SU_CON_NON_ERA_QUE_)
                    partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0995_01_Tu_HO_GI_LET_QUE_LIB_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0996_01_Tu_LIB_DI_NEI_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello19"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["apertoPortaInternoCastello20AndandoInInternoCastello19"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0121_01_Tu_MERDA_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoAccantoABibliotecarioBloccato"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0122_01_Tu_C_PI_SIL_DI_PRI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0122_02_Impo__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0122_03_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0122_04_Tu__QUE_STA__ANC_APE_)
                partiDialogo.append(dialogo)
        elif tipoId == "ServoLancia-11":
            partiDialogo = []
            nome = LI.SOL_CON_LAN
            if avanzamentoDialogo == 0:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0997_01_Tu_SEI_TU_NEI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0997_02_SoldatoConLancia__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0998_01_Tu_QUE_NON__NEI_MA_ALM__QUA_)
                partiDialogo.append(dialogo)
        elif tipoId == "ServoSpada-8":
            partiDialogo = []
            nome = LI.SOL_CON_SPA
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["letto6LibriCastello"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0999_01_SoldatoConSpada_NEI_NON_PU_ANC_RIC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0999_02_Tu_QUA_DEV_ASP_ANC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0999_03_SoldatoConSpada__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._0999_04_Tu_UFF_POT_LEG_QUA_NEL_FRA_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1000_01_SoldatoConSpada_ENT_NEI_PU_RIC_ADE_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1001_01_SoldatoConSpada__)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoFinestraCastello-0":
            partiDialogo = []
            nome = "OggettoFinestraCastello"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                dialogo = []
                dialogo.append("tu")
                if GlobalGameVar.dictAvanzamentoStoria["dormitoNelCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["primoDialogoNeil"]:
                    dialogo.append(LDS._1002_01_Tu__MATTINA_)
                else:
                    dialogo.append(LDS._1002_02_Tu_SIA_PAR_IN_ALT_)
                partiDialogo.append(dialogo)
            else:
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1002_03_Tu__)
                partiDialogo.append(dialogo)
        elif tipoId == "Neil-0":
            partiDialogo = []
            nome = "Neil"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDS._1003_01_Neil__)
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello20"]:
        if tipoId == "Neil-0":
            partiDialogo = []
            nome = "Neil"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["bussatoPortaStudioDiNeil"]:
                nome = LI.SCONOSCIUTO
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0123_01_Tu_PERMESSO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0123_02_Sconosciuto__ENTRA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0123_03_Tu_SEI_TU_NEI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0123_04_Sconosciuto_S_ENTRA_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPrimaVistaDiNeil"]:
                oggettoDato = LI.LISTA_STRUMENTI
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0124_01_Tu_SALVE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0124_02_Sconosciuto__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0124_03_Tu__EHM_EHM_ALL_HAI_CAP_COS_DI_SPE_QUE_IMP_RIS_AGL_ALT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0124_04_Sconosciuto__AGL_ALT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0124_05_Tu_S_CIO_GLI_ALT_SON_MOR_NO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0124_06_Sconosciuto__MORTI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0124_07_Tu_S_MI_HAN_DET_CHE_LI_HAI_PRE_TU_DOP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0124_08_Sconosciuto_OH_E_CHI_TE_LHA_DET_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0124_09_Tu_UHM_UNA_PER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0124_10_Sconosciuto__CON_ROD_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0124_11_Tu__SS_MA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0124_12_Sconosciuto_VA_BEN_SAR_COS_RIC_REN_IN_CAM_DEL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0124_13_Tu_AH_NON_CIO_SER_DEL_INF_SU_UNA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0124_14_Sconosciuto__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0124_15_Tu__SER_SER_INF_SUL_GUE_IN_COR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0124_16_Sconosciuto_SERVONO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0124_17_Tu_S_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0124_18_Sconosciuto__E_COS_SE_IN_PAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0124_19_Tu_EHM_NON_SO_TUT_QUE_CHE_SI_SA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0124_20_Sconosciuto_NE_ABB_GI_DIS_E_GLI_HO_GI_MAN_IL_MAN_IN_CUI_DES_LA_SIT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0124_21_Tu_AH_HAI_SCR_TU_QUE_LIB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0124_22_Sconosciuto_COS_TI_SER_SAP_DA_ME_ESA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0124_23_Tu_COM_FAI_AD_AVE_CEN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0124_24_Sconosciuto___QUE_CHE_VUO_SAP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0124_25_Tu_S_CIO_VOR_SAP_TUT_TUT_QUE_CHE_SAI_TU_VOR_POT_STU_LE_TUE_RIC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0124_26_Sconosciuto_TUT_QUE_CHE_SO_IO_REN_VOR_CHE_TU_STU_LE_MIE_RIC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0124_27_Tu_MH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0124_28_Sconosciuto__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0124_29_Tu_S_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0124_30_Sconosciuto_TU_QUE_CHE_SO_VAL_MOL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0124_31_Tu__AAN_IMP_VAL_MOL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0124_32_Sconosciuto__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0124_33_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0124_34_Sconosciuto__POT_COL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0124_35_Tu_S_COLLABORARE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0124_36_Sconosciuto_QUA_SON_I_TUO_TIT_DI_STU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0124_37_Tu_AH_IO_NES_CRE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0124_38_Sconosciuto__SEI_UNA_STU_DI_REN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0124_39_Tu_NO_IO_IN_REA_REN_LHO_CON_IER_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0124_40_Sconosciuto__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0124_41_Tu_PER_HO_LET_ALC_DEI_TUO_LIB_PRI_MEN_ASP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0124_42_Sconosciuto__MMH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0124_43_Tu__POS_COM_REN_UTI_IN_QUA_MOD_MEN_MI_MET_IN_PAR_CON_GLI_STU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0124_44_Sconosciuto__CON_ROD_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0124_45_Tu_S_CON_ROD__E_FAC_ANC_PAR_DEL_SUA_CON_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0124_46_Sconosciuto__VA_BEN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0124_47_Tu_DAVVERO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0124_48_Sconosciuto_SAR_IL_NOS_AGG_CON_ROD_OGN_TAN_TI_CHI_DI_CON_PER_COM_CON_LUI_A_PAR_DA_OGG_PER_STU_QUE_IMP_SON_NEC_DEG_STR_SON_ABB_SIC_CHE_LUI_CE_LI_POT_FOR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0124_49_Tu__DEG_STR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0124_50_Sconosciuto_QUE__LA_LIS_PUO_USA_LA_SCO_SUL_MON_PER_EVI_IL_LAB_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ricevutoListaStrumentiDaNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0125_01_Sconosciuto_IL_PAS_SUL_MON_LO_RAG_PAS_DAL_CAN_ACC_ALL_DEL_LAB_LE_GUA_TI_LAS_PAS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0125_02_Tu_OK_PER_CRE_DI_AVE_BIS_DI_IMP_PER_IL_VIA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0125_03_Sconosciuto__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0125_04_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0125_05_Sconosciuto__DAC_MA_SAR_LUL_VOL_CHE_POT_AVE_QUA_TOR_ME_LO_RES_CON_GLI_STR_E_TU_AVR_I_MIE_STU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0125_06_Tu_MMH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0125_07_Sconosciuto_ABB_UN_ACC_AL_SEC_PIA_PUO_TRO_DEL_ARM_SE_NE_HAI_BIS_USA_IL_PIA_ASC_PER_TOR_ALL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0125_08_Tu_OK_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0125_09_Sconosciuto_PAR_ADE_COS_POT_TOR_IN_GIO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presiStrumentiPerStudiareImpo"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1004_01_Tu_NEI_HO_ALC_DOM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1004_02_Sconosciuto_ABB_UN_ACC_SAR_QUA_TOR_AVR_TUT_LE_TUE_RIS_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["avviatoBattitoCardiacoPreConsegnaStrumenti"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0126_01_Sconosciuto_SAR_HAI_GLI_STR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0126_02_Tu__SS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0126_03_Sconosciuto_OTT_LAS_SUL_TAV_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["riprodottoSuonoStrumentiSulTavoloDiNeil"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1005_01_Sconosciuto_MET_GLI_STR_SUL_TAV_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["riprodottoSuonoStrumentiSulTavoloDiNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0127_01_Sconosciuto_MMH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0127_02_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0127_03_Sconosciuto_MET_LIM_SUL_TAV_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0127_04_Tu__CHE_COS_VUO_FAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0127_05_Sconosciuto__MET_SUL_TAV_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0127_06_Tu__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tentatoDiAndarteneDaNeilConImpoPietra"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1006_01_Sconosciuto_MMH_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tentatoDiAndarteneDaNeilConImpoPietra"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0128_01_Sconosciuto_SARA_LIMPOPIETRA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0128_02_Tu__COSA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0128_03_Sconosciuto_DAM_LIM_DEL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0128_04_Tu__DIM_COS_VUO_FAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0128_05_Sconosciuto_DEV_STU_SAR_MI_SER_LIM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0128_06_Tu_LO_UCCIDERAI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0128_07_Sconosciuto__NO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0128_08_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0128_09_Sconosciuto__GLI_IMP_NON_SON_ESS_VIV_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0128_10_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0128_11_Sconosciuto__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sdraiataSulTavoloPostRianimazione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0129_01_Tu__NEI_COS_VUO_FAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0129_02_Sconosciuto__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoConBibliotecarioPostRianimazione2"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0130_01_Tu_COS_VOL_FAR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0130_02_Sconosciuto_NIE_SOL_UN_PIC_TES_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0130_03_Tu__PER_SON_COS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0130_04_Sconosciuto_PER_LAC_DEL_LAG_TI_HA_COR__PEN_NEL_E_TI_HA_LOG_LAP_DIG_UN_POL_QUA_TUT_I_MUS_I_BUL_OCU_I_CAN_OLF_E_UDI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0130_05_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0130_06_Sconosciuto_IL_CER_E_IL_SIS_NER_SON_RIM_PER_LO_PI_INT_E_LE_OSS_HAN_RET_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0130_07_Tu__PER_NON_RIE_MUO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0130_08_Sconosciuto_TOR_AUT_TRA_POC_NON_PRE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0130_09_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0130_10_Sconosciuto_DOB_FAR_DEG_ESP_ADE_HO_SVI_DEG_APP_CER_CAP_DI_INC_LE_CAP_PER_E_COG_TU_LI_DOV_TES_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0130_11_Tu__NO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0130_12_Sconosciuto_NON_DOV_FAR_NIE_DI_SPE_SE_QUA_TI_SVE_VED_TUT_BLO_VOR_DIR_CHE_TUT_HA_FUN_COR_A_QUE_PUN_TOR_A_MUO_LIB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0130_13_Tu__NO_IO_IO_VOG_TOR_COM_PRI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0130_14_Sconosciuto_BEN_POS_PRO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0130_15_Tu_ASPETTA_REN_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["apertoOcchiPostIniezioneNeil"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0131_01_Tu__SAR_STA_MEG_PRO_SU_UN_SOL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0131_02_Sconosciuto_NO__NEC_UN_AMB_PUL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0131_03_Tu_MMH_SPE_DI_AVE_PRE_TUT_CON_QUE_SIS_DI_EME_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0131_04_Sconosciuto_NON_FAR_DAN_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["apertoOcchiPostdialogoNeilRene1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0132_01_Tu__E_PER_QUA_RIM_BLO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0132_02_Sconosciuto__PER_QUA_SEC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0132_03_Tu_POTREBBE_IMPAZZIRE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0132_04_Sconosciuto__POS_PAS_ALL_FAS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0132_05_Tu_S_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroNelTempoAPrimaCheNeilLasciasseIlSuoUfficio"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0133_01_Sconosciuto___SUF_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogo1RenéNeilPostAvvioSequenzaNelCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0134_01_Tu__ASPETTA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0134_02_Sconosciuto__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0134_03_Tu_NON_SAR_MEG_ASP_IL_RIS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0134_04_Sconosciuto__FAI_COM_VUO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0134_05_Tu__)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0135_01_Tu_IMP_VA_TUT_BEN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0135_02_Impo__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0135_03_Tu__SEM_A_POS_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoDalloStudioDiNeilConImpo"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0136_01_Tu_MER_AND_DA_QUI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["alzataDaTavoloPostBloccoTempo"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0137_01_Tu_IMPO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostTempoBloccato"]:
                oggettoDato = LI.IMPOPIETRA
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0138_01_Tu__DOVE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0138_02_Tu_OH_ECCOLA_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ricaricatoImpoPostRianimazione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0139_01_Tu_OH_GRA_A_DIO_TU_SEI_ANC_A_POS_DOR_IN_POI_NON_TI_ABB_PI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0139_02_Impo__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0139_03_Tu_AND_DA_QUI_)
                partiDialogo.append(dialogo)
        elif tipo == "Bibliotecario":
            partiDialogo = []
            nome = u"René"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["uscitoDaInternoCastello19PostRianimazione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0140_01_Tu__REN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0140_02_Ren__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoConNeilPostRianimazione1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0141_01_Tu__REN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0141_02_Ren__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0141_03_Tu_REN_AIUTAMI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0141_04_Ren__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0141_05_Tu__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoConImpoPostTempoBloccato"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0142_01_Tu_REN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0142_02_Ren__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoVistoBibliotecarioBloccato"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0143_01_Tu_REN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0143_02_Ren__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0143_03_Tu__REN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0143_04_Ren__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0143_05_Tu__IMMOBILE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["risvegliatoNelVulcano"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1007_01_Tu__IMM_STA_SCR_QUA_MA_LA_PEN__BLO_SUL_FOG_E_LUI_CON_A_FIS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1007_02_Tu_NON_SI_CAP_MOL_MA_SEM_STU_SU_IMP_)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["avviatoSequenzaDiEventiCalcolatore"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1008_01_Tu__REN_STA_SCR_QUA_MA__BLO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostAvvioSequenzaDiEventiCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0144_01_Ren__UFF_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo1RenéPostAvvioSequenzaDiEventiCalcolatore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0145_01_Ren__MERDA_)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroNelTempoAPrimaCheNeilLasciasseIlSuoUfficio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["NeilEntratoNellaCellaDelSuoLaboratorio"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1009_01_Ren__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1010_01_Ren__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1010_02_Tu__BLOCCATO_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1011_01_Ren__)
                partiDialogo.append(dialogo)
        elif tipoId == "ServoSpada-9":
            partiDialogo = []
            nome = LI.SOL_CON_SPA
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1012_01_Tu_EHI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1012_02_SoldatoConSpada__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["chiusoPortaInternoCastello20DaSoldato"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0146_01_Tu_UH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0146_02_SoldatoConSpada_SAR_LAS_LIM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0146_03_Tu__SST_LON_)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoTavoloVuotoCastelloA-0":
            partiDialogo = []
            nome = "OggettoTavoloVuotoCastello"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presiStrumentiPerStudiareImpo"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ripresoImpoDaNeil"]:
                    dialogo.append(LDS._1013_01_Tu__SEN_ENE_PER_NON_LO_STA_NUT_)
                else:
                    dialogo.append(LDS._1013_02_Tu_NON_C_NIE_SU_QUE_TAV_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoNeilPreConsegnaStrumenti"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0147_01_Tu_OK_LI_MET_QUI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1014_01_Tu_SON_GLI_STR_DI_ROD_)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1015_01_Tu_I_MIE_STR_)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["avviatoSequenzaDiEventiCalcolatore"]:
                nome = "Sara"
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0148_01_Sara__)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroNelTempoAPrimaCheNeilLasciasseIlSuoUfficio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["NeilEntratoNellaCellaDelSuoLaboratorio"]:
                nome = "Sara"
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1016_01_Sara__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1017_01_Tu_NON_C_NIE_)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoTavoloVuotoCastelloB-0":
            partiDialogo = []
            nome = "OggettoTavoloVuotoCastello"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoNeilPostConsegnaStrumenti"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ripresoImpoDaNeil"]:
                    dialogo.append(LDS._1018_01_Tu_NON_C_NIE_SU_QUE_PAR_DEL_TAV_)
                else:
                    dialogo.append(LDS._1018_02_Tu_NON_C_NIE_SU_QUE_TAV_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoNeilPostConsegnaStrumenti"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0149_01_Tu_OK_IMP_NON_SUC_NIE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1019_01_Tu_NON_PRE_NON_SUC_NIE_)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1020_01_Tu_NON_C_NIE_SU_QUE_PAR_DEL_TAV_)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["avviatoSequenzaDiEventiCalcolatore"]:
                nome = "Sara"
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0150_01_Sara__)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroNelTempoAPrimaCheNeilLasciasseIlSuoUfficio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["NeilEntratoNellaCellaDelSuoLaboratorio"]:
                nome = "Sara"
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1021_01_Sara__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1022_01_Tu_NON_C_NIE_)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoTavoloAttrezziCastello-0":
            partiDialogo = []
            nome = "OggettoTavoloAttrezziCastello"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1023_01_Tu__UN_TAV_DA_LAV_)
            partiDialogo.append(dialogo)
        elif tipoId == "OggettoAppuntiNeilCastello-0":
            partiDialogo = []
            nome = LI.APP_DI_NEI
            if GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1024_01_Tu_SON_DEG_SCA_DI_NEI_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1025_01_Tu_CI_SON_UN_SAC_DI_APP_E_GRA_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["risvegliatoNelVulcano"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1026_01_Tu_PRO_DI_NEI_SU_DEI_MAC__PIE_DI_FOR_COM_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1027_01_Tu_PRO_DI_NEI_SU_DEI_MAC_)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoPortaCastelloChiusa-0":
            partiDialogo = []
            nome = "OggettoPortaCastelloChiusa"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["presaChiaveSoldatoInternoCastello20"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0151_01_Tu__)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1028_01_Tu__CHI_QUE_SOL_DEV_AVE_LA_CHI_)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoImpoScarico-0":
            partiDialogo = []
            nome = "Impo"
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1029_01_Tu_IMPO_)
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["internoCastello21"]:
        if tipoId == "Neil-0":
            partiDialogo = []
            nome = "Neil"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoRodNotatoPianoAscensoreAperto"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0152_01_Tu__NEIL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0152_02_Neil__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRodNeil1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0153_01_Neil_CHE_VUOI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0153_02_Tu__CHE_STA_SUC_QUI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0153_03_Neil_NON_HO_TEM_ADE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0153_04_Tu_DOV_SARA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0153_05_Neil__DENTRO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0153_06_Tu__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRodNeil2"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0154_01_Neil_HA_UCC_MET_DAI_MIE_UOM_POI_SI__GET_NEL_LAG_MEN_CER_DI_SCA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0154_02_Tu__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["rientratoInInternoCastello21ConRod"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0155_01_Tu_RIVOGLIO_LIMPO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0155_02_Neil__VAT_ROD_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0155_03_Tu_LEI_ERA_NEL_CON_QUI__LA_CON_CHE_DEV_ERE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0155_04_Neil_QUI__LA_CON_CHE_HA_UCC_I_MIE_SOL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0155_05_Tu__QUE_CHE_FAT_TRA_DI_VOI_SON_AFF_VOS_IO_NON_CEN_CON_QUE_STO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0155_06_Neil_AHHH_CAPISCO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0155_07_Tu_NON_VOR_FAR_CRE_CHE__IMP_TUT_UN_TRA_E_HA_INI_A_UCC_CHI_SEN_MOT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0155_08_Neil__HA_INF_UN_ACC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0155_09_Tu_E_A_ME_NON_ME_NE_FRE_NIE_DEI_VOS_ACC_LIM__PRO_DEL_CON_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0155_10_Neil__SU_QUE_POT_ESP_LEI_STE_QUA_SI_SVE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0155_11_Tu_COSA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0155_12_Neil_NON__NEC_RIS_ALT_DIS_AMB_SOL_UN_IDI_TI_AFF_LUL_ESE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0155_13_Tu_PEC_CHE_NON_SIA_TU_A_DOV_DEC_ALL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0155_14_Neil__NEA_TU_DOV_LIM_RIM_DOV__STA_LAS_FIN_IL_SUO_PRO_NON_SI_SVE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0155_15_Tu_LEI__MOR_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRodNeil4"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0156_01_Neil_POV_ROD_NON_SAI_NEM_TU_SE_DIS_DI_PI_PER_LE_TUE_PRO_ECO_O_QUE_SEN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0156_02_Tu_UMP_NON_PAR_DI_PRO_TU_TI_SEI_RIN_IN_QUE_CAS_PER_DEC_PAS_MET_DEL_TEM_A_PEN_DI_COM_TI_SEI_MUT_E_LAL_MET_A_STU_DEI_MOD_PER_RIM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0156_03_Neil_BEN_SE_HAI_FIN_CON_LE_TUE_STU_PUO_ANC_AND_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRodNeil5"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0157_01_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0157_02_Tu__MI_SER_NEI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0157_03_Neil__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0157_04_Tu_NEL_VUL_C_QUA_QUA_CHE_LI_FAB_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0157_05_Neil_NON_SER_CHE_TU_TI_MET_A_INV_QUE_FAB_AGI_IN_AUT__GI_INT_IN_PAS_E_INT_NUO_A_BRE_ANC_SEN_LE_MED_DI_UN_IST_RAG_IMP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0157_06_Tu_CHE_CHE_NE_SAI_TU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0157_07_Neil_VATTENE_ROD_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0157_08_Tu__E_SAI_PER_CER_CHE_VOR_AIU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0157_09_Neil_LUI_NON_VUO_AI_VUO_SOL_MAN_IL_CON_APE_E_IN_EQU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0157_10_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0157_11_Neil_MA_QUE_SON_FAC_CHE_NON_TI_RIG_TOR_AL_TUO_PAL_ROD_E_CON_LA_TUA_TRA_E_SPE_VIT_DI_SEM_AVR_IL_TUO_COM_PER_LIM_E_I_NOS_SCA_PER_GLI_IMP_CON_COM_PRI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0157_12_Tu__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRodNeil6"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0158_01_Tu__E_SAR_DIV_COM_VOI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0158_02_Neil_DEV_ESS_SOS_GRA_PAR_DEI_SUO_ORG_MA_SE_PU_ESS_DI_CON_LE_SAR_RIS_CON_PRI_HO_DEG_ACC_DA_RIS_DOP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0158_03_Tu__)
                partiDialogo.append(dialogo)
        elif tipoId == "ServoLancia-14":
            partiDialogo = []
            nome = LI.SOL_CON_LAN
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoSpecchioPostRianimazione4"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0159_01_SoldatoConLancia_SEGUIMI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0159_02_Tu__COS_MI_AVE_FAT_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["allontanatoSoldatoPostRianimazione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0160_01_Tu__PERCH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0160_02_Tu__COS_MI_AVE_FAT_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoConSoldatoPostRianimazione2"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0161_01_Tu__DOV_MI_STA_POR_)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoSpecchio-0":
            partiDialogo = []
            nome = LI.SPECCHIO
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostRimozioneBendeCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0256_01_Specchio__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0256_02_Tu__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoSpecchioPostRianimazione1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0257_01_Specchio__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0257_02_Tu_OH_CAZZO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["girataDavantiAlloSpecchioPostRianimazione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0258_01_Specchio__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0258_02_Tu__OH_CAZ_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0258_03_Specchio__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0258_04_Tu__SONO_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoTentataLuciditaPostRianimazione"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0260_01_Specchio__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0260_02_Tu__OH_MIO_DIO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0260_03_Specchio__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0260_04_Tu__SON_DIV_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["risvegliatoNelVulcano"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1030_01_Specchio__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1030_02_Tu__PER_SON_TIP_IMM_COM_NEI_ADE_CER_CON_UN_PO_DI_DIF_FIS_E_UN_AP_CER_INS_DA_QUA_PAR_MA_PER_NON_SON_MOR_NON_ANC_ALM_CRE_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1031_01_Specchio__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1031_02_Tu__)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoValvolaMacchinario-0":
            partiDialogo = []
            nome = LI.VALVOLA
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1032_01_Tu_NON_HO_IDE_DI_COS_SIA_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1033_01_Tu__UNA_VAL_DEL_MAC_)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoCapsulaMacchinario-0":
            partiDialogo = []
            nome = LI.CAPSULA
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1034_01_Tu_SEM_UNA_POR_MA_NON_SI_APR_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1035_01_Tu__LA_CAP_PER_LE_OPE_CHI_DI_NEI_INC_COS_SIA_RIU_A_FAR_)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoArmadioRatti-0":
            partiDialogo = []
            nome = LI.RATTO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["lettoAppuntiNeilSuRatti"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1036_01_Tu_CI_SON_DEG_STR_RAT_QUA_ALC_SI_MUO_MA_SON_QUA_TUT_MOR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1036_02_Tu_ASP_NON_SON_MOR_ALC_STA_IN_PIE_MA_SON_IMM_NON_RES_NEA_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1037_01_Tu_SON_CAV_CRE_CHE_SU_ALC_DI_QUE_STI_TES_LA_CER_CHE_HO_ANC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1037_02_Tu_ALC_CAM_LEN_IN_TON_ALT_STA_SDR_E_RES_A_MAL_MA_SEM_TUT_MOL_STA_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1038_01_Tu_SONO_CAVIE_)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoAppuntiRatti-0":
            partiDialogo = []
            nome = LI.APP_DI_NEI
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["creatoOggettoAppuntiRattiNeilInternoCastello21"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0162_01_Tu_SON_APP_DI_NEI_SU_DEG_ESP_SU_QUE_RAT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0162_02_AppuntiDiNeil__TES_APP_CER_AC7_SUL_NOV_GEN_IN_COR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0162_03_Tu__TIP_QUE_CHE_HA_MES_A_ME_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0162_04_AppuntiDiNeil__CAV_STA_ALL_FAS_ADU_IN_DUE_ORE_E_TRA_MIN_UTI_I_PRO_STA_INS_DEL_EFF_IN_TRE_MIN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0162_05_AppuntiDiNeil__LE_CAV_NON_MOS_SEG_DI_INV_FIS_LAT_CER_NON_MOS_LOG_NEC_INS_DI_UN_COM_MNE_PI_SVI_PER_COM_LA_FRE_DI_SUC_TEM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0162_06_Tu_CHE_CAVOLO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0162_07_AppuntiDiNeil__INS_DEL_COM_MNE_M24_CON_CON_SUC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0162_08_AppuntiDiNeil__LIM_MOS_UNA_SUC_DI_EVE_OGN_846_ANN_3_MES_19_GIO_15_ORE_21_MIN_E_4_SEC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0162_09_Tu_CHE_SIGNIFICA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0162_10_AppuntiDiNeil__41_CAV_DEC_AL_MIN_2_E_18_SEC_76_CAV_DEC_AL_MIN_2_E_19_SEC_ULT_27_CAV_DEC_AL_MIN_2_E_20_SEC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0162_11_Tu_OH_MER_DUE_MIN_DUE_MIN_SON_GI_PAS_PER_ME_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0162_12_AppuntiDiNeil__DUR_TOT_ESP_2_MIN_E_20_SEC_TEM_ESP_DAI_SOG_700_MIL_DI_ANN_CAU_INT_LOG_PSI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0162_13_AppuntiDiNeil__TES_APP_CER_AC7_SUL_NOV_GEN_IN_COR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0162_14_Tu_QUA_SI_INT_MA_TEM_ESP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0162_15_Tu_DDE_RIL_UN_ATT_QUE_LIB_DI_NEI_SUL_TEM_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1039_01_Tu_SON_DEI_TES_CHE_NEI_STA_FAC_SU_QUE_CAV_CON_LA_CER_CHE_HA_MES_ANC_A_ME_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1040_01_Tu_SON_DEI_TES_SU_QUE_CAV_)
                partiDialogo.append(dialogo)
        elif tipoId == "OggettoAppuntiRianimazioneSara-0":
            partiDialogo = []
            nome = LI.APP_DI_NEI
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoNotatoQtaSoldatiCastelloPostTempoBloccato"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0163_01_Tu_SON_APP_DI_NEI_SUL_MIO_PRO_DI_GUA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0163_02_AppuntiDiNeil__SON_PAS_DIC_ORE_E_IL_SOG_SI_STA_COM_MEG_DEL_PRE_DI_QUE_PAS_IL_PRO_DI_RIA_SAR_COM_IN_CIR_DUE_SET_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0163_03_AppuntiDiNeil__IL_PRO_DI_RIA_SI__CON_LEG_IN_ANT_IL_SOG_HA_RIP_A_RES_IL_BAT_CAR__REG_E_LAT_CER__PER_NEL_NOR_LIN_DEL_PRO_POT_INI_TRA_TRE_GIO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0163_04_AppuntiDiNeil__LA_FAS_DI_RIP__TER_NEI_TEM_PRE_PRO_DIN_DEL_PRO_AVV_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0163_05_AppuntiDiNeil__IL_SOG_HA_INA_RIP_COS_PER_POC_SEC_DUR_LA_FAS_CON_DEL_RIS_DI_COL_DEL_SIS_ELE_I_TRA_EST_DI_ROD_VER_SOS_FIN_ALL_CON_DEI_TES_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0163_06_AppuntiDiNeil__LIN_SI__CON_CON_SUC_NES_ELE_DEL__STA_DAN_TEM_DIN_QUI_ORE_I_TES_SUL_PRO_INI_NON_APP_IL_SOG_TOR_OPE_TEM_STI_DUE_GIO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0163_07_Tu_QUI_ERO_MOR_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0163_08_Tu_E_ADE_HO_UN_PR_INS_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1041_01_Tu_SON_APP_DI_NEI_SUL_MIO_PRO_DI_GUA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1041_02_Tu_C_SCR_CHE_SON_STA_RIA_E_CHE_MI__STA_INT_UN_PR_CRE_SI_TRA_DEL_AP_CER_DI_CUI_PAR_NEI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1041_03_Tu__IN_TOT_SON_PAS_20_GIO_DA_QUA_MI_SON_BUT_NEL_LAG_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1042_01_Tu_SON_APP_DI_NEI_SUL_MIO_PRO_DI_GUA_)
                partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo


