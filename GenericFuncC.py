# -*- coding: utf-8 -*-

import pygame


def loadImage(path, convert=False):
    if convert:
        img = pygame.image.load(path).convert()
    else:
        img = pygame.image.load(path)
    sizeX, sizeY = img.get_rect().size
    img = pygame.transform.scale(img, (sizeX * 4, sizeY * 4))
    return img


def definisciAvanzamentiStoria():
    dictAvanzamentoStoria = {}

    # la key del dictionary descrive l'evento appena compiuto
    i = 0
    dictAvanzamentoStoria["inizio"] = i
    i += 1
    dictAvanzamentoStoria["dialogoSognoSara1"] = i
    i += 1
    dictAvanzamentoStoria["tutorialMovimento"] = i
    i += 1
    dictAvanzamentoStoria["aperturaPrimoCofanetto"] = i
    i += 1
    dictAvanzamentoStoria["tutorialUtilizzoOggetti"] = i
    i += 1
    dictAvanzamentoStoria["tutorialBattaglia"] = i
    i += 1
    dictAvanzamentoStoria["tutorialOggettiBattaglia"] = i
    i += 1
    dictAvanzamentoStoria["dialogoSognoSara2"] = i
    i += 1
    dictAvanzamentoStoria["dialogoSognoSara3"] = i
    dictAvanzamentoStoria["primoCambioPersonaggio"] = i
    i += 1
    dictAvanzamentoStoria["dialogoCasaSamSara1"] = i
    i += 1
    dictAvanzamentoStoria["tutorialChiusuraPorte"] = i
    i += 1
    dictAvanzamentoStoria["OttenutoBicchiere"] = i
    i += 1
    dictAvanzamentoStoria["OttenutoBicchiereAcqua"] = i
    i += 1
    dictAvanzamentoStoria["dialogoCasaSamSara2"] = i

    i += 100
    dictAvanzamentoStoria["secondoCambioPersonaggio"] = i
    i += 1
    dictAvanzamentoStoria["trovatoMappaDiario"] = i
    i += 1
    dictAvanzamentoStoria["incontratoColco"] = i

    return dictAvanzamentoStoria


def definisciStanze():
    dictStanze = {}

    # la key del dictionary descrive la stanza
    i = 1
    dictStanze["sognoSara1"] = i
    i += 1
    dictStanze["sognoSara2"] = i
    i += 1
    dictStanze["sognoSara3"] = i
    i += 1
    dictStanze["sognoSara4"] = i
    i += 1
    dictStanze["casaSamSara1"] = i
    i += 1
    dictStanze["casaSamSara2"] = i

    return dictStanze


def definisciPorte(dictStanze):
    vetPorte = []

    stanza = dictStanze["sognoSara4"]
    vetPorte += [stanza, 15, 9, False]

    stanza = dictStanze["casaSamSara1"]
    vetPorte += [stanza, 6, 9, False]
    vetPorte += [stanza, 7, 6, False]
    vetPorte += [stanza, 25, 3, False]
    vetPorte += [stanza, 26, 11, False]

    return vetPorte


def definisciCofanetti(dictStanze):
    vetCofanetti = []

    stanza = dictStanze["sognoSara1"]
    vetCofanetti += [stanza, 13, 10, False]

    stanza = dictStanze["sognoSara2"]
    vetCofanetti += [stanza, 13, 5, False]
    vetCofanetti += [stanza, 28, 7, False]

    stanza = dictStanze["sognoSara3"]
    vetCofanetti += [stanza, 3, 13, False]

    stanza = dictStanze["casaSamSara1"]
    vetCofanetti += [stanza, 23, 13, False]
    vetCofanetti += [stanza, 24, 15, False]
    vetCofanetti += [stanza, 27, 15, False]
    vetCofanetti += [stanza, 29, 14, False]

    return vetCofanetti
