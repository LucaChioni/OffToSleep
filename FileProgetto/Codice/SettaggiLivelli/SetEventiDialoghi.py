# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalGameVar as GlobalGameVar
import Codice.FunzioniGeneriche.GenericFunc as GenericFunc


def setImgDialogoProtagonista(avanzamentoStoria):
    if GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
        nomePersonaggio = "Hans"
        imgPersDialogo = GlobalImgVar.imgDialogoFraMaggiore
    else:
        nomePersonaggio = "Lucy"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"]:
            imgPersDialogo = GlobalImgVar.imgDialogoLucy1
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            imgPersDialogo = GlobalImgVar.imgDialogoLucyAssonnata
        elif GlobalGameVar.dictAvanzamentoStoria["fuggitoVersoCittà7"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sedutaInBiblioteca"]:
            imgPersDialogo = GlobalImgVar.imgDialogoLucySconvolta
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["chiestoDiPensareASceltaPassataNelDialogoBibliotecario"]:
            imgPersDialogo = GlobalImgVar.imgDialogoLucyOcchiChiusi
        else:
            imgPersDialogo = GlobalImgVar.imgDialogoLucy2

    return nomePersonaggio, imgPersDialogo


def setImgMercanteMenu(avanzamentoStoria, stanza):
    interlocutore = "Rod"
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
        interlocutore = "Lucy"
    elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["incontratoIDueAggressori"] and stanza == GlobalGameVar.dictStanze["città5"]:
        interlocutore = "Pappagallo"

    return interlocutore


def gestisciEventiPreDialoghi(avanzamentoStoria, personaggio, canzone):
    if avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["tutorialRecuperoPvDifesa"] and personaggio.tipo == "FiglioUfficiale":
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [0], False, posizioneCanaleMusica=0)
        GlobalHWVar.canaleSoundCanzone.stop()
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["cinghialeUcciso"] and personaggio.tipo == "OggettoPersonaCadavereSam":
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [0], False, posizioneCanaleMusica=0)
        GlobalHWVar.canaleSoundCanzone.stop()

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
        GlobalHWVar.canaleSoundCanzone.play(canzone, -1)
        GenericFunc.cambiaVolumeCanaliAudio([GlobalHWVar.canaleSoundCanzone], [GlobalHWVar.volumeCanzoni], False, posizioneCanaleMusica=0)

    return avanzamentoStoria
