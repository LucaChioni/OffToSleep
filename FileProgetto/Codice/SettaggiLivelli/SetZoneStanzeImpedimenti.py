# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche


def nonPuoiProcedere(avanzamentoStoria, stanzaVecchia, stanzaDestinazione, equipaggiamentoIndossato):
    nonProcedere = False

    if stanzaDestinazione == -1:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tutorialUtilizzoOggetti"] and stanzaVecchia == GlobalGameVar.dictStanze["sognoSara1"] and stanzaDestinazione == GlobalGameVar.dictStanze["sognoSara2"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoCasaHansSara2"] and stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara1"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaHansSara2"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["incontroFiglioUfficiale"] and stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"] and stanzaDestinazione == GlobalGameVar.dictStanze["forestaCadetta6"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"] and stanzaDestinazione == GlobalGameVar.dictStanze["forestaCadetta7"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["armaturaNonnoCompletata"] and stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara1"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaHansSara2"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["accampamentoForestaAnalizzato2"] and stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"] and (stanzaDestinazione == GlobalGameVar.dictStanze["forestaCadetta6"] or stanzaDestinazione == GlobalGameVar.dictStanze["forestaCadetta7"]):
        nonProcedere = True
    elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara4"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaHansSara2"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCittà2"] and stanzaVecchia == GlobalGameVar.dictStanze["città1"] and stanzaDestinazione == GlobalGameVar.dictStanze["città2"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and stanzaVecchia == GlobalGameVar.dictStanze["città2"] and (stanzaDestinazione == GlobalGameVar.dictStanze["città1"] or stanzaDestinazione == GlobalGameVar.dictStanze["città5"]):
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCittà3"] and stanzaVecchia == GlobalGameVar.dictStanze["città2"] and stanzaDestinazione == GlobalGameVar.dictStanze["città3"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and stanzaVecchia == GlobalGameVar.dictStanze["città3"] and (stanzaDestinazione == GlobalGameVar.dictStanze["città2"] or stanzaDestinazione == GlobalGameVar.dictStanze["città5"] or stanzaDestinazione == GlobalGameVar.dictStanze["città9"]):
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCittà4"] and stanzaVecchia == GlobalGameVar.dictStanze["città3"] and stanzaDestinazione == GlobalGameVar.dictStanze["città4"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and stanzaVecchia == GlobalGameVar.dictStanze["città4"] and stanzaDestinazione == GlobalGameVar.dictStanze["città3"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["arrivoDavidCasaUfficiale"] and stanzaVecchia == GlobalGameVar.dictStanze["città4"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaDavid1"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and stanzaVecchia == GlobalGameVar.dictStanze["casaDavid1"] and stanzaDestinazione == GlobalGameVar.dictStanze["città4"]:
        nonProcedere = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoDopoBagnoDavid"] and stanzaVecchia == GlobalGameVar.dictStanze["casaDavid3"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaDavid2"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["chiestoDegliAlloggiAlMercante"] and stanzaVecchia == GlobalGameVar.dictStanze["città5"] and stanzaDestinazione == GlobalGameVar.dictStanze["città6"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["rimosseMonetePerEntrareInConfraternita"] and stanzaVecchia == GlobalGameVar.dictStanze["città5"] and stanzaDestinazione == GlobalGameVar.dictStanze["città7"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and stanzaVecchia == GlobalGameVar.dictStanze["città9"] and stanzaDestinazione == GlobalGameVar.dictStanze["stradaPerSelvaArida1"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"] and stanzaVecchia == GlobalGameVar.dictStanze["città10"] and stanzaDestinazione == GlobalGameVar.dictStanze["stradaPerPassoMontano1"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["dialogoServoCasaDavidDopoSuicidio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ricevutoCertificatoDalServo"] and stanzaVecchia == GlobalGameVar.dictStanze["casaDavid2"] and (stanzaDestinazione == GlobalGameVar.dictStanze["casaDavid1"] or stanzaDestinazione == GlobalGameVar.dictStanze["casaDavid3"]):
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["uccisoPrimoAggressore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and stanzaVecchia == GlobalGameVar.dictStanze["città4"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaDavid1"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["monologoDopoArrivoInBiblioteca"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and stanzaVecchia == GlobalGameVar.dictStanze["città7"] and stanzaDestinazione == GlobalGameVar.dictStanze["città5"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and equipaggiamentoIndossato and stanzaVecchia == GlobalGameVar.dictStanze["città7"] and stanzaDestinazione == GlobalGameVar.dictStanze["biblioteca1"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["andatoNelloStudioDelBibliotecario"] and stanzaVecchia == GlobalGameVar.dictStanze["biblioteca2"] and stanzaDestinazione == GlobalGameVar.dictStanze["biblioteca3"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoNeil"] and stanzaVecchia == GlobalGameVar.dictStanze["biblioteca3"] and stanzaDestinazione == GlobalGameVar.dictStanze["biblioteca2"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["incontratoIDueAggressori"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"] and stanzaVecchia == GlobalGameVar.dictStanze["città3"] and stanzaDestinazione == GlobalGameVar.dictStanze["città4"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and stanzaVecchia == GlobalGameVar.dictStanze["città4"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaDavid1"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["risoltoEnigmaMappaLabirinto"] and stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod1"] and stanzaDestinazione == GlobalGameVar.dictStanze["labirinto3"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"] and stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod1"] and stanzaDestinazione == GlobalGameVar.dictStanze["avampostoDiRod3"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"] and stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello1"] and stanzaDestinazione == GlobalGameVar.dictStanze["scorciatoiaLabirinto1"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello1"] and stanzaDestinazione == GlobalGameVar.dictStanze["esternoCastello5"]:
        nonProcedere = True
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSalaDaPranzoCastello"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello7"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["monologoArrivoSecondoPianoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dormitoNelCastello"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello9"] and (stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello8"] or stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello12"]):
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["dormitoNelCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["primoDialogoNeil"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello9"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello8"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["apertoPortaStanza19CastelloVerso20"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello19"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello20"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ripresoImpoDaNeil"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello20"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello19"]:
        nonProcedere = True
    elif (avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"] or GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]) and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello19"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello2"]:
        nonProcedere = True
    elif (avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"] or GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]) and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello2"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello19"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoNotatoAssenzaRodFuoriDallAvamposto"] and stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello1"] and stanzaDestinazione == GlobalGameVar.dictStanze["labirinto20"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["apertoPortaStanza19CastelloVerso21"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello19"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello21"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"] and ((stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara2"] and (stanzaDestinazione == GlobalGameVar.dictStanze["casaHansSara1"] or stanzaDestinazione == GlobalGameVar.dictStanze["casaHansSara3"])) or (stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara4"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaHansSara2"]) or (stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"] and stanzaDestinazione == GlobalGameVar.dictStanze["forestaCadetta4"]) or (stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"] and stanzaDestinazione == GlobalGameVar.dictStanze["forestaCadetta6"]) or (stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"] and stanzaDestinazione == GlobalGameVar.dictStanze["forestaCadetta7"])):
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoHansFuoriCasaSognoCastello"] and stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara4"] and stanzaDestinazione == GlobalGameVar.dictStanze["forestaCadetta5"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sbloccatoTunnelDiRod"] and stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod2"] and stanzaDestinazione == GlobalGameVar.dictStanze["tunnelDiRod3"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["trovatoChiaveAvampostoDiRod"] and stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod3"] and stanzaDestinazione == GlobalGameVar.dictStanze["avampostoDiRod1"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sbloccatoCaverna"] and stanzaVecchia == GlobalGameVar.dictStanze["palazzoDiRod1"] and stanzaDestinazione == GlobalGameVar.dictStanze["caverna1"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoRodAperturaRetroPalazzo"] and stanzaVecchia == GlobalGameVar.dictStanze["palazzoDiRod2"] and stanzaDestinazione == GlobalGameVar.dictStanze["palazzoDiRod5"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["presiStrumentiPerStudiareImpo"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sbloccatoTunnelDiRod"] and stanzaVecchia == GlobalGameVar.dictStanze["palazzoDiRod2"] and stanzaDestinazione == GlobalGameVar.dictStanze["palazzoDiRod1"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sbloccatoTunnelDiRod"] and stanzaVecchia == GlobalGameVar.dictStanze["tunnelDiRod3"] and stanzaDestinazione == GlobalGameVar.dictStanze["avampostoDiRod2"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["avviatoBattitoCardiacoPreConsegnaStrumenti"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presaChiaveSoldatoInternoCastello20"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello20"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello19"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello19"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello20"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"] and stanzaVecchia == GlobalGameVar.dictStanze["palazzoDiRod2"] and stanzaDestinazione == GlobalGameVar.dictStanze["palazzoDiRod1"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"] and stanzaVecchia == GlobalGameVar.dictStanze["palazzoDiRod2"] and stanzaDestinazione == GlobalGameVar.dictStanze["palazzoDiRod3"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"] and stanzaVecchia == GlobalGameVar.dictStanze["palazzoDiRod2"] and stanzaDestinazione == GlobalGameVar.dictStanze["palazzoDiRod4"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"] and stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod1"] and stanzaDestinazione == GlobalGameVar.dictStanze["selvaArida16"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"] and stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod1"] and stanzaDestinazione == GlobalGameVar.dictStanze["labirinto3"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"] and stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello1"] and stanzaDestinazione == GlobalGameVar.dictStanze["labirinto20"]:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["apertoPortaStanza8Castello"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello8"] and stanzaDestinazione == GlobalGameVar.dictStanze["tunnelSubacqueo1"]:
        nonProcedere = True

    return nonProcedere


def possibileAprirePorta(stanza, xPorta, yPorta, avanzamentoStoria):
    procedi = True
    if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"] and xPorta == GlobalHWVar.gpx * 25 and yPorta == GlobalHWVar.gpy * 3:
        procedi = False
    if GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tutorialMappaDiario"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"] and xPorta == GlobalHWVar.gpx * 6 and yPorta == GlobalHWVar.gpy * 9:
        procedi = False
    if GlobalGameVar.dictAvanzamentoStoria["monologoIndicazioniArmaturaNonno"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["trovataChiaveRipostiglio"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"] and xPorta == GlobalHWVar.gpx * 26 and yPorta == GlobalHWVar.gpy * 11:
        procedi = False
    if GlobalGameVar.dictAvanzamentoStoria["arrivoDavidPrimoPiano"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presaChiaveStanzaDaLettoDavid"] and stanza == GlobalGameVar.dictStanze["casaDavid3"] and xPorta == GlobalHWVar.gpx * 12 and yPorta == GlobalHWVar.gpy * 8:
        procedi = False
    if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presoChiaveCameraDaLettoCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello10"] and xPorta == GlobalHWVar.gpx * 8 and yPorta == GlobalHWVar.gpy * 5:
        procedi = False
    if GlobalGameVar.dictAvanzamentoStoria["guardiaCastelloChiusoPortaLibreriaInternoCastello18"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dormitoNelCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello18"] and xPorta == GlobalHWVar.gpx * 17 and yPorta == GlobalHWVar.gpy * 12:
        procedi = False
    if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and stanza == GlobalGameVar.dictStanze["internoCastello20"] and xPorta == GlobalHWVar.gpx * 17 and yPorta == GlobalHWVar.gpy * 9:
        procedi = False
    if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and stanza == GlobalGameVar.dictStanze["internoCastello8"] and xPorta == GlobalHWVar.gpx * 7 and yPorta == GlobalHWVar.gpy * 7:
        procedi = False
    if (GlobalGameVar.dictAvanzamentoStoria["inizioSognoCasaDavid"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCasaDavid"] or GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"]) and stanza == GlobalGameVar.dictStanze["casaHansSara1"] and ((xPorta == GlobalHWVar.gpx * 25 and yPorta == GlobalHWVar.gpy * 3) or (xPorta == GlobalHWVar.gpx * 7 and yPorta == GlobalHWVar.gpy * 6)):
        procedi = False
    if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioParteDiRod"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod2"] and (xPorta == GlobalHWVar.gpx * 12 and yPorta == GlobalHWVar.gpy * 8):
        procedi = False
    if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello20"] and xPorta == GlobalHWVar.gpx * 10 and yPorta == GlobalHWVar.gpy * 6:
        procedi = False
    if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello3"] and xPorta == GlobalHWVar.gpx * 25 and yPorta == GlobalHWVar.gpy * 6:
        procedi = False
    if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello5"] and xPorta == GlobalHWVar.gpx * 25 and yPorta == GlobalHWVar.gpy * 4:
        procedi = False
    if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello16"] and xPorta == GlobalHWVar.gpx * 16 and yPorta == GlobalHWVar.gpy * 5:
        procedi = False
    if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello16"] and xPorta == GlobalHWVar.gpx * 8 and yPorta == GlobalHWVar.gpy * 6:
        procedi = False
    if GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"] and stanza == GlobalGameVar.dictStanze["internoCastello17"] and xPorta == GlobalHWVar.gpx * 8 and yPorta == GlobalHWVar.gpy * 3:
        procedi = False

    return procedi


def scriviNomeZona(stanza, stanzaVecchia):
    nomeDaScrivere = False
    if (stanzaVecchia == GlobalGameVar.dictStanze["sognoSara4"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta1"] and stanza == GlobalGameVar.dictStanze["casaHansSara4"]) or (stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"]):
        nomeDaScrivere = "Casa"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara4"] and stanza == GlobalGameVar.dictStanze["forestaCadetta1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà1"] and stanza == GlobalGameVar.dictStanze["forestaCadetta9"]):
        nomeDaScrivere = "Foresta Cadetta"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta9"] and stanza == GlobalGameVar.dictStanze["stradaPerCittà1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["città1"] and stanza == GlobalGameVar.dictStanze["stradaPerCittà3"]):
        nomeDaScrivere = u"Strada per Città"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà3"] and stanza == GlobalGameVar.dictStanze["città1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["casaDavid1"] and stanza == GlobalGameVar.dictStanze["città4"]) or (stanzaVecchia == GlobalGameVar.dictStanze["biblioteca1"] and stanza == GlobalGameVar.dictStanze["città7"]) or (stanzaVecchia == GlobalGameVar.dictStanze["stradaPerSelvaArida1"] and stanza == GlobalGameVar.dictStanze["città9"]) or (stanzaVecchia == GlobalGameVar.dictStanze["stradaPerPassoMontano1"] and stanza == GlobalGameVar.dictStanze["città10"]):
        nomeDaScrivere = u"Città"
    elif stanzaVecchia == GlobalGameVar.dictStanze["città4"] and stanza == GlobalGameVar.dictStanze["casaDavid1"]:
        nomeDaScrivere = u"Casa di David"
    elif stanzaVecchia == GlobalGameVar.dictStanze["città7"] and stanza == GlobalGameVar.dictStanze["biblioteca1"]:
        nomeDaScrivere = u"Biblioteca"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["città9"] and stanza == GlobalGameVar.dictStanze["stradaPerSelvaArida1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["selvaArida1"] and stanza == GlobalGameVar.dictStanze["stradaPerSelvaArida2"]):
        nomeDaScrivere = u"Strada per Selva Arida"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["stradaPerSelvaArida2"] and stanza == GlobalGameVar.dictStanze["selvaArida1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod1"] and stanza == GlobalGameVar.dictStanze["selvaArida16"]):
        nomeDaScrivere = u"Selva Arida"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["selvaArida16"] and stanza == GlobalGameVar.dictStanze["avampostoDiRod1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["labirinto3"] and stanza == GlobalGameVar.dictStanze["avampostoDiRod1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["scorciatoiaLabirinto2"] and stanza == GlobalGameVar.dictStanze["avampostoDiRod2"]) or (stanzaVecchia == GlobalGameVar.dictStanze["tunnelDiRod3"] and stanza == GlobalGameVar.dictStanze["avampostoDiRod2"]):
        nomeDaScrivere = u"Avamposto di Rod"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod1"] and stanza == GlobalGameVar.dictStanze["labirinto3"]) or (stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello1"] and stanza == GlobalGameVar.dictStanze["labirinto20"]):
        nomeDaScrivere = u"Labirinto"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["labirinto20"] and stanza == GlobalGameVar.dictStanze["esternoCastello1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["internoCastello1"] and stanza == GlobalGameVar.dictStanze["esternoCastello5"]) or (stanzaVecchia == GlobalGameVar.dictStanze["scorciatoiaLabirinto1"] and stanza == GlobalGameVar.dictStanze["esternoCastello1"]):
        nomeDaScrivere = u"Castello di Neil - Esterno"
    elif stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello5"] and stanza == GlobalGameVar.dictStanze["internoCastello1"]:
        nomeDaScrivere = u"Castello di Neil - Interno"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello1"] and stanza == GlobalGameVar.dictStanze["scorciatoiaLabirinto1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod2"] and stanza == GlobalGameVar.dictStanze["scorciatoiaLabirinto2"]):
        nomeDaScrivere = u"Scorciatoia sulle montagne"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["città10"] and stanza == GlobalGameVar.dictStanze["stradaPerPassoMontano1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["passoMontano1"] and stanza == GlobalGameVar.dictStanze["stradaPerPassoMontano2"]):
        nomeDaScrivere = u"Strada per Passo Montano"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["stradaPerPassoMontano2"] and stanza == GlobalGameVar.dictStanze["passoMontano1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["palazzoDiRod1"] and stanza == GlobalGameVar.dictStanze["passoMontano10"]):
        nomeDaScrivere = u"Passo Montano"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["passoMontano10"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["tunnelDiRod1"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod5"]) or (stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello3"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod2"]):
        nomeDaScrivere = u"Palazzo di Rod"
    elif (stanzaVecchia == GlobalGameVar.dictStanze["palazzoDiRod5"] and stanza == GlobalGameVar.dictStanze["tunnelDiRod1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod2"] and stanza == GlobalGameVar.dictStanze["tunnelDiRod3"]):
        nomeDaScrivere = u"Tunnel di Rod"

    if nomeDaScrivere:
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
        FunzioniGraficheGeneriche.messaggio(nomeDaScrivere, GlobalHWVar.grigiochi, GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 8, 150, centrale=True)
        GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 4), int(GlobalHWVar.gpy * 10.6)), (int(GlobalHWVar.gpx * 28) - 1, int(GlobalHWVar.gpy * 10.6)), 2)
        FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=2)
        GlobalHWVar.aggiornaSchermo()


def settaNomeImgStanza(avanzamentoStoria, stanza):
    nomeStanza = "Stanza"
    if stanza == GlobalGameVar.dictStanze["casaHansSara1"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            nomeStanza = "StanzaA"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSognoCasaDavid"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaC"
    if stanza == GlobalGameVar.dictStanze["casaHansSara2"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] or GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["casaHansSara4"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] or GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["forestaCadetta1"] or stanza == GlobalGameVar.dictStanze["forestaCadetta2"] or stanza == GlobalGameVar.dictStanze["forestaCadetta3"] or stanza == GlobalGameVar.dictStanze["forestaCadetta4"] or stanza == GlobalGameVar.dictStanze["forestaCadetta6"] or stanza == GlobalGameVar.dictStanze["forestaCadetta7"] or stanza == GlobalGameVar.dictStanze["forestaCadetta8"] or stanza == GlobalGameVar.dictStanze["forestaCadetta9"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioUltimoDialogoHans"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            nomeStanza = "StanzaB"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] or GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaC"
    if stanza == GlobalGameVar.dictStanze["stradaPerCittà1"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["stradaPerCittà2"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["stradaPerCittà3"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["apertoPortaCittà"]:
            nomeStanza = "StanzaA"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaC"
    if stanza == GlobalGameVar.dictStanze["città1"] or stanza == GlobalGameVar.dictStanze["città2"] or stanza == GlobalGameVar.dictStanze["città3"] or stanza == GlobalGameVar.dictStanze["città4"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            nomeStanza = "StanzaA"
        elif stanza == GlobalGameVar.dictStanze["città4"] and avanzamentoStoria > GlobalGameVar.dictAvanzamentoStoria["monologoDopoUccisioneAggressori"]:
            nomeStanza = "StanzaC"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["casaDavid1"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["casaDavid2"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoPostCambioPerCenaDavid"]:
            nomeStanza = "StanzaA"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaC"
    if stanza == GlobalGameVar.dictStanze["casaDavid3"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["andatoADormireCasaDavid"]:
            nomeStanza = "StanzaA"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dialogoServoRisveglioSecondoGiorno"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaC"
    if stanza == GlobalGameVar.dictStanze["biblioteca3"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["vomitatoInBiblioteca"]:
            nomeStanza = "StanzaA"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["andatoACercareImpo"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaC"
    if stanza == GlobalGameVar.dictStanze["esternoCastello1"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"]:
            nomeStanza = "StanzaA"
        elif GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            nomeStanza = "StanzaC"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["esternoCastello2"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["apertoCancelloPrincipaleCastello"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["internoCastello1"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["internoCastello2"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"] or GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            nomeStanza = "StanzaA"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaC"
    if stanza == GlobalGameVar.dictStanze["internoCastello3"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["internoCastello4"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"]:
            nomeStanza = "StanzaA"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaC"
    if stanza == GlobalGameVar.dictStanze["internoCastello5"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["internoCastello6"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"]:
            nomeStanza = "StanzaA"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaC"
    if stanza == GlobalGameVar.dictStanze["internoCastello7"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cenaCastelloServita"] or GlobalGameVar.dictAvanzamentoStoria["dormitoNelCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"]:
            nomeStanza = "StanzaA"
        elif GlobalGameVar.dictAvanzamentoStoria["cenaCastelloServita"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["dormitoNelCastello"]:
            nomeStanza = "StanzaB"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            nomeStanza = "StanzaC"
        else:
            nomeStanza = "StanzaD"
    if stanza == GlobalGameVar.dictStanze["internoCastello8"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            nomeStanza = "StanzaA"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["apertoPortaStanza8Castello"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaC"
    if stanza == GlobalGameVar.dictStanze["internoCastello9"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"]:
            nomeStanza = "StanzaA"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaC"
    if stanza == GlobalGameVar.dictStanze["internoCastello10"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dormitoNelCastello"]:
            nomeStanza = "StanzaB"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaC"
    if stanza == GlobalGameVar.dictStanze["internoCastello11"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"]:
            nomeStanza = "StanzaA"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaC"
    if stanza == GlobalGameVar.dictStanze["internoCastello12"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["internoCastello13"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["internoCastello14"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["internoCastello15"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"]:
            nomeStanza = "StanzaA"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaC"
    if stanza == GlobalGameVar.dictStanze["internoCastello16"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["internoCastello17"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["internoCastello18"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["internoCastello19"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["apertoPortaStanza19CastelloVerso20"]:
            nomeStanza = "StanzaA"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioViaggioVersoCasaMercante"] or GlobalGameVar.dictAvanzamentoStoria["inizioFugaDalCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            nomeStanza = "StanzaB"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["apertoPortaStanza19CastelloVerso21"]:
            nomeStanza = "StanzaC"
        else:
            nomeStanza = "StanzaD"
    if stanza == GlobalGameVar.dictStanze["internoCastello20"]:
        if GlobalGameVar.dictAvanzamentoStoria["chiusoPortaInternoCastello20DaSoldato"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["apertoPortaInternoCastello20AndandoInInternoCastello19"]:
            nomeStanza = "StanzaB"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaC"
    if stanza == GlobalGameVar.dictStanze["internoCastello21"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"]:
            nomeStanza = "StanzaA"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["alzataDalTavoloLaboratorioCastello"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaC"
    if stanza == GlobalGameVar.dictStanze["avampostoDiRod2"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sbloccatoTunnelDiRod"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["palazzoDiRod1"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sbloccatoCaverna"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["tunnelDiRod3"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sbloccatoTunnelDiRod"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"

    return nomeStanza


def modificaStanzePacifiche(avanzamentoStoria):
    if GlobalGameVar.dictAvanzamentoStoria["incontratoIDueAggressori"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["riavviatoMusicaPostDialogoBibliotecario"]:
        GlobalGameVar.vetStanzePacifiche = []
    elif GlobalGameVar.dictAvanzamentoStoria["avviatoBattitoCardiacoPreConsegnaStrumenti"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
        GlobalGameVar.vetStanzePacifiche = []
    else:
        GlobalGameVar.vetStanzePacifiche = GlobalGameVar.vetStanzePacificheBackUp[:]


def settaPresenzaDiColco(avanzamentoStoria):
    if GlobalGameVar.dictAvanzamentoStoria["ricevutoImpo"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ricevutoImpoPietra"]:
        GlobalGameVar.impoPresente = True
        GlobalGameVar.impoPietraPosseduta = False
    elif GlobalGameVar.dictAvanzamentoStoria["ricevutoImpoPietra"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["impoPresoDaGuardiaCastello"]:
        GlobalGameVar.impoPresente = True
        GlobalGameVar.impoPietraPosseduta = True
    elif GlobalGameVar.dictAvanzamentoStoria["impoPresoDaGuardiaCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["ripresoImpoDaNeil"]:
        GlobalGameVar.impoPresente = False
        GlobalGameVar.impoPietraPosseduta = True
    elif GlobalGameVar.dictAvanzamentoStoria["ripresoImpoDaNeil"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["messoImpoSulTavoloDopoConsegnaStrumenti"]:
        GlobalGameVar.impoPresente = True
        GlobalGameVar.impoPietraPosseduta = True
    elif GlobalGameVar.dictAvanzamentoStoria["messoImpoSulTavoloDopoConsegnaStrumenti"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cliccatoImpoPietraPerFuggireDaNeilConImpo"]:
        GlobalGameVar.impoPresente = False
        GlobalGameVar.impoPietraPosseduta = True
    elif GlobalGameVar.dictAvanzamentoStoria["cliccatoImpoPietraPerFuggireDaNeilConImpo"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
        GlobalGameVar.impoPresente = True
        GlobalGameVar.impoPietraPosseduta = True
    else:
        GlobalGameVar.impoPresente = False
        GlobalGameVar.impoPietraPosseduta = False


def decidiSePoterAprireMenu(avanzamentoStoria):
    possibileAprireMenu = True
    if GlobalGameVar.dictAvanzamentoStoria["inizioSognoCasaDavid"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCasaDavid"]:
        possibileAprireMenu = False
    elif GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"]:
        possibileAprireMenu = False
    elif GlobalGameVar.dictAvanzamentoStoria["risveglioSaraResuscitata"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
        possibileAprireMenu = False

    return possibileAprireMenu


def decidiSePoterParare(avanzamentoStoria):
    impossibileParare = False
    if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
        impossibileParare = True
    elif GlobalGameVar.dictAvanzamentoStoria["incontratoIDueAggressori"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoDopoUccisioneAggressori"]:
        impossibileParare = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"]:
        impossibileParare = True

    return impossibileParare
