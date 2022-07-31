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
    if stanzaDiAppartenenza == GlobalGameVar.dictStanze["esternoCastello1"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoUscitaLabirinto"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0081_01_Tu_WOW_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0081_02_Tu__SIA_ARR_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["esplosioneDelVulcano"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0082_01_Tu_OHHH_MERDA_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostEsplosioneDelVulcano1"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0083_01_Tu___ESP_UNA_MON_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0083_02_Tu__VIC_AL_PAL_DI_ROD_)
                partiDialogo.append(dialogo)
        elif tipo == "ServoLancia":
            partiDialogo = []
            nome = LI.SOL_CON_LAN
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                if tipoId == "ServoLancia-0":
                    if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                        if avanzamentoDialogo == 0:
                            oggettoDato = False
                            avanzaStoria = False
                            menuMercante = False
                            scelta = False
                            avanzaColDialogo = True
                            dialogo = []
                            dialogo.append("tu")
                            dialogo.append(LDS._0804_01_Tu_EHI_SAL_DEV_PAR_CON_NEI_PUO_APR_IL_CAN_)
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("personaggio")
                            dialogo.append(LDS._0804_02_SoldatoConLancia__NO_LEN__DAL_PAR_)
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("tu")
                            dialogo.append(LDS._0804_03_Tu_OH_OK_)
                            partiDialogo.append(dialogo)
                        elif avanzamentoDialogo == 1:
                            oggettoDato = False
                            avanzaStoria = False
                            menuMercante = False
                            scelta = False
                            avanzaColDialogo = True
                            dialogo = []
                            dialogo.append("tu")
                            dialogo.append(LDS._0805_01_Tu_DOV_POR_QUE_STR_)
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("personaggio")
                            dialogo.append(LDS._0805_02_SoldatoConLancia__)
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("tu")
                            dialogo.append(LDS._0805_03_Tu_EHI_)
                            partiDialogo.append(dialogo)
                        else:
                            oggettoDato = False
                            avanzaStoria = False
                            menuMercante = False
                            scelta = False
                            avanzaColDialogo = False
                            dialogo = []
                            dialogo.append("tu")
                            dialogo.append(LDS._0806_01_Tu_EHI_)
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("personaggio")
                            dialogo.append(LDS._0806_02_SoldatoConLancia__)
                            partiDialogo.append(dialogo)
                    else:
                        oggettoDato = False
                        avanzaStoria = False
                        menuMercante = False
                        scelta = False
                        avanzaColDialogo = False
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(LDS._0807_01_Tu_EHI_)
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("personaggio")
                        dialogo.append(LDS._0807_02_SoldatoConLancia__)
                        partiDialogo.append(dialogo)
                elif tipoId == "ServoLancia-1":
                    if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
                        if avanzamentoDialogo == 0:
                            oggettoDato = False
                            avanzaStoria = False
                            menuMercante = False
                            scelta = False
                            avanzaColDialogo = True
                            dialogo = []
                            dialogo.append("personaggio")
                            dialogo.append(LDS._0808_01_SoldatoConLancia__)
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("tu")
                            dialogo.append(LDS._0808_02_Tu_SAL_STO_CER_UN_CER_NEI_ABI_QUI_)
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("personaggio")
                            dialogo.append(LDS._0808_03_SoldatoConLancia__NON_ASP_OSP_SEN_UN_INV_NON_TI__CON_ENT_)
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("tu")
                            dialogo.append(LDS._0808_04_Tu_OK_)
                            partiDialogo.append(dialogo)
                        else:
                            oggettoDato = False
                            avanzaStoria = False
                            menuMercante = False
                            scelta = False
                            avanzaColDialogo = False
                            dialogo = []
                            dialogo.append("personaggio")
                            dialogo.append(LDS._0809_01_SoldatoConLancia_SEN_UN_INV_NON_TI__CON_ENT_)
                            partiDialogo.append(dialogo)
                    else:
                        oggettoDato = False
                        avanzaStoria = False
                        menuMercante = False
                        scelta = False
                        avanzaColDialogo = False
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(LDS._0810_01_Tu_EHI_)
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("personaggio")
                        dialogo.append(LDS._0810_02_SoldatoConLancia__)
                        partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0811_01_SoldatoConLancia__)
                partiDialogo.append(dialogo)
        elif tipo == "Neil":
            partiDialogo = []
            nome = "Neil"
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0084_01_Tu__)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0084_02_Neil__)
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["esternoCastello2"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoEsternoCastello"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0085_01_Tu_C_UN_SIL_TOM_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0085_02_Impo__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0085_03_Tu__CIO_NON_CHE_ABB_QUA_CON_IL_SIL_SIA_CHI__SOL_UN_PO_INQ_TUT_QUI_)
                partiDialogo.append(dialogo)
        elif tipo == "ServoLancia":
            partiDialogo = []
            nome = LI.SOL_CON_LAN
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                if tipoId == "ServoLancia-2":
                    if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["apertoCancelloPrincipaleCastello"]:
                        if avanzamentoDialogo == 0:
                            oggettoDato = False
                            avanzaStoria = False
                            menuMercante = False
                            scelta = False
                            avanzaColDialogo = True
                            dialogo = []
                            dialogo.append("tu")
                            dialogo.append(LDS._0812_01_Tu_DOVREI_ENTRARE_)
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("personaggio")
                            dialogo.append(LDS._0812_02_SoldatoConLancia__HAI_UN_INV_)
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("tu")
                            dialogo.append(LDS._0812_03_Tu_CER_UHM_ECC_TIE_)
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("personaggio")
                            dialogo.append(LDS._0812_04_SoldatoConLancia__CE_DI_RES_NON__VAL_)
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("tu")
                            dialogo.append(LDS._0812_05_Tu_MA_ME_LHA_DAT_COS_)
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("personaggio")
                            dialogo.append(LDS._0812_06_SoldatoConLancia__)
                            partiDialogo.append(dialogo)
                        else:
                            oggettoDato = False
                            avanzaStoria = False
                            menuMercante = False
                            scelta = False
                            avanzaColDialogo = False
                            dialogo = []
                            dialogo.append("tu")
                            dialogo.append(LDS._0813_01_Tu_PER_IL_MIO_INV_NON__VAL_)
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("personaggio")
                            dialogo.append(LDS._0813_02_SoldatoConLancia__)
                            partiDialogo.append(dialogo)
                    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                        if avanzamentoDialogo == 1:
                            oggettoDato = False
                            avanzaStoria = False
                            menuMercante = False
                            scelta = False
                            avanzaColDialogo = True
                            dialogo = []
                            dialogo.append("personaggio")
                            dialogo.append(LDS._0814_01_SoldatoConLancia__)
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("tu")
                            dialogo.append(LDS._0814_02_Tu_EHI_SO_CHE_NON_ERA_UN_INV_QUE_DI_PRI_SCU_SE_TI_HO_MEN_)
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("personaggio")
                            dialogo.append(LDS._0814_03_SoldatoConLancia__)
                            partiDialogo.append(dialogo)
                        else:
                            oggettoDato = False
                            avanzaStoria = False
                            menuMercante = False
                            scelta = False
                            avanzaColDialogo = False
                            dialogo = []
                            dialogo.append("tu")
                            dialogo.append(LDS._0815_01_Tu_SALVE_)
                            partiDialogo.append(dialogo)
                            dialogo = []
                            dialogo.append("personaggio")
                            dialogo.append(LDS._0815_02_SoldatoConLancia__)
                            partiDialogo.append(dialogo)
                elif tipoId == "ServoLancia-3":
                    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoSecondaStanzaEsternoCastello"]:
                        oggettoDato = False
                        avanzaStoria = True
                        menuMercante = False
                        scelta = False
                        avanzaColDialogo = False
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(LDP._0086_01_Tu__QUE_LEN_DEL_CAS_)
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("personaggio")
                        dialogo.append(LDP._0086_02_SoldatoConLancia_CHI_SEI_E_PER_SEI_QUI_)
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(LDP._0086_03_Tu_MI_CHI_SAR_DEV_INC_NEI_)
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("personaggio")
                        dialogo.append(LDP._0086_04_SoldatoConLancia_MOSTRAMI_LINVITO_)
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("tu")
                        dialogo.append(LDP._0086_05_Tu_NON_HO_NES_INV_DEV_CON_QUE_IMP_A_NEI_PER_CON_DI_REN_IL_BIB_CIT_)
                        partiDialogo.append(dialogo)
                        dialogo = []
                        dialogo.append("personaggio")
                        dialogo.append(LDP._0086_06_SoldatoConLancia__DA_QUE_PAR_)
                        partiDialogo.append(dialogo)
                    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["apertoCancelloPrincipaleCastello"]:
                        oggettoDato = False
                        avanzaStoria = True
                        menuMercante = False
                        scelta = False
                        avanzaColDialogo = False
                        dialogo = []
                        dialogo.append("personaggio")
                        dialogo.append(LDP._0087_01_SoldatoConLancia_SEGUIMI_)
                        partiDialogo.append(dialogo)
                    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                        oggettoDato = False
                        avanzaStoria = False
                        menuMercante = False
                        scelta = False
                        avanzaColDialogo = False
                        dialogo = []
                        dialogo.append("personaggio")
                        dialogo.append(LDS._0816_01_SoldatoConLancia_IL_PAD_HA_ORD_DI_LAS_LIB_ACC_)
                        partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._0817_01_SoldatoConLancia__)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoCancelloCastello":
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._0818_01_Tu__CHIUSO_)
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["esternoCastello3"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoNeilFuoriDalCastelloDuranteLaFuga"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0088_01_Tu__)
                partiDialogo.append(dialogo)
        elif tipo == "Neil":
            partiDialogo = []
            nome = "Neil"
            oggettoDato = False
            avanzaStoria = True
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0089_01_Tu_NNO_TI_AVV_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("personaggio")
            dialogo.append(LDP._0089_02_Neil__PER_HAI_UCC_I_MIE_SOL_SAR_)
            partiDialogo.append(dialogo)
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDP._0089_03_Tu__)
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["esternoCastello5"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoNotatoAscensore"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0090_01_Tu_OK_ADE_DOB_TRO_ROD_CHE_SIA_SEM_AL_SUO_AV_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoScomparsaDiNeilPostTempoBloccato"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0091_01_Tu__C_UN_SIL_TOM_ANC_QUA_FUO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0091_02_Tu__CHI_COM_LA_CIT_ADE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0091_03_Tu__E_ROD_MAG_LUI_)
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
            dialogo.append(LDS._0819_01_SoldatoConLancia_NON_PUO_ENT_ARM_)
            partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo


