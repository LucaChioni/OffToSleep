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
    if tipo in GlobalImgVar.vettoreNomiNemici:
        partiDialogo = []
        if tipo == "GufoMarrone":
            nome = LI.GUFO_MARRONE
        elif tipo == "GufoBianco":
            nome = LI.GUFO_BIANCO
        elif tipo == "Struzzo":
            nome = LI.STRUZZO
        elif tipo == "Casuario":
            nome = LI.CASUARIO
        elif tipo == "Falco":
            nome = LI.FALCO
        elif tipo == "Aquila":
            nome = LI.AQUILA
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = False
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDS._1265_01_Aquila__)
        partiDialogo.append(dialogo)
    elif tipo.startswith("OggettoDict"):
        partiDialogo = []
        if tipo.startswith("OggettoDictCadavereGufoMarrone"):
            nome = LI.GUFO_MARRONE
        elif tipo.startswith("OggettoDictCadavereGufoBianco"):
            nome = LI.GUFO_BIANCO
        elif tipo.startswith("OggettoDictCadavereStruzzo"):
            nome = LI.STRUZZO
        elif tipo.startswith("OggettoDictCadavereCasuario"):
            nome = LI.CASUARIO
        elif tipo.startswith("OggettoDictCadavereFalco"):
            nome = LI.FALCO
        elif tipo.startswith("OggettoDictCadavereAquila"):
            nome = LI.AQUILA
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        avanzaColDialogo = True
        dialogo = []
        dialogo.append("personaggio")
        dialogo.append(LDS._1266_01_Aquila__)
        partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["passoMontano1"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoInCitta5CercandoRod"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0359_01_Tu__POR_MIS_CHE_FRE_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoSilenzioCittàPostTempoBloccato"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0360_01_Tu_MA_SON_BLO_A_MEZ_)
                partiDialogo.append(dialogo)
        elif tipo.startswith("Pazzo"):
            partiDialogo = []
            nome = "Rallo"
            if avanzamentoDialogo == 4:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = -1
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1267_01_Tu_RALLO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1267_02_Rallo__RELEI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1267_03_Tu_COM_SEI_ARR_QUI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1267_04_Rallo_VAG_UN_PAZ_MON_DA_QUE_PAR_MEG_FAR_ATT_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1267_05_Tu__UN_PAZ_MON_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1267_06_Rallo_MMH_UNO_DUE_TRE_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1267_07_Tu__CHE_STA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1267_08_Rallo_QUARTA_DOMANDA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1267_09_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1267_10_Rallo_DOMANDA_)
                dialogo.append(LDS._1267_11_Rallo_QUA_DOM_DOV_SEI_)
                dialogo.append(LDS._1267_12_Rallo_SON_DAV_A_TE_)
                dialogo.append(LDS._1267_13_Rallo_SON_NEL_PAS_MON_)
                dialogo.append(LDS._1267_14_Rallo_SON_SUL_TER_)
                dialogo.append(LDS._1267_15_Rallo_NON_LO_SO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1267_16_Rallo_RISPOSTA_)
                dialogo.append(LDS._1267_17_Rallo_DAVANTI_)
                dialogo.append(LDS._1267_18_Rallo_NEL_PAZ_MON_)
                dialogo.append(LDS._1267_19_Rallo_SU_DEL_TER_)
                dialogo.append(LDS._1267_20_Rallo_MMH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1267_21_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1267_22_Rallo_MI_STA_MEN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1267_23_Tu__NO_PER_DOV_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1267_24_Rallo_NON_LO_SAI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1267_25_Tu__COSA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1267_26_Rallo_MMH_)
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 5:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = -1
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1268_01_Tu_RALLO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1268_02_Rallo__TU_TI_FID_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1268_03_Tu__DI_COS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1268_04_Rallo_DOMANDA_)
                dialogo.append(LDS._1268_05_Rallo_QUI_DOM_TI_FID_DI_QUE_CHE_VED_E_RAC_)
                dialogo.append(LDS._1268_06_Rallo_CER_TU_NO_)
                dialogo.append(LDS._1268_07_Rallo_DI_COS_DOV_FID_SE_NON_DI_QUE_)
                dialogo.append(LDS._1268_08_Rallo_NON_DOV_FID_DI_QUE_CHE_VED_)
                dialogo.append(LDS._1268_09_Rallo_NON_LO_SO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1268_10_Rallo_RISPOSTA_)
                dialogo.append(LDS._1268_11_Rallo_IO_SON_IL_CAP_DI_QUE_PER_QUE_CHE_VED_HA_FED_IN_ME_)
                dialogo.append(LDS._1268_12_Rallo_DI_FRR_CAP_DI_QUE_PER_)
                dialogo.append(LDS._1268_13_Rallo_IO_NON_LO_FAR_)
                dialogo.append(LDS._1268_14_Rallo_MMH_PAZ_PAZ_MON_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1268_15_Tu_OK_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1268_16_Rallo_MMH_)
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 6:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1269_01_Rallo_MMH_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["passoMontano7"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoPassoMontano"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0361_01_Tu__STO_CON_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0361_02_Tu_MA_QUE__GHI_DIO_SAN_CHE_CAV_CI_FAC_QUI_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["passoMontano8"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoNemiciBloccatiPassoMontano"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0362_01_Tu_NON__FRE_COM_MI_RIC_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0362_02_Tu_LAR__FRE_MA_NON_SI_SEN_QUA_PER_NIE_SI_RIS_SUB_)
                partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo


