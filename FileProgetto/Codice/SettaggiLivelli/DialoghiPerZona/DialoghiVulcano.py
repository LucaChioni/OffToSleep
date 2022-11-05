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

    if stanzaDiAppartenenza == GlobalGameVar.dictStanze["vulcano1"]:
        if tipo.startswith("Pazzo"):
            partiDialogo = []
            nome = "Rallo"
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                if avanzamentoDialogo == 6:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = -1
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1312_01_Tu__RALLO_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1312_02_Rallo__)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1312_03_Tu__IMM_MA_COM_ARR_FIN_QUI_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1312_04_Tu__OH_HA_UN_FOG_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1312_05_Tu__C_SCR_SE_DOM_CHE_FAI_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1312_06_Tu__MA_COM_POI_CHE_SEN_HA_SE_NON_PUO_NEA_SEN_LA_RIS_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1312_07_Rallo__)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1312_08_Tu_DOMANDA_)
                    dialogo.append(LDS._1312_09_Tu__VA_BEH_SES_DOM_CHE_FAC_)
                    dialogo.append(LDS._1312_10_Tu_NON_LO_SO_)
                    dialogo.append(LDS._1312_11_Tu_VAD_AVA_E_GUA_CHE_SUC_)
                    dialogo.append(LDS._1312_12_Tu_STO_LEG_UN_FOG_)
                    dialogo.append(LDS._1312_13_Tu_PRE_COS_DI_QUE_CHE_PER_)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1312_14_Rallo_RISPOSTA_)
                    dialogo.append(LDS._1312_15_Rallo__)
                    dialogo.append(LDS._1312_16_Rallo__)
                    dialogo.append(LDS._1312_17_Rallo__)
                    dialogo.append(LDS._1312_18_Rallo__)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1312_19_Tu__)
                    partiDialogo.append(dialogo)
                elif avanzamentoDialogo == 7:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("personaggio")
                    dialogo.append(LDS._1313_01_Rallo__)
                    partiDialogo.append(dialogo)
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1313_02_Tu_NON_HA_ALT_FOG_)
                    partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1314_01_Rallo__)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoCumuloImpo":
            partiDialogo = []
            nome = LI.CUMULO_IMPO
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            avanzaColDialogo = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1315_01_Tu__UN_CUM_DI_IMP_)
            partiDialogo.append(dialogo)
        elif tipo == "RoboLeggero":
            partiDialogo = []
            nome = LI.IMPO_LEGGERO
            if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1316_01_Tu_MI_STA_IGN_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1317_01_ImpoLeggero__)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["vulcano2"]:
        if tipo == "OggettoComputerCostruttore":
            partiDialogo = []
            nome = LI.COMPUTER
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoVistoComputerVulcano"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0390_01_Tu__CI_SON_DEI_SIM_LUM_DEL_SCR_STR_E_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0390_02_Tu_OH_QUE_SON_IMP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0390_03_Tu__DIS_DI_DIV_SPE_DI_IMP_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0390_04_Tu__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0390_05_Tu__CHE_SIG_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1318_01_Tu_NON_HO_IDE_DI_COS_SIA_QUE_AFF_CI_SON_DEG_IMP_DIS_SOP_)
                partiDialogo.append(dialogo)
            else:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = 4
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1319_01_Tu__IL_CAL_DI_EVE_DEL_COS_STA_ELA_IL_PRO_FRA_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1319_02_Tu_DOMANDA_)
                dialogo.append(LDS._1319_03_Tu__POS_FER_DOV_)
                dialogo.append(LDS._1319_04_Tu_NO_POT_CAN_LA_REA_)
                dialogo.append(LDS._1319_05_Tu_NO_POT_UCC_TUT_)
                dialogo.append(LDS._1319_06_Tu_NO_POT_CAN_LA_REA_)
                dialogo.append(LDS._1319_07_Tu_SI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1319_08_Tu_RISPOSTA_)
                dialogo.append(LDS._1319_09_Tu__)
                dialogo.append(LDS._1319_10_Tu__)
                dialogo.append(LDS._1319_11_Tu__)
                dialogo.append(LDS._1319_12_Tu_OK_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["vulcano3"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["esclamazionePostRisveglioNelVulcano"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0391_01_Tu_IMPO_)
                partiDialogo.append(dialogo)
        elif tipo == "OggettoCellaCostruttore":
            partiDialogo = []
            nome = LI.SCONOSCIUTO
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologo2PostRisveglioNelVulcano"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0392_01_Tu__EHI_)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDP._0392_02_Sconosciuto__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0392_03_Tu__)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1320_01_Sconosciuto__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1320_02_Tu_C_UN_CAD_HA_DEI_TUB_CHE_GLI_ESC_DAL_COR_)
                partiDialogo.append(dialogo)
            else:
                nome = LI.COSTRUTTORE
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("personaggio")
                dialogo.append(LDS._1321_01_Costruttore__)
                partiDialogo.append(dialogo)
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1321_02_Tu__IL_CAD_DEL_COS_ALL_FIN_NEI__RIU_A_PRE_IL_SUO_POS_)
                partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo


