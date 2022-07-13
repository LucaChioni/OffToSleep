# -*- coding: utf-8 -*-

import os
import pygame
import GlobalHWVar
import Codice.FunzioniGeneriche.GestioneInput as GestioneInput


def loadFile(path, mode):
    if not os.path.exists(GlobalHWVar.gamePath + path):
        creazione = open(GlobalHWVar.gamePath + path, "w+")
        creazione.close()
    file = open(GlobalHWVar.gamePath + path, mode)

    # per poter chiudere il gioco durante il caricamento
    inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)

    return file


def loadImage(path, xScale, yScale, aumentaRisoluzione, canale_alpha=True, imgImpenetrabile=False):
    img = pygame.image.load(GlobalHWVar.gamePath + path)

    # aumento la risoluzione per evitare imprecisioni delle img piccole e bug dello smoothscale per le img grandi (lo smoothscle ha problemi nel ridurre la risoluzione)
    if aumentaRisoluzione:
        risoluzioneXPerFix = xScale
        risoluzioneYPerFix = yScale
    else:
        risoluzioneXPerFix = xScale * 2
        risoluzioneYPerFix = yScale * 2
    sizeX, sizeY = img.get_rect().size
    moltiplicatore = 1
    while sizeX * moltiplicatore < risoluzioneXPerFix and sizeY * moltiplicatore < risoluzioneYPerFix:
        moltiplicatore += 1
    img = pygame.transform.scale(img, (sizeX * moltiplicatore, sizeY * moltiplicatore))

    if xScale != 0 and yScale != 0:
        img = pygame.transform.smoothscale(img, (int(xScale), int(yScale)))
    if canale_alpha:
        img = img.convert_alpha()
    else:
        img = img.convert()

    if imgImpenetrabile:
        for i in range(0, 3):
            img.blit(img, (0, 0))

    # per poter chiudere il gioco durante il caricamento
    inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)

    return img


def loadSound(path):
    try:
        sound = pygame.mixer.Sound(GlobalHWVar.gamePath + path)
    except Exception:
        # print ("Errore: Impossibile caricare " + path)
        sound = False

    # per poter chiudere il gioco durante il caricamento
    inutile, inutile = GestioneInput.getInput(False, False, gestioneDuranteLePause=True)

    return sound
