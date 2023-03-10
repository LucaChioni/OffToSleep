# -*- coding: utf-8 -*-

import hashlib
import pygame
import GlobalHWVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc
import Codice.SettaggiLivelli.DialoghiPerZona.DialoghiNessuno as DialoghiNessuno
import Codice.SettaggiLivelli.DialoghiPerZona.DialoghiTutorial as DialoghiTutorial
import Codice.SettaggiLivelli.DialoghiPerZona.DialoghiSogno as DialoghiSogno
import Codice.SettaggiLivelli.DialoghiPerZona.DialoghiCasa as DialoghiCasa
import Codice.SettaggiLivelli.DialoghiPerZona.DialoghiForestaCadetta as DialoghiForestaCadetta
import Codice.SettaggiLivelli.DialoghiPerZona.DialoghiStradaPerCitta as DialoghiStradaPerCitta
import Codice.SettaggiLivelli.DialoghiPerZona.DialoghiCitta as DialoghiCitta
import Codice.SettaggiLivelli.DialoghiPerZona.DialoghiCasaUfficiale as DialoghiCasaUfficiale
import Codice.SettaggiLivelli.DialoghiPerZona.DialoghiBiblioteca as DialoghiBiblioteca
import Codice.SettaggiLivelli.DialoghiPerZona.DialoghiStradaPerSelvaArida as DialoghiStradaPerSelvaArida
import Codice.SettaggiLivelli.DialoghiPerZona.DialoghiSelvaArida as DialoghiSelvaArida
import Codice.SettaggiLivelli.DialoghiPerZona.DialoghiAvampostoDiRod as DialoghiAvampostoDiRod
import Codice.SettaggiLivelli.DialoghiPerZona.DialoghiLabirinto as DialoghiLabirinto
import Codice.SettaggiLivelli.DialoghiPerZona.DialoghiEsternoCastello as DialoghiEsternoCastello
import Codice.SettaggiLivelli.DialoghiPerZona.DialoghiInternoCastello as DialoghiInternoCastello
import Codice.SettaggiLivelli.DialoghiPerZona.DialoghiScorciatoiaLabirinto as DialoghiScorciatoiaLabirinto
import Codice.SettaggiLivelli.DialoghiPerZona.DialoghiStradaPerPassoMontano as DialoghiStradaPerPassoMontano
import Codice.SettaggiLivelli.DialoghiPerZona.DialoghiPassoMontano as DialoghiPassoMontano
import Codice.SettaggiLivelli.DialoghiPerZona.DialoghiPalazzoDiRod as DialoghiPalazzoDiRod
import Codice.SettaggiLivelli.DialoghiPerZona.DialoghiTunnelDiRod as DialoghiTunnelDiRod
import Codice.SettaggiLivelli.DialoghiPerZona.DialoghiCavernaImpo as DialoghiCavernaImpo
import Codice.SettaggiLivelli.DialoghiPerZona.DialoghiVulcano as DialoghiVulcano
import Codice.SettaggiLivelli.DialoghiPerZona.DialoghiTunnelSubacqueo as DialoghiTunnelSubacqueo
import Codice.SettaggiLivelli.DialoghiPerZona.DialoghiLaboratorioNeil as DialoghiLaboratorioNeil
import Codice.Localizzazione.LocalizInterfaccia as LI
import Codice.Localizzazione.LocalizDialoghiSecondari as LDS


def setGender(tipo):
    gender = "m"
    if tipo == "Tutorial" or tipo == "Nessuno" or tipo.startswith("Oggetto"):
        gender = "n"
    elif tipo == "Madre" or tipo == "MadreUfficiale" or tipo.startswith("Ragazza"):
        gender = "f"

    return gender


def avanzaDialoghiSpecifici(avanzamentoStoria, stanza, listaAvanzamentoDialoghi, listaPersonaggiTotali):
    # if stanza == GlobalGameVar.dictStanze["palazzoDiRod2"] and GlobalGameVar.dictAvanzamentoStoria["dateMonetePerStrumentiPerStudiareImpo"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
    #     avanzaDialogo = False
    #     for personaggio in listaPersonaggiTotali:
    #         if personaggio.tipo == "Mercante" and personaggio.avanzamentoDialogo == 1:
    #             avanzaDialogo = True
    #             break
    #     if avanzaDialogo:
    #         for personaggio in listaPersonaggiTotali:
    #             if personaggio.tipo == "OggettoAppuntiInElaborazioneRod":
    #                 personaggio.avanzamentoDialogo = 1
    #                 break
    #         i = 0
    #         while i < len(listaAvanzamentoDialoghi):
    #             if listaAvanzamentoDialoghi[i] == "OggettoAppuntiInElaborazioneRod-0":
    #                 listaAvanzamentoDialoghi[i + 1] = 1
    #                 break
    #             i += 2

    return listaAvanzamentoDialoghi, listaPersonaggiTotali


def gestisciRisposteSbagliate(avanzamentoStoria):
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["spiegazioneEnigmaBibliotecario4"]:
        GlobalGameVar.datiEnigmaBibliotecario["reset"] = True


def gestisciRisposteCorrette(avanzamentoStoria, tipoPersonaggio):
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["passatiMoltiAnniGuardandoGliEventi"] and tipoPersonaggio == "OggettoComputerCostruttore":
        GlobalGameVar.spengiCalcolatore = True


def gestisciEventiPreDialoghi(avanzamentoStoria, personaggio, canzone):
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialRecuperoPvDifesa"] and personaggio.tipo == "FiglioUfficiale":
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [0], False, posizioneCanaleMusica=0)
        GlobalHWVar.canaleSoundCanzone.stop()
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["cinghialeUcciso"] and personaggio.tipo == "OggettoPersonaCadavereSam":
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [0], False, posizioneCanaleMusica=0)
        GlobalHWVar.canaleSoundCanzone.stop()
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreAttimoPericoloso)
        GlobalHWVar.canaleSoundBattitoCardiaco.play(GlobalSndVar.rumoreBattitoCardiaco, -1)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["comparsoCadavereSoldatoInternoCastello20"] and personaggio.tipo.startswith("OggettoDictCadavereSoldatoCastello"):
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreAttimoPericoloso)
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"] and personaggio.tipo == "OggettoSiepe":
        if personaggio.avanzamentoDialogo == 0:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreLamentoHansCinghiale)
        else:
            GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreLamentoCinghiale)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["ottenutoBicchiere"] and (personaggio.tipo == "OggettoLavandinoCucina" or personaggio.tipo == "OggettoLavandinoBagno"):
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreRiempimentoBicchiere)
        i = 0
        while i < 30:
            pygame.time.wait(100)
            inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)
            i += 1

    return avanzamentoStoria


def gestisciEventiPostDialoghi(avanzamentoStoria, personaggio, canzone):
    if GlobalGameVar.dictAvanzamentoStoria["tutorialRecuperoPvDifesa"] <= avanzamentoStoria <= GlobalGameVar.dictAvanzamentoStoria["incontroFiglioUfficiale"] and personaggio.tipo == "FiglioUfficiale":
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["incontroFiglioUfficiale"]:
            avanzamentoStoria += 1
        GlobalHWVar.canaleSoundCanzone.play(canzone, -1)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [GlobalHWVar.volumeCanzoni], False, posizioneCanaleMusica=0)
    elif (avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["cinghialeUcciso"] and personaggio.tipo == "OggettoPersonaCadavereSam") or (avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoDopoTombaSam"] and personaggio.tipo == "Nessuno"):
        if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["monologoDopoTombaSam"]:
            avanzamentoStoria += 1
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundBattitoCardiaco], [0], False, posizioneCanaleMusica=0)
        GlobalHWVar.canaleSoundBattitoCardiaco.stop()
        GlobalHWVar.canaleSoundBattitoCardiaco.set_volume(GlobalHWVar.volumeEffetti)
        GlobalHWVar.canaleSoundCanzone.play(canzone, -1)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [GlobalHWVar.volumeCanzoni], False, posizioneCanaleMusica=0)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["vomitatoInBiblioteca"] and personaggio.tipo == "Nessuno":
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreVomito)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dialogoRodAperturaRetroPalazzo"] and personaggio.tipo == "Mercante":
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreSbloccoPorta)

    return avanzamentoStoria


def caricaDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute):
    tipo = tipoId.split("-")[0]
    partiDialogoTradotte = []
    nome = "---"
    oggettoDato = False
    avanzaStoria = False
    menuMercante = False
    scelta = False
    avanzaColDialogo = False

    # se c'?? una scelta la variabile scelta conterr?? il numero corrispondente a quella giusta (se ce n'?? pi?? di una giusta, la variabile conterr?? i numeri di queste una dopo l'altra (es. 12, 134))
    # i dialoghi che iniziano con "???DOMANDA???" contengono 6 frasi in totale (ossia => "???DOMANDA???", la domanda posta, opzione 1, opzione 2, opzione 3, opzione 4)
    # i dialoghi che iniziano con "!!!RISPOSTA!!!" contengono 5 frasi in totale (ossia => "!!!RISPOSTA!!!", risposta opzione 1, risposta opzione 2, risposta opzione 3, risposta opzione 4)
    if tipo == "Nessuno":
        partiDialogoTradotte, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiNessuno.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif tipo == "Tutorial":
        partiDialogoTradotte, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiTutorial.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif tipo == "OggettoDictCofanettoChiuso" and GlobalGameVar.dictAvanzamentoStoria["inizioUsoCalcolatore"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineUsoCalcolatore"]:
        nome = LI.COFANETTO
        partiDialogoTradotte = []
        oggettoDato = False
        avanzaStoria = False
        menuMercante = False
        scelta = False
        dialogo = []
        dialogo.append("tu")
        dialogo.append(LDS._0393_01_Tu_NON_POS_APR_ADE_)
        partiDialogoTradotte.append(dialogo)
    elif GlobalGameVar.dictStanze["sognoSara1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["sognoSara4"]:
        partiDialogoTradotte, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiSogno.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["casaHansSara1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["casaHansSara4"]:
        partiDialogoTradotte, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiCasa.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["forestaCadetta1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["forestaCadetta9"]:
        partiDialogoTradotte, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiForestaCadetta.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["stradaPerCitt??1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["stradaPerCitt??3"]:
        partiDialogoTradotte, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiStradaPerCitta.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["citt??1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["citt??10"]:
        partiDialogoTradotte, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiCitta.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["casaDavid1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["casaDavid3"]:
        partiDialogoTradotte, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiCasaUfficiale.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["biblioteca1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["biblioteca3"]:
        partiDialogoTradotte, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiBiblioteca.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["stradaPerSelvaArida1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["stradaPerSelvaArida2"]:
        partiDialogoTradotte, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiStradaPerSelvaArida.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["selvaArida1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["selvaArida16"]:
        partiDialogoTradotte, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiSelvaArida.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["avampostoDiRod1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["avampostoDiRod3"]:
        partiDialogoTradotte, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiAvampostoDiRod.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["labirinto1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["labirinto23"]:
        partiDialogoTradotte, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiLabirinto.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["esternoCastello1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["esternoCastello5"]:
        partiDialogoTradotte, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiEsternoCastello.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["internoCastello1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["internoCastello21"]:
        partiDialogoTradotte, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiInternoCastello.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["scorciatoiaLabirinto1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["scorciatoiaLabirinto2"]:
        partiDialogoTradotte, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiScorciatoiaLabirinto.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["stradaPerPassoMontano1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["stradaPerPassoMontano2"]:
        partiDialogoTradotte, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiStradaPerPassoMontano.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["passoMontano1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["passoMontano10"]:
        partiDialogoTradotte, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiPassoMontano.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["palazzoDiRod1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["palazzoDiRod5"]:
        partiDialogoTradotte, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiPalazzoDiRod.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["tunnelDiRod1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["tunnelDiRod3"]:
        partiDialogoTradotte, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiTunnelDiRod.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["caverna1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["caverna18"]:
        partiDialogoTradotte, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiCavernaImpo.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["vulcano1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["vulcano3"]:
        partiDialogoTradotte, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiVulcano.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["tunnelSubacqueo1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["tunnelSubacqueo2"]:
        partiDialogoTradotte, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiTunnelSubacqueo.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)
    elif GlobalGameVar.dictStanze["laboratorioSegretoNeil1"] <= stanzaDiAppartenenza <= GlobalGameVar.dictStanze["laboratorioSegretoNeil1"]:
        partiDialogoTradotte, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo = DialoghiLaboratorioNeil.setDialogo(tipoId, x, y, avanzamentoStoria, stanzaDiAppartenenza, avanzamentoDialogo, monetePossedute)

    # se le parti che compongono le battute dei dialoghi non sono dictionary (come "tu" e "personaggio"), le traformo in dictionary qui
    partiDialogoTradotteTemp = []
    for dialogo in partiDialogoTradotte:
        dialogoTemp = []
        for pezzoDialogo in dialogo:
            if not type(pezzoDialogo) is dict:
                dictTempLocalizzazioniDialoghi = {}
                for lingua in GlobalHWVar.lingueDelGioco:
                    dictTempLocalizzazioniDialoghi[lingua] = pezzoDialogo
                dialogoTemp.append(dictTempLocalizzazioniDialoghi)
            elif type(pezzoDialogo) is dict:
                for lingua in GlobalHWVar.lingueDelGioco:
                    if not lingua in pezzoDialogo.keys():
                        pezzoDialogo[lingua] = pezzoDialogo["ita"]
                dialogoTemp.append(pezzoDialogo)
            else:
                dialogoTemp.append(pezzoDialogo)
        partiDialogoTradotteTemp.append(dialogoTemp)
    partiDialogoTradotte = partiDialogoTradotteTemp
    # se il nome dell'interlocutore non ?? un dictionary (non c'?? bisogno di tradurlo), lo traformo in dictionary qui
    if not type(nome) is dict:
        dictTempLocalizzazioniNomi = {}
        for lingua in GlobalHWVar.lingueDelGioco:
            dictTempLocalizzazioniNomi[lingua] = nome
        nome = dictTempLocalizzazioniNomi
    # se l'oggetto dato non ?? un dictionary (?? == False), lo traformo in dictionary qui
    if not type(oggettoDato) is dict:
        dictTempLocalizzazioniOggetti = {}
        for lingua in GlobalHWVar.lingueDelGioco:
            dictTempLocalizzazioniOggetti[lingua] = oggettoDato
        oggettoDato = dictTempLocalizzazioniOggetti

    # creo un digest dell'intero dialogo per avere un id da usare per il controllo dei dialoghi gi?? letti (non lo faccio per i dialoghi con nessuno, tutorial e cadaveri (eccetto i soldati nel castello))
    if tipo == "Nessuno" or tipo == "Tutorial" or (tipo.startswith("OggettoDictCadavere") and not tipo.startswith("OggettoDictCadavereSoldatoCastello")):
        idDialogoCorrente = False
    else:
        idDialogoCorrente = tipo
        for dialogo in partiDialogoTradotte:
            for pezzoDialogo in dialogo:
                idDialogoCorrente += pezzoDialogo["ita"]
        md5 = hashlib.md5()
        md5.update(idDialogoCorrente.encode("utf-8"))
        idDialogoCorrente = md5.hexdigest()

    return partiDialogoTradotte, nome, oggettoDato, avanzaStoria, menuMercante, scelta, avanzaColDialogo, idDialogoCorrente
