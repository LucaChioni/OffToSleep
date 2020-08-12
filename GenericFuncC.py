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
