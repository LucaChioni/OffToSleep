# -*- coding: utf-8 -*-

import GlobalHWVar
import Codice.Variabili.GlobalImgVar as GlobalImgVar
import Codice.Variabili.GlobalSndVar as GlobalSndVar
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
        elif GlobalGameVar.dictAvanzamentoStoria["fineCenaAlCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"]:
            if not GlobalGameVar.cambiataAlCastello[0]:
                imgPersDialogo = GlobalImgVar.imgDialogoSaraAssonnataPostCenaCastello
            else:
                imgPersDialogo = GlobalImgVar.imgDialogoSaraAssonnataCastelloPostCenaCastello
        elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["dormitoNelCastello"]:
            if not GlobalGameVar.cambiataAlCastello[0]:
                imgPersDialogo = GlobalImgVar.imgDialogoSaraAssonnata
            else:
                imgPersDialogo = GlobalImgVar.imgDialogoSaraAssonnataCastello
        elif GlobalGameVar.dictAvanzamentoStoria["comparsoCadavereSoldatoInternoCastello20"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
            if not GlobalGameVar.cambiataAlCastello[0]:
                imgPersDialogo = GlobalImgVar.imgDialogoSaraSconvolta
            else:
                imgPersDialogo = GlobalImgVar.imgDialogoSaraSconvoltaCastello
        elif not GlobalGameVar.cambiataAlCastello[0]:
            imgPersDialogo = GlobalImgVar.imgDialogoSara2
        else:
            imgPersDialogo = GlobalImgVar.imgDialogoSara3

    return nomePersonaggio, imgPersDialogo


def setImgMenuStartProtagonista(avanzamentoStoria):
    if avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"]:
        perssta = GlobalImgVar.sara1GrafMenu
    elif GlobalGameVar.dictAvanzamentoStoria["primoCambioPersonaggio"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["secondoCambioPersonaggio"]:
        perssta = GlobalImgVar.fraMaggioreGrafMenu
    elif avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["cambiataPerCenaDavid"]:
        perssta = GlobalImgVar.sara1GrafMenu
    elif GlobalGameVar.dictAvanzamentoStoria["monologoDopoArrivoInBiblioteca"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["alzataDallaSediaInBiblioteca"]:
        perssta = GlobalImgVar.saraSconvoltaGrafMenu
    elif GlobalGameVar.dictAvanzamentoStoria["fineCenaAlCastello"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["inizioSognoCastello"]:
        if not GlobalGameVar.cambiataAlCastello[0]:
            perssta = GlobalImgVar.saraAssonnataPostCenaCastello
        else:
            perssta = GlobalImgVar.saraAssonnataCastelloPostCenaCastello
    elif GlobalGameVar.dictAvanzamentoStoria["comparsoCadavereSoldatoInternoCastello20"] <= avanzamentoStoria < GlobalGameVar.dictAvanzamentoStoria["fineFugaDalCastello"]:
        if not GlobalGameVar.cambiataAlCastello[0]:
            perssta = GlobalImgVar.saraSconvoltaGrafMenu
        else:
            perssta = GlobalImgVar.saraSconvoltaCastelloGrafMenu
    elif not GlobalGameVar.cambiataAlCastello[0]:
        perssta = GlobalImgVar.sara2GrafMenu
    else:
        perssta = GlobalImgVar.sara3GrafMenu

    return perssta


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
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreAttimoPericoloso)
        GlobalHWVar.canaleSoundBattitoCardiaco.play(GlobalSndVar.rumoreBattitoCardiaco, -1)
    elif avanzamentoStoria == GlobalGameVar.dictAvanzamentoStoria["comparsoCadavereSoldatoInternoCastello20"] and personaggio.tipo.startswith("OggettoDictCadavereSoldato"):
        GlobalHWVar.canaleSoundInterazioni.play(GlobalSndVar.rumoreAttimoPericoloso)

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
