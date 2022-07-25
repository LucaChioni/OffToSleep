# -*- coding: utf-8 -*-

import pygame
import GlobalHWVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.GestioneGrafica.FunzioniGraficheGeneriche as FunzioniGraficheGeneriche
import Codice.Localizzazione.LocalizInterfaccia as LI


def nonPuoiProcedere(avanzamentoStoria, stanzaVecchia, stanzaDestinazione, equipaggiamentoIndossato, listaAvanzamentoDialoghi):
    tiratoLevaTunnelDiRod = False
    i = 0
    while i < len(listaAvanzamentoDialoghi):
        if listaAvanzamentoDialoghi[i] == "OggettoLevaTunnelDiRod-0":
            if listaAvanzamentoDialoghi[i + 1] >= 1:
                tiratoLevaTunnelDiRod = True
            break
        i += 2
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
    elif GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara4"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaHansSara2"]:
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
    elif GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoPostLetturaAppuntiNeilSuRatti"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello19"] and (stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello18"] or stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello2"]):
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["riletturaLibroNeilSulTempo"] and ((stanzaVecchia == GlobalGameVar.dictStanze["internoCastello19"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello2"]) or (stanzaVecchia == GlobalGameVar.dictStanze["internoCastello18"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello17"])):
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologoApprofondimentoParadossiTempoBloccato"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello18"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello17"]:
        nonProcedere = True
    elif (GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] or avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]) and stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod2"] and stanzaDestinazione == GlobalGameVar.dictStanze["tunnelDiRod3"] and not tiratoLevaTunnelDiRod:
        nonProcedere = True
    elif (GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] or avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]) and stanzaVecchia == GlobalGameVar.dictStanze["tunnelDiRod3"] and stanzaDestinazione == GlobalGameVar.dictStanze["avampostoDiRod2"] and not tiratoLevaTunnelDiRod:
        nonProcedere = True
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["interagitoConComputerVulcano"] and stanzaVecchia == GlobalGameVar.dictStanze["vulcano2"] and stanzaDestinazione == GlobalGameVar.dictStanze["vulcano1"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["monologoNotatoCellaDiNeil"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["interagitoConCalcolatoreDiEventi"] and stanzaVecchia == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"] and stanzaDestinazione == GlobalGameVar.dictStanze["tunnelSubacqueo2"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello2"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello19"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello1"] and stanzaDestinazione == GlobalGameVar.dictStanze["esternoCastello5"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["avviatoSequenzaDiEventiCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello20"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello19"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello19"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello20"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello19"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello21"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello19"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello18"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["viaggioRapidoCalcolatore1UfficioNeil"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello2"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello1"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["viaggioRapidoCalcolatore1UfficioNeil"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello2"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello3"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["viaggioRapidoCalcolatore1UfficioNeil"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello7"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello2"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["viaggioRapidoCalcolatore1UfficioNeil"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello7"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello4"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["viaggioRapidoCalcolatore1UfficioNeil"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello7"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello6"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["viaggioRapidoCalcolatore1UfficioNeil"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello8"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello7"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["viaggioRapidoCalcolatore1UfficioNeil"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello8"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello9"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["viaggioRapidoCalcolatore1UfficioNeil"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] and stanzaVecchia == GlobalGameVar.dictStanze["tunnelSubacqueo1"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello8"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["viaggioRapidoCalcolatore1UfficioNeil"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sparitoNeilDallaCellaDelLaboratorioSecondaVolta"] and stanzaVecchia == GlobalGameVar.dictStanze["tunnelSubacqueo2"] and stanzaDestinazione == GlobalGameVar.dictStanze["tunnelSubacqueo1"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["viaggioRapidoCalcolatore1UfficioNeil"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sparitoNeilDallaCellaDelLaboratorioSecondaVolta"] and stanzaVecchia == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"] and stanzaDestinazione == GlobalGameVar.dictStanze["tunnelSubacqueo2"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["tunnelSubacqueo2"] and stanzaDestinazione == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["tunnelSubacqueo1"] and stanzaDestinazione == GlobalGameVar.dictStanze["tunnelSubacqueo2"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello8"] and stanzaDestinazione == GlobalGameVar.dictStanze["tunnelSubacqueo1"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello8"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello9"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello7"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello8"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello7"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello6"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello7"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello4"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello2"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello7"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello2"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello3"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello5"] and stanzaDestinazione == GlobalGameVar.dictStanze["internoCastello1"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello4"] and stanzaDestinazione == GlobalGameVar.dictStanze["esternoCastello5"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello2"] and stanzaDestinazione == GlobalGameVar.dictStanze["esternoCastello4"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello2"] and stanzaDestinazione == GlobalGameVar.dictStanze["esternoCastello3"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello1"] and stanzaDestinazione == GlobalGameVar.dictStanze["esternoCastello2"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello1"] and stanzaDestinazione == GlobalGameVar.dictStanze["labirinto20"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["scorciatoiaLabirinto1"] and stanzaDestinazione == GlobalGameVar.dictStanze["esternoCastello1"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["scorciatoiaLabirinto2"] and stanzaDestinazione == GlobalGameVar.dictStanze["scorciatoiaLabirinto1"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod2"] and stanzaDestinazione == GlobalGameVar.dictStanze["scorciatoiaLabirinto2"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod2"] and stanzaDestinazione == GlobalGameVar.dictStanze["avampostoDiRod3"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["tunnelDiRod3"] and stanzaDestinazione == GlobalGameVar.dictStanze["avampostoDiRod2"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["tunnelDiRod2"] and stanzaDestinazione == GlobalGameVar.dictStanze["tunnelDiRod3"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["tunnelDiRod1"] and stanzaDestinazione == GlobalGameVar.dictStanze["tunnelDiRod2"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["palazzoDiRod5"] and stanzaDestinazione == GlobalGameVar.dictStanze["tunnelDiRod1"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["palazzoDiRod5"] and stanzaDestinazione == GlobalGameVar.dictStanze["palazzoDiRod2"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara2"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaHansSara1"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara2"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaHansSara3"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara4"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaHansSara2"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta1"] and stanzaDestinazione == GlobalGameVar.dictStanze["casaHansSara4"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta2"] and stanzaDestinazione == GlobalGameVar.dictStanze["forestaCadetta1"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta3"] and stanzaDestinazione == GlobalGameVar.dictStanze["forestaCadetta2"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta4"] and stanzaDestinazione == GlobalGameVar.dictStanze["forestaCadetta3"]:
        nonProcedere = True
    elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] and stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"] and stanzaDestinazione == GlobalGameVar.dictStanze["forestaCadetta4"]:
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
    if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presoChiavePianoInterratoPalazzoRod"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod4"] and xPorta == GlobalHWVar.gpx * 15 and yPorta == GlobalHWVar.gpy * 4:
        procedi = False

    return procedi


def scriviNomeZona(stanza, stanzaVecchia, attesa):
    nomeDaScrivere = False
    if (stanzaVecchia == GlobalGameVar.dictStanze["sognoSara4"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta1"] and stanza == GlobalGameVar.dictStanze["casaHansSara4"]) or (stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"]):
        nomeDaScrivere = LI.CASA[GlobalHWVar.linguaImpostata]
    elif (stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara4"] and stanza == GlobalGameVar.dictStanze["forestaCadetta1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà1"] and stanza == GlobalGameVar.dictStanze["forestaCadetta9"]):
        nomeDaScrivere = LI.FORESTA_CADETTA[GlobalHWVar.linguaImpostata]
    elif (stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta9"] and stanza == GlobalGameVar.dictStanze["stradaPerCittà1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["città1"] and stanza == GlobalGameVar.dictStanze["stradaPerCittà3"]):
        nomeDaScrivere = LI.STR_PER_CIT[GlobalHWVar.linguaImpostata]
    elif (stanzaVecchia == GlobalGameVar.dictStanze["stradaPerCittà3"] and stanza == GlobalGameVar.dictStanze["città1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["casaDavid1"] and stanza == GlobalGameVar.dictStanze["città4"]) or (stanzaVecchia == GlobalGameVar.dictStanze["biblioteca1"] and stanza == GlobalGameVar.dictStanze["città7"]) or (stanzaVecchia == GlobalGameVar.dictStanze["stradaPerSelvaArida1"] and stanza == GlobalGameVar.dictStanze["città9"]) or (stanzaVecchia == GlobalGameVar.dictStanze["stradaPerPassoMontano1"] and stanza == GlobalGameVar.dictStanze["città10"]):
        nomeDaScrivere = LI.CITT[GlobalHWVar.linguaImpostata]
    elif stanzaVecchia == GlobalGameVar.dictStanze["città4"] and stanza == GlobalGameVar.dictStanze["casaDavid1"]:
        nomeDaScrivere = LI.CAS_DI_DAV[GlobalHWVar.linguaImpostata]
    elif stanzaVecchia == GlobalGameVar.dictStanze["città7"] and stanza == GlobalGameVar.dictStanze["biblioteca1"]:
        nomeDaScrivere = LI.BIBLIOTECA[GlobalHWVar.linguaImpostata]
    elif (stanzaVecchia == GlobalGameVar.dictStanze["città9"] and stanza == GlobalGameVar.dictStanze["stradaPerSelvaArida1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["selvaArida1"] and stanza == GlobalGameVar.dictStanze["stradaPerSelvaArida2"]):
        nomeDaScrivere = LI.STR_PER_SEL_ARI[GlobalHWVar.linguaImpostata]
    elif (stanzaVecchia == GlobalGameVar.dictStanze["stradaPerSelvaArida2"] and stanza == GlobalGameVar.dictStanze["selvaArida1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod1"] and stanza == GlobalGameVar.dictStanze["selvaArida16"]):
        nomeDaScrivere = LI.SELVA_ARIDA[GlobalHWVar.linguaImpostata]
    elif (stanzaVecchia == GlobalGameVar.dictStanze["selvaArida16"] and stanza == GlobalGameVar.dictStanze["avampostoDiRod1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["labirinto3"] and stanza == GlobalGameVar.dictStanze["avampostoDiRod1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["scorciatoiaLabirinto2"] and stanza == GlobalGameVar.dictStanze["avampostoDiRod2"]) or (stanzaVecchia == GlobalGameVar.dictStanze["tunnelDiRod3"] and stanza == GlobalGameVar.dictStanze["avampostoDiRod2"]):
        nomeDaScrivere = LI.AVA_DI_ROD[GlobalHWVar.linguaImpostata]
    elif (stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod1"] and stanza == GlobalGameVar.dictStanze["labirinto3"]) or (stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello1"] and stanza == GlobalGameVar.dictStanze["labirinto20"]):
        nomeDaScrivere = LI.LABIRINTO[GlobalHWVar.linguaImpostata]
    elif (stanzaVecchia == GlobalGameVar.dictStanze["labirinto20"] and stanza == GlobalGameVar.dictStanze["esternoCastello1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["internoCastello1"] and stanza == GlobalGameVar.dictStanze["esternoCastello5"]) or (stanzaVecchia == GlobalGameVar.dictStanze["scorciatoiaLabirinto1"] and stanza == GlobalGameVar.dictStanze["esternoCastello1"]):
        nomeDaScrivere = LI.CAS_DI_NEI___EST[GlobalHWVar.linguaImpostata]
    elif (stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello5"] and stanza == GlobalGameVar.dictStanze["internoCastello1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["tunnelSubacqueo1"] and stanza == GlobalGameVar.dictStanze["internoCastello8"]):
        nomeDaScrivere = LI.CAS_DI_NEI___INT[GlobalHWVar.linguaImpostata]
    elif (stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello1"] and stanza == GlobalGameVar.dictStanze["scorciatoiaLabirinto1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod2"] and stanza == GlobalGameVar.dictStanze["scorciatoiaLabirinto2"]):
        nomeDaScrivere = LI.SCO_SUL_MON[GlobalHWVar.linguaImpostata]
    elif (stanzaVecchia == GlobalGameVar.dictStanze["città10"] and stanza == GlobalGameVar.dictStanze["stradaPerPassoMontano1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["passoMontano1"] and stanza == GlobalGameVar.dictStanze["stradaPerPassoMontano2"]):
        nomeDaScrivere = LI.STR_PER_PAS_MON[GlobalHWVar.linguaImpostata]
    elif (stanzaVecchia == GlobalGameVar.dictStanze["stradaPerPassoMontano2"] and stanza == GlobalGameVar.dictStanze["passoMontano1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["palazzoDiRod1"] and stanza == GlobalGameVar.dictStanze["passoMontano10"]):
        nomeDaScrivere = LI.PASSO_MONTANO[GlobalHWVar.linguaImpostata]
    elif (stanzaVecchia == GlobalGameVar.dictStanze["passoMontano10"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["tunnelDiRod1"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod5"]) or (stanzaVecchia == GlobalGameVar.dictStanze["caverna1"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["esternoCastello3"] and stanza == GlobalGameVar.dictStanze["palazzoDiRod2"]):
        nomeDaScrivere = LI.PAL_DI_ROD[GlobalHWVar.linguaImpostata]
    elif (stanzaVecchia == GlobalGameVar.dictStanze["palazzoDiRod5"] and stanza == GlobalGameVar.dictStanze["tunnelDiRod1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["avampostoDiRod2"] and stanza == GlobalGameVar.dictStanze["tunnelDiRod3"]):
        nomeDaScrivere = LI.TUN_DI_ROD[GlobalHWVar.linguaImpostata]
    elif (stanzaVecchia == GlobalGameVar.dictStanze["palazzoDiRod1"] and stanza == GlobalGameVar.dictStanze["caverna1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["vulcano1"] and stanza == GlobalGameVar.dictStanze["caverna18"]):
        nomeDaScrivere = LI.CAVERNA_IMPO[GlobalHWVar.linguaImpostata]
    elif (stanzaVecchia == GlobalGameVar.dictStanze["caverna18"] and stanza == GlobalGameVar.dictStanze["vulcano1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["caverna18"] and stanza == GlobalGameVar.dictStanze["vulcano3"]):
        nomeDaScrivere = LI.VULCANO[GlobalHWVar.linguaImpostata]
    elif (stanzaVecchia == GlobalGameVar.dictStanze["internoCastello8"] and stanza == GlobalGameVar.dictStanze["tunnelSubacqueo1"]) or (stanzaVecchia == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"] and stanza == GlobalGameVar.dictStanze["tunnelSubacqueo2"]):
        nomeDaScrivere = LI.TUNNEL_SUBACQUEO[GlobalHWVar.linguaImpostata]
    elif stanzaVecchia == GlobalGameVar.dictStanze["tunnelSubacqueo2"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        nomeDaScrivere = LI.LAB_DI_NEI[GlobalHWVar.linguaImpostata]

    if nomeDaScrivere:
        if attesa:
            i = 0
            while i < 10:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
        else:
            GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
            FunzioniGraficheGeneriche.messaggio(nomeDaScrivere, GlobalHWVar.grigiochi, GlobalHWVar.gpx * 16, GlobalHWVar.gpy * 8, 150, centrale=True)
            GlobalHWVar.disegnaLineaSuSchermo(GlobalHWVar.schermo, GlobalHWVar.grigiochi, (int(GlobalHWVar.gpx * 4), int(GlobalHWVar.gpy * 10.6) - 1), (int(GlobalHWVar.gpx * 28), int(GlobalHWVar.gpy * 10.6) - 1), 2)
            FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=2)
            GlobalHWVar.aggiornaSchermo()


def mostraTempoPassato(avanzamentoStoria, stanza, stanzaVecchia):
    tempoPassato1 = False
    tempoPassato2 = ""
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and stanzaVecchia == GlobalGameVar.dictStanze["casaHansSara1"] and stanza == GlobalGameVar.dictStanze["casaDavid3"]:
        tempoPassato1 = LI.GIORNO_1[GlobalHWVar.linguaImpostata]
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dormitoNelCastello"] and stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"] and stanza == GlobalGameVar.dictStanze["internoCastello10"]:
        tempoPassato1 = LI.GIORNO_2[GlobalHWVar.linguaImpostata]
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["fineParteDiRod"] and stanzaVecchia == GlobalGameVar.dictStanze["internoCastello21"] and stanza == GlobalGameVar.dictStanze["internoCastello21"]:
        tempoPassato1 = LI.GIORNO_22[GlobalHWVar.linguaImpostata]
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"] and stanzaVecchia == GlobalGameVar.dictStanze["forestaCadetta5"] and stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        tempoPassato1 = LI.GIORNO_22[GlobalHWVar.linguaImpostata]
        tempoPassato2 = LI._ANNO_13[GlobalHWVar.linguaImpostata]

    if tempoPassato1:
        xScritta = GlobalHWVar.gpx * 3
        yScritta = GlobalHWVar.gpy * 13
        GlobalHWVar.disegnaColoreSuTuttoLoSchermo(GlobalHWVar.schermo, GlobalHWVar.nero)
        i = 0
        while i < 10:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        larghezzaTesto = FunzioniGraficheGeneriche.messaggio(tempoPassato1, GlobalHWVar.grigiochi, xScritta, yScritta, 150, restituisciLarghezza=True)
        FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=2)
        GlobalHWVar.aggiornaSchermo()
        i = 0
        while i < 30:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1
        if tempoPassato2 != "":
            superficieSecondaScritta = pygame.Surface((GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 3), flags=pygame.SRCALPHA)
            i = 0
            while i <= 255:
                GlobalHWVar.disegnaRettangoloSuSchermo(GlobalHWVar.schermo, GlobalHWVar.nero, (xScritta + larghezzaTesto, yScritta, GlobalHWVar.gpx * 15, GlobalHWVar.gpy * 3))
                FunzioniGraficheGeneriche.messaggio(tempoPassato2, GlobalHWVar.grigiochi, xScritta + larghezzaTesto, yScritta, 150)
                superficieSecondaScritta.fill((0, 0, 0, 255 - i))
                GlobalHWVar.disegnaImmagineSuSchermo(superficieSecondaScritta, (xScritta + larghezzaTesto, yScritta))
                GlobalHWVar.aggiornaSchermo()
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                GlobalHWVar.clockFadeToBlack.tick(GlobalHWVar.fpsFadeToBlack)
                i += 10
            i = 0
            while i < 30:
                pygame.time.wait(100)
                inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
                i += 1
        FunzioniGraficheGeneriche.oscuraIlluminaSchermo(illumina=False, tipoOscuramento=1)
        i = 0
        while i < 20:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1


def settaNomeImgStanza(avanzamentoStoria, stanza, listaAvanzamentoDialoghi):
    tiratoLevaTunnelDiRod = False
    i = 0
    while i < len(listaAvanzamentoDialoghi):
        if listaAvanzamentoDialoghi[i] == "OggettoLevaTunnelDiRod-0":
            if listaAvanzamentoDialoghi[i + 1] >= 1:
                tiratoLevaTunnelDiRod = True
            break
        i += 2
    nomeStanza = "Stanza"

    if stanza == GlobalGameVar.dictStanze["casaHansSara1"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
            nomeStanza = "StanzaA"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSognoCasaDavid"]:
            nomeStanza = "StanzaB"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            nomeStanza = "StanzaC"
        elif GlobalGameVar.dictAvanzamentoStoria["monologoPerTornareIndietroNelTempoAllaSeraDellInizioDelGioco"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["HansUscitoDaCasa2NellaSeraDellInizioDelGioco"]:
            nomeStanza = "StanzaE"
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["sdraiataSulLettoDiCasaPostPassatiMoltiAnni"] or (avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["oltreFinalePartenzaCasa"] and GlobalGameVar.partitaAppenaAvviataPostFinale):
            nomeStanza = "StanzaF"
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["chiusoGliOcchiSulLettoDiCasaPostPassatiMoltiAnni"]:
            nomeStanza = "StanzaG"
        else:
            nomeStanza = "StanzaD"
    if stanza == GlobalGameVar.dictStanze["casaHansSara2"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] or GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"] or GlobalGameVar.dictAvanzamentoStoria["HansUscitoDaCasa1NellaSeraDellInizioDelGioco"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["HansUscitoDaCasa4NellaSeraDellInizioDelGioco"]:
            nomeStanza = "StanzaA"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaC"
    if stanza == GlobalGameVar.dictStanze["casaHansSara3"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["casaHansSara4"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] or GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"] or GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["forestaCadetta1"] or stanza == GlobalGameVar.dictStanze["forestaCadetta2"] or stanza == GlobalGameVar.dictStanze["forestaCadetta3"] or stanza == GlobalGameVar.dictStanze["forestaCadetta4"] or stanza == GlobalGameVar.dictStanze["forestaCadetta6"] or stanza == GlobalGameVar.dictStanze["forestaCadetta7"] or stanza == GlobalGameVar.dictStanze["forestaCadetta8"] or stanza == GlobalGameVar.dictStanze["forestaCadetta9"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] or GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["forestaCadetta5"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioUltimoDialogoHans"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"] or GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["colpitoHansDalCinghialeCalcolatore"]:
            nomeStanza = "StanzaB"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] or GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineSognoCastello"] or GlobalGameVar.dictAvanzamentoStoria["colpitoHansDalCinghialeCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
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
    if stanza == GlobalGameVar.dictStanze["esternoCastello4"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["apertoCancelloCastelloDaRenéPreFineDelMondo"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaA"
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
        elif GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
            nomeStanza = "StanzaD"
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["apertoPortaInternoCastello8DaRenéPreFineDelMondo"]:
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
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sbloccatoTunnelDiRod"] or (avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and not tiratoLevaTunnelDiRod) or GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
            nomeStanza = "StanzaA"
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["apertoSbarreTunnelDiRodDaRenéPreFineDelMondo"]:
                nomeStanza = "StanzaC"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["palazzoDiRod1"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sbloccatoCaverna"] or GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["palazzoDiRod3"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["palazzoDiRod4"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sbloccatoCaverna"] or GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["palazzoDiRod5"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaA"
    if stanza == GlobalGameVar.dictStanze["tunnelDiRod3"]:
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sbloccatoTunnelDiRod"] or (avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"] and not tiratoLevaTunnelDiRod) or GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
            nomeStanza = "StanzaA"
            if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["apertoSbarreTunnelDiRodDaRenéPreFineDelMondo"]:
                nomeStanza = "StanzaC"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        if GlobalGameVar.dictAvanzamentoStoria["tornatoIndietroNelTempoAPrimaCheNeilLasciasseIlSuoUfficio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["trasformatoLaboratorioDiNeil"]:
            nomeStanza = "StanzaC"
        elif GlobalGameVar.dictAvanzamentoStoria["sparitoNeilDallaCellaDelLaboratorio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["monologo2PostScomparsaNeilDallaCella"] or GlobalGameVar.dictAvanzamentoStoria["monologoPostTornatoIndietroNelTempo10SecInLaboratorio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sedutoSulCalcolatoreRenéNelLaboratorioDiNeil"]:
            nomeStanza = "StanzaD"
        elif GlobalGameVar.dictAvanzamentoStoria["sedutoSulCalcolatoreRenéNelLaboratorioDiNeil"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["RenéOperatoComeTeENeilSulCalcolatore"]:
            nomeStanza = "StanzaE"
        elif GlobalGameVar.dictAvanzamentoStoria["RenéOperatoComeTeENeilSulCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"]:
            nomeStanza = "StanzaF"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPerPassareUnGiornoAspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"] or avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPerPassareUnOra3AspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"]:
                nomeStanza = "StanzaD"
        elif GlobalGameVar.dictAvanzamentoStoria["alzatoRenéDalCalcolatoreDopoSetteAnni"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
            nomeStanza = "StanzaD"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["riapertoGliOcchiSulCalcolatorePostStopTempoACasaTua"]:
                nomeStanza = "StanzaB"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["scesoDalCalcolatorePostScopertaFineDelMondo"]:
                nomeStanza = "StanzaA"
            if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"]:
                nomeStanza = "StanzaG"
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["oltreFinalePartenzaCalcolatore"] and GlobalGameVar.partitaAppenaAvviataPostFinale:
            nomeStanza = "StanzaG"
        elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sedutaSulCalcolatore"] or GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"] or avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["rialzataDalCalcolatore"]:
            nomeStanza = "StanzaA"
        else:
            nomeStanza = "StanzaB"
    if stanza == GlobalGameVar.dictStanze["vulcano3"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaA"
    if stanza == GlobalGameVar.dictStanze["tunnelSubacqueo1"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaA"
    if stanza == GlobalGameVar.dictStanze["caverna1"]:
        if GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
            nomeStanza = "StanzaB"
        else:
            nomeStanza = "StanzaA"
    if stanza == GlobalGameVar.dictStanze["stanzaEsplosa"]:
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["aggiornatoStanzaPerDistruzioneDelMondo1"]:
            nomeStanza = "StanzaA"
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoUnAnno2AspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"]:
            nomeStanza = "StanzaB"
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["passatoUnMese2AspettandoRenéSulCalcolatorePostVisioneDellaDistruzione"]:
            nomeStanza = "StanzaC"
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["missileNucleareScoppiato"]:
            nomeStanza = "StanzaD"
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoPostFineDelMondo2"]:
            nomeStanza = "StanzaE"

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
    elif GlobalGameVar.dictAvanzamentoStoria["riapparsoImpoInternoCastello20PostRianimazione"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["presoImpoPietraPostRianimazione"]:
        GlobalGameVar.impoPresente = True
        GlobalGameVar.impoPietraPosseduta = False
    elif GlobalGameVar.dictAvanzamentoStoria["presoImpoPietraPostRianimazione"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["lasciatoImpoNelLaboratorioDiNeil"]:
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
    elif GlobalGameVar.dictAvanzamentoStoria["terremotoUltimaStanzaCavernaImpo"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["uccisoDagliImpoTorri"]:
        impossibileParare = True

    return impossibileParare


def decidiInteragibilitaPorte(avanzamentoStoria, porte):
    if GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
        porte = []

    return porte


def decidiInteragibilitaCofanetti(avanzamentoStoria, stanza, cofanetti):
    if GlobalGameVar.dictAvanzamentoStoria["monologoPerTornareIndietroNelTempoAllaSeraDellInizioDelGioco"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["HansUscitoDaCasa1NellaSeraDellInizioDelGioco"] and stanza == GlobalGameVar.dictStanze["casaHansSara1"]:
        cofanetti = []

    return cofanetti
