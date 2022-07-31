# -*- coding: utf-8 -*-

import Codice.Variabili.GlobalGameVar as GlobalGameVar
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
    if stanzaDiAppartenenza == GlobalGameVar.dictStanze["labirinto10"]:
        if tipo.startswith("Pazzo"):
            partiDialogo = []
            nome = "Rallo"
            if avanzamentoDialogo == 2:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = -1
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1043_01_Tu_RAL_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1043_02_Rallo_SECONDA_DOMANDA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1043_03_Tu_COS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1043_04_Rallo_DOMANDA_)
                dialogo.append(LDS._1043_05_Rallo_SEC_DOM_COS_VED_)
                dialogo.append(LDS._1043_06_Rallo_VED_TE_RAL_)
                dialogo.append(LDS._1043_07_Rallo_VED_UN_UOM_STR_)
                dialogo.append(LDS._1043_08_Rallo_VED_UN_UOM_STR_)
                dialogo.append(LDS._1043_09_Rallo_VED_UN_PAZ_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1043_10_Rallo_RISPOSTA_)
                dialogo.append(LDS._1043_11_Rallo_SONO_FFFRELLOU_)
                dialogo.append(LDS._1043_12_Rallo_MMH_)
                dialogo.append(LDS._1043_13_Rallo_MMH_)
                dialogo.append(LDS._1043_14_Rallo_UUULULULU_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1043_15_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1043_16_Rallo__)
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 3:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = -1
                avanzaColDialogo = True
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1044_01_Tu__ADE__FIN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1044_02_Rallo_DOMANDA_)
                dialogo.append(LDS._1044_03_Rallo_TER_DOM_COM_FAI_A_VED_)
                dialogo.append(LDS._1044_04_Rallo_SEI_QUI_DAV_A_ME_TI_VED_)
                dialogo.append(LDS._1044_05_Rallo_CON_GLI_OCC_)
                dialogo.append(LDS._1044_06_Rallo_POS_VED_LE_COS_CHE_RIF_LA_LUC_)
                dialogo.append(LDS._1044_07_Rallo_NON_LO_SO_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1044_08_Rallo_RISPOSTA_)
                dialogo.append(LDS._1044_09_Rallo_DOVE_SONO_)
                dialogo.append(LDS._1044_10_Rallo__)
                dialogo.append(LDS._1044_11_Rallo_LA_LUCE_)
                dialogo.append(LDS._1044_12_Rallo_MMH_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1044_13_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1044_14_Rallo__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1044_15_Tu__CRE_CHE_CI_SIA_UNA_SPE_DI_MEC_NEG_OCC_CHE_CI_PER_DI_VED_NON_HO_IDE_DI_COM_FUN_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1044_16_Rallo_MMH_)
                partiDialogo.append(dialogo)
            elif avanzamentoDialogo == 4:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1045_01_Rallo_MMH_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["labirinto14"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialStartNelLabirinto"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0164_01_Tu__MER_DI_QUA_CI_SIA_GI_PAS_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0164_02_Tu__NO_ASP__GIU_ERA_SOL_TU_NON_PRE_SO_ESA_DOV_STI_AND_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["labirinto20"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoMetaLabirinto"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0165_01_Tu_CE_LAB_FAT_ALL_FIN_NON__STA_COS_COM_BAS_SEG_LA_MAP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0165_02_Tu__TE_LAV_DET_CHE_POT_FID_DI_ROD_DEV_SOL_CER_DI_ESS_PI_OTT_)
                partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo


