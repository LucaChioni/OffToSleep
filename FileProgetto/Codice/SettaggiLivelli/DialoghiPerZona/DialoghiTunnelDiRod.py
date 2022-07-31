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

    if tipo.startswith("OggettoDictCofanetto"):
        nome = LI.COFANETTO
        if tipo == "OggettoDictCofanettoAperto":
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1302_01_Tu_MA_SI__PRE_LA_MIA_ROB_)
            partiDialogo.append(dialogo)
        elif tipo == "OggettoDictCofanettoChiuso":
            oggettoDato = False
            avanzaStoria = False
            menuMercante = False
            scelta = False
            dialogo = []
            dialogo.append("tu")
            dialogo.append(LDS._1303_01_Tu_ADE_NON_MI_SER_QUE_ROB_)
            partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["tunnelDiRod1"]:
        if tipo == "OggettoImpo":
            partiDialogo = []
            nome = "Impo"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoUscitoDalPalazzoDiRod"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0373_01_Tu__BUI_QUA_DEN_)
                partiDialogo.append(dialogo)
    elif stanzaDiAppartenenza == GlobalGameVar.dictStanze["tunnelDiRod3"]:
        if tipo == "OggettoLevaTunnelDiRod":
            partiDialogo = []
            nome = "OggettoLevaTunnelDiRod"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoTunnelDiRod"]:
                oggettoDato = False
                avanzaStoria = True
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDP._0374_01_Tu_FOR_SE_TIR_QUE_LEV_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1304_01_Tu_NON_VOG_CHI_DI_NUO_LE_SBA_)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1305_01_Tu_LO_LAS_APE_FIN_NON_TOR_)
                partiDialogo.append(dialogo)
            elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1306_01_Tu__LA_LEV_CHE_HO_USA_PER_APR_IL_TUN_)
                partiDialogo.append(dialogo)
            elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
                oggettoDato = False
                avanzaStoria = False
                menuMercante = False
                scelta = False
                avanzaColDialogo = False
                dialogo = []
                dialogo.append("tu")
                dialogo.append(LDS._1307_01_Tu_NON_POS_TIR_ADE_)
                partiDialogo.append(dialogo)
            else:
                if avanzamentoDialogo == 0:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = True
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1308_01_Tu_TIR_LA_LEV_)
                    partiDialogo.append(dialogo)
                else:
                    oggettoDato = False
                    avanzaStoria = False
                    menuMercante = False
                    scelta = False
                    avanzaColDialogo = False
                    dialogo = []
                    dialogo.append("tu")
                    dialogo.append(LDS._1309_01_Tu__LA_LEV_CHE_HO_USA_PER_APR_IL_TUN_)
                    partiDialogo.append(dialogo)

    return partiDialogo, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo


