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
        nomePersonaggio = "Sara"
        if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"]:
            imgPersDialogo = GlobalImgVar.imgDialogoSara1
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["inizioSecondoGiorno"]:
            imgPersDialogo = GlobalImgVar.imgDialogoSaraAssonnata
        elif GlobalGameVar.dictAvanzamentoStoria["fuggitoVersoCittà7"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["sedutaInBiblioteca"]:
            imgPersDialogo = GlobalImgVar.imgDialogoSaraSconvolta
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["chiestoDiPensareASceltaPassataNelDialogoBibliotecario"]:
            imgPersDialogo = GlobalImgVar.imgDialogoSaraOcchiChiusi
        elif GlobalGameVar.dictAvanzamentoStoria["monologoCenaAlCastello2"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"]:
            if not GlobalGameVar.cambiataAlCastello[0]:
                imgPersDialogo = GlobalImgVar.imgDialogoSaraAssonnataPostCenaCastello
            else:
                imgPersDialogo = GlobalImgVar.imgDialogoSaraAssonnataCastelloPostCenaCastello
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dormitoNelCastello"]:
            if not GlobalGameVar.cambiataAlCastello[0]:
                imgPersDialogo = GlobalImgVar.imgDialogoSaraAssonnata
            else:
                imgPersDialogo = GlobalImgVar.imgDialogoSaraAssonnataCastello
        elif not GlobalGameVar.cambiataAlCastello[0]:
            imgPersDialogo = GlobalImgVar.imgDialogoSara2
        else:
            imgPersDialogo = GlobalImgVar.imgDialogoSara3

    return nomePersonaggio, imgPersDialogo


def setImgMercanteMenu(avanzamentoStoria, stanza):
    interlocutore = "Rod"
    if avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["tempoBloccato"]:
        interlocutore = "Sara"
    elif avanzamentoStoria >= GlobalGameVar.dictAvanzamentoStoria["incontratoIDueAggressori"] and stanza == GlobalGameVar.dictStanze["città5"]:
        interlocutore = "Pappagallo"
    elif stanza == GlobalGameVar.dictStanze["avampostoDiRod3"]:
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
